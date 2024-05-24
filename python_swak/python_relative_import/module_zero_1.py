import sys
import os
print()
print('PYTHONPATH: ', os.environ.get('PYTHONPATH'))
print()
print(sys.path)
print()
print(sys.modules.keys())
print('here is module_zero_1.py')
print()

from pkg_1 import module_one
print(sys.modules.keys())
print()

import pkg_1.module_one # not gonna be imported again because it's already in sys.modules
print(sys.modules['pkg_1'])
print(sys.modules['pkg_1.module_one'])
print()

import pkg_2.module_two

if __name__ == '__main__':
    print('module_zero_1.py is being run as the main program')