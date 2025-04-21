# database
https://ckan.org/
http://matthewrocklin.com/blog/work/2014/11/19/Blaze-Datasets
https://github.com/mgraupe/hdf5Manager
virtual dataset h5py
big data platform for h5 files
http://www.space-research.org/
https://www.forschungsdaten.org/index.php/Repository_Software


# Naming convention:

| spatial_dimension  | solver  | physics  | time_dependency  | material_model  | deformation |
|--------------------|---------|----------|------------------|-----------------|-------------|
| 2d                 | FEM     | mech     | static           | elastic         | smalldef    |
| 3d                 | FFT     | ther     | dynamic          | plastic         | largedef    |
|                    |         | thmech   |                  | hyperelastic    |             |

eg: __3d_fem_mech_static_elastic_smalldef_[laminate_sphere].h5__

# datasets / attributes:
- files:
  - RB
  - vtk files
  - code snapshot or git history id

- ref FEM
  - B matrix
  - Mass and stiffness matrices
- microstructure
  - image of the microstructure
  - total volume (including voids)
  - number_of_phases
  - volume fraction of each phase
  - material_index (for each gp)
  - material parameters (either here or a link to a JSON file)
- reduced_basis
  - strain_modes
  - singular_values (or eigen_values)
- mesh
  - dof
  - integration_coefficients (split into weights and det(J)?)
  - mesh (structured/unstructured)
  - element type (hex_8gp, tet_4gp)
- training
  - directions (load cases)
  - effective stress
  - effective tangent
  - FEM effective stress
  - FEM effective tangent
- verification
  - directions
  - effective stress
  - effective tangent
  - FEM effective stress
  - FEM effective tangent


elements connectivity
force/displacement control // BC index [not RVE]
