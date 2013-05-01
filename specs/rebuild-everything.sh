#!/usr/bin/env bash

echo "== WARNING WARNING WARNING WARNING WARGNING =="
echo
echo "You're about to rebuild everything in the eval.so repository."
echo "This can take a really long time and be very CPU intensive."
echo "We typically only do this once per Fedora release."
echo
echo "It might be worth spinning up a beefy cloud instance and doing this"
echo "there instead."
echo
echo "== WARNING WARNING WARNING WARNING WARGNING =="
echo "Type yes to continue."
echo -n "> "

read confirm

if [[ "$confirm" != "yes" ]]
then
  echo "Quitting."
  exit 1
fi

export EVALSO_NOCONFIRM=1

for d in `find . -type d`
do
  pushd $d
  ../build.sh "$1" "$2"
done
