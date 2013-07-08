# https://fedoraproject.org/wiki/Packaging:Haskell

%global pkg_name concatenative

Name:           ghc-%{pkg_name}
Version:        1.0.1
Release:        1%{?dist}
Summary:        A library for postfix control flow

License:        BSD
URL:            http://hackage.haskell.org/package/%{pkg_name}
Source0:        http://hackage.haskell.org/packages/archive/%{pkg_name}/%{version}/%{pkg_name}-%{version}.tar.gz

BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
# Begin cabal-rpm deps:
BuildRequires:  ghc-template-haskell-devel
ExclusiveArch:  %{ghc_arches_with_ghci}
# End cabal-rpm deps

%description
Concatenative gives haskell factor style combinators and arrows for postfix
notation. For more information on stack based languages, see
<http://concatenative.org>.


%package devel
Summary:        Haskell %{pkg_name} library development files
Requires:       ghc-compiler = %{ghc_version}
Requires(post): ghc-compiler = %{ghc_version}
Requires(postun): ghc-compiler = %{ghc_version}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package provides the development files for
the Haskell %{pkg_name} library.


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


%changelog
* Mon Jul  8 2013 Fedora Haskell SIG <haskell@lists.fedoraproject.org> - 1.0.1-1
- spec file generated by cabal-rpm-0.8.2
