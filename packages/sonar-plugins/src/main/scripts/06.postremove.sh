# Remove last version of package: 0                         
if [ "$1" = "0" ] ; then
    echo "@{project.artifactId}-@{appVersion} has been removed from the system"
fi    
