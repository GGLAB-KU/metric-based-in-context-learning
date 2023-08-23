This folder contains model outputs for TurkCorpus, ASSET, and FestAbility datasets. The folders are organized as follows:

* BERTPrec - Examples selected using the BERTPrecision metric.
* CR - Examples selected by highest compression ratio.
* FestAbility - SOTA results replicated on the FestAbility dataset during task-transfer experiments
* KATE-GPT - Examples selected with the KATE-GPT algorithm.
* Ordering Examples - We ordered the examples selected by scores in different ways, and this folder includes those results.
* Random Baseline - We perform 3 random baseline experiments, where we randomly select examples without any particular metric in mind.
* SARI - Examples selected using the SARI metric.
* Zero-shot - The model was only given the prompt to simplify, and no examples were provided in this experiment.