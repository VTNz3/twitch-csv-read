import pandas as pd
import time
import glob
import os
import csv

number = input('Twitch kullanıcı kimliğini girin. -- (twitchinsights.net/checkuser adresinden aratabilirsiniz)\n')

def append_list_as_row(file_name, list_of_elem):
    with open(file_name, 'a+', newline='') as write_obj:
        csv_writer = csv.writer(write_obj)
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
    writer = csv.writer(f)
    writer = csv.DictWriter(f, fieldnames = ['user_id', 'payout_entity_id', 'ad_share_gross', 'sub_share_gross', 'bits_share_gross', 'bits_developer_share_gross', 'bits_extension_share_gross', 'prime_sub_share_gross', 'bit_share_ad_gross', 'fuel_rev_gross', 'bb_rev_gross', 'report_date'])
    writer.writeheader()

start = time.time()
index = 1
for filee in newFiles:
    print(str(index) + ": İşlem başlıyor...")
    data = pd.read_csv(filee)
    data.dropna(inplace=True)
    wData = data[data["user_id"] == int(number)]
    wData.head()
    wData.sort_index(inplace=True)
    if (index != 1):
        if (prevIsEmpty == False):
            if  ((str(i1) == str(wData.iloc[0]['user_id'])) and (str(i2) == str(wData.iloc[0]['payout_entity_id'])) and (str(i3) == str(wData.iloc[0]['ad_share_gross'])) and (str(i4) == str(wData.iloc[0]['sub_share_gross'])) and (str(i5) == str(wData.iloc[0]['bits_share_gross'])) and (str(i6) == str(wData.iloc[0]['bits_developer_share_gross'])) and (str(i7) == str(wData.iloc[0]['bits_extension_share_gross'])) and (str(i8) == str(wData.iloc[0]['prime_sub_share_gross'])) and (str(i9) == str(wData.iloc[0]['bit_share_ad_gross'])) and (str(i10) == str(wData.iloc[0]['fuel_rev_gross'])) and (str(i11) == str(wData.iloc[0]['bb_rev_gross'])) and (str(i12) == str(wData.iloc[0]['report_date']))):
                index = index + 1
                print(str(index) + ": Veri, bir önceki veri ile birebir aynı olduğu için pas geçildi.")
                continue


    if wData.empty:
        print(str(index) + ": Kullanıcıya ait veri bulunamadı. Pas geçiliyor.")
        index = index + 1
        prevIsEmpty = True
        continue
    else:
        prevIsEmpty = False
        print(str(index) + ": Veri bulundu. Kaydedilip bir sonraki işleme geçiliyor.")
        items.append(wData.iloc[0])
        wData.to_csv('.\outputs/output.csv', mode='a', index=False, header=False)
        i1 = wData.iloc[0]['user_id']
        i2 = wData.iloc[0]['payout_entity_id']
        i3 = wData.iloc[0]['ad_share_gross']
        i4 = wData.iloc[0]['sub_share_gross']
        i5 = wData.iloc[0]['bits_share_gross']
        i6 = wData.iloc[0]['bits_developer_share_gross']
        i7 = wData.iloc[0]['bits_extension_share_gross']
        i8 = wData.iloc[0]['prime_sub_share_gross']
        i9 = wData.iloc[0]['bit_share_ad_gross']
        i10 = wData.iloc[0]['fuel_rev_gross']
        i11 = wData.iloc[0]['bb_rev_gross']
        i12 = wData.iloc[0]['report_date']
    index = index + 1

end = time.time()
print("Bütün veriler işlendi ve 'Outputs' klasörüne kaydedildi.")
print("Toplam işlem süresi:" + str(end-start) + " saniye")

soru = input('Uygulamadan çıkmak için herhangi bir tuşa basın.')

