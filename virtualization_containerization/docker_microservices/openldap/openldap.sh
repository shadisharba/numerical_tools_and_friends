https://github.com/wheelybird/ldap-user-manager/issues/11
https://hub.docker.com/r/wheelybird/ldap-user-manager


docker pull osixia/openldap:latest
docker pull wheelybird/ldap-user-manager

docker run --name openldap -e LDAP_ORGANISATION=example -e LDAP_DOMAIN=example.org -e LDAP_ADMIN_PASSWORD=somepassword -e LDAP_CONFIG_PASSWORD=somepassword -e LDAP_RFC2307BIS_SCHEMA=true -e LDAP_REMOVE_CONFIG_AFTER_SETUP=true -e LDAP_TLS=false -p 389:389 -p 636:636 --volume C:/Users/sha79396/Desktop/deeeeeel/openldap/var_lib_ldap:/var/lib/ldap --volume C:/Users/sha79396/Desktop/deeeeeel/openldap/etc_ldap_slapd:/etc/ldap/slapd.d osixia/openldap:latest --loglevel debug
docker stop openldap && docker rm openldap

docker run --detach --restart unless-stopped --name openldap -p 389:389 -p 636:636 -e LDAP_TLS=false --volume C:/Users/sha79396/Desktop/deeeeeel/openldap/var_lib_ldap:/var/lib/ldap --volume C:/Users/sha79396/Desktop/deeeeeel/openldap/etc_ldap_slapd:/etc/ldap/slapd.d --hostname=localhost --env KEEP_EXISTING_CONFIG=true osixia/openldap
docker run --detach --restart unless-stopped --name=lum -p 80:80 -p 443:443 -e SERVER_HOSTNAME=localhost -e LDAP_URI=ldap://172.17.0.1 -e LDAP_BASE_DN=dc=example,dc=org -e LDAP_ADMINS_GROUP=admins -e LDAP_ADMIN_BIND_DN="cn=admin,dc=example,dc=org" -e LDAP_ADMIN_BIND_PWD=somepassword -e NO_HTTPS=TRUE wheelybird/ldap-user-manager


http://localhost/setup
user:
somepassword
pass:
0-charged-plains-Expired

stevens-employee-Elected-14
