Bu projede, birden fazla karar ağacını bir araya getirerek yüksek doğruluk ve kararlılık sağlayan Random Forest algoritmasını uyguladım. Modelin temel hedefi, kredi kartı verileri üzerinden kullanıcı davranışlarını veya onay durumlarını en düşük hata payı ile sınıflandırmaktır.

--- Neler Yaptım? 

Veri Ön İşleme (Preprocessing): CreditCard.csv veri setindeki kategorik değişkenleri sayısal formata dönüştürmek için get_dummies yöntemini kullandım. Bu sayede modelin tüm öznitelikleri anlamlandırabileceği bir veri yapısı oluşturdum.

Dengeli Veri Ayrımı: Veri setini %20 test, %80 eğitim olacak şekilde bölerken stratify parametresini kullandım. Bu, hedef sınıfların oranını hem eğitim hem de test setinde koruyarak modelin tarafsız öğrenmesini sağladı.

Ensemble Modelleme: Toplam 50 adet karar ağacından (n_estimators=50) oluşan bir RandomForestClassifier inşa ettim. Rastgele seçilen veri alt kümeleri ve özelliklerle eğitilen bu ağaçların çoğunluk oyunu (voting) alarak nihai tahmini üretmesini sağladım.

Kapsamlı Raporlama: Modelin performansını sadece tek bir skorla değil, Precision, Recall ve F1-Score değerlerini içeren classification_report ile detaylıca analiz ettim.

--- Teknolojik Stack 

Kütüphaneler: Scikit-learn (RandomForestClassifier, train_test_split), Pandas, NumPy.

Algoritma: Random Forest (Ensemble Learning).

Yöntem: Bagging (Bootstrap Aggregating).

--- Nasıl Çalışır? Random Forest, "akıl akıldan üstündür" prensibiyle çalışır. Eğitim aşamasında veri setinden rastgele örneklemler seçilerek 50 farklı karar ağacı birbirinden bağımsız olarak eğitilir. Tahmin aşamasında, yeni bir veri tüm ağaçlara sorulur. Her ağaç kendi kararını verir ve en çok oyu alan sınıf final sonuç olarak seçilir. Bu yöntem, tek bir karar ağacının aşırı öğrenme (overfitting) riskini minimize ederek çok daha güvenilir sonuçlar üretir.
