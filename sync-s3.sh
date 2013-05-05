#!/usr/bin/env bash
for f in f18 f19
do
  if [[ ! -d "$f" ]]
  then
    mkdir $f
  fi
  pushd $f/rpms
    rm -v *debuginfo*.rpm
    rpm --addsign *.rpm
    createrepo .
  popd

  s3cmd del s3://yum.eval.so/$f/rpms/repodata/*
  s3cmd sync $f s3://yum.eval.so

  find $f/rpms/repodata/ -name '*.gz' -exec s3cmd put --add-header="Content-Encoding:gzip" \{\} s3://yum.eval.so/$f/rpms/repodata/ \;
done
