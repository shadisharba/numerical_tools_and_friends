# Numerical tools and friends

This repository serves as a comprehensive toolkit showcasing a variety of numerical methods and data processing pipelines. It is designed to be a personal resource, offering practical tools and providing experimental testing for a wide range of methods in machine learning, data engineering, and data science.

## Third-party Repos

### [Numerical Tours](https://github.com/gpeyre/numerical-tours)
```
rm -rf numerical_tours_of_data_sciences
git clone https://github.com/gpeyre/numerical-tours.git numerical_tours_of_data_sciences
echo numerical_tours_of_data_sciences>>.gitignore
```

### [Mathematical Tours](https://mathematical-tours.github.io/)
```
rm -rf mathematical_tours_of_data_sciences
git clone https://github.com/mathematical-tours/mathematical-tours.github.io.git mathematical_tours_of_data_sciences
echo mathematical_tours_of_data_sciences>>.gitignore
```


### Automatic and Symbolic Differentiation
```
rm -rf automatic_and_symbolic_differentiation/symbolic_mat_diff0
git clone https://github.com/mshvartsman/symbolic-mat-diff.git automatic_and_symbolic_differentiation/symbolic_mat_diff0
echo automatic_and_symbolic_differentiation/symbolic_mat_diff0>>.gitignore

rm -rf automatic_and_symbolic_differentiation/symbolic_mat_diff
git clone https://github.com/aztennenbaum/symbolic-mat-diff.git automatic_and_symbolic_differentiation/symbolic_mat_diff
echo automatic_and_symbolic_differentiation/symbolic_mat_diff>>.gitignore
```

### Python Documentation
```
rm -rf languages/python/python_documentation_sphinx/sphinx_doc_tutorial
git clone https://git.opendfki.de/dinesh_krishna.natarajan/sphinx-doc-tutorial.git languages/python/python_documentation_sphinx/sphinx_doc_tutorial
echo languages/python/python_documentation_sphinx/sphinx_doc_tutorial>>.gitignore

rm -rf languages/python/python_documentation_sphinx/python_sample_code
git clone https://github.com/shunsvineyard/python-sample-code languages/python/python_documentation_sphinx/python_sample_code
echo languages/python/python_documentation_sphinx/python_sample_code>>.gitignore
```

### RaspberryPI and Arduino Projects
```
rm -rf pi_arduino_projects/exploring_arduino_2nd_edition
git clone https://github.com/sciguy14/Exploring-Arduino-2nd-Edition.git pi_arduino_projects/exploring_arduino_2nd_edition
echo pi_arduino_projects/exploring_arduino_2nd_edition>>.gitignore

rm -rf pi_arduino_projects/l293d_module_example
git clone https://github.com/layadcircuits/L293D_module_example.git pi_arduino_projects/l293d_module_example
echo pi_arduino_projects/l293d_module_example>>.gitignore

rm -rf pi_arduino_projects/zhaojinghua_arduino
git clone https://github.com/zhaojinghua/Arduino.git pi_arduino_projects/zhaojinghua_arduino
echo pi_arduino_projects/zhaojinghua_arduino>>.gitignore
```


### Finite Element Method (FEM)

http://www.calculix.de/

https://prepomax.fs.um.si/

```
rm -rf fem/rbnics
git clone https://gitlab.com/RBniCS/RBniCS.git fem/rbnics
echo fem/rbnics>>.gitignore

rm -rf fem/pymor
git clone https://github.com/pymor/pymor.git fem/pymor
echo fem/pymor>>.gitignore

rm -rf fem/ngsolve
git clone https://github.com/NGSolve/ngsolve.git fem/ngsolve
echo fem/ngsolve>>.gitignore

rm -rf fem/fenics/fenics_tutorial
git clone https://github.com/hplgit/fenics-tutorial.git fem/fenics/fenics_tutorial
echo fem/fenics/fenics_tutorial>>.gitignore

rm -rf fem/fenics/dolfinx
git clone https://github.com/FEniCS/dolfinx.git fem/fenics/dolfinx
echo fem/fenics/dolfinx>>.gitignore

rm -rf fem/gmsh_fem
git clone https://gitlab.onelab.info/gmsh/fem.git fem/gmsh_fem
echo fem/gmsh_fem>>.gitignore

rm -rf fem/gmsh_domain_decomposition
git clone https://gitlab.onelab.info/gmsh/ddm.git fem/gmsh_domain_decomposition
echo fem/gmsh_domain_decomposition>>.gitignore

rm -rf fem/scikit_fem
git clone https://github.com/kinnala/scikit-fem.git fem/scikit_fem
echo fem/scikit_fem>>.gitignore
```

### Meshing
```
rm -rf fem/meshing/intermediate_mesh_representation
git clone https://github.com/dbeurle/imr.git fem/meshing/intermediate_mesh_representation
echo fem/meshing/intermediate_mesh_representation>>.gitignore

rm -rf fem/meshing/meshio
git clone https://github.com/nschloe/meshio.git fem/meshing/meshio
echo fem/meshing/meshio>>.gitignore

rm -rf fem/meshing/gmsh
git clone https://gitlab.onelab.info/gmsh/gmsh.git fem/meshing/gmsh
echo fem/meshing/gmsh>>.gitignore
```

### Tensor Factorisation
```
rm -rf tensor_factorisation/dictionary_learning/spams_python
git clone https://github.com/samuelstjean/spams-python.git tensor_factorisation/dictionary_learning/spams_python
echo tensor_factorisation/dictionary_learning/spams_python>>.gitignore

rm -rf tensor_factorisation/dictionary_learning/odl
git clone https://github.com/jsulam/Online-Dictionary-Learning-demo.git tensor_factorisation/dictionary_learning/odl
echo tensor_factorisation/dictionary_learning/odl>>.gitignore

rm -rf tensor_factorisation/dictionary_learning/ksvd
git clone https://github.com/nel215/ksvd.git tensor_factorisation/dictionary_learning/ksvd
echo tensor_factorisation/dictionary_learning/ksvd>>.gitignore

rm -rf tensor_factorisation/dictionary_learning/lyssandra
git clone https://github.com/ektormak/Lyssandra.git tensor_factorisation/dictionary_learning/lyssandra
echo tensor_factorisation/dictionary_learning/lyssandra>>.gitignore

rm -rf tensor_factorisation/dictionary_learning/multi_dim_mdla
git clone https://github.com/sylvchev/mdla.git tensor_factorisation/dictionary_learning/multi_dim_mdla
echo tensor_factorisation/dictionary_learning/multi_dim_mdla>>.gitignore

rm -rf tensor_factorisation/dictionary_learning/multi_dim_ktsvd
git clone https://github.com/takshingchan/ktsvd.git tensor_factorisation/dictionary_learning/multi_dim_ktsvd
echo tensor_factorisation/dictionary_learning/multi_dim_ktsvd>>.gitignore

rm -rf tensor_factorisation/dictionary_learning/multi_dim_tensor_sparsecoding
git clone https://github.com/hust512/Tensor_Sparse_Coding.git tensor_factorisation/dictionary_learning/multi_dim_tensor_sparsecoding
echo tensor_factorisation/dictionary_learning/multi_dim_tensor_sparsecoding>>.gitignore

rm -rf tensor_factorisation/tensorly
git clone https://github.com/tensorly/tensorly.git tensor_factorisation/tensorly
echo tensor_factorisation/tensorly>>.gitignore

rm -rf tensor_factorisation/pymf
git clone https://github.com/cthurau/pymf.git tensor_factorisation/pymf
echo tensor_factorisation/pymf>>.gitignore

rm -rf tensor_factorisation/algebraic_pgd_tools
export GIT_SSL_NO_VERIFY=1
git clone https://git.lacan.upc.edu/zlotnik/algebraicPGDtools.git tensor_factorisation/algebraic_pgd_tools
export GIT_SSL_NO_VERIFY=0
echo tensor_factorisation/algebraic_pgd_tools>>.gitignore

rm -rf tensor_factorisation/h_matrices/awesome_hmatrices
git clone https://github.com/gchavez2/awesome_hierarchical_matrices.git tensor_factorisation/h_matrices/awesome_hmatrices
echo tensor_factorisation/h_matrices/awesome_hmatrices>>.gitignore

rm -rf tensor_factorisation/h_matrices/h2tools
git clone https://bitbucket.org/muxas/h2tools.git tensor_factorisation/h_matrices/h2tools
echo tensor_factorisation/h_matrices/h2tools>>.gitignore

rm -rf tensor_factorisation/h_matrices/hmatrix1
git clone https://github.com/maekke97/HierarchicalMatrices.git tensor_factorisation/h_matrices/hmatrix1
echo tensor_factorisation/h_matrices/hmatrix1>>.gitignore

rm -rf tensor_factorisation/h_matrices/hmatrix2
git clone https://github.com/haskell-numerics/hmatrix.git tensor_factorisation/h_matrices/hmatrix2
echo tensor_factorisation/h_matrices/hmatrix2>>.gitignore

rm -rf tensor_factorisation/quantics_tensor_train/pydecomp
git clone https://github.com/llestandi/pydecomp.git tensor_factorisation/quantics_tensor_train/pydecomp
echo tensor_factorisation/quantics_tensor_train/pydecomp>>.gitignore

rm -rf tensor_factorisation/quantics_tensor_train/qtt
git clone https://github.com/gasongjian/QTT.git tensor_factorisation/quantics_tensor_train/qtt
echo tensor_factorisation/quantics_tensor_train/qtt>>.gitignore
```

### Matlab
```
rm -rf matlab/mtimesx
git clone https://github.com/cybertk/mtimesx.git matlab/mtimesx
echo matlab/mtimesx>>.gitignore

rm -rf matlab/mbeautifier
git clone https://github.com/davidvarga/MBeautifier.git matlab/mbeautifier
echo matlab/mbeautifier>>.gitignore
```

### FEM homogenization
http://www.ltas-cm3.ulg.ac.be/openSource.htm
```
rm -rf fem/homogenization/cm3libraries
git clone https://gitlab.onelab.info/cm3/cm3Libraries.git fem/homogenization/cm3libraries
echo fem/homogenization/cm3libraries>>.gitignore

rm -rf fem/homogenization/cm3data
git clone https://gitlab.onelab.info/cm3/cm3Data.git fem/homogenization/cm3data
echo fem/homogenization/cm3data>>.gitignore
```
