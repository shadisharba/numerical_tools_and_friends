# http://localhost:7474/browser/

from neo4j import __version__ as neo4j_version
print(neo4j_version)

from neo4j import GraphDatabase

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

conn.query("CREATE OR REPLACE DATABASE coradb")
query_string = '''
USING PERIODIC COMMIT 500
LOAD CSV WITH HEADERS FROM
'https://raw.githubusercontent.com/ngshya/datasets/master/cora/cora_content.csv'
AS line FIELDTERMINATOR ','
CREATE (:Paper {id: line.paper_id, class: line.label})
'''
conn.query(query_string, db='coradb')

query_string = '''
USING PERIODIC COMMIT 500
LOAD CSV WITH HEADERS FROM
'https://raw.githubusercontent.com/ngshya/datasets/master/cora/cora_cites.csv'
AS line FIELDTERMINATOR ','
MATCH (citing_paper:Paper {id: line.citing_paper_id}),(cited_paper:Paper {id: line.cited_paper_id})
CREATE (citing_paper)-[:CITES]->(cited_paper)
'''
conn.query(query_string, db='coradb')

#%%
query_string = '''
MATCH (p:Paper)
RETURN DISTINCT p.class
ORDER BY p.class
'''
conn.query(query_string, db='coradb')

query_string = '''
MATCH ()-->(p:Paper)
RETURN id(p), count(*) as indegree
ORDER BY indegree DESC LIMIT 10
'''
conn.query(query_string, db='coradb')

#%% Graph Data Science Library
query_string = '''
CALL gds.graph.create(
  'coraGraph',
  'Paper',
  'CITES'
)
'''
conn.query(query_string, db='coradb')

query_string = '''
CALL gds.pageRank.write('coraGraph', {
  writeProperty: 'pagerank'
})
YIELD nodePropertiesWritten, ranIterations
'''
conn.query(query_string, db='coradb')

query_string = '''
CALL gds.betweenness.write('coraGraph', {
  writeProperty: 'betweenness' })
YIELD minimumScore, maximumScore, scoreSum, nodePropertiesWritten
'''
conn.query(query_string, db='coradb')

from pandas import DataFrame
query_string = '''
MATCH (p:Paper)
RETURN DISTINCT p.id, p.class, p.pagerank, p.betweenness
'''
dtf_data = DataFrame([dict(_) for _ in conn.query(query_string, db='coradb')])
dtf_data.sample(10)

conn.close()
