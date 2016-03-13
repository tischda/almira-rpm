===============================================================================
almira.rpm.tomcat-native
===============================================================================

Overview
--------
Apache Tomcat Native RPM.


Customization
-------------
The original spec does not work and the package is not even named correctly.

Our spec file is inspired from Fedora's, we just changed a few dependencies so
that we can build with java 7.

http://rpm.pbone.net/index.php3/stat/3/srodzaj/2/search/tomcat-native-1.1.27-1.el6.src.rpm

On CentOS 6 you now need a recent version of OpenSSL. Since this is not available,
you must compile and install it manually:

~~~
cd /usr/src
wget https://www.openssl.org/source/openssl-1.0.2-latest.tar.gz
tar -zxf openssl-1.0.2*.tar.gz
cd openssl-1.0.2*
./config --prefix=/usr
make
make test
make install

# check
openssl version
cat /usr/include/openssl/opensslv.h | grep OPENSSL_VERSION_TEXT
~~~


Update
------
To update version number, update Version: in tomcat-native.spec and rebuild.
