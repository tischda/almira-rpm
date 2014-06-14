%define amqhome /usr/share/activemq

Name: apache-activemq
Version: 5.10.0
Release: 1%{?dist}
Summary: ActiveMQ Messaging Broker
Group: System Environment/Daemons
License: ASL 2.0
URL: http://activemq.apache.org/
Source0: http://www.apache.org/dist/activemq/%{name}/%{version}/%{name}-%{version}-bin.tar.gz
Patch0: activemq.patch
Patch1: wrapper.conf.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch: x86_64

%description
ActiveMQ Messaging Broker.


%package client
Summary: Client jar for Apache ActiveMQ
Group: System Environment/Libraries

%description client
Client jar for Apache ActiveMQ.


%prep
%setup -q -n %{name}-%{version}
%patch0 -p1
%patch1 -p1


%build


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/etc/init.d
mkdir -p $RPM_BUILD_ROOT/var/run/activemq

mkdir -p $RPM_BUILD_ROOT%{amqhome}
mv * $RPM_BUILD_ROOT%{amqhome}

mkdir -p $RPM_BUILD_ROOT/usr/bin
pushd $RPM_BUILD_ROOT/usr/bin
    ln -s %{amqhome}/bin/activemq-admin activemq-admin
    ln -s %{amqhome}/bin/activemq activemq
popd

mv $RPM_BUILD_ROOT%{amqhome}/conf $RPM_BUILD_ROOT/etc/activemq
pushd $RPM_BUILD_ROOT%{amqhome}
    ln -s /etc/activemq conf
popd

mkdir -p $RPM_BUILD_ROOT/var/lib/activemq/data
# this shuld be blank - it comes with an empty logfile
rm -rf $RPM_BUILD_ROOT/%{amqhome}/data
pushd $RPM_BUILD_ROOT%{amqhome}
    ln -s /var/lib/activemq/data data
popd

mkdir -p $RPM_BUILD_ROOT%{_javadir}
mv $RPM_BUILD_ROOT%{amqhome}/activemq-all-%{version}.jar \
    $RPM_BUILD_ROOT%{_javadir}/activemq-all-%{version}.jar
(cd %{buildroot}%{_javadir} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)

# Fix up binaries
mv $RPM_BUILD_ROOT%{amqhome}/bin/linux-x86-64/wrapper.conf $RPM_BUILD_ROOT/etc/activemq
mv $RPM_BUILD_ROOT%{amqhome}/bin/linux-x86-64/activemq $RPM_BUILD_ROOT/etc/init.d
mv $RPM_BUILD_ROOT%{amqhome}/bin/linux-x86-64/libwrapper.so $RPM_BUILD_ROOT%{amqhome}/bin
mv $RPM_BUILD_ROOT%{amqhome}/bin/linux-x86-64/wrapper $RPM_BUILD_ROOT%{amqhome}/bin
rm -rf $RPM_BUILD_ROOT%{amqhome}/bin/linux-x86-32
rm -rf $RPM_BUILD_ROOT%{amqhome}/bin/linux-x86-64
rm -rf $RPM_BUILD_ROOT%{amqhome}/bin/macosx

# Fix up permissions (rpmlint complains)
find $RPM_BUILD_ROOT%{amqhome}/webapps -perm 755 -type f -exec chmod -x '{}' \;
find $RPM_BUILD_ROOT%{amqhome}/examples/stomp/ruby -name \*.rb -type f -exec chmod +x '{}' \;


%clean
rm -rf $RPM_BUILD_ROOT


%pre
# Add the "activemq" user and group
# we need a shell to be able to use su - later
getent group activemq > /dev/null || /usr/sbin/groupadd -g 92 -r activemq 2> /dev/null || :
getent passwd activemq > /dev/null || /usr/sbin/useradd -c "Apache ActiveMQ" -u 92 -g activemq -s /bin/bash -r -d /usr/share/activemq activemq 2>/dev/null || :


%post
/sbin/chkconfig --add activemq


%preun
if [ $1 = 0 ]; then
    [ -f /var/lock/subsys/activemq ] && /etc/init.d/activemq stop
    [ -f /etc/init.d/activemq ] && /sbin/chkconfig --del activemq
fi


%files
%defattr(-,root,root,-)
%config(noreplace) %attr(644,root,root) /etc/activemq/*
%attr(0755,root,root) /etc/init.d/activemq
%attr(0755,root,root) /usr/bin/activemq
%attr(0755,root,root) /usr/bin/activemq-admin
%attr(755,activemq,activemq) %dir /var/run/activemq
%attr(755,activemq,activemq) /var/lib/activemq
%{amqhome}


%files client
%defattr(-,root,root,-)
%{_javadir}


%changelog
* Fri Oct 25 2013 Daniel Tischer <dos.7182@gmail.com> - 5.9.0-3
- rebuild for 5.9.0
- updated wrapper.conf 5.8.0 -> 5.9.0

* Sun May 12 2013 Daniel Tischer <dos.7182@gmail.com> - 5.8.0-1
- rebuild for 5.8.0
- removed dependency on jre to support oracle jdk
- removed options for snapshots and 32 bit
- reset package name to its default
- named patches after the files they modify

* Thu Dec 20 2012 Zhigang Wang <w1z2g3@gmail.com> - 5.7.0-1
- rebuild for 5.7.0

* Thu Jan 06 2011 James Casey <james.casey@cern.ch> - 5.4.2-1
- rebuild for 5.4.2

* Sun Nov 07 2010 James Casey <jamesc.000@gmail.com> - 5.4.1-1
- rebuild for 5.4.1

* Tue May 18 2010 James Casey <james.casey@cern.ch> - 5.4-1
- rebuild for 5.4

* Tue May 18 2010 James Casey <james.casey@cern.ch> - 5.3.2-3
- Fix bug where /var/lib/activemq/data would not be installed

* Tue May 18 2010 James Casey <james.casey@cern.ch> - 5.3.2-2
- Rename package to activemq from apache-activemq
- Integrated comments from Marc Schöchlin
- moved /var/cache/activemq to /var/lib/activemq
- added dependency on java
- Fixed file permissions (executable bit set on many files)
- Fixed rpmlint errors
- move platform dependant binaries to /usr/lib

* Fri May 07 2010 James Casey <james.casey@cern.ch> - 5.3.2-1
- First version of specfile
