#!/usr/bin/env bash
for f in f18
do
  pushd $f/rpms
    rpm --addsign *.rpm
    createrepo .
  popd
  s3cmd sync $f s3://yum.eval.so
done
