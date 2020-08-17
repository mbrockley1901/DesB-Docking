#!/bin/bash

#preparing receptor pdbqt file with MGLtools
#python prepare_receptor4.py -r DesB_6XBBB.pdb -U 'waters' -A 'hydrogens'

#preparing ligand pdbqt files
for molecule in ligands/*.pdb; do
	python prepare_ligand4.py -l ${molecule} -A 'hydrogens' -B
done


#docking execution
for substrate in ./ligands/*.pdbqt; do
	{vina_program_path} --receptor DesB_6XBBB.pdbqt --ligand $substrate --config conf.txt --out "./results/vina_${basename substrate}" --log "./logs/log_${basename -s .pdbqt substrate).txt"
done
