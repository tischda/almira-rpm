# Install MySQL connector
mv @{destBase}/mysql-connector-java-*.jar @{destBase}/plugins/com.pmease.quickbuild.libs

# Make scripts executable
chmod -R 755 @{destBase}/bin/*.sh

# Configure startup script
sed -i 's|chkconfig: 2345 20 80|chkconfig: 2345 70 20|g' @{destBase}/bin/server.sh
sed -i 's|PIDDIR="."|PIDDIR="/var/run/@{appServiceName}"|g' @{destBase}/bin/server.sh
sed -i 's|#RUN_AS_USER=|RUN_AS_USER=@{appUserName}|g' @{destBase}/bin/server.sh

# Initial installation => install service
if [ "$1" = "1" ]; then
  @{destBase}/bin/server.sh install
fi

# Link back from /etc
rm -rf @{destBase}/conf
ln -sf @{destConf} @{destBase}/conf

# Migrate data and remove old
if [ "$1" = "2" ]; then
  echo Starting migration...
  su - @{appUserName} -c "@{destBase}/bin/migrate.sh @{destBase}.old && rm -rf @{destBase}.old"
fi
