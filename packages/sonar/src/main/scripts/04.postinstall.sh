# Make scripts executable
chmod -R 755 @{destBase}/bin/linux-x86-64/*.sh
chmod -R 755 @{destBase}/bin/linux-x86-64/wrapper

# Configure startup script
sed -i 's|chkconfig: 2345 20 80|chkconfig: 2345 70 20|g' @{destBase}/bin/linux-x86-64/sonar.sh
sed -i 's|PIDDIR="."|PIDDIR="/var/run/@{appServiceName}"|g' @{destBase}/bin/linux-x86-64/sonar.sh
sed -i 's|#RUN_AS_USER=|RUN_AS_USER=@{appUserName}|g' @{destBase}/bin/linux-x86-64/sonar.sh

# Fix user rights
chown -R @{appUserName}:@{appGroupName} @{destBase}

# Initial installation
if [ "$1" = "1" ]; then
  cd /etc/rc.d/init.d
  ln -sf @{destBase}/bin/linux-x86-64/sonar.sh @{appServiceName}

  chkconfig --add @{appServiceName}
fi

# Workaround for BUG: http://jira.codehaus.org/browse/MRPM-89
chown -R root:root @{destConf}

# Link back from /etc
mkdir -p @{destBase}/conf
ln -sf @{destConf}/sonar.properties @{destBase}/conf/sonar.properties
ln -sf @{destConf}/wrapper.conf @{destBase}/conf/wrapper.conf
