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


Upgrade
-------

Since version 7, run `upgrade.sh` instead of `migrate.sh`. This requires a temporary new installation,
you then run `upgrade.sh <absolute_path_to_old_directory>` to upgrade the old installation in place.

It's a bit tricky because the upgrade tool (started by `upgrade.sh`, but actually written in java) does
a lot of stuff (copying files, etc) and breaks if you symlink the conf directory (source and target would
be the same). You'll also get these errors in the RPM cleanup process, because the files have already been
removed by the upgrade, so there's nothing left to remove for RPM: 

~~~
warning:    erase unlink of /home/quickbuild/quickbuild/plugins/com.pmease.quickbuild_7.0.11.jar failed: No such file or directory
warning:    erase unlink of /home/quickbuild/quickbuild/plugins/com.pmease.quickbuild.plugin.versionupdater_7.0.11.jar failed: No such file or directory
warning:    erase unlink of /home/quickbuild/quickbuild/plugins/com.pmease.quickbuild.plugin.versionbumper_7.0.11.jar failed: No such file or directory
warning:    erase unlink of /home/quickbuild/quickbuild/plugins/com.pmease.quickbuild.plugin.tracker.trac_7.0.11.jar failed: No such file or directory
~~~

The solution would be to rewrite the SPEC file by hand and exclude this files from monitoring by RPM. 

The `VM warning: ignoring option MaxPermSize=256m; support was removed in 8.0` is a problem inside `upgrade.sh`
so we don't care here.



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


### TODO with Puppet:

* prepare a template for hibernate.properties so that the settings below
  MySQL comments are modified and not the ones below H2.

    hibernate.dialect=org.hibernate.dialect.MySQLDialect
    hibernate.connection.driver_class=com.mysql.jdbc.Driver
    hibernate.connection.url=jdbc:mysql://localhost:3306/quickbuild
    hibernate.connection.username=root
    hibernate.connection.password=mysql



References
----------
http://wiki.pmease.com/display/QB50/Server+Installation+Guide
http://forum.pmease.com/viewtopic.php?f=1&t=1435
