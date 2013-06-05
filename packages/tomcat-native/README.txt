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


Update
------
To update version number, update Version: in tomcat-native.spec and rebuild.