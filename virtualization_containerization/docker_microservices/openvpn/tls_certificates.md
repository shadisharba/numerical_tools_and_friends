intro:
https://www.youtube.com/watch?v=j9QmMEWmcfo&ab_channel=ByteByteGo
https://easy-rsa.readthedocs.io/en/latest/
https://community.openvpn.net/openvpn/wiki/EasyRSA3-OpenVPN-Howto
https://openvpn.net/community-resources/how-to

sudo apt install easy-rsa

make-cadir cert

./easyrsa init-pki

./easyrsa build-ca nopass
CA creation complete and you may now import and sign cert requests.
Your new CA certificate file for publishing is at:
/home/shadi/tls_test/cert/pki/ca.crt


./easyrsa gen-dh
DH parameters of size 2048 created at /home/shadi/tls_test/cert/pki/dh.pem

./easyrsa gen-crl
CRL file: /home/shadi/tls_test/cert/pki/crl.pem

./easyrsa build-server-full vpn_server nopass

./easyrsa build-client-full vpn_client1 nopass

