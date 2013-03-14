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

# Link back from /etc
ln -sf @{destConf} @{destBase}/conf
