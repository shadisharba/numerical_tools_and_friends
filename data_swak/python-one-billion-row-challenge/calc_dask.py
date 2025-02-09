# Almost identical API to Pandas, but is lazy evaluated. You can use Dask to scale Pandas code across CPU cores locally or across machines on a cluster.

import dask.dataframe as dd

df = (
    dd.read_csv("data/measurements.txt", sep=";", header=None, names=["station_name", "measurement"], engine="pyarrow")
        .groupby("station_name")
        .agg(["min", "mean", "max"])
        .compute()
)

df.columns = df.columns.get_level_values(level=1)
df = df.reset_index()
df.columns = ["station_name", "min_measurement", "mean_measurement", "max_measurement"]
df = df.sort_values("station_name")

print("{", end="")
for row in df.itertuples(index=False):
    print(
        f"{row.station_name}={row.min_measurement:.1f}/{row.mean_measurement:.1f}/{row.max_measurement:.1f}",
        end=", "
    )
print("\b\b} ")