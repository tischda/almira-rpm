# Initial installation
if [ "$1" = "1" ]; then
  mkdir -p -m775 @{destBase}/{conf,logs,temp,work}
  mkdir -p -m775 @{appWorkFolder}/conf
  chown -R @{appUserName}:@{appGroupName} @{destBase}
  chown -R @{appUserName}:@{appGroupName} @{appWorkFolder}

  cd /etc/rc.d/init.d
  ln -sf tomcat @{appServiceName}

  chkconfig --add @{appServiceName}
fi

# When we update, make sure we're clean
if [ "$1" = "2" ]; then
  rm -rf @{destBase}/temp/*
  rm -rf @{destBase}/work/*
fi

# Workaround for BUG: http://jira.codehaus.org/browse/MRPM-89
chown -R root:root @{destConf}

# Link back from /etc
ln -sf @{destConf}/catalina.policy @{destBase}/conf/catalina.policy
ln -sf @{destConf}/catalina.properties @{destBase}/conf/catalina.properties
ln -sf @{destConf}/context.xml @{destBase}/conf/context.xml
ln -sf @{destConf}/logging.properties.xml @{destBase}/conf/logging.properties
ln -sf @{destConf}/server.xml @{destBase}/conf/server.xml
ln -sf @{destConf}/tomcat-users.xml @{destBase}/conf/tomcat-users.xml
ln -sf @{destConf}/web.xml @{destBase}/conf/web.xml
