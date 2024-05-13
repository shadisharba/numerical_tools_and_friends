# The idea is to go from uncompressed and unoptimized 13.8 GB of text data to a compressed and columnar-oriented 2.51 GB Parquet file.

import pandas as pd

df = pd.read_csv("measurements.txt", sep=";", header=None, names=["station_name", "measurement"], engine="pyarrow")
df.to_parquet("measurements.parquet")