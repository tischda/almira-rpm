# Make scripts executable
chmod -R 755 @{destBase}.new/bin/*.sh

# Initial installation => install service
if [ "$1" = "1" ]; then
  mv @{destBase}.new @{destBase}

  # Configure startup script
  sed -i 's|chkconfig: 2345 20 80|chkconfig: 2345 70 20|g' @{destBase}/bin/server.sh
  sed -i 's|PIDDIR="."|PIDDIR="/var/run/@{appServiceName}"|g' @{destBase}/bin/server.sh
  sed -i 's|#RUN_AS_USER=|RUN_AS_USER=@{appUserName}|g' @{destBase}/bin/server.sh

  # Perform installation
  @{destBase}/bin/server.sh install

  # Link back from /etc
  rm -rf @{destBase}/conf
  ln -sf @{destConf} @{destBase}/conf
fi

# Upgrade
if [ "$1" = "2" ]; then
  echo Starting inplace upgrade...
  su - @{appUserName} -c "@{destBase}.new/bin/upgrade.sh @{destBase} && rm -rf @{destBase}.new"
fi

# Install MySQL connector (do this after the uprade which copies old libs)
rm -f @{destBase}/plugins/com.pmease.quickbuild.libs/mysql-connector-java-*.jar 2>/dev/null
mv @{destBase}/mysql-connector-java-*.jar @{destBase}/plugins/com.pmease.quickbuild.libs
