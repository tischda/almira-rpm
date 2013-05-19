===============================================================================
almira.rpm.tomcat-native
===============================================================================

Overview
--------
Apache Tomcat Native RPM.


Customization
-------------
Unpacking the source package and replacing the existing spec file so we can
build it directly with 'rpmbuild -tb' command.

The original spec does not work and the package is not even named correctly,
so we repack from jni/native into tomcat-native-${version}.tar.gz


Update
------
To update version number, update Version: in tomcat-native.spec and rebuild.