# Initial installation
if [ "$1" = "1" ]; then
  mkdir -p -m775 @{destBase}/{logs,temp,work}
  chown :@{appGroupName} @{destBase}/{logs,temp,work}
  mkdir -p -m775 @{appWorkFolder}
  chown :@{appGroupName} @{appWorkFolder}

  cd /etc/rc.d/init.d
  ln -sf tomcat @{appServiceName}

  chkconfig --add @{appServiceName}
fi

# Workaround for BUG: http://jira.codehaus.org/browse/MRPM-89
chown -R root:root @{destConf}

# Link back from /etc
ln -sf @{destConf} @{destBase}/conf
