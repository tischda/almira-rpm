===============================================================================
almira.rpm.apache-tomcat
===============================================================================

Overview
--------
Apache Tomcat RPM.


TODO
----
- catalina.sh not very useful since this variable is not available in startup
  scripts and therefore needs to be redefined in every app using tomcat.

- Clean stop: echo SHUTDOWN | nc localhost 8005 