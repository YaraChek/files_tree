# Scripts for renaming files in the specified directory and update specified file.
***main.py*** - is the main file.  
  
*create_files_random_names.py* - a script to create test files by randomly combining a random number (up to six) of words from “words.txt” sometimes adding the words “patch” to the end of the name.  
  
Underscores are replaced with dashes. The word “patch” at the end of the name has been removed.  
The script displays information about non-renamed *problematic* files to the terminal and writes it to the log file.  
Then it overwrites yaml-file: deletes renamed old filenames from the file list and adds new filenames to the end of the file list.    
  
You can customize file generation and renaming by editing the files "settings_create_files.yaml" 
and "settings_rename_files.yaml", which are located in the "presets" directory.

-----------------

*Example files before ranaming (Attention: the last 4 files are problematic):*

1. ability-between-to-application-tree-patch.yaml
2. ability-hook-back-crew-pay-customer.yaml
3. ability_medium_approval_crew.yaml
4. able_young_v2_customer_sell_patch.yaml
5. approval_jan_common_buy_buy_customer_patch.yaml
6. back-riddle-middle-begin-customer-force.yaml
7. between_front_run_yield.yaml
8. eagle_end_patch.yaml
9. end_run_trade_web_under.yaml
10. follow-force-follow-processor.yaml
11. follow_force_walk_grand_jewel_v2_patch.yaml
12. force_bought_able_arc_able.yaml
13. force_fill_version_noon_patch.yaml
14. front_application_xpro_xpro_flower_patch.yaml
15. front_island_amount_patch.yaml
16. hedgehog_customer_zeal_stand.yaml
17. ignore_grand_down_work_jan_medium_patch.yaml
18. ignore_throw.yaml
19. lead_lead_between_mirror_tree.yaml
20. light-buy-processor-salesforce-patch.yaml
21. patch-arc-medium.yaml
22. patch_lead_follow_ignore_patch.yaml
23. standard-middle-up-amount.yaml
24. standard_processor.yaml
25. stand_tree_patch.yaml
26. to-customer-proceed-patch.yaml
27. under-ability-start-front-walkman.yaml
28. working-between-narrow-eagle.yaml
29. work-light-stand-young-side-between.yaml
30. zeal-able-opt-jan-patch.yaml
31. zeal_able_opt_jan_patch.yaml
32. zeal-able-opt-jan.yaml
33. zeal_able_opt_jan.yaml

*Example filenames after ranaming:*

1. ability-between-to-application-tree.yaml
2. ability-hook-back-crew-pay-customer.yaml
3. ability-medium-approval-crew.yaml
4. able-young-v2-customer-sell.yaml
5. approval-jan-common-buy-buy-customer.yaml
6. back-riddle-middle-begin-customer-force.yaml
7. between-front-run-yield.yaml
8. eagle-end.yaml
9. end-run-trade-web-under.yaml
10. follow-force-follow-processor.yaml
11. follow-force-walk-grand-jewel-v2.yaml
12. force-bought-able-arc-able.yaml
13. force-fill-version-noon.yaml
14. front-application-xpro-xpro-flower.yaml
15. front-island-amount.yaml
16. hedgehog-customer-zeal-stand.yaml
17. ignore-grand-down-work-jan-medium.yaml
18. ignore-throw.yaml
19. lead-lead-between-mirror-tree.yaml
20. light-buy-processor-salesforce.yaml
21. patch-arc-medium.yaml
22. patch-lead-follow-ignore.yaml
23. standard-middle-up-amount.yaml
24. standard-processor.yaml
25. stand-tree.yaml
26. to-customer-proceed.yaml
27. under-ability-start-front-walkman.yaml
28. working-between-narrow-eagle.yaml
29. work-light-stand-young-side-between.yaml
30. zeal-able-opt-jan-patch.yaml
31. zeal_able_opt_jan_patch.yaml
32. zeal-able-opt-jan.yaml
33. zeal_able_opt_jan.yaml

-----------------

There already exists the file named "zeal-able-opt-jan.yaml" in result directory in our example. 
Files "zeal-able-opt-jan-patch.yaml", "zeal_able_opt_jan_patch.yaml" and "zeal_able_opt_jan.yaml" 
must be renamed into "zeal-able-opt-jan.yaml". That's why the files won't be proceeded and the
information about this will be displayed to the terminal and will be written to the log file.
