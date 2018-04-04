import pandas as pd
import requests
from lxml import html
import getpass

# Acquiring user information.
username = raw_input("Please input your username: ")
lab_pi = raw_input("Please input your PI name: ")
lab_pass = getpass.getpass(
            prompt="Please input your password (case sensitive): ")

# Opening excel spreadsheet containing sample information.
sequencing_csv = pd.read_excel('sequencing_xcel.xlsx', header=None)

# Generating a dictionary that has the submission numbers tied to the names.
name_dict = {}
for index, row in sequencing_csv.iterrows():
    try:
        temp = int(row[0])
    except:
        continue
    name_dict[temp] = row[2]

# Accessing sequencing core webpage.
r = requests.get('https://%s:%s@client-seqcore.brcf.med.umich.edu/users/%s/%s/'
                 % (lab_pi, lab_pass, lab_pi, username))

# Getting the content from the webpage.
webpage = html.fromstring(r.content)

# Generating a list of just the downloadable files.
temp_list = webpage.xpath('//a/@href')

# Getting the sample names from the name_dict dictionary keys.
key_list = [str(unit) for unit in name_dict.keys()]

# Making a list of the files that are both on the webpage and in key_list.
files_needed = [item for item in temp_list if
                str(item.split('.')[0]) in key_list]

# Getting just the .ab1 files and ignoring the .seq files.
ab1_elements = [item for item in files_needed if 'ab1' in item]

# Generating a string to allow downloading of each .ab1 sample.
sample_string = ('https://%s:%s@client-seqcore.brcf.med.umich.edu/users/%s/%s/'
                 % (lab_pi, lab_pass, lab_pi, username))

# Iterating through and downloading each ab1 files
for item in ab1_elements:
    try:
        with open('./%s.%s' % (name_dict[int(item.split('.')[0])],
                  '.'.join(item.split('.')[1:])), 'wb') as fd:
            temp_r = requests.get(sample_string+item)
            fd.write(temp_r.content)
            fd.close()
    except:
        print "Couldn't download sample: %s" % str(item)