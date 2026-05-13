Bu projede, gözetimsiz öğrenme tekniklerinden biri olan K-Means Clustering algoritmasını kullanarak veri setindeki gizli örüntüleri ve doğal gruplandırmaları tespit ettim. Verilerin birbirlerine olan uzaklıklarını temel alarak mantıksal kümeler oluşturmayı hedefledim.

--- Neler Yaptım? 

Veri Simülasyonu: Modelin çalışma prensibini gözlemlemek amacıyla NumPy kullanarak 2 boyutlu düzlemde 100 adet rastgele veri noktası ürettim.

Kümeleme Algoritması: Scikit-learn kütüphanesinden KMeans modelini kullanarak, verileri 3 ayrı kümeye (n_clusters=3) ayıracak şekilde yapılandırdım.

Görsel Analiz: Matplotlib kütüphanesini kullanarak sonuçları bir dağılım grafiğine (scatter plot) döktüm. Her bir kümeyi farklı renklerle (viridis color map) işaretleyerek gruplandırmayı netleştirdim.

Merkez Noktası Tespiti: Algoritmanın her bir küme için belirlediği merkez noktalarını (centroids) grafikte büyük kırmızı yıldızlarla işaretleyerek, kümelerin hangi odak noktaları etrafında toplandığını teknik olarak sundum.

--- Teknolojik Stack 

Kütüphaneler: Scikit-learn (KMeans), NumPy, Matplotlib.

Algoritma: K-Means Clustering.

Yöntem: Gözetimsiz Öğrenme (Unsupervised Learning).

--- Nasıl Çalışır? Süreç, veri noktalarının koordinat sistemine yerleştirilmesiyle başlar. K-Means algoritması, başlangıçta rastgele merkez noktaları seçer ve her bir veri noktasını kendisine en yakın olan merkeze atar. Ardından, merkez noktaları atanan verilerin ortalamasına göre yeniden hesaplanır ve bu işlem gruplar stabilize olana kadar devam eder. Sonuç olarak veriler, birbirine en benzer oldukları (en yakın oldukları) gruplara ayrılmış olur.
