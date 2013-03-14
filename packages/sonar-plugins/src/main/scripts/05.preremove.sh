# Remove last version of package: 0                         
if [ "$1" = "0" ] ; then
	service @{appServiceName} stop
fi
