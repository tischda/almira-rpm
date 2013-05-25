Name: cmake
Version: 2.8.11
Release: 1%{?dist}
Summary: Cross-platform make system

Group: Development/Tools

License: BSD and MIT and zlib
URL: http://www.cmake.org
Source0: http://www.cmake.org/files/v2.8/cmake-%{version}%{?rcver}.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: gcc-c++
BuildRequires: ncurses-devel

#BuildRequires: gcc-gfortran
#BuildRequires: bzip2-devel
#BuildRequires: curl-devel
#BuildRequires: expat-devel
#BuildRequires: libarchive-devel
#BuildRequires: zlib-devel
#BuildRequires: xmlrpc-c-devel
#BuildRequires: qt4-devel, desktop-file-utils

%description
CMake is used to control the software compilation process using simple 
platform and compiler independent configuration files. CMake generates 
native makefiles and workspaces that can be used in the compiler 
environment of your choice. CMake is quite sophisticated: it is possible 
to support complex environments requiring system configuration, preprocessor
generation, code generation, and template instantiation.


%prep
%setup -q -n cmake-%{version}


%build
export CFLAGS="$RPM_OPT_FLAGS"
export CXXFLAGS="$RPM_OPT_FLAGS"
mkdir build
pushd build
../bootstrap --prefix=%{_prefix} --datadir=/share/%{name} \
             --docdir=/share/doc/%{name}-%{version} --mandir=/share/man \
             --no-system-libs \
             --parallel=`/usr/bin/getconf _NPROCESSORS_ONLN`
make VERBOSE=1 %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
pushd build
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT/%{_datadir}/%{name}/Modules -type f | xargs chmod -x
popd
cp -a Example $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/
mkdir -p $RPM_BUILD_ROOT%{_datadir}/emacs/site-lisp/cmake
install -m 0644 Docs/cmake-mode.el $RPM_BUILD_ROOT%{_datadir}/emacs/site-lisp/cmake/cmake-mode.el


%check
unset DISPLAY
pushd build
# exclude (-E) tests that require internet access and https://bugzilla.redhat.com/show_bug.cgi?format=multiple&id=828467
bin/ctest -V -E CMake.HTML -E CTestTestUpload -E AllFindModules
popd


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%{_docdir}/%{name}-%{version}/
%{_bindir}/ccmake
%{_bindir}/cmake
%{_bindir}/cpack
%{_bindir}/ctest
%{_datadir}/aclocal/cmake.m4
%{_datadir}/%{name}/
%{_mandir}/man1/*
%{_datadir}/emacs/site-lisp/cmake

