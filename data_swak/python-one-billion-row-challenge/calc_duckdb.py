# Code credits: https://github.com/ifnesi/1brc#submitting

# Open-source, embedded, in-process, relational OLAP DBMS that is typically orders of magnitude faster than Pandas. You can use it from the shell or over 10 different programming languages. In most of them, you can choose between a traditional analytical interface and a SQL interface.

import duckdb

with duckdb.connect() as conn:
    data = conn.sql("""
        select
            station_name,
            min(measurement) as min_measurement,
            cast(avg(measurement) as decimal(8, 1)) as mean_measurement,
            max(measurement) as max_measurement
        from read_csv(
            'data/measurements.txt',
            header=false,
            columns={'station_name': 'varchar', 'measurement': 'decimal(8, 1)'},
            delim=';',
            parallel=true
        )
        group by station_name
        order by station_name
    """)

    print("{", end="")
    for row in sorted(data.fetchall()):
        print(
            f"{row[0]}={row[1]}/{row[2]}/{row[3]}",
            end=", ",
        )
    print("\b\b} ")