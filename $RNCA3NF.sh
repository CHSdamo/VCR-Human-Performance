#!/bin/bash

#SBATCH --mail-user=shenchu@tnt.uni-hannover.de
#SBATCH --mail-type=ALL             # Eine Mail wird bei Job-Start/Ende versendet
#SBATCH --job-name=r2c_triplet       # Name unter dem der Job in der Job-History gespeichert wird
#SBATCH --output=./slurm_log/test_gmail1.txt         # Logdatei für den merged STDOUT/STDERR output
#SBATCH --partition=gpu_cluster_enife # Partition auf der gerechnet werden soll
                                    #   ohne Angabe des Parameters wird auf der Default-Partition gerechnet
#SBATCH --nodes=1                   # Reservierung von 2 Rechenknoten
                                    #   alle nachfolgend reservierten CPUs müssen sich auf den reservierten Knoten befinden
#SBATCH --gres=gpu:1
#SBATCH --mem=16G
#SBATCH --cpus-per-task=8
echo "Here begin to train r2c"
working_dir=~/code/r2c/models
cd $working_dir
srun hostname
source activate r2c
#sh train_refine.sh
#sh train_h2.sh
# python eval.py
# python eval_ensemble_online.py
srun python train.py
echo "training  train r2c!"
