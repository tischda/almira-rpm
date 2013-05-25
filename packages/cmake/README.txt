===============================================================================
almira.rpm.cmake
===============================================================================

Overview
--------
CMake is a family of tools designed to build, test and package software. CMake
is used to control the software compilation process using simple platform and
compiler independent configuration files. CMake generates native makefiles and
workspaces that can be used in the compiler environment of your choice.


Build
-----
yum install rpm-build gcc gcc-c++ make ncurses-devel

rpmbuild/
├── SOURCES
│   └── cmake-2.8.11.tar.gz
└── SPECS
    └── cmake.spec


rm -rf BUILD BUILDROOT RPMS SRPMS
rpmbuild -D '%_topdir %(echo $PWD)' -ba SPECS/cmake.spec

RPM will be located in rpmbuild/RPMS/x86_64
