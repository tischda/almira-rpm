#!/bin/sh

version=`grep Version tomcat-native.spec | sed -e 's/Version: \(.*\)/\1/'`

# remove old files
rm -rf  SOURCES BUILD BUILDROOT RPMS SRPMS

# extract source package
tar xzvf tomcat-native-$version-src.tar.gz

# clean up mess in source package
cd tomcat-native-$version-src
cp CHANGELOG.txt jni/native/CHANGES
cp LICENSE jni/native/LICENSE
cp NOTICE jni/native/NOTICE
rm -f jni/native/tcnative.spec
cd ..

# create a new valid package
mv tomcat-native-$version-src/jni/native tomcat-native-$version

# inject a working spec file
cp tomcat-native.spec tomcat-native-$version
tar czvf tomcat-native-$version.tar.gz tomcat-native-$version

# build
rpmbuild -D '%_topdir %(echo $PWD)' -tb tomcat-native-$version.tar.gz
