# Web Sitesi Projesi: Yapay Zeka Soruları
Bu proje, kullanıcıların zeka ile ilgili soruları yanıtladığı ve en yüksek puanların görüntülendiği bir web uygulamasıdır. Flask ile geliştirilmiş olan bu web sitesi, OpenCV kullanılarak kullanıcıların kameradan alınan görüntülerinin ortalanmasını sağlar.

**Proje Özellikleri**

Web Tabanlı Uygulama: Flask kullanılarak geliştirilmiş.

Veritabanı Entegrasyonu: Sorular veritabanında saklanır ve her oturumda rastgele 5 soru seçilir.

Zeka Soruları: Kullanıcıların çözmesi için rastgele seçilen 5 zeka sorusu.

Puanlama Sistemi: Kullanıcıların doğru yanıtları üzerinden puanlama yapılır ve en yüksek puanlar kaydedilir.

Canlı Kamera Görüntüsü: OpenCV kullanılarak kullanıcının kamerasından alınan görüntü ortalanır ve ekrana yansıtılır.

Kurulum ve Kullanım
Gereksinimler
Projenin çalışabilmesi için aşağıdaki yazılım ve kütüphanelere ihtiyaç vardır:

Python 3.8
Flask
OpenCV
SQLite (veritabanı için)
Kurulum Adımları
Bu projeyi bilgisayarınıza klonlayın:

bash
Kodu kopyala
git clone https://github.com/kullaniciadi/zeka-sorulari-web.git
Proje klasörüne gidin:

bash
Kodu kopyala
cd zeka-sorulari-web
*Gerekli Python kütüphanelerini yükleyin:*
bash
Kodu kopyala
pip install -r requirements.txt


**Kullanım Kılavuzu**
Web sitesini açtığınızda, sistem otomatik olarak veritabanından 5 rastgele soru seçer.
Kullanıcı her soruyu yanıtladıktan sonra, puanlama sistemine göre skoru hesaplanır ve ekrana yansıtılır.
Kameradan alınan görüntüler, OpenCV kullanılarak ortalanır ve görüntü ekranda düzgün bir şekilde gösterilir.
**Kullanılan Teknolojiler**
Python: Programlama dili
Flask: Web uygulama çatısı
OpenCV: Görüntü işleme
SQLite: Veritabanı yönetim sistemi
Katkıda Bulunanlar
Proje geliştiricisi: [Adınız]
