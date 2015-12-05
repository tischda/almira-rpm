# Make scripts executable
chmod 755 @{destBase}/bin/nexus
chmod 755 @{destBase}/bin/jsw/linux-x86-64/wrapper

# Configure startup script
sed -i 's|PIDDIR="."|PIDDIR="/var/run/@{appServiceName}"|g' @{destBase}/bin/nexus
sed -i 's|#RUN_AS_USER=|RUN_AS_USER=@{appUserName}|g' @{destBase}/bin/nexus

# Fix user rights
chown -R @{appUserName}:@{appGroupName} @{destBase}
chown -R @{appUserName}:@{appGroupName} @{appWorkFolder}

# Initial installation
if [ "$1" = "1" ]; then
  cd /etc/rc.d/init.d
  ln -sf @{destBase}/bin/nexus @{appServiceName}

  mkdir /var/run/@{appServiceName}
  chown -R @{appUserName}:@{appGroupName} /var/run/@{appServiceName}

  chkconfig --add @{appServiceName}
fi

# Workaround for BUG: http://jira.codehaus.org/browse/MRPM-89
chown -R root:root @{destConf}

# Link back  conf -> /etc/nexus
rm -rf @{destBase}/conf
ln -sf @{destConf} @{destBase}/conf
