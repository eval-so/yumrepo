#!/usr/bin/env bash

if [[ -e 'build.sh' ]]
then
  echo "Run this script from a directory down from here."
  echo "e.g.: cd evalso-release; ../build.sh"
  exit 1
fi

if [[ "$1" == "" ]]
then
  versions="18"
else
  versions="$1"
fi

if [[ "$2" == "" ]]
then
  archs="x86_64 i386"
else
  archs="$1"
fi

echo "Building: $(rpmspec -P *.spec -q  --queryformat='%{name}-%{version}\n')"
echo "On Fedora versions: $versions"
echo "And Architectures: $archs"
echo

if [[ $EVALSO_NOCONFIRM != 1 ]];
then
  echo "Type yes to continue."
  echo -n "> "
  read confirm

  if [[ "$confirm" != "yes" ]]
  then
    echo "Quitting."
    exit 1
  fi
fi

echo "== Downloading sources =="
spectool -g -A *.spec

echo "== Running mock (this will take some time) =="
for version in $versions
do
  for arch in $archs
  do
    tmpdir=`mktemp -d`
    mock -r fedora-$version-$arch --buildsrpm --spec *.spec --sources .
    mv -v /var/lib/mock/fedora-$version-$arch/result/*.src.rpm $tmpdir
    mock -r fedora-$version-$arch $tmpdir/*.src.rpm
    if [[ $? != 0 ]]
    then
      echo " *** BUILD FAILED *** "
      echo "Determine why the build failed, fix the issue, and try again."
      exit 1
    fi
    rm -rf $tmpdir
    if [[ ! -d "../../f$version" ]]
    then
      mkdir "../../f$version"
    fi
    mv -v /var/lib/mock/fedora-$version-$arch/result/*.src.rpm ../../f$version/srpms
    mv -v /var/lib/mock/fedora-$version-$arch/result/*.rpm ../../f$version/srpms
  done
done

echo "== Cleaning up =="
for file in `spectool *.spec | grep http | awk '{print $2}'`
do
  echo "Found file downloaded via http(s): $(basename $file)"
done

if [[ $EVALSO_NOCONFIRM != 1 ]];
then
  echo "Type yes to continue."
  read confirm
fi

if [[ $EVALSO_NOCONFIRM == 1 || "$confirm" == "yes" ]]
then
  for file in `spectool *.spec | grep http | awk '{print $2}'`
  do
    rm -v "$(basename $file)"
  done
fi

echo "== DONE =="
echo "Run the following command to sign the RPMs and push the repository."
echo "  pushd ../../; ./sync-s3.sh; popd"
echo
echo "Once you've done that, remember to push any specfile changes to git."
