# [Intel(R) Extension for Scikit-learn](https://github.com/intel/scikit-learn-intelex)
# Speed up your scikit-learn applications for Intel(R) CPUs and GPUs across single- and multi-node configurations
# Intel(R) Extension for Scikit-learn is a free software AI accelerator designed to deliver over 10-100X acceleration to your existing scikit-learn code. The software acceleration is achieved with vector instructions, AI hardware-specific memory optimizations, threading, and optimizations for all upcoming Intel(R) platforms at launch time.

import numpy as np
from sklearnex import patch_sklearn

patch_sklearn()

from sklearn.cluster import DBSCAN

X = np.array([[1.0, 2.0], [2.0, 2.0], [2.0, 3.0], [8.0, 7.0], [8.0, 8.0], [25.0, 80.0]], dtype=np.float32)
clustering = DBSCAN(eps=3, min_samples=2).fit(X)
print(clustering.labels_)