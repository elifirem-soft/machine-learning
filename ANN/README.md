Bu projede, derin öğrenme tekniklerini kullanarak prostat kanseri verileri üzerinden teşhis tahmini yapan bir Yapay Sinir Ağı (ANN) modeli inşa ettim. Model, karmaşık veri setleri arasındaki doğrusal olmayan ilişkileri öğrenerek sınıflandırma başarısını optimize etmek üzere tasarlandı.

--- Neler Yaptım?
Veri Analizi ve Görselleştirme: Veri setindeki özelliklerin (PSA seviyeleri gibi) dağılımını ve etiketlerle olan ilişkisini Seaborn ve Matplotlib kullanarak analiz ettim. Bu adım, modelin hangi verilerle beslendiğini anlamak adına kritikti.

Veri Ön İşleme (Preprocessing): Modelin daha hızlı ve kararlı öğrenmesi için StandardScaler kullanarak verileri standardize ettim. Ayrıca veriyi eğitim ve test seti olarak ikiye böldüm (train_test_split).

Model Mimarisi: TensorFlow ve Keras kütüphanelerini kullanarak çok katmanlı (Sequential) bir ANN yapısı kurdum. Giriş, gizli ve çıkış katmanlarını Dense katmanları ile yapılandırarak derin öğrenme sürecini başlattım.

Performans Değerlendirme: Modelin başarısını ölçmek için accuracy_score ve confusion_matrix metriklerini kullanarak sonuçları analiz ettim.

--- Teknolojik Stack
Framework: TensorFlow & Keras

Kütüphaneler: NumPy, Pandas, Matplotlib, Seaborn, Scikit-learn

Model: Yapay Sinir Ağları (Sequential Model)

--- Nasıl Çalışır?

Proje, prostate_cancer_data.csv dosyasından verileri yükleyerek başlar. İlk aşamada PSA seviyelerinin dağılım grafikleri oluşturulur. Ardından, özellikler ve etiketler ayrıştırılarak modelin eğitim süreci gerçekleştirilir. Model eğitildikten sonra, test verileri üzerinde tahminler yaparak doğruluk oranlarını ve hata matrisini çıktı olarak sunar.
