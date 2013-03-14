# Remove last version of package: 0                         
if [ "$1" = "0" ] ; then
	service @{appServiceName} stop
	rm -f @{destBase}/lib/libtcnative-1.so
	rm -f @{destBase}/lib/libtcnative-1.so.0
fi
