# https://fedoraproject.org/wiki/Packaging:Haskell

%global pkg_name utf8-light

Name:           ghc-%{pkg_name}
Version:        0.4.0.1
Release:        1%{?dist}
Summary:        Lightweight UTF8 handling

License:        BSD
URL:            http://hackage.haskell.org/package/%{pkg_name}
Source0:        http://hackage.haskell.org/packages/archive/%{pkg_name}/%{version}/%{pkg_name}-%{version}.tar.gz

BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
# Begin cabal-rpm deps:
BuildRequires:  ghc-bytestring-devel
# End cabal-rpm deps

%description
Lightweight UTF8 handling.


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


%changelog
* Mon Jul  8 2013 Fedora Haskell SIG <haskell@lists.fedoraproject.org> - 0.4.0.1-1
- spec file generated by cabal-rpm-0.8.2
