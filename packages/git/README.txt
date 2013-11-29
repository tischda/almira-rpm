===============================================================================
almira.rpm.git
===============================================================================

Overview
--------
Man pages for Git.


Build
-----
Source structure:

rpmbuild/
├── SOURCES
│   └── git-manpages-1.8.5.tar.gz
└── SPECS
    └── git-manpages.spec


rm -rf BUILD BUILDROOT RPMS SRPMS
rpmbuild -D '%_topdir %(echo $PWD)' -ba SPECS/git-manpages.spec

RPM will be located in rpmbuild/RPMS/noarch
