===============================================================================
almira.rpm.sonar
===============================================================================

Overview
--------
Sonar - Continuous Code Quality Management (http://www.sonarsource.com/)


Customization
-------------
Copied server.xml, web.xml and context.xml from original Tomcat distribution.
Changed port in server.xml to 9000.

Provided sonar.properties preconfigured for mysql. This also avoids conversion
with dos2unix.

Notes
-----
We probably should update the MySQL JDBC driver to 5.1.24 to support MySQL 5.6