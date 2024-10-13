https://www.youtube.com/watch?v=pwV2p-NReUg

# native:
  https://openvpn.net/community-resources/how-to
  https://www.digitalocean.com/community/tutorials/how-to-set-up-an-openvpn-server-on-ubuntu-16-04

# simple docker, no encryption:
  https://dockovpn.io/
  https://github.com/dockovpn/dockovpn

  docker run -it --rm --cap-add=NET_ADMIN \
  -p 1194:1194/udp -p 80:8080/tcp \
  -e HOST_ADDR=$(curl -s https://api.ipify.org) \
  --name dockovpn alekslitvinenk/openvpn

  DOCKOVPN_CONFIG_PORT=443
  DOCKOVPN_TUNNEL_PORT=444
  docker run -it --rm --cap-add=NET_ADMIN \
  -p $DOCKOVPN_TUNNEL_PORT:1194/udp -p $DOCKOVPN_CONFIG_PORT:8080/tcp \
  -e HOST_CONF_PORT="$DOCKOVPN_CONFIG_PORT" \
  -e HOST_TUN_PORT="$DOCKOVPN_TUNNEL_PORT" \
  --name dockovpn alekslitvinenk/openvpn

# docker
  https://blog.oyam.dev/quick-openvpn-server/
  https://github.com/kylemanna/docker-openvpn/blob/master/docs/docker-compose.md

  scp -i aws_ec2.pem ubuntu@34.235.119.245:/home/ubuntu/userr* . 

# client
OpenVPN Connect for Windows
https://openvpn.net/client/client-connect-vpn-for-windows/

