if __package__ is None or __package__ == '':
    # uses current directory visibility [works with vscode]
    import module_one
else:
    # uses current package visibility [works with python -m pkg_1.module_relative]
    from . import module_one 

print()
print('package: ', __package__)
print('name:    ', __name__)
print()

# python -m pkg_1.module_relative -> __package__ = 'pkg_1'
# python -m python_relative_import.pkg_1.module_relative -> __package__ = 'python_relative_import.pkg_1'
# from ..pkg_2 import module_two

# vscode add "env": {"PYTHONPATH": "${workspaceFolder}"} to launch.json
from pkg_2 import module_two
from pkg_2.pkg_2_sub_1 import module_two_sub
