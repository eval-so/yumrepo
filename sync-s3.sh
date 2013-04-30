#!/usr/bin/env bash
for f in f18
do
  pushd $f
    createrepo .
    rpm --addsign rpms/*.rpm
  popd
  s3cmd sync $f s3://yum.eval.so
done
