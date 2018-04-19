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
Binaries are not checked into VCS. This is what you need in your `dist` directory:

~~~
+---apache-activemq
|       apache-activemq-5.15.3-bin.tar.gz
|
+---apache-httpd
|       apr-1.6.3.tar.bz2
|       apr-util-1.6.1.tar.bz2
|       distcache-1.4.5-23.src.rpm
|       httpd-2.4.33.tar.bz2
|
+---apache-maven
|       apache-maven-3.5.3-bin.tar.gz
|
+---apache-tomcat
|   |   apache-tomcat-7.0.86.tar.gz
|   |
|   \---extras
|           catalina-jmx-remote.jar
|           catalina-ws.jar
|           tomcat-juli-adapters.jar
|           tomcat-juli.jar
|
+---atlassian-jira-software
|       atlassian-jira-software-7.9.0.tar.gz
|       mysql-connector-java-5.1.46.tar.gz
|
+---cmake
|       cmake-3.9.6.tar.gz
|
+---git
|       git-2.17.0.tar.gz
|       git-manpages-2.17.0.tar.gz
|       git.spec.template
|
+---gradle
|       gradle-4.6-bin.zip
|
+---java
|       jdk-8u162-linux-x64.rpm
|
+---nexus
|       nexus-2.14.8-01-bundle.tar.gz
|
+---oracle-mysql
|       MySQL-client-5.6.38-1.el6.x86_64.rpm
|       MySQL-devel-5.6.38-1.el6.x86_64.rpm
|       MySQL-server-5.6.38-1.el6.x86_64.rpm
|       MySQL-shared-5.6.38-1.el6.x86_64.rpm
|       MySQL-shared-compat-5.6.38-1.el6.x86_64.rpm
|
+---quickbuild
|       mysql-connector-java-5.1.46.tar.gz
|       quickbuild-8.0.2.tar.gz
|
+---rsync
|       rsync-3.1.3.tar.gz
|
+---sonar
|   |   sonarqube-7.0.zip
|   |
|   +---plugins (add to zip in extensions_plugins)
|   |       sonar-csharp-plugin-7.0.1.4822.jar
|   |       sonar-go-plugin-0.2.0.875.jar
|   |       sonar-java-plugin-5.3.0.13828.jar
|   |       sonar-javascript-plugin-4.1.0.6085.jar
|   |       sonar-php-plugin-2.13.0.3107.jar
|   |       sonar-python-plugin-1.9.1.2080.jar
|   |       sonar-scm-git-plugin-1.4.0.1037.jar
|   |       sonar-xml-plugin-1.5.0.1373.jar
|   |
|   \---plugins-legacy
|           sonar-cxx-plugin-0.9.8.jar
|           sonar-scm-mercurial-plugin-1.1.1.jar
|           sonar-timeline-plugin-1.5.jar
|           sonar-typescript-plugin-1.1.0.1079.jar
|
\---tomcat-native
        tomcat-native-1.2.16-src.tar.gz
~~~


References
----------
* http://blog.quilitz.de/2010/03/checkout-sub-directories-in-git-sparse-checkouts/comment-page-1/#comment-3146
* http://stackoverflow.com/questions/4114887/is-it-possible-to-do-a-sparse-checkout-without-checking-out-the-whole-repository


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

