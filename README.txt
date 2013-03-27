===============================================================================
rpm
===============================================================================

Overview
--------
Maven PRM source packages.


Sources
-------
git clone git://github.com/tischda/rpm.git


Dependencies
------------
Binaries are not checked into VCS.

To package the 'dist' directory, execute 'mvn assembly:single'


Installation
------------
Copy binary files to 'dist' directory:

+---apache-ant
|       apache-ant-1.8.4-bin.tar.gz
|       apache-ivy-2.2.0-bin-with-deps.tar.gz
|
+---apache-maven
|       apache-maven-3.0.4-bin.tar.gz
|
+---apache-tc-native
|   |   apache-tc-native-1.1.24.tar.gz
|   |
|   \---src
|           apr-1.4.6.tar.gz
|           apr-iconv-1.2.1.tar.gz
|           apr-util-1.5.1.tar.gz
|           tomcat-native-1.1.24-src.tar.gz
|
+---apache-tomcat
|   |   apache-tomcat-7.0.35.tar.gz
|   |
|   \---extra
|           catalina-jmx-remote.jar
|           catalina-ws.jar
|           tomcat-juli-adapters.jar
|           tomcat-juli.jar
|
+---atlassian-jira
|       atlassian-jira-5.2.4.1.tar.gz
|
+---atlassian-jira-plugins
|       jira-dvcs-connector-plugin-1.2.6.jar
|
+---nexus
|       nexus-2.3.0-04-bundle.tar.gz
|
+---sonar
|       sonar-3.4.1.zip
|
\---sonar-plugins
        sonar-plugins-3.1-bundle.zip


References
----------
http://blog.quilitz.de/2010/03/checkout-sub-directories-in-git-sparse-checkouts/comment-page-1/#comment-3146
http://stackoverflow.com/questions/4114887/is-it-possible-to-do-a-sparse-checkout-without-checking-out-the-whole-repository


Knows Issues
------------
You need to specify <filemode> when specifyint username and groupname, the
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
                ^--- if not specified, it will be 644 and overrides the default

See also:
    http://jira.codehaus.org/browse/MRPM-89
    http://jira.codehaus.org/browse/MRPM-8
    http://jira.codehaus.org/browse/MRPM-68

