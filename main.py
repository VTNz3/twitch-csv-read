import pandas as pd
import time
import glob
import os
import sys
import csv

number = input('Enter number to find\n')

def append_list_as_row(file_name, list_of_elem):
    # Open file in append mode
    with open(file_name, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        csv_writer = csv.writer(write_obj)
        # Add contents of list as last row in the csv file
        csv_writer.writerow(list_of_elem)

path = ".\directory/"
newFiles = []
prevIsEmpty = False
items = []
text_files = glob.glob(path + "/**/*.csv", recursive = True)
for file in range(len(text_files)):
    if (file%2!=0):
        newFiles.append(text_files[file])

with open('.\outputs/output.csv', 'w', encoding='UTF8', newline='') as f:
    print("sad")
    writer = csv.writer(f)
    writer = csv.DictWriter(f, fieldnames = ['user_id', 'payout_entity_id', 'ad_share_gross', 'sub_share_gross', 'bits_share_gross', 'bits_developer_share_gross', 'bits_extension_share_gross', 'prime_sub_share_gross', 'bit_share_ad_gross', 'fuel_rev_gross', 'bb_rev_gross', 'report_date'])
    writer.writeheader()

start = time.time()
indx = 1
for filee in newFiles:
    print(indx)
    splitted = filee.split(os.sep)
    fileName = splitted[7]
    data = pd.read_csv(filee)
    data.dropna(inplace=True)
    xxx = data[data["user_id"] == int(number)]
    xxx.head()
    xxx.sort_index(inplace=True)
    if (indx != 1):
        print("ok")
        if (prevIsEmpty == False):
            if  ((str(i1) == str(xxx.iloc[0]['user_id'])) and (str(i2) == str(xxx.iloc[0]['payout_entity_id'])) and (str(i3) == str(xxx.iloc[0]['ad_share_gross'])) and (str(i4) == str(xxx.iloc[0]['sub_share_gross'])) and (str(i5) == str(xxx.iloc[0]['bits_share_gross'])) and (str(i6) == str(xxx.iloc[0]['bits_developer_share_gross'])) and (str(i7) == str(xxx.iloc[0]['bits_extension_share_gross'])) and (str(i8) == str(xxx.iloc[0]['prime_sub_share_gross'])) and (str(i9) == str(xxx.iloc[0]['bit_share_ad_gross'])) and (str(i10) == str(xxx.iloc[0]['fuel_rev_gross'])) and (str(i11) == str(xxx.iloc[0]['bb_rev_gross'])) and (str(i12) == str(xxx.iloc[0]['report_date']))):
            ##if (str(i1) == str(xxx.iloc[0]['user_'])):
                indx = indx + 1
                continue


    print("789")
    if xxx.empty:
        print("bos")
        indx = indx + 1
        prevIsEmpty = True
        continue
    else:
        prevIsEmpty = False
        print("degil")
        items.append(xxx.iloc[0])
        xxx.to_csv('.\outputs/output.csv', mode='a', index=False, header=False)
        i1 = xxx.iloc[0]['user_id']
        i2 = xxx.iloc[0]['payout_entity_id']
        i3 = xxx.iloc[0]['ad_share_gross']
        i4 = xxx.iloc[0]['sub_share_gross']
        i5 = xxx.iloc[0]['bits_share_gross']
        i6 = xxx.iloc[0]['bits_developer_share_gross']
        i7 = xxx.iloc[0]['bits_extension_share_gross']
        i8 = xxx.iloc[0]['prime_sub_share_gross']
        i9 = xxx.iloc[0]['bit_share_ad_gross']
        i10 = xxx.iloc[0]['fuel_rev_gross']
        i11 = xxx.iloc[0]['bb_rev_gross']
        i12 = xxx.iloc[0]['report_date']
    indx = indx + 1
# dropping null value columns to avoid errors

end = time.time()
print(end-start)



