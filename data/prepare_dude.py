# wget http://dude.docking.org/db/subsets/all/all.tar.gz
# tar -xzvf all.tar.gz
from glob import glob
import pandas as pd
import os


dude_target_names = set(map(lambda x: os.path.split(x)[-1], glob("all/*")))
table = pd.read_html("http://dude.docking.org/targets")[1]
name_to_pdb_mapping = dict(zip(table['Target Name'].lower(), table.PDB))
pdbbind_processed = set(map(lambda x: os.path.split(x)[-1], glob("PDBBind_processed")))
dude_pbd = set(map(lambda x: name_to_pdb_mapping[x], dude_target_names))
overlapped = dude_pdb & pdbbind_processed
with open('dude', 'w') as f:
    f.write('\n'.join(overlapped))
