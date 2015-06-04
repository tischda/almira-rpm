===============================================================================
almira-rpm
===============================================================================

Overview
--------
Maven PRM source packages.


Sources
-------
git clone git://github.com/tischda/almira-rpm.git


Dependencies
------------
Binaries are not checked into VCS.
To package the 'dist' directory, execute 'mvn assembly:single'


Installation
------------
Copy binary files to 'dist' directory:

+---apache-activemq
|       apache-activemq-5.11.1-bin.tar.gz
|
+---apache-httpd
|   |   apr-1.5.1.tar.bz2
|   |   apr-util-1.5.4.tar.bz2
|   |   distcache-1.4.5-23.src.rpm
|   |   httpd-2.4.12.tar.bz2
|   |
|   \---deps
|           httpd-2.4.12-deps.tar.bz2
|
+---apache-maven
|       apache-maven-3.3.3-bin.tar.gz
|
+---apache-tomcat
|   |   apache-tomcat-7.0.62.tar.gz
|   |
|   \---extra
|           catalina-jmx-remote.jar
|           catalina-ws.jar
|           tomcat-juli-adapters.jar
|           tomcat-juli.jar
|
+---atlassian-jira
|       atlassian-jira-6.4.5.tar.gz
|       mysql-connector-java-5.1.35.tar.gz
|
+---cmake
|       cmake-3.2.3.tar.gz
|
+---git
|       git-2.4.2.tar.gz
|       git-manpages-2.4.2.tar.gz
|       perl-YAML-0.84-1.2.noarch.rpm
|
+---java
|       jdk-8u45-linux-x64.rpm
|
+---nexus
|       nexus-2.11.3-01.war
|
+---oracle-mysql
|       MySQL-client-5.6.25-1.el6.x86_64.rpm
|       MySQL-devel-5.6.25-1.el6.x86_64.rpm
|       MySQL-server-5.6.25-1.el6.x86_64.rpm
|       MySQL-shared-5.6.25-1.el6.x86_64.rpm
|       MySQL-shared-compat-5.6.25-1.el6.x86_64.rpm
|
+---quickbuild
|       mysql-connector-java-5.1.35.tar.gz
|       quickbuild-6.0.17.tar.gz
|
+---rsync
|       rsync-3.1.1.tar.gz
|
+---sonar
|       README.md
|       sonar-plugins-5.1-1.zip
|       sonarqube-5.1.zip
|
\---tomcat-native
        tomcat-native-1.1.33-src.tar.gz
                

References
----------
http://blog.quilitz.de/2010/03/checkout-sub-directories-in-git-sparse-checkouts/comment-page-1/#comment-3146
http://stackoverflow.com/questions/4114887/is-it-possible-to-do-a-sparse-checkout-without-checking-out-the-whole-repository


Known Issues
------------
You need to specify <filemode> when specifying username and groupname, the
RPM plugin misses the defaults:

    <mapping>
        <directory>/var/run/${appServiceName}</directory>
        <username>${appUserName}</username>
        <groupname>${appGroupName}</groupname>
        <filemode>755</filemode>
    </mapping>

   will become:

    %files
    %defattr(644,root,root,755)
    %attr(755,quickbuild,quickbuild) "/home/quickbuild/quickbuild"
    %dir %attr(755,quickbuild,quickbuild) "/var/run/quickbuild"
               ^--- if not specified, it will be 644 and override the default

Another perhaps related problem is that intermediate directories in the path are
not created with default username:

    <mapping>
        <directory>${destBase}/bin</directory>
    </mapping>                 ^----- if you don't specify, 'bin' belongs to root
    <mapping>
        <directory>${destBase}/bin/jsw</directory>
                                   ^----- should belong to default username

Finally, because of the previous issue, when you do excludes, all files are
listed but not the containing directory, which now also gets owned by root.

See also:
    http://jira.codehaus.org/browse/MRPM-89
    http://jira.codehaus.org/browse/MRPM-8
    http://jira.codehaus.org/browse/MRPM-68

