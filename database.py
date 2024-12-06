import sqlite3

def create_database():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()


    cursor.execute("""
    CREATE TABLE IF NOT EXISTS questions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        question_text TEXT,
        option_a TEXT,
        option_b TEXT,
        option_c TEXT,
        option_d TEXT,
        correct_option CHAR
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL,
        age INTEGER NOT NULL,
        salary REAL NOT NULL,
        category TEXT NOT NULL,
        score INTEGER NOT NULL
    )
    """)

  

    cursor.execute("""
    INSERT INTO questions (question_text, option_a, option_b, option_c, option_d, correct_option)
    VALUES
  ("YOLO (You Only Look Once) algoritması hangi amaçla kullanılır?", "A)  Metin analizi", "B) Görüntüde nesne tespiti", "C) Ses tanıma", "D) Zaman serisi analizi", "B"),
    ("Yapay Zeka'nın amacı nedir?", "A) İnsanları anlamak", "B) Zekayı simüle etmek", "C) Veri işlemek", "D) Matematik öğrenmek", "B"),
    ("Makine öğrenmesi nedir?", "A) Bilgisayarların insan gibi düşünmesi", "B) Veri üzerinden öğrenme", "C) Sistem optimizasyonu", "D) Kodlama", "B"),
    ("Bir doğal dil işleme (NLP) görevi olan dil modeli eğitmek için aşağıdaki yöntemlerden hangisi kullanılır?", "A) Convolutional Neural Networks (CNN)", "B) Recurrent Neural Networks (RNN)", "C) Support Vector Machines (SVM)", "D) K-Nearest Neighbors (KNN)", "B"),
    ("Generative Adversarial Networks (GANs) hangi amaç için kullanılır?", "A) Veri artırma ve yeni veri oluşturma", "B) Kayıp fonksiyonlarını hesaplama", "C) Doğru sınıflandırma oranını artırma", "D) Veri setlerini temizleme", "A"),
    ("Deep Learning hangi alanda kullanılmaz?", "A) Görüntü tanıma", "B) Ses işleme", "C) Oyun geliştirme", "D) Hisse senedi tahmini", "C"),
    ("Support Vector Machines (SVM) hangi tür problemleri çözmek için kullanılır?", "A) Sınıflandırma ve regresyon", "B) Grafik analizi", "C) Dil işleme", "D) Ses analizi", "A"),
    ("Bir veri kümesinin boyutunu azaltmak için kullanılan teknik hangisidir?", "A) Veri madenciliği", "B) PCA (Principal Component Analysis)", "C) RNN (Recurrent Neural Networks)", "D) K-Means", "B"),
    ("Python'da kullanılan popüler makine öğrenme kütüphanesi hangisidir?", "A) TensorFlow", "B) NumPy", "C) Pandas", "D) Flask", "A"),
    ("Random Forest algoritması hangi öğrenme yöntemine aittir?", "A) Denetimsiz öğrenme", "B) Denetimli öğrenme", "C) Pekiştirmeli öğrenme", "D) Hiyerarşik öğrenme", "B"),
    ("Bir yapay sinir ağı modeli hangi bileşenlerden oluşur?", "A) Katmanlar, ağırlıklar ve aktivasyon fonksiyonları", "B) Düğümler ve graf yapıları", "C) Klasörler ve dosyalar", "D) Etiketler ve veriler", "A"),
    ("CNN (Convolutional Neural Networks) hangi alanda sıklıkla kullanılır?", "A) Zaman serisi analizi", "B) Görüntü işleme", "C) Ses sentezi", "D) Doğal dil işleme", "B"),
    ("Gradient Descent algoritması ne işe yarar?", "A) Model eğitmek için optimizasyon", "B) Veri artırımı", "C) Model doğrulama", "D) Veriyi temizleme", "A"),
    ("Naive Bayes algoritması hangi durumlarda kullanılır?", "A) Sürekli veri setleri", "B) Metin sınıflandırma", "C) Görüntü tanıma", "D) Ses işleme", "B"),
    ("Overfitting nedir?", "A) Modelin eğitim verisine çok iyi uyum sağlaması", "B) Modelin test verisine kötü sonuç vermesi", "C) Eğitim süresinin uzaması", "D) Çok fazla veri kullanılması", "A"),
    ("Dropout yöntemi ne için kullanılır?", "A) Ağırlıkları sıfırlamak", "B) Overfitting'i azaltmak", "C) Eğitim süresini kısaltmak", "D) Veri artırımı", "B"),
    ("Bir zaman serisi problemini çözmek için en uygun model hangisidir?", "A) CNN", "B) RNN", "C) SVM", "D) Naive Bayes", "B"),
    ("Python'da veri analizi için kullanılan kütüphane nedir?", "A) NumPy", "B) Pandas", "C) Matplotlib", "D) Flask", "B"),
    ("Decision Trees algoritması nasıl çalışır?", "A) Veri kümesini bölerek", "B) Ağırlık hesaplayarak", "C) Rastgele seçim yaparak", "D) Tahmin değerlerini çıkararak", "A"),
    ("Bir sinir ağında geri yayılım (backpropagation) ne işe yarar?", "A) Ağırlıkları günceller", "B) Veri artırır", "C) Aktivasyon fonksiyonlarını çalıştırır", "D) Eğitim hızını artırır", "A"),
    ("K-Means algoritması ne için kullanılır?", "A) Veri sınıflandırma", "B) Kümeleme", "C) Zaman serisi analizi", "D) Doğal dil işleme", "B"),
    ("Makine öğrenmesinde doğruluk metriği nedir?", "A) Tahmin edilen doğruların oranı", "B) Eğitim süresi", "C) Eğitim setinin boyutu", "D) Modelin karmaşıklığı", "A"),
    ("Bir dil modeli hangi görev için uygundur?", "A) Görüntü sınıflandırma", "B) Metin oluşturma", "C) Ses analizi", "D) Grafik çizimi", "B"),
    ("Reinforcement Learning (Pekiştirmeli Öğrenme) nedir?", "A) Etiketli verilerle öğrenme", "B) Deneme yanılma yoluyla öğrenme", "C) Zaman serileri tahmini", "D) Doğal dil işleme", "B"),
    ("Bir veri setinin hatalarını azaltmak için hangi teknik kullanılır?", "A) Regularization", "B) Gradient Boosting", "C) Veri madenciliği", "D) PCA", "A"),
    ("SVM'in temel amacı nedir?", "A) Veri kümelerini ayıran en iyi hiperdüzlemi bulmak", "B) Veri kümelerini birleştirmek", "C) Etiketleri yeniden düzenlemek", "D) Hataları en aza indirmek", "A"),
    ("Doğal dil işleme (NLP) hangi alanda uygulanmaz?", "A) Metin analizi", "B) Ses sentezi", "C) Görüntü sınıflandırma", "D) Çeviri", "C"),
    ("TensorFlow ve PyTorch hangi amaçla kullanılır?", "A) Veri analizi", "B) Derin öğrenme modeli geliştirme", "C) Web geliştirme", "D) Ses işleme", "B"),
    ("Transfer Learning nedir?", "A) Yeni bir model eğitme", "B) Mevcut bir modelin bilgilerini başka bir görev için kullanma", "C) Veri setini değiştirme", "D) Aktivasyon fonksiyonlarını optimize etme", "B"),
    ("Bir sinir ağında epoch nedir?", "A) Bir veri kümesinin modelden geçirilme sayısı", "B) Ağırlıkların güncellenmesi", "C) Eğitim verilerinin normalizasyonu", "D) Aktivasyon fonksiyonlarının çalıştırılması", "A"),
    ("Overfitting'i önlemek için hangi teknik kullanılır?", "A) Daha fazla veri kullanmak", "B) Daha az parametre kullanmak", "C) Modeli erken durdurmak", "D) Tüm seçenekler", "D"),
    ("Batch normalization nedir?", "A) Eğitim hızını artıran bir teknik", "B) Veriyi normalleştiren bir yöntem", "C) Aktivasyon fonksiyonlarını optimize eder", "D) Eğitim setini bölmek için kullanılır", "A"),
    ("Bir nesne tespit modelinde IoU (Intersection over Union) metriği neyi ölçer?", "A) Modelin hızını", "B) Tahmin doğruluğunu", "C) Nesneler arasındaki örtüşme oranını", "D) Veri setinin kalitesini", "C"), ("Adam optimizasyon algoritması ne için kullanılır?", "A) Eğitim sürecinde ağırlıkları güncellemek", "B) Veri artırımı yapmak", "C) Model karmaşıklığını azaltmak", "D) Modeli test etmek", "A"), ("Bir modelin karmaşıklığını azaltmak için hangi yöntem kullanılabilir?", "A) Regularization", "B) Data Augmentation", "C) Dropout", "D) Tüm seçenekler", "D"), ("Feature engineering nedir?", "A) Veri setini temizleme süreci", "B) Modelin ağırlıklarını değiştirme süreci", "C) Model performansını artırmak için özellikler oluşturma süreci", "D) Modelin doğruluk oranını ölçme süreci", "C"), ("Bir yapay sinir ağında katman sayısını artırmak neyi etkiler?", "A) Modelin kapasitesini", "B) Eğitim süresini", "C) Overfitting riskini", "D) Tüm seçenekler", "D"), ("ReLU (Rectified Linear Unit) aktivasyon fonksiyonu ne yapar?", "A) Negatif değerleri sıfır yapar", "B) Pozitif değerleri artırır", "C) Tüm değerleri normalize eder", "D) Sadece negatif değerleri işler", "A"), ("Veri setindeki dengesizlik (class imbalance) problemini çözmek için hangi teknik kullanılabilir?", "A) Veri artırımı", "B) Ağırlıklandırma", "C) Alt örnekleme", "D) Tüm seçenekler", "D"), ("Bir sinir ağı modelinin doğruluğunu artırmak için hangi yöntemler uygulanabilir?", "A) Daha fazla veri kullanmak", "B) Modeli optimize etmek", "C) Veriyi ön işlemek", "D) Tüm seçenekler", "D"), ("YOLO algoritmasında 'anchor box' nedir?", "A) Görüntüdeki nesne sınıflarını tanımlamak için kullanılır", "B) Nesne tespiti için tahmin edilen kutuları tanımlamak için kullanılır", "C) Modelin öğrenme hızını optimize eder", "D) Görüntü boyutunu normalize eder", "B"), ("Bir derin öğrenme modelinin genel performansını ölçmek için hangi metrikler kullanılabilir?", "A) Doğruluk", "B) F1 skoru", "C) Hata oranı", "D) Tüm seçenekler", "D"), ("Bir sinir ağında öğrenme oranı (learning rate) neyi kontrol eder?", "A) Ağırlıkların ne kadar hızlı güncelleneceğini", "B) Eğitim veri setinin boyutunu", "C) Aktivasyon fonksiyonlarının tipini", "D) Modelin karmaşıklığını", "A"), ("ResNet (Residual Network) ne için geliştirilmiştir?", "A) Daha derin sinir ağlarını eğitmek için", "B) Zaman serisi analizini hızlandırmak için", "C) Dil modellerini optimize etmek için", "D) Görüntüleri normalleştirmek için", "A"), ("Data Augmentation (Veri Çoğaltma) ne sağlar?", "A) Eğitim veri setini artırır", "B) Overfitting'i azaltır", "C) Modelin genelleme yeteneğini artırır", "D) Tüm seçenekler", "D"), ("Transformer mimarisi hangi alanda sıklıkla kullanılır?", "A) Görüntü işleme", "B) Doğal dil işleme", "C) Ses analizi", "D) Tüm seçenekler", "B"), ("Bir derin öğrenme modelini değerlendirmek için kullanılan 'validation set' nedir?", "A) Eğitim sırasında modelin performansını ölçmek için kullanılan veri kümesi", "B) Test veri setine eklenen veri", "C) Modelin nihai doğruluğunu ölçmek için kullanılan veri", "D) Eğitim setinin bir kopyası", "A"), ("Gradient Boosting algoritması hangi öğrenme yöntemi ile ilişkilidir?", "A) Denetimli öğrenme", "B) Denetimsiz öğrenme", "C) Pekiştirmeli öğrenme", "D) Derin öğrenme", "A");

    """)

    conn.commit()
    conn.close()

create_database()
