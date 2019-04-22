===============================================================================
almira.rpm.apache-activemq
===============================================================================

Overview
--------
Apache ActiveMQ RPM.


Build
-----
yum install rpm-build

rpmbuild/
├── SOURCES
│   ├── activemq.patch
│   ├── apache-activemq-5.15.9-bin.tar.gz
│   └── wrapper.conf.patch
└── SPECS
    └── activemq.spec

Update
------

Obtain new version:

~~~
NEW_VERSION=5.15.9
wget http://www.apache.org/dist/activemq/${NEW_VERSION}/apache-activemq-${NEW_VERSION}-bin.tar.gz
tar xf apache-activemq-${NEW_VERSION}-bin.tar.gz
~~~

What has changed ?

~~~
OLD_VERSION=5.15.3
wget http://archive.apache.org/dist/activemq/${OLD_VERSION}/apache-activemq-${OLD_VERSION}-bin.tar.gz
tar xf apache-activemq-${OLD_VERSION}-bin.tar.gz

diff apache-activemq-${OLD_VERSION}/bin/linux-x86-64/activemq apache-activemq-${NEW_VERSION}/bin/linux-x86-64/activemq
diff apache-activemq-${OLD_VERSION}/bin/linux-x86-64/wrapper.conf apache-activemq-${NEW_VERSION}/bin/linux-x86-64/wrapper.conf
~~~

--> ok, nothing has changed.


Changes
-------
edit files that need patching in {package}, or if installed, copy from:
    /etc/rc.d/init.d/activemq
    /etc/activemq/wrapper.conf

~~~
# Create a copy of new version
mv apache-activemq-${NEW_VERSION} apache-activemq-${NEW_VERSION}.orig
tar xf apache-activemq-${NEW_VERSION}-bin.tar.gz

# Compare modified files to latest version
cp /etc/rc.d/init.d/activemq  apache-activemq-${NEW_VERSION}/bin/linux-x86-64/activemq
cp /etc/activemq/wrapper.conf apache-activemq-${NEW_VERSION}/bin/linux-x86-64/wrapper.conf

diff -Nur apache-activemq-${NEW_VERSION}.orig/bin/linux-x86-64/activemq apache-activemq-${NEW_VERSION}/bin/linux-x86-64/activemq > activemq.patch
diff -Nur apache-activemq-${NEW_VERSION}.orig/bin/linux-x86-64/wrapper.conf apache-activemq-${NEW_VERSION}/bin/linux-x86-64/wrapper.conf > wrapper.conf.patch
~~~

Rebuild
-------
copy patches to rpmbuild/SOURCES

~~~
cd /d u:\src\almira\rpm\packages\apache-activemq\SOURCES\
scp root@luke:/root/activemq-update/*.patch .
~~~

TODO: replace '%define amqhome /usr/share/activemq' by prefix
