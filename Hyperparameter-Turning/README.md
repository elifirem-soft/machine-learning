Bu projede, makine öğrenmesi modellerinin tahmin gücünü maksimize etmek amacıyla hiperparametre optimizasyonu tekniklerini uyguladım. Modelin sadece mevcut veriyi öğrenmesini değil, en verimli parametre setini kullanarak en yüksek performansa ulaşmasını hedefledim.

--- Neler Yaptım? 

Model Seçimi ve Yapılandırma: Güçlü bir topluluk öğrenme (ensemble) algoritması olan Random Forest modelini temel yapı taşı olarak belirledim.

Kapsamlı Parametre Taraması: n_estimators, max_depth, min_samples_split ve min_samples_leaf gibi modelin derinliğini ve ağaç sayısını belirleyen kritik parametreler için geniş bir param_grid havuzu oluşturdum.

GridSearch ve Cross-Validation: GridSearchCV kullanarak belirlenen tüm parametre kombinasyonlarını 5 katlı çapraz doğrulama (cv=5) ile test ettim. Bu sayede modelin farklı veri alt kümelerinde en stabil ve yüksek başarıyı veren parametrelerini sistematik olarak tespit ettim.

Sonuç Analizi: Optimizasyon sonucunda elde edilen "en iyi parametre seti" ile test verisi üzerinde final tahminleri gerçekleştirdim. Başarıyı ölçmek için çok sınıflı sınıflandırmaya uygun şekilde weighted-average metriklerini kullandım.

--- Teknolojik Stack 

Kütüphaneler: Scikit-learn (GridSearchCV, RandomForestClassifier), Pandas, NumPy.

Algoritma: Random Forest Classifier.

Yöntem: Grid Search Cross-Validation (Parametre Optimizasyonu).

--- Nasıl Çalışır? 

Süreç, Iris veri setinin yüklenmesi ve standart eğitim/test ayrımının yapılmasıyla başlar. Ardından oluşturulan parametre ızgarası (grid), GridSearchCV mekanizmasına verilir. Sistem, her bir kombinasyon için modeli tekrar eğiterek performans skorlarını karşılaştırır. En yüksek doğruluğu veren "Best Estimator" seçildikten sonra, bu optimize edilmiş model ile test seti üzerinden final metrikleri (Accuracy, Precision, Recall, F1) hesaplanarak süreç tamamlanır.
