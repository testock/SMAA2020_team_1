# Data Transfrom

The goal of this part is to transform the json files (see dataset part) into IOB form files.

The tags is : 
-> ***P*** : the parties of cases
-> ***A*** : the author of the opinion of the case 
-> ***D*** : the date of case
-> ***N*** : the number of the files

***Be careful*** with path data of in different script (all information are in the script.

## Use scripts

To have IOB for data you need to execute in this order:

        python make_xml.py
        python make_meta.py
        python make_text.py
        python make_data.py


