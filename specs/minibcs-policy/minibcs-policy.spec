%global selinux_variants mls strict targeted
%global selinux_policyver %(%{__sed} -e 's,.*selinux-policy-\\([^/]*\\)/.*,\\1,' /usr/share/selinux/devel/policyhelp || echo 0.0.0)

Name:           minibcs-policy
Version:        1.1
Release:        1%{?dist}
License:        MIT
Summary:        Custom policy for Eval.so's compilation system
Group:          System Environment/Base
BuildRequires:  checkpolicy, selinux-policy-devel, /usr/share/selinux/devel/policyhelp, hardlink
%if "%{selinux_policyver}" != ""
Requires:       selinux-policy >= %{selinux_policyver}
%endif
Requires(post):   /usr/sbin/semodule, /sbin/restorecon
Requires(postun): /usr/sbin/semodule, /sbin/restorecon

Source0:        minibcs.te

%description
Custom SELinux policy for BCS.

%prep
mkdir SELinux
cp -p %{SOURCE0} SELinux

%build
cd SELinux
for selinuxvariant in %{selinux_variants}
do
  make NAME=${selinuxvariant} -f /usr/share/selinux/devel/Makefile

  mv minibcs.pp minibcs.pp.${selinuxvariant}

  make NAME=${selinuxvariant} -f /usr/share/selinux/devel/Makefile clean
done
cd -

%install
for selinuxvariant in %{selinux_variants}
do
  install -d %{buildroot}%{_datadir}/selinux/${selinuxvariant}

  install -p -m 644 SELinux/minibcs.pp.${selinuxvariant} \
    %{buildroot}%{_datadir}/selinux/${selinuxvariant}/minibcs.pp

done

/usr/sbin/hardlink -cv %{buildroot}%{_datadir}/selinux

%post
for selinuxvariant in %{selinux_variants}
do

  /usr/sbin/semodule -s ${selinuxvariant} -i \
    %{_datadir}/selinux/${selinuxvariant}/minibcs.pp &> /dev/null || :

done

%postun
if [ $1 -eq 0 ] ; then
  for selinuxvariant in %{selinux_variants}
  do

    /usr/sbin/semodule -s ${selinuxvariant} -r minibcs &> /dev/null || :

  done
fi

%files
%defattr(-,root,root,0755)
%doc SELinux/*
%{_datadir}/selinux/*/*.pp

%changelog
* Fri May 3 2013 Ricky Elrod <codeblock@fedoraproject.org> - 1.1-1
- Make spec version match module version.

* Thu May 2 2013 Ricky Elrod <codeblock@fedoraproject.org> - 1.0.0-1
- Initial build.
