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
│   ├── apache-activemq-5.13.0-bin.tar.gz
│   └── wrapper.conf.patch
└── SPECS
    └── activemq.spec

~~~
wget http://mir2.ovh.net/ftp.apache.org/dist/activemq/5.13.0/apache-activemq-5.13.0-bin.tar.gz
tar xf apache-activemq-5.13.0-bin.tar.gz
mv apache-activemq-5.13.0 apache-activemq-5.13.0.orig
tar xf apache-activemq-5.13.0-bin.tar.gz
~~~

Update
------

What has changed ?

~~~
diff apache-activemq-5.12.1.orig/bin/linux-x86-64/activemq apache-activemq-5.13.0/bin/linux-x86-64/activemq
diff apache-activemq-5.12.1.orig/bin/linux-x86-64/wrapper.conf apache-activemq-5.13.0/bin/linux-x86-64/wrapper.conf
~~~

--> ok, nothing has changed.


Changes
-------
edit files that need patching in {package}, or if installed, copy from:
    /etc/rc.d/init.d/activemq
    /etc/activemq/wrapper.conf

~~~
cp /etc/rc.d/init.d/activemq  apache-activemq-5.13.0/bin/linux-x86-64/activemq
cp /etc/activemq/wrapper.conf apache-activemq-5.13.0/bin/linux-x86-64/wrapper.conf

diff -Nur apache-activemq-5.13.0.orig/bin/linux-x86-64/activemq apache-activemq-5.13.0/bin/linux-x86-64/activemq > activemq.patch
diff -Nur apache-activemq-5.13.0.orig/bin/linux-x86-64/wrapper.conf apache-activemq-5.13.0/bin/linux-x86-64/wrapper.conf > wrapper.conf.patch
~~~

Rebuild
-------
copy patches to rpmbuild/SOURCES

~~~
cd /d u:\src\almira\rpm\packages\apache-activemq\SOURCES\
scp root@luke:/root/activemq-update/*.patch .
~~~

TODO: replace '%define amqhome /usr/share/activemq' by prefix
