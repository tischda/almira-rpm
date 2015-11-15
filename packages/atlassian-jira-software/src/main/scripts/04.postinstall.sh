# Initial installation
if [ "$1" = "1" ]; then
  mkdir -p -m775 @{destBase}/{conf,logs,temp,work}

  chkconfig --add @{appServiceName}
fi

# Fix user rights
chown -R @{appUserName}:@{appGroupName} @{destBase}
chown -R @{appUserName}:@{appGroupName} @{appWorkFolder}

# Workaround for BUG: http://jira.codehaus.org/browse/MRPM-89
chown -R root:root @{destConf}

# Make scripts executable
chmod -R 755 @{destBase}/bin/*.sh

# Link back from /etc
ln -sf @{destConf}/catalina.policy @{destBase}/conf/catalina.policy
ln -sf @{destConf}/catalina.properties @{destBase}/conf/catalina.properties
ln -sf @{destConf}/context.xml @{destBase}/conf/context.xml
ln -sf @{destConf}/logging.properties @{destBase}/conf/logging.properties
ln -sf @{destConf}/server.xml @{destBase}/conf/server.xml
ln -sf @{destConf}/tomcat-users.xml @{destBase}/conf/tomcat-users.xml
ln -sf @{destConf}/web.xml @{destBase}/conf/web.xml
