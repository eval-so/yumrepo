#!/usr/bin/env bash
for f in f18
do
  pushd $f/rpms
    createrepo .
    rpm --addsign *.rpm
  popd
  s3cmd sync $f s3://yum.eval.so
done
