# VirFinder_Tara_trained_models
Machine learning models for VirFinder trained using the Tara Ocean viromes and metagenomes

## Description
Logistic classifier for the classification of viral and non viral contig sequences from marine metagenomes. The model was trained on Tara Ocean metagenomes and viromes (the list of samples used for the training is available in Document/list.txt and raw sequence files available in Documents/Training_set). 

The Tara-trained model was trained using VirFinder training function, on 10 000 viral sequences and 10 000 non viral sequences of 5000pb with a kmer size of 8pb.

## usage
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

## Training set cleaning

Prior to be used for the model training, the Tara Ocean metagenomes were cleaned for potential viral sequences using[Centrifuge](https://github.com/infphilo/centrifuge/releases/tag/v1.0.3) (version 1.0.3, database Bacteria, Archea, Virus, Human as updated in 12/06/2016).
The Tara Ocean viromes were cleaned for potential non-viral sequences using Centrifuge. A second cleaning step was performed using a logistic classifier trained on 20 000 viral and 20 000 non-viral sequences of 5000pb from the RefSeq genome database.The logistic classifier was trained using the [graphlab create python library](https://turi.com/download/install-graphlab-create.html) using a L2 penalty of O.5 to avoid overfitting. and is available in Scripts/modelk8v1_5000pb_L2_0.5_ex20000vs20000. Sequences from the Tara viromes classified as non-viral with a certainty treshold above 0.9 were removed from the training set.
An example script for using the RefSeq trained logistic classifier is provided in Scripts/example.py and the pipeline to extract kmer frequencies from contig sequences is available [here](https://github.com/aponsero/kmer_frequency_python).
