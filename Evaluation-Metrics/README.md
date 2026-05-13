Bu projede, bir sınıflandırma modelinin başarısını ölçmek için kullanılan temel kalite metriklerinin matematiksel hesaplama mantığını ve birbirleriyle olan ilişkilerini analiz eden bir simülasyon hazırladım.

--- Neler Yaptım? 

Performans Simülasyonu: Karışıklık matrisindeki (Confusion Matrix) True Negative (TN), False Negative (FN), False Positive (FP) ve True Positive (TP) değerlerini döngüsel bir yapıda simüle ederek farklı senaryolar oluşturdum.

Metrik Hesaplamaları: Sadece hazır kütüphane kullanmak yerine Accuracy, Precision, Recall ve F1-Score formüllerini kod seviyesinde manuel olarak kurguladım. Bu sayede her bir metriğin veri değişimlerine karşı nasıl tepki verdiğini gözlemleme şansı buldum.

Dinamik Analiz: Döngüler yardımıyla FN ve FP değerleri değiştikçe precision ve recall arasındaki o meşhur dengenin (trade-off) nasıl şekillendiğini ve F1-Score'un bu iki değer arasındaki dengeleyici rolünü teknik bir çıktı olarak sundum.

--- Teknolojik Stack 

Kütüphaneler: Saf Python (Mantıksal hesaplamalar için herhangi bir ek kütüphaneye ihtiyaç duymadan kurgulanmıştır).

Algoritma: Performans Metrikleri Analizi.

Metrikler: Precision, Recall, Accuracy, F1-Score.

--- Nasıl Çalışır? 

Sistem, belirli bir örneklem sayısı üzerinden TN değerini sabit tutarak başlar. İç içe döngüler kullanarak olası tüm hata paylarını (FN ve FP) hesaplamaya dahil eder. Her bir iterasyonda, güncel değerlere göre tüm başarı metrikleri formüllere dökülür ve sonuçlar karşılaştırılabilir bir tablo formatında ekrana basılır. Bu süreç, model performansını yorumlama kabiliyetini artırmak için bir temel teşkil eder.
