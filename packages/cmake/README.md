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
yum install rpm-build gcc gcc-c++ make ncurses-devel python-devel

Before you compile, you also need (manpages):

   yum install python-devel
   wget https://bitbucket.org/pypa/setuptools/raw/bootstrap/ez_setup.py
   python ez_setup.py
   easy_install sphinx
   easy_install pygments
   easy_install markupsafe
   sphinx-build --version


SPEC file is adapted from Fedora's spec file:

    rpm2cpio cmake-3.4.2-1.fc24.src.rpm | cpio -mi \*.spec
    rpm2cpio cmake-3.4.2-1.fc24.src.rpm | cpio -mi \*.patch
    rpm2cpio cmake-3.4.2-1.fc24.src.rpm | cpio -mi cmake.attr
    rpm2cpio cmake-3.4.2-1.fc24.src.rpm | cpio -mi cmake.prov
    rpm2cpio cmake-3.4.2-1.fc24.src.rpm | cpio -mi cmake-init.el
    rpm2cpio cmake-3.4.2-1.fc24.src.rpm | cpio -mi macros.cmake


Removed:

    GUI and Emacs     (we don't want this as prereq to install cmake)
    Manpages          (cmake-gui doc not packaged fails build)


Layout:

    rpmbuild/
    ├── SOURCES
    │   ├── cmake.attr
    │   ├── cmake.prov
    │   ├── cmake-dcmtk.patch
    │   ├── cmake-findruby.patch
    │   ├── cmake-init.el
    │   └── macros.cmake
    └── SPECS
        └── cmake.spec


Build:

    rm -rf BUILD BUILDROOT RPMS SRPMS
    rpmbuild -D '%_topdir %(echo $PWD)' -ba SPECS/cmake.spec

RPM will be located in rpmbuild/RPMS/x86_64
