Name: tomcat-native
Version: 1.1.27
Release: 1.el6
Summary: Tomcat Native Java library
License: ASL 2.0
Vendor: Apache
URL: http://tomcat.apache.org/native-doc/
Group: System Environment/Libraries
Requires: apr >= 1.4.6
autoprov: yes
autoreq: yes
Source0: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: autoconf, libtool, apr-devel >= 1.4.6, openssl >= 1.0.0

%description
Apache Tomcat native libaries (APR).

%prep
%setup -q

%build
%configure --with-apr=%{_prefix}/bin/apr-1-config --with-ssl=yes
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
libtool --finish $RPM_BUILD_ROOT%{_libdir}

# Unpackaged files
rm -f $RPM_BUILD_ROOT%{_libdir}/tcnative.exp

%files
%defattr(-,root,root,-)
%doc CHANGES LICENSE NOTICE
%{_libdir}/libtcnative-1.so*
%{_libdir}/libtcnative-1.*a
%{_libdir}/pkgconfig/tcnative-1.pc

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun
/sbin/ldconfig

# Remove last version of package: 0
if [ "$1" = "0" ] ; then
    echo "%{name}-%{version} has been removed from the system"
fi
