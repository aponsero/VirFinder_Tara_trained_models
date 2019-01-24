# VirFinder_Tara_trained_models
Machine learning models for VirFinder trained using the Tara Ocean viromes and metagenomes

## Description
Logistic classifier for the classification of viral and non viral contig sequences from marine metagenomes. The model was trained on Tara Ocean metagenomes and viromes (the list of samples used for the training is available in Document/list.txt and raw sequence files available in Documents/Training_set). 

The Tara-trained model was trained using VirFinder training function, on 10 000 viral sequences and 10 000 non viral sequences of 5000pb with a kmer size of 8pb.

## Usage
The installation of VirFinder is described here https://github.com/jessieren/VirFinder

To use the custom Tara-trained model, download the model from Models/VF.trainModUser.mod1_Tara_10k.rda 

In order to use the model on contigs, use the following code :

```
library(VirFinder)

### load the model

modFile <- "<path_to_the_model_file>/VF.trainModUser.mod1_Tara_10k.rda"
load(modFile)

### predict the contigs using the customized model
inFaFile <- system.file("data", "<path_to_the_contig_file>/contigs.fa")
predResultUser <- VF.pred.user(inFaFile, VF.trainModUser)
predResultUser
```
