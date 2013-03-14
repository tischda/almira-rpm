===============================================================================
almira.rpm.nexus 
===============================================================================

Overview
--------
Sonatype Nexus RPM.


Customization
-------------
Changes to the startup script:
Original is located in ${nexus_home}/bin/nexus. Copy it to src/main/etc/init.d

Change this:

    NEXUS_HOME="@{app.dest.home}"
    RUN_AS_USER=@{app.username}
    PIDDIR="${sys.pid.folder}"


Run 'mvn package'


Note that Nexus expects its default directory structure, it's quite hard to
change the location of the work directory. PLEXUS_NEXUS_WORK does not work.  



Passwords
---------
admin / admin123
deployment / deployment123


References
----------
http://www.sonatype.com/books/nexus-book/reference/install-sect-dirs.html
http://stackoverflow.com/questions/710596/how-do-i-backup-a-nexus-repository-manager
http://www.sonatype.com/people/2011/06/nexus-tips-and-tricks-backup-nexus/
