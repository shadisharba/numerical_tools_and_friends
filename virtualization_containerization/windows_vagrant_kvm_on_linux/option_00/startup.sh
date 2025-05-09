#!/bin/bash
set -eou pipefail
VAGRANT_DEFAULT_PROVIDER=libvirt

chown root:kvm /dev/kvm

iptables-save > $HOME/firewall.rules
iptables -X
iptables -t nat -F
iptables -t nat -X
iptables -t mangle -F
iptables -t mangle -X
iptables -P INPUT ACCEPT
iptables -P FORWARD ACCEPT
iptables -P OUTPUT ACCEPT

# iptables -A FORWARD -i eth0 -o virbr1 -p tcp --syn --dport 3389 -m conntrack --ctstate NEW -j ACCEPT
# iptables -A FORWARD -i eth0 -o virbr1 -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT
# iptables -A FORWARD -i virbr1 -o eth0 -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT
# iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 3389 -j DNAT --to-destination 192.168.121.227
# iptables -t nat -A POSTROUTING -o virbr1 -p tcp --dport 3389 -d 192.168.121.227 -j SNAT --to-source 192.168.121.1
# 
# iptables -D FORWARD -o virbr1 -j REJECT --reject-with icmp-port-unreachable
# iptables -D FORWARD -i virbr1 -j REJECT --reject-with icmp-port-unreachable
# iptables -D FORWARD -o virbr0 -j REJECT --reject-with icmp-port-unreachable
# iptables -D FORWARD -i virbr0 -j REJECT --reject-with icmp-port-unreachable

exec "$@"
# exec "$@" is typically used to make the entrypoint a pass through that then runs the docker command. It will replace the current running shell with the command that "$@" is pointing to. By default, that variable points to the command line arguments.

service libvirtd start
service virtlogd start
vagrant up