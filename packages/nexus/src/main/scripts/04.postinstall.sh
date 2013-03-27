# Initial installation
if [ "$1" = "1" ]; then
  mkdir -p @{appWorkFolder}
  chkconfig --add @{appServiceName}
fi

# Make wrapper executable
chmod -R 755 @{destBase}/bin/jsw/linux-x86-64

# Link back from /etc
ln -sf @{destConf}/jetty.xml @{destBase}/conf/jetty.xml
ln -sf @{destConf}/logback.xml @{destBase}/conf/logback.xml
ln -sf @{destConf}/nexus.properties @{destBase}/conf/nexus.properties
ln -sf @{destConf}/wrapper.conf @{destBase}/bin/jsw/conf/wrapper.conf
