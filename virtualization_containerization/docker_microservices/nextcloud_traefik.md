Install docker and docker-compose
```
curl -sSL https://get.docker.com | sh
sudo usermod -aG docker $USER
sudo reboot now
```

```
mkdir nextcloud_compose && cd nextcloud_compose
mkdir nextcloud_data && mkdir db_data

cat <<EOF > nextcloud-compose.yml
***
EOF

docker compose -f nextcloud-compose.yml up -d
```

Open [nextcloud web app](http://192.168.178.38:8080/)

# Upgrade
```
docker compose -f nextcloud-compose.yml pull app
docker compose -f nextcloud-compose.yml up -d
```

# Backup [WIP]
```
use 'docker cp' to copy the data from the container to the host
docker exec -t nextcloud_db_1 mysqldump -u nextcloud -pnextcloud nextcloud > nextcloud-sqlbkp_`date +"%Y%m%d"`.bak
```

# Nextcloud with Traefik
```
sudo docker compose -f nextcloud-compose.yml up -d
```


# Setup
```
sudo docker compose -f compose_nextcloud_dokuwiki_traefik.yml up -d
```

[Traefik dashboard](http://localhost:8080/dashboard/)

http://nextcloud.localhost/
http://dokuwiki.localhost/


# options
Remove "Talk" folder
<https://help.nextcloud.com/t/talk-folder-created-for-all-users-any-chance-to-change-this/94904>

Add email to nextcloud
<https://che-adrian.medium.com/add-an-smtp-account-to-make-your-nextcloud-send-emails-f636e6f34d8>


# sharing with nice/readable links
use "Custom public link" (might need an app)
or
https://apps.nextcloud.com/apps/sharerenamer

# Resetting a lost admin password
https://docs.nextcloud.com/server/latest/admin_manual/configuration_user/reset_admin_password.html

docker ps
// nextcloud image

docker exec -it a797c81fcd26 /bin/bash
sudo -u#1000 ./config/www/nextcloud/occ user:resetpassword sharba
