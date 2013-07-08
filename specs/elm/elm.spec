# https://fedoraproject.org/wiki/Packaging:Haskell

%global pkg_name Elm

Name:           elm
Version:        0.8.0.3
Release:        1%{?dist}
Summary:        The Elm language module

License:        BSD
URL:            http://hackage.haskell.org/package/%{pkg_name}
Source0:        http://hackage.haskell.org/packages/archive/%{pkg_name}/%{version}/%{pkg_name}-%{version}.tar.gz

BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
# Begin cabal-rpm deps:
BuildRequires:  ghc-blaze-html-devel
BuildRequires:  ghc-blaze-markup-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-cmdargs-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-deepseq-devel
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-hjsmin-devel
BuildRequires:  ghc-indents-devel
BuildRequires:  ghc-json-devel
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-pandoc-devel
BuildRequires:  ghc-parsec-devel
BuildRequires:  ghc-shakespeare-devel
BuildRequires:  ghc-template-haskell-devel
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-transformers-devel
ExclusiveArch:  %{ghc_arches_with_ghci}
# End cabal-rpm deps
BuildRequires:  prelink

%description
Elm aims to make client-side web-development more pleasant. It is a
statically/strongly typed, functional reactive language to HTML, CSS, and JS.
This package provides a library for Elm compilation in Haskell and a compiler
executable.


%package -n ghc-%{name}
Summary:        Haskell %{pkg_name} library

%description -n ghc-%{name}
This package provides the Haskell %{pkg_name} shared library.


%package -n ghc-%{name}-devel
Summary:        Haskell %{pkg_name} library development files
Requires:       ghc-compiler = %{ghc_version}
Requires(post): ghc-compiler = %{ghc_version}
Requires(postun): ghc-compiler = %{ghc_version}
Requires:       ghc-%{name}%{?_isa} = %{version}-%{release}

%description -n ghc-%{name}-devel
This package provides the development files for the Haskell %{pkg_name} library.


%prep
%setup -q -n %{pkg_name}-%{version}

# https://fedoraproject.org/wiki/Common_Rpmlint_issues#wrong-file-end-of-line-encoding
sed -i 's/\r//' docs.json

%build
%ghc_lib_build


%install
%ghc_lib_install

# https://fedoraproject.org/wiki/Packaging_tricks#Executable_stack
execstack -c %{buildroot}%{_bindir}/elm{,-doc}

%post -n ghc-%{name}-devel
%ghc_pkg_recache


%postun -n ghc-%{name}-devel
%ghc_pkg_recache


%files
%doc LICENSE
%doc docs.json
%{_bindir}/elm-doc
%{_bindir}/elm
%{_datadir}/%{pkg_name}-%{version}


%files -n ghc-%{name} -f ghc-%{pkg_name}.files
%doc LICENSE


%files -n ghc-%{name}-devel -f ghc-%{pkg_name}-devel.files
%doc docs.json


%changelog
* Mon Jul  8 2013 Fedora Haskell SIG <haskell@lists.fedoraproject.org> - 0.8.0.3-1
- spec file generated by cabal-rpm-0.8.2
