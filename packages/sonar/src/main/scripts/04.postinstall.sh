# Initial installation
if [ "$1" = "1" ]; then
  mkdir -p -m775 @{destBase}/{conf,logs,temp,work,webapps}
  mkdir -p -m775 @{appWorkFolder}/conf
  chown -R @{appUserName}:@{appGroupName} @{destBase}
  chown -R @{appUserName}:@{appGroupName} @{appWorkFolder}

  cd /etc/rc.d/init.d
  ln -sf tomcat @{appServiceName}

  chkconfig --add @{appServiceName}
fi

# Workaround for BUG: http://jira.codehaus.org/browse/MRPM-89
chown -R root:root @{destConf}

# Link back from /etc
ln -sf @{destConf}/server.xml @{destBase}/conf/server.xml
ln -sf @{destConf}/context.xml @{destBase}/conf/context.xml
ln -sf @{destConf}/web.xml @{destBase}/conf/web.xml
ln -sf @{destConf}/catalina.policy @{destBase}/conf/catalina.policy
ln -sf @{destConf}/catalina.properties @{destBase}/conf/catalina.properties

ln -sf @{destConf}/logback.xml @{appWorkFolder}/conf/logback.xml
ln -sf @{destConf}/sonar.properties @{appWorkFolder}/conf/sonar.properties

# Recompile WAR
echo Building...
cd @{appWorkFolder}/war
chmod +x build-war.sh
chmod +x apache-ant-*/bin/ant
./build-war.sh > /dev/null 2>&1
rm -rf @{destBase}/webapps/@{appServiceName}
mv build/sonar-server @{destBase}/webapps/@{appServiceName}
rm -f sonar.war