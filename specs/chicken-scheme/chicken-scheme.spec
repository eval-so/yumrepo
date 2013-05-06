Name:           chicken-scheme
Version:        4.8.0.3
Release:        1%{?dist}
Summary:        A practical and portable Scheme system

Group:          Development/Languages
License:        BSD
URL:            http://call-cc.org
Source0:        http://code.call-cc.org/releases/4.8.0/chicken-%{version}.tar.gz
BuildRequires:  hostname chrpath

%description
CHICKEN is a compiler for the Scheme programming language.
CHICKEN produces portable, efficient C, supports almost all of the R5RS
Scheme language standard, and includes many enhancements and extensions.

%prep
%setup -q -n chicken-%{version}

%package doc
Summary: Documentation files for CHICKEN scheme.
Provides: chicken-scheme-doc = %{version}-%{release}

%description doc
Documentation for CHICKEN (chicken-scheme).

%build
make CFLAGS="%{optflags}" \
     PREFIX=%{_prefix} \
     BINDIR=%{_bindir} \
     LIBDIR=%{_libdir} \
     DATADIR=%{_datadir}/chicken \
     INCLUDEDIR=%{_includedir}/chicken \
     INFODIR=%{_infodir}/chicken \
     TOPMANDIR=%{_mandir} \
     DOCDIR=%{_docdir}/chicken \
     PLATFORM=linux

%install
make CFLAGS="%{optflags}" \
     PREFIX=%{_prefix} \
     BINDIR=%{_bindir} \
     LIBDIR=%{_libdir} \
     DATADIR=%{_datadir}/chicken \
     INCLUDEDIR=%{_includedir}/chicken \
     INFODIR=%{_infodir}/chicken \
     TOPMANDIR=%{_mandir} \
     DOCDIR=%{_docdir}/chicken \
     DESTDIR=%{buildroot} \
     PLATFORM=linux install

rm -f %{buildroot}/%{_docdir}/chicken/LICENSE %{buildroot}/%{_docdir}/chicken/README

find %{buildroot} -name \*.so -exec chrpath --delete \{\} \;
find %{buildroot} -name \*.a -exec rm \{\} \;
chrpath --delete %{buildroot}/%{_bindir}/*


%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc README LICENSE
%dir %{_datadir}/chicken
%{_datadir}/chicken/setup.defaults
%{_bindir}/chicken
%{_bindir}/chicken-bug
%{_bindir}/chicken-install
%{_bindir}/chicken-profile
%{_bindir}/chicken-status
%{_bindir}/chicken-uninstall
%{_bindir}/csc
%{_bindir}/csi
%dir %{_includedir}/chicken
%{_includedir}/chicken/chicken-config.h
%{_includedir}/chicken/chicken.h
%{_libdir}/libchicken.so
%{_libdir}/libchicken.so.6
%dir %{_libdir}/chicken
%dir %{_libdir}/chicken/6
%{_libdir}/chicken/6/*
%{_mandir}/man1/chicken-bug.1.gz
%{_mandir}/man1/chicken-install.1.gz
%{_mandir}/man1/chicken-profile.1.gz
%{_mandir}/man1/chicken-status.1.gz
%{_mandir}/man1/chicken-uninstall.1.gz
%{_mandir}/man1/chicken.1.gz
%{_mandir}/man1/csc.1.gz
%{_mandir}/man1/csi.1.gz

%files doc
%{_docdir}/chicken/manual

%changelog
* Sun May 05 2013 Ricky Elrod <codeblock@fedoraproject.org> 4.8.0.3-1
- Clean spec file up a lot.
- Bump to latest upstream release.

* Thu May 03 2012 J R Jones <fedora@zaniyah.org> 4.7.0-2
- Separated into separate sub-packages

* Thu May 03 2012 J R Jones <fedora@zaniyah.org> 4.7.0-1
- Specfile created.
