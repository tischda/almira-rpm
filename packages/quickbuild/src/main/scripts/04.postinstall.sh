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

# Upgrade
if [ "$1" = "2" ]; then
  echo Starting inplace upgrade...
  su - @{appUserName} -c "@{destBase}.new/bin/upgrade.sh @{destBase} && rm -rf @{destBase}.new"
fi

# Install MySQL connector (do this after the migration which copies old libs)
rm -f @{destBase}/plugins/com.pmease.quickbuild.libs/mysql-connector-java-*.jar
mv @{destBase}/mysql-connector-java-*.jar @{destBase}/plugins/com.pmease.quickbuild.libs
