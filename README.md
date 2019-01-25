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

## Tara Ocean Metagenomes training set preparation
Assembled sequences from the Tara Ocean expedition were downloaded from EBI metagenomics (list of the metagenomes in Supplemental File2). Contigs with a size less than 5kb were filtered out, and Centrifuge v1.0.4-beta (https://github.com/infphilo/centrifuge) was run on the remaining sequences using the Bacteria, Archaea, Human and Virus compressed index (updated 12/06/2016), using the default settings. 
Centrifuge is classification engine that enables rapid, accurate, and sensitive labeling of metagenomic sequences. The system uses an optimized indexing scheme that requires a relatively small index and classifies sequences at very high speed (Kim et al. 2016)
Sequences in the microbiomes with viral matches were removed from the negative training set. Sequences in viromes with a Bacterial, Archeal or Human match were removed from the positive training set. The remaining sequences were broken down to 5000bp to be used as training set.

## VirFinder training and evaluation parameters
VirFinder version 1.1 was used, and the Tara-trained models were trained using the built-in training function, using a kmer-size of 8bp and a training set of 10 000 viral and 10 000 non-viral sequences randomly selected from the cleaned Tara metagenomic sequences broken down to 5000pb. A Tara-trained model is available in :
https://github.com/aponsero/VirFinder_Tara_trained_models/VirFinder_Tara_trained_models/Models/VF.trainModUser.mod1_Tara_10k.rda 
