# umich_sanger_seq
This script downloads multiple Sanger sequencing files (.ab1 format) from the University of Michigan sequencing core concurrently, while changing the file name from "Sample Number" to "Sample Name".

## Getting started
Create an excel file in the same directory as the script called "sequencing_xcel". Copy the spreadsheet from the sequencing core submission into the sequencing_xcel file, copying over pre-existing lines if necessary. Save the file, then run `python umich_seq_pyX.py`. You will be prompted to type in your username (often your last name), your PI's name (often their last name), and your lab password. The script will then download and rename all the files listed in your sequencing_xcel file to the sample name given on submission.

Note: umich_seq_py2.py is written in python2 and umich_seq_py3.py is written in python3.

This script works on Mac and Windows.

## Dependencies
 - pandas
 - requests
 - lxml
 - xlrd (no longer automatically loaded with pandas)
