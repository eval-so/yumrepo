Name:           lci
Version:        0.11.1
Release:        1%{?dist}
Summary:        A LOLCODE interpreter written in C

Group:          Development/Languages
License:        GPLv3+
URL:            http://lolcode.org/
Source0:        https://github.com/justinmeza/%{name}/archive/v%{version}.tar.gz
BuildRequires:  cmake readline-devel


%description
lci is a LOLCODE interpreter written in C and is designed to be correct,
portable, fast, and precisely documented.

%prep
%setup -q

%build
%cmake .
make

%install
make install DESTDIR=%{buildroot}

%files
%defattr(-,root,root,-)
%{_bindir}/%{name}

%changelog
* Sun May 05 2013 Ricky Elrod <codeblock@fedoraproject.org> 0.11.1-1
- Initial build.
