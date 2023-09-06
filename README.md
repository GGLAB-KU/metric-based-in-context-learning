# Metric-Based In-Context Learning: A Case Study in Text Simplification

This is code for the implementation of the paper ["Metric-Based In-Context Learning: A Case Study in Text Simplification."](https://arxiv.org/abs/2307.14632) (Will be published at INLG 2023 proceedings)

## Code

In the code folder of the repository, you will find the code used to generate data for all of the experiments, including how to generate simplifications from GPT-3 (used in all of our example selection experiments) and our own implementation of KATE-GPT for optimized example selection.

## Outputs

In the output folder of the repository, you will find the results for all experiments present in the paper. The results folder has several sub-folders, for the various methods of example selection that were performed. The names of the sub-folders correspond to the method of selecting examples. Each individual folder has its own README with more information regarding the files and folders inside. 

## Evaluation

In the eval folder, the code and implementation of how to generate the EASSE reports are provided, so you can replicate our SARI and BLEU scores in our results. The original datasets that our generations are compared against are also provided for ease of access and use.

If you have any questions, please feel free to email subhavee2@gmail.com. Thank you!
