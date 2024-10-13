A reverse proxy sits in front of web servers and forwards client requests to those servers. Here are some reasons to use a reverse proxy:

SSL Termination: Offloads the process of encrypting and decrypting SSL traffic from the backend server to the reverse proxy. This makes it easier to manage SSL certificates and allows for centralized SSL management.

Load Balancing: Distributes incoming requests across multiple servers to balance load and ensure redundancy. If one server fails, the reverse proxy directs traffic to the remaining online servers.

Security and Anonymity: Hides the identity and internal structure of your backend servers from external users. It can also provide additional layers of defense against security threats.

Caching: Some reverse proxies can cache content, reducing the load on backend servers and improving response times.

Compression: Reduces the size of data before sending it to the client, speeding up content delivery and reducing bandwidth usage.

Global Server Load Balancing: Directs client requests to the nearest geographical server, improving response times for global audiences.

Traefik is a modern reverse proxy and load balancer that can automatically discover services and create routes to them. It's especially popular in containerized environments due to its dynamic configurations.





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
