#!/usr/bin/env bash
for f in f18 f19
do
  if [[ ! -d "$f" ]]
  then
    mkdir $f
  fi
  pushd $f/rpms
    rpm --addsign *.rpm
    createrepo .
  popd
  s3cmd sync $f s3://yum.eval.so
done
