===============================================================================
almira.rpm.apache-activemq
===============================================================================

Overview
--------
Apache ActiveMQ RPM.


Build
-----

rpmbuild/
├── SOURCES
│   ├── activemq.patch
│   ├── apache-activemq-5.8.0-bin.tar.gz
│   └── wrapper.conf.patch
└── SPECS
    └── activemq.spec


Download from:
http://ftp.udc.es/apache/activemq/apache-activemq/5.8.0/apache-activemq-5.8.0-bin.tar.gz

untar to {package}
mv {package} to {package}.orig
untar to {package}

edit files that need patching in {package}

diff -Nur apache-activemq-5.8.0.orig/bin/linux-x86-64/wrapper.conf apache-activemq-5.8.0/bin/linux-x86-64/activemq.conf > activemq.patch

diff -Nur apache-activemq-5.8.0.orig/bin/linux-x86-64/wrapper.conf apache-activemq-5.8.0/bin/linux-x86-64/wrapper.conf > wrapper.conf.patch

copy patches to rpmbuild/SOURCES

cd rpmbuild
rm -rf BUILD BUILDROOT RPMS SRPMS
rpmbuild -D '%_topdir %(echo $PWD)' -ba SPECS/activemq.spec

RPM will be located in:
rpmbuild/RPMS/x86_64/activemq-5.8.0-1.el6.x86_64.rpm
