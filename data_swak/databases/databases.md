# Databases

**Data Structure**: SQL databases are relational, meaning they organize data into tables with rows and columns, similar to a spreadsheet. NoSQL databases are non-relational and can store data in a variety of formats, including key-value pairs, wide-column stores, graph databases, or document-oriented databases.

**Schema**: SQL databases have a predefined schema that dictates the structure of the data, including the tables and the types of data that can be stored in each column. NoSQL databases are schema-less, meaning they can store any type of data without a predefined structure.

**Scalability**: SQL databases are typically scaled vertically by increasing the horsepower (CPU, RAM, SSD) of the existing server. NoSQL databases are designed to scale horizontally, meaning they can handle increased load by adding more servers to the database.

**ACID Properties**: SQL databases are ACID compliant (Atomicity, Consistency, Isolation, Durability), ensuring that transactions are processed reliably. While some NoSQL databases offer ACID compliance, many prioritize performance and scalability over strict consistency.

**Query Language**: SQL databases use Structured Query Language (SQL) for defining and manipulating the data. In NoSQL databases, queries are focused on a collection of documents, and the query language varies from database to database.

**Use Cases**: SQL databases are typically used when you need to ensure ACID compliance and the data structure is not changing frequently. NoSQL databases are used when dealing with large volumes of data or when the data structure is evolving rapidly.

**Some common examples of SQL databases include:**

- SQLite
- MySQL
- Oracle
- PostgreSQL
- Microsoft SQL Server

**NoSQL database examples include:**

- DynamoDB
- Cassandra
- Redis
- CouchDB
- RethinkDB
- RavenDB
- MongoDB

## [SQLite](https://www.sqlite.org/index.html)
SQLite is a C-language library that implements a small, fast, self-contained, high-reliability, full-featured, SQL database engine.

**MySQL** is a server-based database system. It runs on a server and can be accessed from different machines and applications to manage the database. **SQLite**, on the other hand, is an embedded database which is integrated with the application and runs on the local system where the application runs.

[DB Browser for SQLite](https://sqlitebrowser.org/dl/) 


## [Postgres](https://www.enterprisedb.com/postgresql-tutorial-resources-training-1?uuid=d732dc13-c15a-484b-b783-307823940a11&campaignId=Product_Trial_PostgreSQL_16)
PostgreSQL also known as Postgres, is a free and open-source relational database management system (RDBMS) emphasizing extensibility and SQL compliance. PostgreSQL features transactions with atomicity, consistency, isolation, durability (ACID) properties, automatically updatable views, materialized views, triggers, foreign keys, and stored procedures. It is supported on all major operating systems, including Linux, FreeBSD, OpenBSD, macOS, and Windows, and handles a range of workloads from single machines to data warehouses or web services with many concurrent users.


[psql terminal](https://www.postgresql.org/docs/9.2/app-psql.html)
Once you’re connected, you can list all tables in the current database with the command: \dt.

