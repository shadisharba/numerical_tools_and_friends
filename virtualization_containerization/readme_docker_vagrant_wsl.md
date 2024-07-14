https://www.notion.so/Virtualization-ec07328995024e86b1db674d5c3acdcd#f45c2f22fd0a4679b87c09de95d64e36


# Virtualization and Containerization

## WSL

### WSL Storage Location
look for `ext4.vhdx`
https://askubuntu.com/questions/1380253/where-is-wsl-located-on-my-computer
https://dev.to/kim-ch/move-docker-desktop-data-distro-out-of-system-drive-4cg2

### VSCode + WSL
from within vscode, ctrl+shift+p, type reopen folder in wsl


## Docker

### Docker Storage Location (with WSL2 backend)
- default: C:\Users\sha79396\AppData\Local\Docker\wsl
- changable using Docker Desktop Settings -> Resources -> Advanced
- check the section about "WSL Storage Location"

### PyCharm + Docker
https://www.jetbrains.com/help/pycharm/docker-run-configurations.html



## Already Configured Virtual Machines
[Linux VMs](https://www.osboxes.org/virtualbox-images/)

[Win 10 evaluation ISO](https://www.microsoft.com/en-us/evalcenter/evaluate-windows-10-enterprise)
[Win 10 VM](https://developer.microsoft.com/en-us/windows/downloads/virtual-machines/)
[Win 10 VM](https://www.heise.de/download/product/windows-vm-image)
[Win 11 Vagrant box](https://app.vagrantup.com/gusztavvargadr/boxes/windows-11)


## Vagrant

### Vagrant storage location
- default: %HOMEDRIVE%\.vagrant.d\boxes
- changable using VAGRANT_HOME environmental variable 

### [Ubuntu using Vagrant](https://app.vagrantup.com/ubuntu/boxes/focal64)
```
echo %VAGRANT_HOME%
vagrant init ubuntu/focal64
vagrant up
```
The created VM can be seen in [Oracle VM VirtualBox Manager](https://www.virtualbox.org/wiki/Downloads)

username: vagrant
password: vagrant

### [Win 11 Vagrant box](https://app.vagrantup.com/gusztavvargadr/boxes/windows-11)

## KVM
https://github.com/acudovs/windows-kvm-imaging-tools
https://www.server-world.info/en/note?os=Ubuntu_20.04&p=kvm&f=4

### Remote desktop (not tested)
use [virt-viewer](https://virt-manager.org/download.html)
virt-viewer --connect qemu+ssh://root@KVM_HOST:22/system VM_NAME

or

Forward the RDP port then connect to the VM using the host IP address and the forwarded port
https://serverfault.com/questions/401739/remote-desktop-to-my-kvm-virtual-machine
```
virsh qemu-monitor-command --hmp HOSTNAME123456 'hostfwd_add ::13389-:3389'
redir --lport 13389 --caddr=192.168.122.215 --cport 3389
```

### Share Folder Between Guest and Host (not tested)
https://www.heiko-sieger.info/sharing-files-between-the-linux-host-and-a-windows-vm-using-virtiofs/
https://www.debugpoint.com/share-folder-virt-manager/

### GPU passthrough (not tested)
https://wiki.gentoo.org/wiki/GPU_passthrough_with_libvirt_qemu_kvm
https://www.reddit.com/r/VFIO/comments/gpreiq/share_gpu_between_vm_and_host/
https://github.com/joeknock90/Single-GPU-Passthrough


## [Ubuntu Multipass](https://multipass.run/)
Start Ubuntu VMs with each platform's native hypervisor
Multipass uses Hyper-V on Windows, QEMU and HyperKit on macOS and LXD on Linux for minimal overhead and the fastest possible start time.
