# -*- coding: utf-8 -*-

import numpy as np
from collections import namedtuple

def read_xyz_traj(file):
    
    with open(file) as f:
        num_s = 0;
        cell = np.zeros((0,2), dtype = object);
        
        rd = f.readline();
        
        while rd:
            n_atoms = int(rd);
            title = f.readline()[:-1];
            coords = np.zeros([n_atoms, 3], dtype="float64");
            atomtypes = [];
            for x in coords:
                line = f.readline().split()
                atomtypes.append(line[0])
                x[:] = list(map(float, line[1:4]))
            z = namedtuple("xyz_record", ["coords", "title", "atomtypes"]) \
                (coords, title, atomtypes);
            num_s += 1;
            cell.resize(num_s,2);
            cell[num_s-1,0] = num_s;
            cell[num_s-1,1] = z;
            rd = f.readline();
    f.closed
    
    return cell;
