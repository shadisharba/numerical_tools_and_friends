import h5py
import fire
from termcolor import colored
import numpy as np
np.set_printoptions(formatter={'float': '{:>2.2e}'.format}, linewidth=5000)

def print_attributes(node, shift):
    for key, val in node.attrs.items():
        # with np.printoptions(formatter={'float': '{:>2.2e}'.format}, linewidth=5000):
        print(colored(f"{shift} {key}: {val} [attribute]", 'yellow'))

def print_node_info(name, node):
    space = '    '
    shift = name.count('/') * space
    if isinstance(node, h5py.Dataset):
        print(shift + node.name, ' [dataset]')
        print(f"{shift + space} shape: {node.shape} [shape]")
    else:
        print(colored(f'{shift + node.name} [group]', 'green'))
    print_attributes(node, shift + space)

def h5ls(name='mytestfile.h5'):
    if '/' in name:
        name, ext = name.split('/', 1)
    else:
        ext = ''
    print(name)
    print(ext)
    with h5py.File(name, 'r') as obj:
        print_attributes(obj[f'/{ext}'], shift='')
        obj[f'/{ext}'].visititems(print_node_info)
    return '***************** end of file *****************'

if __name__ == '__main__':
    fire.Fire(h5ls)

# h5ll() {
#   python h5ll.py --name=$1
# }
