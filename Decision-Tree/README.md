Bu projede, kullanıcı verileri üzerinden belirli davranışları tahmin etmek amacıyla bir Karar Ağacı (Decision Tree) modeli geliştirdim. Modelin odak noktası, verideki karmaşıklığı (entropy) azaltarak doğru karar düğümlerini oluşturmaktır.

--- Neler Yaptım?
Veri Seçimi ve Hazırlığı: user-data.csv dosyasından ilgili öznitelikleri seçerek başladım. Veri setini %25 test, %75 eğitim oranında böldüm.

Özellik Ölçeklendirme (Feature Scaling): Karar ağaçları mesafe tabanlı olmasa da, modelin daha stabil çalışması ve farklı algoritmalarla karşılaştırılabilir olması için StandardScaler uyguladım.

Entropi Tabanlı Modelleme: Dallanma kriteri olarak entropy kullanarak, verideki belirsizliği minimuma indiren bir DecisionTreeClassifier inşa ettim.

Hata Matrisi Analizi: Tahminlerin doğruluğunu sadece skor bazlı değil, confusion_matrix ve Seaborn heatmap kullanarak görsel bir şekilde analiz ettim. Bu sayede hangi sınıflarda daha fazla hata yapıldığını netleştirdim.

--- Teknolojik Stack
Kütüphaneler: Scikit-learn, Pandas, NumPy, Seaborn, Matplotlib

Algoritma: Decision Tree Classifier

Kriter: Entropy (Bilgi Kazanımı)

--- Nasıl Çalışır?
Sistem, kullanıcı verilerini yükledikten sonra her bir özelliği birer soruya dönüştürerek ağaç yapısını oluşturur. Eğitim sürecinde, entropi değerini en çok düşüren özellikler ağacın üst düğümlerine yerleştirilir. Test aşamasında ise yeni gelen bir verinin bu düğümlerdeki sorulardan geçerek hangi yaprağa (sınıfa) düştüğü belirlenir ve nihai tahmin üretilir.
