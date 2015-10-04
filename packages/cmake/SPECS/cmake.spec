%define rpm_macros_dir %{_sysconfdir}/rpm

Name:           cmake
Version:        3.3.2
Release:        1%{?dist}
Summary:        Cross-platform make system

Group:          Development/Tools

License:        BSD and MIT and zlib
URL:            http://www.cmake.org
Source0:        http://www.cmake.org/files/v3.3/cmake-%{version}%{?rcver}.tar.gz
Source1:        cmake-init.el
Source2:        macros.cmake
# See https://bugzilla.redhat.com/show_bug.cgi?id=1202899
Source3:        cmake.attr
Source4:        cmake.prov

# Patch to find DCMTK in Fedora (bug #720140)
Patch0:         cmake-dcmtk.patch
# Patch to fix FindRuby vendor settings
# http://public.kitware.com/Bug/view.php?id=12965
# https://bugzilla.redhat.com/show_bug.cgi?id=822796
Patch2:         cmake-findruby.patch
# Fix issue with redhat-hardened-ld
# http://www.cmake.org/Bug/view.php?id=15737
# https://bugzilla.redhat.com/show_bug.cgi?id=1260490
Patch3:         cmake.git-97ffbcd8.patch

## upstream patches
# some post v3.3.1 tag commits
Patch624:       0624-FindBoost-Add-support-for-Boost-1.59.patch
Patch640:       0640-FindPkgConfig-remove-variable-dereference.patch

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: gcc-c++
BuildRequires: ncurses-devel
BuildRequires: python-devel

# https://fedorahosted.org/fpc/ticket/555
Provides: bundled(kwsys)

%description
CMake is used to control the software compilation process using simple
platform and compiler independent configuration files. CMake generates
native makefiles and workspaces that can be used in the compiler
environment of your choice. CMake is quite sophisticated: it is possible
to support complex environments requiring system configuration, preprocessor
generation, code generation, and template instantiation.


%package        doc
Summary:        Documentation for %{name}
Group:          Development/Tools
Requires:       %{name} = %{version}-%{release}

%description    doc
This package contains documentation for CMake.


%prep
%setup -q -n %{name}-%{version}
%patch0 -p1
%patch2 -p1
%patch3 -p1
%patch624 -p1
%patch640 -p1

%build
export CFLAGS="%{optflags}"
export CXXFLAGS="%{optflags}"
mkdir build
pushd build

../bootstrap --prefix=%{_prefix} --datadir=/share/%{name} \
             --docdir=/share/doc/%{name} --mandir=/share/man \
             --no-system-libs \
             --parallel=`/usr/bin/getconf _NPROCESSORS_ONLN`
make VERBOSE=1 %{?_smp_mflags}


%install
rm -rf %{buildroot}
pushd build
make install DESTDIR=%{buildroot}
find %{buildroot}/%{_datadir}/%{name}/Modules -type f | xargs chmod -x
popd

# Install bash completion symlinks
mkdir -p %{buildroot}%{_datadir}/bash-completion/completions
for f in %{buildroot}%{_datadir}/%{name}/completions/*
do
  ln -s ../../%{name}/completions/$(basename $f) %{buildroot}%{_datadir}/bash-completion/completions/
done

# RPM macros
install -p -m0644 -D %{SOURCE2} %{buildroot}%{rpm_macros_dir}/macros.cmake
sed -i -e "s|@@CMAKE_VERSION@@|%{version}|" %{buildroot}%{rpm_macros_dir}/macros.cmake
touch -r %{SOURCE2} %{buildroot}%{rpm_macros_dir}/macros.cmake
%if 0%{?_rpmconfigdir:1}
# RPM auto provides
install -p -m0644 -D %{SOURCE3} %{buildroot}%{_prefix}/lib/rpm/fileattrs/cmake.attr
install -p -m0755 -D %{SOURCE4} %{buildroot}%{_prefix}/lib/rpm/cmake.prov
%endif
mkdir -p %{buildroot}%{_libdir}/%{name}

# Install copyright files for main package
cp -p Copyright.txt %{buildroot}/%{_docdir}/%{name}/
find Source Utilities -type f -iname copy\* | while read f
do
  fname=$(basename $f)
  dir=$(dirname $f)
  dname=$(basename $dir)
  cp -p $f %{buildroot}/%{_docdir}/%{name}/${fname}_${dname}
done


%check
unset DISPLAY
pushd build


#CMake.FileDownload, and CTestTestUpload require internet access
bin/ctest -V -E 'CMake.FileDownload|CTestTestUpload' %{?_smp_mflags}
popd


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%dir %{_docdir}/%{name}
%{_docdir}/%{name}/Copyright.txt*
%{_docdir}/%{name}/COPYING*
%{rpm_macros_dir}/macros.cmake
%if 0%{?_rpmconfigdir:1}
%{_prefix}/lib/rpm/fileattrs/cmake.attr
%{_prefix}/lib/rpm/cmake.prov
%endif
%{_bindir}/ccmake
%{_bindir}/cmake
%{_bindir}/cpack
%{_bindir}/ctest
%{_datadir}/aclocal/cmake.m4
%{_datadir}/bash-completion/
%{_datadir}/%{name}/
%{_libdir}/%{name}/

%files doc
%{_docdir}/%{name}/


%changelog
* Thu Sep 17 2015 Orion Poplawski <orion@cora.nwra.com> - 3.3.2-1
- Update to 3.3.2
- Fix test exclusion

* Fri Sep 11 2015 Orion Poplawski <orion@cora.nwra.com> - 3.3.1-5
- Apply upstream patch to fix Fortran linker detection with redhat-hardened-ld
  (bug #1260490)

* Wed Sep 9 2015 Orion Poplawski <orion@cora.nwra.com> - 3.3.1-4
- Apply upstream patch to fix trycompile output (bug #1260490)

* Tue Aug 25 2015 Rex Dieter <rdieter@fedoraproject.org> 3.3.1-3
- pull in some upstream fixes (FindPkgConfig,boost-1.59)

* Fri Aug 21 2015 Rex Dieter <rdieter@fedoraproject.org> 3.3.1-2
- Provides: bundled(kwsys)

* Thu Aug 13 2015 Orion Poplawski <orion@cora.nwra.com> - 3.3.1-1
- Update to 3.3.1

* Thu Jul 23 2015 Orion Poplawski <orion@cora.nwra.com> - 3.3.0-1
- Update to 3.3.0

* Thu Jul 9 2015 Orion Poplawski <orion@cora.nwra.com> - 3.3.0-0.4.rc3
- Update to 3.3.0-rc3
- Fix cmake.attr to handle 32-bit libraries

* Tue Jun 23 2015 Orion Poplawski <orion@cora.nwra.com> - 3.3.0-0.3.rc2
- Update to 3.3.0-rc2

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.0-0.2.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 8 2015 Orion Poplawski <orion@cora.nwra.com> - 3.3.0-0.1.rc1
- Update to 3.3.0-rc1

* Mon Jun 8 2015 Orion Poplawski <orion@cora.nwra.com> - 3.2.3-1
- Update to 3.2.3

* Wed Apr 15 2015 Orion Poplawski <orion@cora.nwra.com> - 3.2.2-1
- Update to 3.2.2

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 3.2.1-5
- Add an AppData file for the software center

* Mon Mar 23 2015 Daniel Vrátil <dvratil@redhat.com> - 3.2.1-4
- cmake.prov: handle exceptions

* Wed Mar 18 2015 Rex Dieter <rdieter@fedoraproject.org> 3.2.1-3
- cmake.prov: use /usr/bin/python (instead of /bin/python)

* Tue Mar 17 2015 Rex Dieter <rdieter@fedoraproject.org> 3.2.1-2
- RFE: CMake automatic RPM provides  (#1202899)

* Wed Mar 11 2015 Orion Poplawski <orion@cora.nwra.com> - 3.2.1-1
- Update to 3.2.1

* Thu Feb 26 2015 Orion Poplawski <orion@cora.nwra.com> - 3.2.0-0.2.rc2
- Update to 3.2.0-rc2
- Drop C++11 ABI workaround, fixed in gcc
- Drop strict_aliasing patch fixed upstream long ago
- Drop FindLua52, FindLua should work now for 5.1-5.3

* Sun Feb 15 2015 Orion Poplawski <orion@cora.nwra.com> - 3.2.0-0.1.rc1
- Update to 3.2.0-rc1
- Drop ninja patch fixed upstream
- Upstream now ships icons, add icon-cache scriptlets

* Fri Feb 13 2015 Orion Poplawski <orion@cora.nwra.com> - 3.1.3-1
- Update to 3.1.3

* Sat Feb 7 2015 Orion Poplawski <orion@cora.nwra.com> - 3.1.2-1
- Update to 3.1.2

* Fri Jan 23 2015 Orion Poplawski <orion@cora.nwra.com> - 3.1.1-1
- Update to 3.1.1
- Drop ruby patch applied upstream

* Sat Jan 17 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.1.0-2
- Fix ruby 2.2.0 teeny (0) detection

* Wed Dec 17 2014 Orion Poplawski <orion@cora.nwra.com> - 3.1.0-1
- Update to 3.1.0 final
