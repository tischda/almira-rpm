# Initial installation
if [ "$1" = "1" ]; then
  chown @{appUserName}:@{appGroupName} @{destBase}
  mkdir -p -m775 @{appWorkFolder}
  chown @{appUserName}:@{appGroupName} @{appWorkFolder}
  chkconfig --add @{appServiceName}
fi

# Make wrapper executable
chmod -R 755 @{destBase}/bin/jsw/linux-x86-64

# Workaround for BUG: http://jira.codehaus.org/browse/MRPM-89
chown -R root:root @{destConf}

# Link back from /etc
ln -sf @{destConf}/jetty.xml @{destBase}/conf/jetty.xml
ln -sf @{destConf}/logback.xml @{destBase}/conf/logback.xml
ln -sf @{destConf}/nexus.properties @{destBase}/conf/nexus.properties
ln -sf @{destConf}/wrapper.conf @{destBase}/bin/jsw/conf/wrapper.conf
