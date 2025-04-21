# in neo4j: create project, database and click on start
# from database: add user
# after creating the db here change from database menue from the default neo4j ...
# http://localhost:7474/browser/

# conn and filename are global objects

from neo4j import __version__ as neo4j_version
from neo4j import GraphDatabase
import h5py

print(neo4j_version)


class Neo4jConnection:
    def __init__(self, uri, user, pwd):
        self.__uri = uri
        self.__user = user
        self.__pwd = pwd
        self.__driver = None
        try:
            self.__driver = GraphDatabase.driver(self.__uri, auth=(self.__user, self.__pwd))
        except Exception as e:
            print("Failed to create the driver:", e)

    def close(self):
        if self.__driver is not None:
            self.__driver.close()

    def query(self, query, db=None):
        assert self.__driver is not None, "Driver not initialized!"
        session = None
        response = None
        try:
            session = self.__driver.session(database=db) if db is not None else self.__driver.session()
            response = list(session.run(query))
        except Exception as e:
            print("Query failed:", e)
        finally:
            if session is not None:
                session.close()
        print(response)
        return response


conn = Neo4jConnection(uri="bolt://localhost:7687", user="dae", pwd="123456")

conn.query("CREATE OR REPLACE DATABASE h5db")


def get_attributes(node, shift):
    attributes = ","
    for key, val in node.attrs.items():
        # print(f"{shift} {key}: {val} [attribute]")
        attributes += f"{key}: '{val}',"
    if len(attributes) < 2:
        return ""
    return attributes[:-1]


def get_node_info(name, node):
    space = '    '
    shift = name.count('/') * space
    if isinstance(node, h5py.Dataset):
        # print(shift + node.name,' [dataset]')
        # print(f"{shift + space} shape: {node.shape} [shape]")
        attributes = get_attributes(node, shift + space) + f",shape: '{node.shape}'"
        conn.query(f"CREATE (n:Dataset {{ name: '{node.name}' {attributes} }})", db='h5db')
        conn.query(
            f"MATCH(a: File), (b:Dataset) WHERE a.name = '{file_name}' AND b.name = '{node.name}' CREATE (a)-[r:file_set]->(b)",
            db='h5db')
        conn.query(
            f"MATCH(a: Group), (b:Dataset) WHERE a.name = '{node.parent.name}' AND b.name = '{node.name}' CREATE (a)-[r:group_set]->(b)",
            db='h5db')
    else:
        # print(shift + node.name,' [group]')
        attributes = get_attributes(node, shift + space)
        conn.query(f"CREATE (n:Group {{ name: '{node.name}' {attributes} }})", db='h5db')
        conn.query(
            f"MATCH(a: File), (b:Group) WHERE a.name = '{file_name}' AND b.name = '{node.name}' CREATE (a)-[r:file_group]->(b)",
            db='h5db')


file_names = ['mytestfile.h5', 'dolfin_fine.h5']
# file_name = 'mytestfile.h5'

for file_name in file_names:
    obj = h5py.File(file_name, 'r')
    attributes = get_attributes(obj, shift='')
    conn.query(f"CREATE (n:File {{ name: '{file_name}' {attributes} }})", db='h5db')
    obj.visititems(get_node_info)
    obj.close()

conn.close()
