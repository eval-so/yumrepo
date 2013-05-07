Name:           fsharp
Version:        3.0.27
Release:        1%{?dist}
Summary:        Open source F# compiler

Group:          Development/Languages
License:        ASL 2.0
URL:            http://fsharp.org/
Source0:        https://github.com/fsharp/fsharp/archive/%{version}.tar.gz
Autoreq:        0
BuildRequires:  mono-devel autoconf automake
Requires:       mono-core mono-web

%description
F# is an open source, functional-first programming language which empowers
users and organizations to tackle complex computing problems with simple,
maintainable and robust code. It is used in a wide range of application areas
and is available across multiple platforms.

%prep
%setup -q -n %{name}-%{version}
chmod +x autogen.sh
./autogen.sh
%configure

%build
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc README.md LICENSE
%{_bindir}/fsharp*
%{_prefix}/lib/mono/*

%changelog
* Sat May 4 2013 Ricky Elrod <codeblock@fedoraproject.org> - 3.0.27-1
- Latest upstream release.

* Sat Feb 23 2013 Ricky Elrod <codeblock@fedoraproject.org> - 3.0.25-1
- Initial build.
