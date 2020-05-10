from angstrom import Molecule
import numpy as np


mol = Molecule(read="intersection-of-32-pipes-cross-section.xyz")
ref_atom = 5000
ref_coor = mol.coordinates[ref_atom]
cutoff = 200

atoms, coords = [], []
for idx, (a, c) in enumerate(zip(mol.atoms, mol.coordinates)):
    dist = np.linalg.norm(ref_coor - c)
    if dist < cutoff:
        atoms.append(a)
        coords.append(c)
new_mol = Molecule(atoms=atoms, coordinates=coords)
new_mol.write("new.xyz")
