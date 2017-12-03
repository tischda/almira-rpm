Name: tomcat-native
Version: 1.2.16
Release: 1%{?dist}
Summary: Tomcat native library
License: Apache Software License
Group: System Environment/Libraries

URL: http://tomcat.apache.org/tomcat-7.0-doc/apr.html
Source0: http://www.apache.org/dist/tomcat/tomcat-connectors/native/%{version}/source/%{name}-%{version}-src.tar.gz

BuildRequires: apr-devel >= 1.5.2, openssl

Provides: tcnative = %{version}-%{release}

%description
The Apache Tomcat Native Library provides portable API for features
not found in contemporary JDK's. It uses Apache Portable Runtime as
operating system abstraction layer and OpenSSL for SSL networking and
allows optimal performance in production environments.


%prep
%setup -q -n %{name}-%{version}-src

%build
cd native

# Yes we're running old CentOS with old - but patched - openssl, so we disable the check.
# Alternative: http://svn.apache.org/repos/asf/tomcat/native/trunk/download_deps.sh

%configure \
    --disable-openssl-version-check \
    --with-apr=%{_bindir}/apr-1-config
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
%make_install -C native
# Perhaps a devel package sometime?  Not for now; no headers are installed.
rm -f $RPM_BUILD_ROOT%{_libdir}/libtcnative*.*a
rm -rf $RPM_BUILD_ROOT%{_libdir}/pkgconfig


%files
%doc CHANGELOG.txt LICENSE NOTICE TODO.txt
%{_libdir}/libtcnative*.so*


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig
