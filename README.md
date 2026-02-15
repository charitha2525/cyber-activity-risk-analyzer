this program analyzes student login activity scores to detect suspicious behavior. it performs data cleaning ,categorizes risk levels, applies personalized filtering ,and generates a final security report.
the program performs the following steps:
it accepts the list of integer activity scores.
divided into different categorizes 
0-30 ->low-risk
31-60 ->medium-risk
61->99 ->high-risk
above 100 ->critical-risk
applies personalized security filtering based on register number
generates final security report
personalized filtering logic
enter the last three digits of your register number 
find the sum of the digits .if the sum of the digit is even the remove all the elements from the medium-risk otherwise remove all the elements of the critical-risk
in this python challenge we strictly follow only conditional statements and loops no build functions.
