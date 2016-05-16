# Create user and group
getent group @{appGroupName} > /dev/null || groupadd -r @{appGroupName}
getent passwd @{appUserName} > /dev/null || useradd -r -m -g @{appGroupName} @{appUserName}

# Uninstall or Update => stop service
if [ "$1" = "0" -o "$1" = "2" ]; then
  service @{appServiceName} stop

  # TODO: first stop fails, not sure why...
  sleep 10
  service @{appServiceName} stop
fi

# When we update, make sure we're clean
if [ "$1" = "2" ]; then
  rm -rf @{destBase}/temp/*
  rm -rf @{destBase}/work/*
  rm -rf @{destBase}/webapps/*

  echo Clearing @{appWorkFolder}/plugins/installed-plugins
  rm -f @{appWorkFolder}/plugins/installed-plugins/*
fi
