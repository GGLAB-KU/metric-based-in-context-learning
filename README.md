# Metric-Based In-Context Learning: A Case Study in Text Simplification

This is code for the implementation of the paper "Metric-Based In-Context Learning: A Case Study in Text Simplification."

In the code folder of the repository, you will find the code used to generate data for all of the experiments, including calls to the GPT-3 API and our own implementation of KATE-GPT for example selection.

In the results folder of the repository, you will find the results for all experiments that were explained in the paper. The results folder has several sub-folders, for the various experiments that were done. The names of the sub-folders correspond to the method of selecting examples. Each individual folder has its own README with more information on the files and folders inside. 
* BERTPrec - BERTPrec selected examples
* CR - Compression Ratio selected examples
* EASSE Reports - This includes the original EASSE reports with information on the BLEU, SARI, and FKGL scores of each experiment. They can be replicated using the original EASSE code linked here: EASSE
* FestAbility - SOTA results replicated on the FestAbility dataset during task-transfer experiments
* KATE-GPT - We tried using KATE-GPT to select examples, and the folder includes our results and code utilizing that method.
* Ordering Examples - We ordered the examples selected by scores in different ways, and this folder includes those results.
* Random Baseline - Results of our random baseline
* SARI - SARI selected examples
* Zeroshot - Model's zero-shot results

In the eval folder, the EASSE reports for each of the experiments are provided. The code and implementation of how to generate the EASSE reports is also provided, so you can replicate our SARI and BLEU scores in our results.

If you have any questions, please feel free to email subhavee2@gmail.com. Thank you!
