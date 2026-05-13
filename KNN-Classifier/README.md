K-Nearest Neighbors (KNN) - Distance & Classification

Bu projede, mesafe tabanlı en temel sınıflandırma algoritmalarından biri olan K-Nearest Neighbors (KNN) yöntemini hem teorik (manuel hesaplama) hem de pratik (kütüphane kullanımı) seviyelerinde ele aldım.

--- Neler Yaptım?

Matematiksel Temel: distance_metrics.py içerisinde, algoritmanın kalbi sayılan Öklid mesafesini (Euclidean Distance) numpy.linalg.norm kullanarak manuel olarak fonksiyonlaştırdım. Bu, algoritmanın arka planda iki veri noktası arasındaki benzerliği nasıl ölçtüğünü teknik olarak analiz etmemi sağladı.

KNN Modeli ve Eğitim: knn_classifier.py dosyasında, Scikit-learn kütüphanesinden KNeighborsClassifier kullanarak bir sınıflandırma modeli inşa ettim. Modeli, en yakın tek komşu (n_neighbors=1) prensibine göre yapılandırarak en agresif karar sınırlarını gözlemledim.

Veri Hazırlığı ve Tahmin: Mevcut x, y koordinatlarını ve sınıflarını zip fonksiyonu ile birleştirerek eğitim setini oluşturdum. Sisteme dahil olmayan yeni bir veri noktası (new_point) ekleyerek, modelin bu noktayı en yakın komşusuna göre hangi sınıfa atayacağını simüle ettim.

Görselleştirme: Matplotlib kullanarak eğitim verilerini ve modelin tahmin ettiği yeni noktayı koordinat sistemi üzerinde gösterdim. Yeni noktanın sınıfını grafik üzerine metin olarak ekleyerek görsel bir doğrulama sağladım.


--- Teknolojik Stack 

Kütüphaneler: Scikit-learn (KNeighborsClassifier), NumPy (Linalog/Norm), Matplotlib.Algoritma: K-Nearest Neighbors.

Yöntem: Mesafe Tabanlı Sınıflandırma (Classification).


--- Nasıl Çalışır? 

Süreç iki aşamadan oluşur: İlk olarak distance fonksiyonu, vektörel farkların normunu alarak noktalar arası uzaklığı hesaplar. İkinci aşamada KNN algoritması, koordinat düzlemine yerleştirilen eğitim verileri arasında yeni gelen noktaya en yakın olan $k$ adet komşuyu tespit eder. Bu projede $k=1$ seçildiği için, yeni nokta direkt olarak kendisine en yakın olan komşusunun sınıfını miras alır ve bu sonuç hem terminalde hem de grafik arayüzünde kullanıcıya sunulur.
