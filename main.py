import glob
import os
import gzip
import shutil

## all_revenues.csv.gz dosyalarını çıkartır, ve .gz uzantılı sıkıştırılmış dosyayı siler.


path = ".\directory/"
newFiles = []

## directory klasörünün içerisindeki .csv.gz uzantılı dosyaların tespit edilmesi
text_files = glob.glob(path + "/**/*.csv.gz", recursive = True)

## .csv.gz uzantılı dosyaların oluşturulan klasöre çıkartılması
index = 1
for file in text_files:
    split = os.path.split(file)
    os.mkdir(split[0] + "/all_revenues.csv")
    with gzip.open(file, 'rb') as f_in:
        with open(split[0] + "/all_revenues.csv/all_revenues.csv", 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)
            print(str(index) + ". dosya işlendi.")
            index = index + 1

## .gz uzantılı dosyaların silinmesi.
secIndex = 1
for file in text_files:
    os.chmod(file, 0o0777)
    os.remove(file)
    print(str(index) + ". dosya silindi.")
    index = index + 1
