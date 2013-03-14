# Uninstall or Update => stop service    
if [ "$1" = "0" -o "$1" = "2" ]; then
	service @{appServiceName} stop
fi
