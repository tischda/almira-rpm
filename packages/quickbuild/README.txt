===============================================================================
almira.rpm.quickbuild
===============================================================================

Overview
--------
PMEase Quickbuild RPM.


Customization
-------------
Ran bin/server.sh install to generate /etc/init.d/quickbuild and added to RPM.
Then I added/changed the following:

    QUICKBUILD_HOME="@{destBase}"

    # Wrapper
    WRAPPER_CMD="$QUICKBUILD_HOME/bin/wrapper"
    WRAPPER_CONF="$QUICKBUILD_HOME/conf/wrapper.conf"

    PIDDIR="/var/run/@{appServiceName}"

    RUN_AS_USER=@{appUserName}


Added the following line ine wrapper.conf

    wrapper.java.additional.4=-XX:MaxPermSize=256m


Edited hibernate.properties to use MySQL instead of embedded database.

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

Click on root, Settings, Advanced Setting, Edit
    Workspace Directory Setting
        -> Select 'Use Specified workspace directory'
            Path: /home/quickbuild/workspace/${configuration.pathName}
    Save


References
----------
http://wiki.pmease.com/display/QB50/Server+Installation+Guide
http://forum.pmease.com/viewtopic.php?f=1&t=1435