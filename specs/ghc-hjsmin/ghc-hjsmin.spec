# https://fedoraproject.org/wiki/Packaging:Haskell

%global pkg_name hjsmin

Name:           ghc-%{pkg_name}
Version:        0.1.4.1
Release:        1%{?dist}
Summary:        Haskell implementation of a javascript minifier

License:        BSD
URL:            http://hackage.haskell.org/package/%{pkg_name}
Source0:        http://hackage.haskell.org/packages/archive/%{pkg_name}/%{version}/%{pkg_name}-%{version}.tar.gz

BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
# Begin cabal-rpm deps:
BuildRequires:  ghc-blaze-builder-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-language-javascript-devel
BuildRequires:  ghc-text-devel
# End cabal-rpm deps

%description
Reduces size of javascript files by stripping out extraneous whitespace and
other syntactic elements, without changing the semantics.


%package devel
Summary:        Haskell %{pkg_name} library development files
Requires:       ghc-compiler = %{ghc_version}
Requires(post): ghc-compiler = %{ghc_version}
Requires(postun): ghc-compiler = %{ghc_version}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package provides the development files for the Haskell %{pkg_name} library.


%prep
%setup -q -n %{pkg_name}-%{version}


%build
%ghc_lib_build


%install
%ghc_lib_install


%post devel
%ghc_pkg_recache


%postun devel
%ghc_pkg_recache


%files -f %{name}.files
%doc LICENSE


%files devel -f %{name}-devel.files
%doc TODO.txt README.markdown


%changelog
* Mon Jul  8 2013 Fedora Haskell SIG <haskell@lists.fedoraproject.org> - 0.1.4.1-1
- spec file generated by cabal-rpm-0.8.2