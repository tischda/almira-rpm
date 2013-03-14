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
Sonar 3.4.1 does not work with MySQL 5.6. This is fixed in 3.5:
  http://jira.codehaus.org/browse/SONAR-4137

When 3.5 is released, replace sonar.properties with sonar.properties.mysql and
adapt puppet scripts accordingly. For now, stick with H2.
