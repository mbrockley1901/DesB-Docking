#iterative Autodock Vina
import os

#structures
enzyme = "DesB_6XBBB.pdbqt" #enzyme must be in pdbqt format
substrates = ["1_3_diaminopentane", "1_3_diaminopropane", "n_butylamine",
	"ornithine", "spermidine", "lysine", "putrescine", "cadaverine"]

#docking each substrate with DesB
for ligand in substrates:
	
	logfile = "logs/log_" + ligand + ".txt"
	output = "results/vina_" + ligand + ".pdbqt"
	command = "C:\Program Files (x86)\The Scripps Research Institute\Vina\'vina" + " --receptor " + enzyme + "--ligand " + "ligands/" + ligand + ".pdbqt" " --config conf.txt --out " + output + " --log " + logfile
	"""concatenates strings for execution"""
	
	#this command changes based on the location of vina and the Os of the system
	os.system(command)
	#executes command
	
