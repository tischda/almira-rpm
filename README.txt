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


Installation ("c:\windows\System32\tree.com" /A /F dist | find /v ".url")
------------
Copy binary files to 'dist' directory:

+---apache-activemq
|       apache-activemq-5.10.0-bin.tar.gz
|
+---apache-ant
|       apache-ant-1.9.4-bin.tar.gz
|       apache-ivy-2.3.0-bin-with-deps.tar.gz
|
+---apache-httpd
|   |   apr-1.5.0.tar.bz2
|   |   apr-util-1.5.3.tar.bz2
|   |   distcache-1.4.5-23.src.rpm
|   |   httpd-2.4.9.tar.bz2
|   |
|   \---deps
|           httpd-2.4.9-deps.tar.bz2
|
+---apache-maven
|       apache-maven-3.2.1-bin.tar.gz
|
+---apache-tomcat
|   |   apache-tomcat-7.0.52.tar.gz
|   |
|   \---extra
|           catalina-jmx-remote.jar
|           catalina-ws.jar
|           tomcat-juli-adapters.jar
|           tomcat-juli.jar
|
+---atlassian-jira
|   |   atlassian-jira-6.2.7-patched.tar.gz
|   |   mysql-connector-java-5.1.31.tar.gz
|   |
|   \---patch
|       |   README.txt
|       |   spring-2.5.6.SEC03-atlassian-1.jar
|       |
|       +---original.6.2.2
|       |       atlassian-plugins-osgi-3.0.12.jar
|       |
|       +---original.6.2.3
|       |       atlassian-plugins-osgi-3.0.12.jar
|       |
|       +---original.6.2.4
|       |       atlassian-plugins-osgi-3.0.12.jar
|       |
|       +---original.6.2.7
|       |       atlassian-plugins-osgi-3.0.12.jar
|       |
|       +---patched.6.2.1
|       |       atlassian-plugins-osgi-3.0.12.jar.6.2.1-patched
|       |
|       \---patched.6.2.2
|               atlassian-plugins-osgi-3.0.12.jar
|
+---cmake
|       cmake-3.0.0.tar.gz
|
+---git
|       git-2.0.0.tar.gz
|       git-manpages-2.0.0.tar.gz
|       git.spec
|       perl-YAML-0.84-1.2.noarch.rpm
|       README.txt
|
+---nexus
|       nexus-2.8.1-01.war
|
+---oracle-mysql
|       MySQL-client-5.6.19-1.el6.x86_64.rpm
|       MySQL-devel-5.6.19-1.el6.x86_64.rpm
|       MySQL-server-5.6.19-1.el6.x86_64.rpm
|       MySQL-shared-5.6.19-1.el6.x86_64.rpm
|       MySQL-shared-compat-5.6.19-1.el6.x86_64.rpm
|
+---quickbuild
|       mysql-connector-java-5.1.31.tar.gz
|       quickbuild-5.1.29.tar.gz
|
+---sonar
|       README.md
|       sonar-plugins-4.3-1.zip
|       sonarqube-4.3.1.zip
|
\---tomcat-native
        tomcat-native-1.1.30-src.tar.gz


References
----------
http://blog.quilitz.de/2010/03/checkout-sub-directories-in-git-sparse-checkouts/comment-page-1/#comment-3146
http://stackoverflow.com/questions/4114887/is-it-possible-to-do-a-sparse-checkout-without-checking-out-the-whole-repository


Knows Issues
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

