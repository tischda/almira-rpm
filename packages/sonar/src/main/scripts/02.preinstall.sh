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
  rm -f  @{appWorkFolder}/extensions/plugins/*
fi

echo `date` > /tmp/sonar-rpm-install.log
echo "destbase is @{destBase}" >> /tmp/sonar-rpm-install.log
echo "PRE *****************" >> /tmp/sonar-rpm-install.log
ls -al /home/sonar/sonar >> /tmp/sonar-rpm-install.log
echo "PRE *****************" >> /tmp/sonar-rpm-install.log
ls @{appWorkFolder}/war/sonar-server/WEB-INF/lib >> /tmp/sonar-rpm-install.log
