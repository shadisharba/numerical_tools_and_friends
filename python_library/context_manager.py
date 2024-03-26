import contextlib
import psycopg2
import sys
from io import StringIO
from dotenv import load_dotenv, dotenv_values

with open("../requirements.txt", "r") as file:
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


with open_file("../requirements.txt") as file:
    print(file)
    data = file.read()

print()

with SampleContextVariable() as variable:
    print(variable)

# install (PostgreSQL)[https://www.postgresql.org/download/]
secrets = dotenv_values("../.env_local")
db_params = dict(
    host="localhost", database="sample_db", user="postgres", password=secrets["DB_PASSWORD"]
)


@contextlib.contextmanager
def database(params):
    print("Connecting to PostgreSQL database...")
    # Setup script
    conn = psycopg2.connect(user=params['user'], password=params['password'], host=params['host'])
    conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
    cur = conn.cursor()

    print("Dropping existing database and creating a new one.")
    cur.execute(f"DROP DATABASE IF EXISTS {params['database']};")
    cur.execute(f"CREATE DATABASE {params['database']};")
    print("Database created.")
    cur.close()
    conn.close()

    try:
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS table1 (id serial PRIMARY KEY, num integer, data varchar);")
        print("returning DB cursor.")
        yield cur
    finally:
        # Teardown script
        cur.close()
        conn.close()
        print("Database connection closed.")


with database(db_params) as db_conn:
    data = db_conn.execute("SELECT * FROM table1")


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
