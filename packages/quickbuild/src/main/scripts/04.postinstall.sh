# Install MySQL connector
mv @{destBase}/mysql-connector-java-*.jar @{destBase}/plugins/com.pmease.quickbuild.libs

# Make scripts executable
chmod -R 755 @{destBase}/bin/*.sh

# Initial installation => install service
if [ "$1" = "1" ]; then
  @{destBase}/bin/server.sh install
fi

# Workaround for BUG: http://jira.codehaus.org/browse/MRPM-89
chown -R root:root @{destConf}

# Link back from /etc
ln -sf @{destConf} @{destBase}/conf

# Configure startup script
sed -i 's|PIDDIR="."|PIDDIR="/var/run/@{appServiceName}"|g' @{destBase}/bin/server.sh
sed -i 's|#RUN_AS_USER=|RUN_AS_USER=@{appUserName}|g' @{destBase}/bin/server.sh

# Migrate data and remove old
if [ "$1" = "2" ]; then
  @{destBase}/bin/migrate.sh @{destBase}.old && rm -rf @{destBase}.old
fi
