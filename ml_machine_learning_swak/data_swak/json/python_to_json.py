# python python_to_json.py && cat output_file.json

import json
import fire
import numpy as np
import pathlib

class NumpyArrayEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        else:
            return super(NumpyArrayEncoder, self).default(obj)
    
def main_python_function(file_name='del_output_file'):

    out_dict = {}

    for k in range(2):
        out_dict[f'key_{k}'] = f'key_{k}_value'

    young = 210000
    posn =  0.22

    K_IC = 1e-3
    fracture_energy = K_IC**2 / young * (1-posn**2)
    print(fracture_energy)
    # print(f'{fracture_energy =}')

    shear_modulus = young / (2 * (1.0 + posn))
    bulk_modulus = young / (3 * (1.0 - 2.0 * posn))

    I2 = np.asarray([1.0, 1.0, 1.0, 0, 0, 0])
    I4 = np.eye(6)
    IxI = np.outer(I2, I2)
    P1 = IxI / 3.0
    P2 = I4 - P1
    stiffness_mandel = bulk_modulus * IxI + 2.0 * shear_modulus * P2
    stiffness = np.copy(stiffness_mandel)
    stiffness[3:, 3:] = stiffness[3:, 3:] / 2
    stiffness[:3, 3:] = stiffness[:3, 3:] / np.sqrt(2)
    stiffness[3:, :3] = stiffness[3:, :3] / np.sqrt(2)

    out_dict[f'solver_options']={'solver':'cg','max_iter':stiffness}

    with open(f'{file_name}.json', 'w', encoding='utf-8') as f:
        json.dump(out_dict, f, ensure_ascii=False, indent=4,cls=NumpyArrayEncoder)

if __name__ == '__main__':
    fire.Fire(main_python_function)
