#!/usr/bin/env bash
file=$1

if [[ "$file" == "" ]]; then
  echo "No file given."
  exit 1
fi

echo "Removing f*/*/$file*"
echo "Type 'yes' to continue."
read confirm

if [[ "$confirm" != "yes" ]]; then
  echo "Aborting."
  exit 1
fi

rm -Iv f*/*/$file*
s3cmd del s3://yum.eval.so/f*/*/$file*
