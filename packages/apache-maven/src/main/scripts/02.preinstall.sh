# Create user and group
getent group @{appGroupName} > /dev/null || groupadd -r @{appGroupName}
getent passwd @{appUserName} > /dev/null || useradd -r -m -g @{appGroupName} @{appUserName}
