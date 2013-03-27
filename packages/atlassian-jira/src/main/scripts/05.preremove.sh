# Remove last version of package: 0
if [ "$1" = "0" ] ; then
  service @{appServiceName} stop
  chkconfig --del @{appServiceName}
  rm -rf /var/run/@{appServiceName}.pid
  rm -rf @{destBase}
fi
