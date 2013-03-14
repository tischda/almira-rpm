# Cannot create symlinks with <softlinkSource>, so let's simply overwrite the
# files with symlinks. BUG: http://jira.codehaus.org/browse/MRPM-83

chmod -R 755 @{destBase}/bin
ln -sf @{destConf}/m2.conf @{destBase}/bin/m2.conf
ln -sf @{destConf}/settings.xml @{destBase}/conf/settings.xml
