# Create user and group
getent group @{appGroupName} > /dev/null || groupadd -r @{appGroupName}
getent passwd @{appUserName} > /dev/null || useradd -r -m -g @{appGroupName} @{appUserName}

# Uninstall or Update => stop service
if [ "$1" = "0" -o "$1" = "2" ]; then
  service @{appServiceName} stop
fi

# Update => Save old folder
# Removing symlinks because update.sh will copy its files to this location
# But because it iselfs has them linked to /etc/quickbuild, this will not work
if [ "$1" = "2" ]; then
  echo Making a copy of the configuration
  rm -f @{destBase}/conf
  su - @{appUserName} -c "cp -r @{destConf} @{destBase}/conf"

  echo Backing up old version for upgrade
  rm -rf @{destBase}.old
  mv @{destBase} @{destBase}.old
fi
