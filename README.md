Twitch CSV Read

Sızdırılan Twitch ödeme dosyalarını analiz etmek amacıyla oluşturulmuş, herhangi bir resmiyeti olmayan bir proje.

NOT: Uygulamayı kullanabilmek için uygulamanın olduğu konuma "directory" adında bir klasör oluşturmanız ve Twitch'ten sızdırılan "all_revenues" dosyasını "directory" dosyasının içine atmanız gerekiyor.

NOT 2: "all_revenues" dosyasını attığınız zaman içerisinde ki .gz uzantılı dosyaları klasöre çıkartması için "gz-extract.exe" isimli uygulamayı çalıştırmalısınız. İsterseniz uygulamayı kullanmadan ellede çıkartabilirsiniz ama toplam 116 adet dosya olduğundan tek tek yapmakta zorlanabilirsiniz.

Uygulamanın Kullanımı

Uygulamayı çalıştırdığınız zaman aratacağınız Twitch kullanıcısının ID'sini girmeniz gerekiyor. Bu ID'yi twitchinsights.net/checkuser adresinden alabilirsiniz.
ID'yı girdikten sonra uygulama "directory" klasörünün içinde ki tüm .csv uzantılı verileri içeren dosyaları tek tek taramaya başlar.

Tarama bittiği zaman veriler "outputs" klasörünün içinde ki "output.csv" isimli dosyaya kaydedilir.

Tarama işlemi ortalama 3 ila 6 dakika arası sürmektedir fakat bilgisayarınızın performansına göre değişiklik gösterebilir.

Bu projeyi belki kimse kullanmayacak olabilir fakat yapma amacım kendimi geliştirmek.

Furkan Kılıç - @furkankilics
