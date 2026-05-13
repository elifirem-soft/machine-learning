Bu projede, verileri birbirinden ayıran en geniş boşluğu (margin) bulmayı hedefleyen Destek Vektör Makineleri (SVM) algoritmasını uyguladım. Modelin temel amacı, sınıflar arasında en optimize karar sınırını matematiksel olarak belirlemektir.

--- Neler Yaptım? 

Boyut İndirgeme ve Hazırlık: Iris veri setini kullanarak, görselleştirme kolaylığı sağlaması adına ilk iki öznitelik (feature) üzerinden bir çalışma kurguladım. Veriyi %30 test, %70 eğitim oranında stratejik olarak böldüm.

Lineer Modelleme: svm.SVC sınıfını kernel='linear' parametresi ile yapılandırarak, verileri doğrusal bir düzlemde ayıran en uygun hiper-düzlemi (hyperplane) inşa ettim.

Karar Sınırı Analizi: Modelin eğittiği ağırlık vektörlerini (coef_) ve sapma değerini (intercept_) kullanarak karar doğrusunun eğimini ve kesişim noktasını manuel olarak hesapladım. Bu sayede algoritmanın "karar verme" anını grafik üzerinde somut bir çizgiye dönüştürdüm.

Görsel Doğrulama: Matplotlib kullanarak verileri sınıflarına göre dağılım grafiğine döktüm ve hesapladığım "Decision Boundary" doğrusunu bu verilerin arasına yerleştirerek modelin başarısını görsel olarak sundum.

--- Teknolojik Stack 

Kütüphaneler: Scikit-learn (SVM), NumPy, Matplotlib.

Algoritma: Support Vector Classification (SVC).

Yöntem: Linear Kernel & Decision Boundary Analysis.

--- Nasıl Çalışır? 

SVM algoritması, iki sınıf arasındaki sınırı çizerken sadece sınıflara en yakın olan "Destek Vektörleri"ni baz alır. Bu projede kullanılan lineer kernel, verileri düz bir çizgi ile ayırmaya çalışır. Kod yürütüldüğünde, algoritma her iki sınıfa da en uzak mesafede duran o ideal çizgiyi hesaplar. Ardından elde edilen katsayılar ile bu çizgi koordinat sisteminde çizdirilir; böylece yeni gelecek bir verinin çizginin hangi tarafında kalacağına bakılarak sınıflandırma işlemi gerçekleştirilir.
