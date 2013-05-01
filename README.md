# Eval.so public yum repository

This repository is home of http://yum.eval.so/ used internally by the
Eval.so infrastructure.

It provides RPMs for various compilers and interpreters that are not part of
the official Fedora repos

Only `/spec/*` is available in Git, but the contents of the whole repo are
available via S3.

We accept Pull Requests on files in `spec/`.

# Repo admins

All RPMs in this repository are signed with key `E28C47E4`.

If you don't have access to this key and feel you should, please contact
@CodeBlock (github).

## Building and Pushing RPMs

### Prereqs

* Have the GPG key imported so that you can sign them.
* Have a working Mock environment, capable of building in an F18 chroot.

### The process

* `cd` into the relevant `specs/` directory, for example `cd specs/go`
* run `../build.sh` and answer prompts.
* When done, run `pushd ../../; ./sync-s3.sh; popd` from the current directory,
  (or move up to the repo root and run `./sync-s3.sh`).
* Enter the GPG password when asked
* Wait for things to sign and upload.

The same process applies for pull requests. Review the request and merge it in,
then follow the above process.

**Be sure to bump the `Release` field of updated specs.**

### Deleting RPMs

We don't typically keep old RPMs around in the repo. To remove an old RPM
run `./remove-file.sh <valid NVR>` from the repo root.

e.g. Run `./remove-file.sh evalso-release-1.0.0-2` after building/uploading
`evalso-release-1.0.0-3`.

### New Fedora releases and new Architectures

When a new Fedora release comes out (or gets branched), you can start building
packages for it right away. You need to add it to a few scripts, first,
however.

* Line 2 of `s3-sync.sh` (space separated list)
* Line 12 of `specs/build.sh` (space separated list)

For adding a new architecture:

* Line 19 of `specs/build.sh` (space separated list)

Lastly, you'll want to build everything for the new version.

`cd` into the `specs/` directory, and run
`./rebuild-everything <version number>`

# License

GPLv2 to remain compatible with Fedora repos unless otherise noted in
`specs/*/LICENSE`.
