Name:           factor
Version:        0.96
Release:        1%{?dist}
Summary:        A stack-based programming language

Group:          Development/Languages
License:        BSD
URL:            http://factorcode.org
Source0:        http://downloads.factorcode.org/releases/%{version}/%{name}-src-%{version}.zip
Source1:        %{name}.desktop
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires:  GLC_lib-devel
BuildRequires:  cairo-devel
BuildRequires:  pango-devel
BuildRequires:  gtkglext-devel
BuildRequires:  desktop-file-utils

%description
The Factor programming language combines powerful language features
with a full-featured library. The implementation is fully compiled
for performance, while still supporting interactive development.
Factor applications are portable between all common platforms.
Factor can deploy stand-alone applications on all platforms. Full
source code for the Factor project is available under a BSD license.

%prep
%setup -q -n %{name}

%build
make %{?_smp_mflags}
if [ "$(arch)" = "x86_64" ];
then
  ./factor -i=boot.unix-x86.64.image
else
  ./factor -i=boot.unix-x86.32.image
fi

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_libdir}/%{name}
cp -a %{name} misc extra core basis %{name}.image %{buildroot}/%{_libdir}/%{name}

# Remove tests, they are pointless once it's compiled, and cause rpmlint to growl.
find %{buildroot}/%{_libdir}/%{name} -type d -name test -prune -execdir rm -rf {} \;
find %{buildroot}/%{_libdir}/%{name} -type d -name tests -prune -execdir rm -rf {} \;

# Factor looks for its image relative to its binary, so we must install the
# binary where the image gets installed (libdir/factor). Then we can
# symlink it to bindir successfully.
mkdir -p %{buildroot}/%{_bindir}
ln -s %{_libdir}/%{name}/%{name} %{buildroot}/%{_bindir}/%{name}-vm

# Handle the desktop file, since it can be run as a GUI.
mkdir -p %{buildroot}/%{_datadir}/pixmaps
cp -a misc/icons/Factor_48x48.png %{buildroot}/%{_datadir}/pixmaps/%{name}.png

desktop-file-install \
--dir=%{buildroot}%{_datadir}/applications \
%{SOURCE1}

# Some cleanup to make rpmlint happy.
find %{buildroot}%{_libdir}/%{name} -type f -exec chmod -x {} \;
chmod +x %{buildroot}/%{_libdir}/%{name}/%{name} %{buildroot}/%{_libdir}/%{name}/misc/bash/cdfactor.sh
find %{buildroot} -size 0 -delete

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc license.txt readme.html
%{_bindir}/%{name}-vm
%{_libdir}/%{name}
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop

%changelog
* Sun May 5 2013 Ricky Elrod <codeblock@fedoraproject.org> - 0.96-1
- Latest upstream.

* Sat Mar 10 2012 Ricky Elrod <codeblock@fedoraproject.org> - 0.94-1
- Initial build.
