import h5py

f     = h5py.File("mytestfile.h5", "w")
f.attrs['temperature']=3.5
dset  = f.create_dataset("mydataset", (100,), dtype="i")
dset.attrs['temperature'] = 99.5
f.close()

f     = h5py.File("mytestfile.h5", "a")
grp   = f.create_group("subgroup")
grp.attrs['temperature'] = 9.5
dset2 = grp.create_dataset("another_dataset", (50,), dtype="f") # add data to 'subgroup'
dset2.attrs['temperature'] = 199.5
f.close()