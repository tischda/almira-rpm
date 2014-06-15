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

SPEC file created by adapting Fedora's spec file:

    rpm2cpio cmake-3.0.0-0.11.rc6.fc21.src.rpm | cpio -mi \*.spec
    rpm2cpio cmake-3.0.0-0.11.rc6.fc21.src.rpm | cpio -mi cmake-init.el
    rpm2cpio cmake-3.0.0-0.11.rc6.fc21.src.rpm | cpio -mi macros.cmake


Removed:

    Patches and GUI
    Documentation     (python-sphinx and python-docutils are too old)
    Emacs cmake mode  (requires emacs, we don't want emacs as prereq for cmake)


Layout:

rpmbuild/
├── SOURCES
│   ├── cmake-3.0.0.tar.gz
│   ├── cmake-init.el
│   └── macros.cmake
└── SPECS
    └── cmake.spec


rm -rf BUILD BUILDROOT RPMS SRPMS
rpmbuild -D '%_topdir %(echo $PWD)' -ba SPECS/cmake.spec

RPM will be located in rpmbuild/RPMS/x86_64


Manpages
--------
Before you can compile manpages, you need:

   yum install python-devel
   wget https://bitbucket.org/pypa/setuptools/raw/bootstrap/ez_setup.py
   python ez_setup.py
   easy_install sphinx
   easy_install pygments
   easy_install markupsafe
   sphinx-build --version
