# Create user and group
getent group @{appGroupName} > /dev/null || groupadd -r @{appGroupName}
getent passwd @{appUserName} > /dev/null || useradd -r -m -g @{appGroupName} @{appUserName}

# Uninstall or Update => stop service
if [ "$1" = "0" -o "$1" = "2" ]; then
  service @{appServiceName} stop
fi

# Update => Save old folder
if [ "$1" = "2" ]; then
  echo Backing up old version for upgrade
  mv @{destBase} @{destBase}.old
fi
