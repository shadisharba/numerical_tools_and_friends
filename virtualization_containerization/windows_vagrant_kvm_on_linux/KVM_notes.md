Kernel-based Virtual Machine (KVM) is a free and open-source virtualization module in the Linux kernel that allows the kernel to function as a hypervisor.

KVM itself emulates very little hardware, instead deferring to a higher level client application such as QEMU, crosvm, or Firecracker for device emulation.

QEMU A generic and open source machine emulator and virtualizer


0- using docker image
https://github.com/acudovs/windows-kvm-imaging-tools#how-to-build-a-windows-qemu-kvm-qcow2-image

1- use virtual machine manager to create a VM
https://raphtlw.medium.com/how-to-set-up-a-kvm-qemu-windows-10-vm-ca1789411760


2- https://medium.com/axon-technologies/installing-a-windows-virtual-machine-in-a-linux-docker-container-c78e4c3f9ba1

3- Performance optimizer
https://leduccc.medium.com/improving-the-performance-of-a-windows-10-guest-on-qemu-a5b3f54d9cf5

[export the setup to xml](https://www.vinchin.com/en/blog/kvm-export-vm-xml-ova-ovf.html)
virsh define win10.xml

virtio-win
https://fedorapeople.org/groups/virt/virtio-win/direct-downloads/archive-virtio/virtio-win-0.1.240-1/

- copy/paste to KVM (virtio-win)
- NVME drive which can then be passed with PCI Passthrough
- .raw

# TODO
- GPU passthrough?
sudo lshw -C video
Test on a new device with a dedicated GPU / try old GPU then we can buy one that's compatible with discovery?

- the link to host/intranet (license + network drive)
- Remote desktop directly to Windows VM
https://askubuntu.com/questions/952697/rdp-to-kvm-guest

- windows activation

# Benchmark, prob. affected by the host's tasks
baremetal Ubuntu:
    CPU https://browser.geekbench.com/v6/cpu/3570180
    GPU https://browser.geekbench.com/v6/compute/1295889
KVM Windows:
    CPU https://browser.geekbench.com/v6/cpu/3570627
    RAW + optimizations
        https://browser.geekbench.com/v6/cpu/3572136
    docker + virtio-win
        https://browser.geekbench.com/v6/cpu/3572970
    raw
        https://browser.geekbench.com/v6/cpu/3583863
    qcow2
        https://browser.geekbench.com/v6/cpu/3583964
My laptop Windows: (best performance)
    CPU https://browser.geekbench.com/v6/cpu/3570683
    GPU https://browser.geekbench.com/v6/compute/1296098

# Current setup
```
# bash
sudo apt-get install -y qemu-kvm libvirt-bin bridge-utils virt-manager qemu virt-viewer spice-vdagent
sudo apt-get install -y libnss-libvirt freerdp2-x11

sudo docker pull docker.io/alekseychudov/windows-10-pro:1912
sudo docker info | grep 'Storage Driver' # overlay2

# Create a guest disk image
image="$(sudo docker inspect --format {{.GraphDriver.Data.UpperDir}} docker.io/alekseychudov/windows-10-pro:1912)/images/Windows-10-Pro.qcow2.gz"
sudo pigz -c -d "${image}" | sudo dd of=/var/lib/libvirt/images/HOSTDISK123456.qcow2 status=progress
sudo qemu-img resize /var/lib/libvirt/images/HOSTDISK123456.qcow2 100G
sudo qemu-img info /var/lib/libvirt/images/HOSTDISK123456.qcow2

# Create a cloudbase-init ISO image to automate guest configuration
mkdir -pv cloudbase-init/openstack/latest
echo '{"admin_pass": "88888888", "hostname": "COMPUTERNAME123456"}' > cloudbase-init/openstack/latest/meta_data.json
sudo genisoimage -input-charset utf-8 -joliet -rock -volid config-2 -output /var/lib/libvirt/images/HOSTISO123456.iso cloudbase-init

# Provision a new virtual machine
sudo virt-install \
    --name HOSTNAME123456 \
    --memory 4096 \
    --vcpus 4 \
    --cpu host \
    --import \
    --disk /var/lib/libvirt/images/HOSTDISK123456.qcow2,device=disk,bus=virtio \
    --disk /var/lib/libvirt/images/HOSTISO123456.iso,device=cdrom \
    --network default \
    --graphics spice \
    --channel unix,target_type=virtio,name=org.qemu.guest_agent.0 \
    --virt-type kvm \
    --os-variant win10 \
    --noautoconsole

# Connect to the guest
sudo virsh domifaddr win10.localhost
xfreerdp /v:win10.localhost /u:Administrator
xfreerdp 192.168.122.147
or use Remmina
```


# Issues and solutions
sudo umount -f thinclient_drives
sudo rm -rf thinclient_drives







# TODO
https://www.one-tab.com/page/cQDM6tbfQ5WTlPAQC0e2ug

# Remote
https://wiki.libvirt.org/Networking.html#Forwarding_Incoming_Connections

remote: 10.166.50.35:3300

https://serverfault.com/questions/233760/port-forwarding-from-host-to-guest-with-libvirt-0-8-3-using-kvm-on-ubuntu

https://www.server-world.info/en/note?os=Ubuntu_20.04&p=kvm&f=5