#!/bin/bash
#SBATCH -J RPMovie
#SBATCH --account=gts-jw254                     
#SBATCH -N2 --ntasks-per-node=20                 
#SBATCH --mem-per-cpu=1G                        
#SBATCH -t4:00:00                              
#SBATCH -qinferno                               
#SBATCH -oReport-%j.out                         
#SBATCH --mail-type=BEGIN,END,FAIL              
#SBATCH --mail-user=bsherwin6@gatech.edu        
srun python Movie.py