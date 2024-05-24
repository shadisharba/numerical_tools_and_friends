@REM The -m option in Python allows you to run a module as a script. This can be useful for running library modules directly, without needing to write an explicit script file to call them. Here are some common uses of python -m
@REM The -m option allows the script to be located using Python’s sys.path module search path, which includes the current directory

python -m module_zero_1
python -m pkg_1.module_one
@REM Python debugger (pdb) can be invoked on a module by running python -m pdb module_name.py
@REM python -m pdb pkg_1.module_one

@REM This will execute the module_name as if it were a script, running the code in the if __name__ == "__main__": block.