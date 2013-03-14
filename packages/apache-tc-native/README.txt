===============================================================================
almira.rpm.apache-tc-native
===============================================================================

Overview
--------
Apache Tomcat Native RPM. This is a binary package linked against package APR
version 1.3.9 that comes with CentOS 6 and Oracle JDK 6. To build from source:

yum install gcc make apr-devel openssl-devel
export CATALINA_HOME=/opt/apache-tomcat

tar xzvf tomcat-native-1.1.24-src.tar.gz
cd tomcat-native-1.1.24-src/jni/native
./configure --with-apr=/usr/bin/apr-1-config --with-ssl=/usr/include/openssl --with-java-home=/usr/java/default --prefix=$CATALINA_HOME
make && make install
