# Initial installation                          
if [ "$1" = "1" ]; then
	mkdir -p -m775 @{destConf}/Catalina/localhost
	chown -R :@{appGroupName} @{destConf}/Catalina

  chmod 775 @{destBase}/{temp,logs,work}
  chown -R :@{appGroupName} @{destBase}/{logs,temp,work}

	chkconfig --add @{appServiceName}
fi

# Link back from /etc
ln -sf @{destConf} @{destBase}/conf 

export CATALINA_HOME=@{destBase}
chmod 755 @{destBase}/bin/*.sh
