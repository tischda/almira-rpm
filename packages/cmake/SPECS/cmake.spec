%define rpm_macros_dir %{_sysconfdir}/rpm

Name:           cmake
Version:        3.2.1
Release:        2%{?dist}
Summary:        Cross-platform make system

Group:          Development/Tools

License:        BSD and MIT and zlib
URL:            http://www.cmake.org
Source0:        http://www.cmake.org/files/v3.2/cmake-%{version}%{?rcver}.tar.gz
Source1:        cmake-init.el
Source2:        macros.cmake

# Patch to find DCMTK in Fedora (bug #720140)
Patch0:         cmake-dcmtk.patch
# Patch to fix FindRuby vendor settings
# http://public.kitware.com/Bug/view.php?id=12965
# https://bugzilla.redhat.com/show_bug.cgi?id=822796
Patch2:         cmake-findruby.patch

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: gcc-c++
BuildRequires: ncurses-devel
BuildRequires: python-devel


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


%build
export CFLAGS="$RPM_OPT_FLAGS"
export CXXFLAGS="$RPM_OPT_FLAGS"
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
# ModuleNotices fails for some unknown reason, and we don't care
# CMake.HTML currently requires internet access
# CTestTestUpload requires internet access
# CPackComponentsForAll-RPM-IgnoreGroup test fails: [http://www.cmake.org/Bug/view.php?id=15442]
bin/ctest -V -E ModuleNotices -E CMake.HTML -E CTestTestUpload -E CPackComponentsForAll-RPM-IgnoreGroup %{?_smp_mflags}
popd


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%dir %{_docdir}/%{name}
%{_docdir}/%{name}/Copyright.txt*
%{rpm_macros_dir}/macros.cmake
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

* Sat Nov 15 2014 Orion Poplawski <orion@cora.nwra.com> - 3.1.0-0.2.rc2
- Update to 3.1.0-rc2

* Wed Oct 29 2014 Orion Poplawski <orion@cora.nwra.com> - 3.1.0-0.1.rc1
- Update to 3.1.0-rc1

* Mon Sep 15 2014 Dan Horák <dan[at]danny.cz> - 3.0.2-2
- fix FindJNI for ppc64le (#1141782)

* Sun Sep 14 2014 Orion Poplawski <orion@cora.nwra.com> - 3.0.2-1
- Update to 3.0.2

* Mon Aug 25 2014 Orion Poplawski <orion@cora.nwra.com> - 3.0.1-3
- Update wxWidgets patches

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Aug 6 2014 Orion Poplawski <orion@cora.nwra.com> - 3.0.1-1
- Update to 3.0.1

* Thu Jul 03 2014 Rex Dieter <rdieter@fedoraproject.org> 3.0.0-2
- optimize mimeinfo scriptlet

* Sat Jun 14 2014 Orion Poplawski <orion@cora.nwra.com> - 3.0.0-1
- Update to 3.0.0 final

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.0-0.11.rc6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 27 2014 Orion Poplawski <orion@cora.nwra.com> - 3.0.0-0.10.rc6
- Update to 3.0.0-rc6

* Wed May 14 2014 Orion Poplawski <orion@cora.nwra.com> - 3.0.0-0.9.rc5
- Update to 3.0.0-rc5
- Drop icon patch applied upstream

* Tue Apr 22 2014 Orion Poplawski <orion@cora.nwra.com> - 3.0.0-0.8.rc4
- Update to 3.0.0-rc4

* Thu Apr 10 2014 Orion Poplawski <orion@cora.nwra.com> - 3.0.0-0.7.rc3
- Fix doc duplication

* Fri Apr 4 2014 Orion Poplawski <orion@cora.nwra.com> - 3.0.0-0.6.rc3
- Rebase patches to prevent .orig files in Modules
- Add install check for .orig files

* Wed Mar 26 2014 Orion Poplawski <orion@cora.nwra.com> - 3.0.0-0.5.rc3
- Update to 3.0.0-rc3
- Add patch to fix FindwxWidgets when cross-compiling for Windows (bug #1081207)

* Wed Mar 5 2014 Orion Poplawski <orion@cora.nwra.com> - 3.0.0-0.4.rc1
- Add additional FindPythonLibs patch from upstream (bug #1072964)

* Mon Mar 3 2014 Orion Poplawski <orion@cora.nwra.com> - 3.0.0-0.3.rc1
- Update to upstreams version of FindPythonLibs patch

* Mon Mar 3 2014 Orion Poplawski <orion@cora.nwra.com> - 3.0.0-0.2.rc1
- Use symlinks for bash completions

* Fri Feb 28 2014 Orion Poplawski <orion@cora.nwra.com> - 3.0.0-0.1.rc1
- Update to 3.0.0-rc1
- Update qtdeps patch to upstreamed version
- Install bash completions

