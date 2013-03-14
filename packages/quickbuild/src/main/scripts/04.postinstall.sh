# Initial installation
if [ "$1" = "1" ]; then
  chkconfig --add @{appServiceName}
fi

# Make scripts executable
chmod -R 755 @{destBase}/bin/*.sh

# Link back from /etc
ln -sf @{destConf}/attributes.properties @{destBase}/conf/attributes.properties 
ln -sf @{destConf}/hibernate.properties  @{destBase}/conf/hibernate.properties
ln -sf @{destConf}/log4j.properties      @{destBase}/conf/log4j.properties
ln -sf @{destConf}/node.properties       @{destBase}/conf/node.properties
ln -sf @{destConf}/wrapper.conf          @{destBase}/conf/wrapper.conf
ln -sf @{destConf}/wrapper-license.conf  @{destBase}/conf/wrapper-license.conf

# Install mysql connector
mv @{destBase}/mysql-connector-java-*.jar @{destBase}/plugins/com.pmease.quickbuild.libs 