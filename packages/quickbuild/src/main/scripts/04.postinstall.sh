# Make scripts executable
chmod -R 755 @{destBase}/bin/*.sh

# Install MySQL connector (do this before installation or upgrade)
mv @{destBase}/mysql-connector-java-*.jar @{destBase}/plugins/com.pmease.quickbuild.libs

# Initial installation => install service
if [ "$1" = "1" ]; then
  # Configure startup script
  sed -i 's|chkconfig: 2345 20 80|chkconfig: 2345 70 20|g' @{destBase}/bin/server.sh
  sed -i 's|PIDDIR="."|PIDDIR="/var/run/@{appServiceName}"|g' @{destBase}/bin/server.sh
  sed -i 's|#RUN_AS_USER=|RUN_AS_USER=@{appUserName}|g' @{destBase}/bin/server.sh

  # Perform installation (as root ?)
  @{destBase}/bin/server.sh install

  # Link back from /etc
  rm -rf @{destBase}/conf
  ln -sf @{destConf} @{destBase}/conf
fi

# Upgrade
if [ "$1" = "2" ]; then
  echo Starting inplace upgrade...
  su - @{appUserName} -c "@{destBase}/bin/upgrade.sh @{destBase}.old && rm -rf @{destBase} && mv @{destBase}.old @{destBase}"
fi
