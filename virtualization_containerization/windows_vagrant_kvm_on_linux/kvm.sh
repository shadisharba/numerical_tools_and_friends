# Create a guest disk image
image="$(sudo docker inspect --format {{.GraphDriver.Data.UpperDir}} docker.io/alekseychudov/windows-10-pro:1912)/images/Windows-10-Pro.qcow2.gz"
sudo pigz -c -d "${image}" | sudo dd of=/home/sha79396/kvm_vm/images/HOSTDISK123456.qcow2 status=progress
sudo qemu-img resize /home/sha79396/kvm_vm/images/HOSTDISK123456.qcow2 100G
sudo qemu-img info /home/sha79396/kvm_vm/images/HOSTDISK123456.qcow2

# Create a cloudbase-init ISO image to automate guest configuration
mkdir -pv cloudbase-init/openstack/latest
echo '{"admin_pass": "88888888", "hostname": "COMPUTERNAME123456"}' > cloudbase-init/openstack/latest/meta_data.json
sudo genisoimage -input-charset utf-8 -joliet -rock -volid config-2 -output /home/sha79396/kvm_vm/images/HOSTISO123456.iso cloudbase-init

# Provision a new virtual machine
sudo virt-install \
    --name HOSTNAME123456 \
    --memory 50000 \
    --vcpus 16 \
    --cpu host \
    --import \
    --disk /home/sha79396/kvm_vm/images/HOSTDISK123456.qcow2,device=disk,bus=virtio \
    --disk /home/sha79396/kvm_vm/images/HOSTISO123456.iso,device=cdrom \
    --network default \
    --graphics spice \
    --channel unix,target_type=virtio,name=org.qemu.guest_agent.0 \
    --virt-type kvm \
    --os-variant win10 \
    --noautoconsole
