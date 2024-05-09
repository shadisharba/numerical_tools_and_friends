import contextlib
import sys
from io import StringIO

with open("../python_env_pip.txt", "r") as file:
    data = file.read()
    # file is closed after the block of code is executed


@contextlib.contextmanager
def open_file(file_name):
    try:
        print('1-opening file')
        file = open(file_name, "r")
        print('2-yielding/returning file')
        yield file
        print('3-closing file')
        file.close()
    except FileNotFoundError:
        raise FileNotFoundError("File cannot be found")


# Context Manager Class
class SampleContextVariable:
    def __enter__(self):
        print("1-entering")
        return "2-returning"

    def __exit__(self, *args):
        print("3-exiting")
        pass


with open_file("../python_env_pip.txt") as file:
    print(file)
    data = file.read()

print()

with SampleContextVariable() as variable:
    print(variable)


# capture print statements (e.g. from external Python libraries)


def print_function():
    print("Hello")
    print("World")
    print("New\nLine")


class Capturing(list):
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = StringIO()
        self._current_string = sys.stdout
        return self

    def __exit__(self, *args):
        self.extend(self._current_string.getvalue().splitlines())
        del self._current_string
        sys.stdout = self._stdout


print('Nothing will be printed to console since it is captured')
with Capturing() as output:
    print_function()
print('Now all captured print statements will be printed to console')
print(output)

# capture as string instead of list
f = StringIO()
with contextlib.redirect_stdout(f):
    print_function()
output = f.getvalue()
print(output)
