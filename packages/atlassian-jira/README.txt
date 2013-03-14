===============================================================================
almira.rpm.atlassian-jira
===============================================================================

Overview
--------
Atlassian Jira.


Customization
-------------
Copied server.xml and web.xml from original distribution.
Changed port in server.xml to 8085.
Copied libraries to lib
dbconfig.xml


TODO
----
- hardcoded $CATALINA_HOME in startup script. Environment variables defined in
  /etc/profile.d/catalina.sh are not available here.
   

References
----------
https://confluence.atlassian.com/display/JIRA/Installing+JIRA+WAR
