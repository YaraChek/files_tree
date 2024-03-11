# Scripts for renaming files in the specified directory.
***underscore_to_dash.py*** - is the main file.  
  
*create_files_random_names.py* - a script to create test files by randomly combining a random number (up to six) of words from “words.txt” sometimes adding the words “patch” to the end of the name.  
Underscores are replaced with dashes. The word “patch” at the end of the name has been removed.  
The script displays information about non-renamed *problematic* files to the terminal and writes it to the log file.
Then it overwrites yaml-file: deletes renamed old filenames from the file list and adds new filenames to the end of the file list.

-----------------

*Example files before ranaming (Attention: the last 4 files are problematic):*

1. account-workflow-approval-lh-patch.yaml
2. amount-flow-loan-patch.yaml
3. application_approval_sell_salesforce_opt_workflow_patch.yaml
4. commodity-patch-riddle-processor-under-patch.yaml
5. crew_workflow_account_fee.yaml
6. down_side_lh_patch.yaml
7. flow-sales-crew-patch.yaml
8. forced-start-fee-pay-patch.yaml
9. hook-customer-lh-end-able-patch.yaml
10. loan_sell_otp_patch.yaml
11. mirror-riddle-mambu-finance-begin.yaml
12. opt-crew-trade-follow-mirror.yaml
13. otp_matching_working_able_buy_amount_patch.yaml
14. payment-stand-opt-between-otp-ability.yaml
15. pay_ua_commodity_loan_patch.yaml
16. proceed-working-patch.yaml
17. salesforce_run_approval_sales_loan_patch.yaml
18. stab-sell-up-payment-application-patch.yaml
19. stab_stab_application_proceed_patch.yaml
20. standard_back_sales_front_able.yaml
21. throw-archive-begin-patch.yaml
22. throw_common.yaml
23. ua_able_able_patch.yaml
24. under_medium_crew_hook_ua.yaml
25. v2-work-sell-pay.yaml
26. webhook-customer-loan-arc-standard-patch.yaml
27. work-ability-tree-between-finance-patch.yaml
28. workflow_loan_pay_sell.yaml
29. working_flow_to_patch.yaml
30. pay-trade-patch.yaml
31. pay_trade_patch.yaml
32. pay-trade.yaml
33. pay_trade.yaml

*Example filenames after ranaming:*

1. account-workflow-approval-lh.yaml
2. amount-flow-loan.yaml
3. application-approval-sell-salesforce-opt-workflow.yaml
4. commodity-patch-riddle-processor-under.yaml
5. crew-workflow-account-fee.yaml
6. down-side-lh.yaml
7. flow-sales-crew.yaml
8. forced-start-fee-pay.yaml
9. hook-customer-lh-end-able.yaml
10. loan-sell-otp.yaml
11. mirror-riddle-mambu-finance-begin.yaml
12. opt-crew-trade-follow-mirror.yaml
13. otp-matching-working-able-buy-amount.yaml
14. payment-stand-opt-between-otp-ability.yaml
15. pay-ua-commodity-loan.yaml
16. proceed-working.yaml
17. salesforce-run-approval-sales-loan.yaml
18. stab-sell-up-payment-application.yaml
19. stab-stab-application-proceed.yaml
20. standard-back-sales-front-able.yaml
21. throw-archive-begin.yaml
22. throw-common.yaml
23. ua-able-able.yaml
24. under-medium-crew-hook-ua.yaml
25. v2-work-sell-pay.yaml
26. webhook-customer-loan-arc-standard.yaml
27. work-ability-tree-between-finance.yaml
28. workflow-loan-pay-sell.yaml
29. working-flow-to.yaml
30. pay-trade-patch.yaml
31. pay_trade_patch.yaml
32. pay-trade.yaml
33. pay_trade.yaml

-----------------

There already exists the file named "pay-trade.yaml" in result directory in our example. Files "pay-trade-patch.yaml", "pay_trade_patch.yaml", "pay_trade.yaml" must be renamed into "pay-trade.yaml". That's why the files won't be proceeded and the information about this will be displayed to the terminal and will be written to the log file.
