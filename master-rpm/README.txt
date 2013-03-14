===============================================================================
almira.rpm.master-rpm
===============================================================================

Overview
--------
Parent POM for Almira RPMs.

Hierarchy: distribution -> versions -> plugins -> master-rpm -> project

Split up into several files.

We use <relativepath> to speed up development and avoid dependency issues when
compiling (e.g. master poms not deployed).

You need to checkout the master-pom together with the rest of the code.

Note that current structure (within almira.configuration) does not allow for
individual module release via maven-release-plugin. We consider releasing RPMs
as a consistent group as part of the environment profile.

Tagging a release of almira-configuration will fix the version of each
individual RPM module. 



Quickstart
----------

For each module, the RPM is created by running:

    mvn package
    
The generated RPM will be stored in:

    target\rpm\<module>\RPMS\<arch>\
    
    
Notes
-----
To build on Windows (generated RPMs won't run on Unix), see :

    http://crlog.info/2012/09/11/building-rpms-on-windows/


Plugins configured, update with:  mvn versions:display-plugin-updates

    http://maven.apache.org/plugins/maven-clean-plugin/plugin-info.html
    http://maven.apache.org/plugins/maven-compiler-plugin/plugin-info.html
    http://maven.apache.org/plugins/maven-dependency-plugin/plugin-info.html
    http://maven.apache.org/plugins/maven-deploy-plugin/plugin-info.html
    http://maven.apache.org/plugins/maven-install-plugin/plugin-info.html
    http://maven.apache.org/plugins/maven-project-info-reports-plugin/plugin-info.html
    http://maven.apache.org/plugins/maven-resources-plugin/plugin-info.html
    http://maven.apache.org/plugins/maven-site-plugin/plugin-info.html
    http://mojo.codehaus.org/versions-maven-plugin/plugin-info.html
    http://mojo.codehaus.org/rpm-maven-plugin/plugin-info.html



Package Upgrades
----------------
1. Upgrade artifact <version> and reset last digit to 1 
2. Change <app.version> in pom.xml
3. Reset <app.release> to 1 in pom.xml
4. Test with 'mvn package'
5. Update CHANGES.txt
6. Commit changes to VCS
7. mvn release:clean
8. mvn release:prepare
9. Update <app.release> to 2 in pom.xml (new snapshot version)

10. checkout on sysrepo
11. mvn package
12. cp .rpm from target to /share/CentOS/6/addons/<architecture>
12. createrepo /share/CentOS/6/addons/<architecture>



TODO
----
- use <changelogFile> to integrate the change log in the RPM. Note: The current 
  formatting of CHANGES.txt does not work, it must be:
  
    * [dow mon dd yyyy] [packager [email address]] [RPM version]
     -list of changes  

- do not filter shell script on ${}, this will fail if variables are defined locally


Known problems
--------------
* rpm-maven-plugin: ${project.build.directory} fails on windows


References
----------
http://stackoverflow.com/questions/8930251/maven-unpack-zip-artifact-to-a-specific-folder-name
http://stackoverflow.com/questions/11222982/tomcat-binary-distribution-zip-as-maven-artifact
http://stackoverflow.com/questions/3264064/unpack-zip-in-zip-with-maven
http://crlog.info/2012/09/11/building-rpms-on-windows/
http://stnor.wordpress.com/category/devops/
http://code.google.com/p/webdroid-tomcat-package/source/browse/trunk/src/main/rpm/tomcat.spec?r=2
http://serverfault.com/questions/82193/creating-symlink-in-usr-bin-when-creating-an-rpm
http://maven.40175.n5.nabble.com/RPMs-for-Maven-3-td5569139i40.html
http://thomaswabner.wordpress.com/2010/02/16/howto-disable-inherited-maven-plugin/
https://blogs.oracle.com/sreekanth/entry/java_lang_noclassdeffounderror_org_codehaus
http://stackoverflow.com/questions/7398834/rpm-upgrade-uninstalls-the-rpm
http://www.linuxquestions.org/questions/linux-newbie-8/useradd-r-option-and-system-account-question-892978/

    