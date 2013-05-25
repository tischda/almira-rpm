===============================================================================
almira.rpm.cmake
===============================================================================

Overview
--------
CMake.


Build
-----
yum install rpm-build

rpmbuild/
├── SOURCES
│   └── cmake-2.8.11.tar.gz
└── SPECS
    └── cmake.spec


rm -rf BUILD BUILDROOT RPMS SRPMS
rpmbuild -D '%_topdir %(echo $PWD)' -ba SPECS/cmake.spec

RPM will be located in rpmbuild/RPMS/x86_64
