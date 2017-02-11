===============================================================================
almira.rpm.quickbuild
===============================================================================

Overview
--------
PMEase Quickbuild RPM.


Customization
-------------
Run 'bin/server.sh install' this creates link:

    /etc/init.d/quickbuild -> /home/quickbuild/quickbuild/bin/./server.sh

customize server.sh:

 sed -i 's|PIDDIR="."|PIDDIR="/var/run/quickbuild"|g' server.sh
 sed -i 's|#RUN_AS_USER=|RUN_AS_USER=quickbuild|g' server.sh

Since version 7, run upgrade.sh instead of migrate.sh. This requires a temporary installation with the new files,
you then run `upgrade.sh <absolute_path_to_old_directory>` to upgrade in place. It's a bit tricky because maven-rpm
is not setting owner and permissions correctly. 


TODO with Puppet:

* prepare a template for hibernate.properties so that the settings below
  MySQL comments are modified and not the ones below H2.

    hibernate.dialect=org.hibernate.dialect.MySQLDialect
    hibernate.connection.driver_class=com.mysql.jdbc.Driver
    hibernate.connection.url=jdbc:mysql://localhost:3306/quickbuild
    hibernate.connection.username=root
    hibernate.connection.password=mysql


Configuration
-------------
http://server:8810/setup

1. Setup Administrator
    Login name: admin
    Login password: admin

2. System Settings
    URL to Access QuickBuild: http://server:8810/
    Global Storage Directory: /home/quickbuild/storage

3. Email Setting
    STMP Host: localhost

4. Workspace directory (not moved during upgrade):

    Click on root, Settings, Advanced Setting, Edit
        Workspace Directory Setting
            -> Select 'Use Specified workspace directory', Path:

${groovy:
  String mypath = system.getInstallDir();
  if (node.hasAttribute( "ALMIRA_HOME" )) {
      mypath += "/workspace/" + configuration.getPathName();
  \} else {
      mypath += "/../workspace/" + configuration.getPathName();
  \};
}

    Save


References
----------
http://wiki.pmease.com/display/QB50/Server+Installation+Guide
http://forum.pmease.com/viewtopic.php?f=1&t=1435
