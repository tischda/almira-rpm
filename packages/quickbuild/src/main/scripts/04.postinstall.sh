# Install MySQL connector
mv @{destBase}/mysql-connector-java-*.jar @{destBase}/plugins/com.pmease.quickbuild.libs

# Make scripts executable
chmod -R 755 @{destBase}/bin/*.sh

# Initial installation => install service and link configuration to /etc
if [ "$1" = "1" ]; then
  @{destBase}/bin/server.sh install
  ln -sf @{destBase}/conf @{destConf}
fi

# Configure startup script
sed -i 's|PIDDIR="."|PIDDIR="/var/run/@{appServiceName}"|g' @{destBase}/bin/server.sh
sed -i 's|#RUN_AS_USER=|RUN_AS_USER=@{appUserName}|g' @{destBase}/bin/server.sh

# Migrate data and remove old
if [ "$1" = "2" ]; then
  @{destBase}/bin/migrate.sh @{destBase}.old && rm -rf @{destBase}.old
fi
