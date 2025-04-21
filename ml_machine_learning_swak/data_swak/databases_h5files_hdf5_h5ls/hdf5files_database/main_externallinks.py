# https://pythontic.com/hdf5/h5py/links
# check: https://github.com/PyTables/datasette-pytables

import os
# os.system('pip install datasette-pytables')
# conda install -c anaconda pytables
# vitables
# conda install -c conda-forge vitables
# ptdump mytestfile1.h5

import tables as pytables
import h5py
file = h5py.File('externallinks.h5', 'w')
file['extlink1'] = h5py.ExternalLink('mytestfile1.h5', '/')
file['extlink2'] = h5py.ExternalLink('mytestfile2.h5', '/')
file['extlink1'].attrs['updated'] = True
file['extlink1'].attrs['mech'] = True
file.close()

myfile = h5py.File('externallinks.h5', 'r')
print(myfile.attrs.keys())
keys = list(myfile.keys())
print(keys)
print(list(myfile[keys[0]]))
print(list(myfile[keys[1]]))
# print(myfile.attrs['updated'])
# print('mech' in myfile.attrs)
# print('elec' in myfile.attrs)
print(myfile['extlink2']['mydataset'])
myfile.close()

h5file = pytables.open_file('externallinks.h5', 'r')
print(h5file)
print(h5file.get_node('/extlink1/mydataset'))
# table = h5file.root
# h5file.root.extlink1._v_attrs
# table.attrs.temperature = 18.4
# table._v_attrs
h5file.close()

# myfile = h5py.File('externallinks.h5', 'r')
# from blaze import data
# d = data(myfile)
# myfile.close()

# https://github.com/okfn/docker-fiware-ckan

# https://www.forschungsdaten.org/index.php/Repository_Software
# https://www.izus.uni-stuttgart.de/en/fokus/darus/

# Blaze seems great but it's not well maintained
# http://matthewrocklin.com/blog/work/2014/11/19/Blaze-Datasets
# https://github.com/blaze/blaze

# datasette serve path/to/data.h5 [didn't work with external links]
# http://localhost:8001/

# don't know how to search with pytables yet
# 3.1.6 Reading (and selecting) data in a table
# https://www.pytables.org/usersguide/introduction.html
# https://www.pytables.org/usersguide/utilities.html
