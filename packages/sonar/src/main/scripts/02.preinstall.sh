# Create user and group
getent group @{appGroupName} > /dev/null || groupadd -r @{appGroupName}
getent passwd @{appUserName} > /dev/null || useradd -r -m -g @{appGroupName} @{appUserName}

# Uninstall or Update => stop service
if [ "$1" = "0" -o "$1" = "2" ]; then
    service @{appServiceName} stop
fi

# When we update, make sure we remove old versions and start clean
if [ "$1" = "2" ]; then
  rm -rf @{destBase}/temp/*
  rm -rf @{destBase}/work/*
  rm -rf @{destBase}/webapps/*

  # RPM removes old versions *after* postinstall... uh, this is ugly:
  rm -rf  @{appWorkFolder}/{extensions,extras,lib,temp,war}
fi
