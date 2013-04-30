Name:		evalso-release
Summary:	Eval.so yum repository
Version:	1.0.0
Release:	2%{?dist}
License:	GPLv2
Group:		System Environment/Base
URL:		http://eval.so
Source0:	evalso.repo
Source1:	RPM-GPG-KEY-evalso.gz
BuildArch:	noarch
BuildRequires:	gzip

%description
Yum configuration for the Eval.so repository.

%prep

%build

%install
install -d %{buildroot}/etc/yum.repos.d
install -d %{buildroot}/etc/pki/rpm-gpg
install -m 644 %{SOURCE0} %{buildroot}/etc/yum.repos.d/
gunzip -c %{SOURCE1} > %{buildroot}/etc/pki/rpm-gpg/RPM-GPG-KEY-evalso

%files
%config(noreplace) %{_sysconfdir}/yum.repos.d/evalso.repo
%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-evalso

%changelog
* Tue Apr 30 2013 Ricky Elrod <ricky@elrod.me> - 1.0.0-2
- Make gunzip go to stdout properly.

* Tue Apr 30 2013 Ricky Elrod <ricky@elrod.me> - 1.0.0-1
- Initial release.
