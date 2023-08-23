The package EASSE was used to generate reports for our project.

As per the original implementation, we use "easse report" to generate detailed reports. We use the 'custom' functionality for easse to evaluate on both TurkCorpus, ASSET, and FestAbility sentences. The original datasets of TurkCorpus, ASSET, and FestAbility are copied directly from the original papers, and they are also provided in this folder for ease of access.

For ASSET, TurkCorpus, and Festability, we use the following code to generate reports, where YOUR_PATH_HERE is a string with the relative path of the file you are trying to assess. The specific directories may need to be changed based on where you store the original datasets.

ASSET:
```easse report -t custom --orig_sents_path "new_datasets/asset_test/ASSET_Orig.txt" --refs_sents_paths "./new_datasets/asset_test/ASSET_Simp0.txt,./new_datasets/asset_test/ASSET_Simp1.txt,./new_datasets/asset_test/ASSET_Simp2.txt,./new_datasets/asset_test/ASSET_Simp3.txt,./new_datasets/asset_test/ASSET_Simp4.txt,./new_datasets/asset_test/ASSET_Simp5.txt,./new_datasets/asset_test/ASSET_Simp6.txt,./new_datasets/asset_test/ASSET_Simp7.txt,./new_datasets/asset_test/ASSET_Simp8.txt,./new_datasets/asset_test/ASSET_Simp9.txt" --sys_sents_path YOUR_PATH_HERE```

TurkCorpus:
```easse report -t custom --orig_sents_path "new_datasets/general_datasets/TURK_Original_Cleaned.txt" --refs_sents_paths "./new_datasets/turk_test_cleaned/TURK_SIMP0_Cleaned.txt,./new_datasets/turk_test_cleaned/TURK_SIMP1_Cleaned.txt,./new_datasets/turk_test_cleaned/TURK_SIMP2_Cleaned.txt,./new_datasets/turk_test_cleaned/TURK_SIMP3_Cleaned.txt,./new_datasets/turk_test_cleaned/TURK_SIMP4_Cleaned.txt,./new_datasets/turk_test_cleaned/TURK_SIMP5_Cleaned.txt,./new_datasets/turk_test_cleaned/TURK_SIMP6_Cleaned.txt,./new_datasets/turk_test_cleaned/TURK_SIMP7_Cleaned.txt" --sys_sents_path YOUR_PATH_HERE```

FestAbility:
```easse report -t custom --orig_sents_path "new_datasets/general_datasets/Fest_Orig.txt" --refs_sents_paths "./new_datasets/general_datasets/Fest_Simp.txt" --sys_sents_path YOUR_PATH_HERE```


