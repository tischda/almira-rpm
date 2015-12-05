# Initial installation
if [ "$1" = "1" ]; then
  mkdir -p -m775 @{destBase}/{conf,logs,temp,work}

  chkconfig --add @{appServiceName}
fi

# Fix user rights
chown -R @{appUserName}:@{appGroupName} @{destBase}
chown -R @{appUserName}:@{appGroupName} @{appWorkFolder}

# Workaround for BUG: http://jira.codehaus.org/browse/MRPM-89
chown -R root:root @{destConf}

# Make scripts executable
chmod -R 755 @{destBase}/bin/*.sh

# Link back from /etc
rm -rf @{destBase}/conf
ln -sf @{destConf} @{destBase}/conf
