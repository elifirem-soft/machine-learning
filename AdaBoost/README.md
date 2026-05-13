Bu çalışmada, öğrenicileri bir araya getirerek güçlü bir model oluşturan AdaBoost (Adaptive Boosting) algoritmasını uyguladım. Projenin ana odak noktası, topluluk öğrenme yöntemlerinin sınıflandırma başarısı üzerindeki etkisini gözlemlemektir.

--- Neler Yaptım?
Veri Seti Hazırlığı: Makine öğrenmesi dünyasının "merhaba dünya"sı sayılan Iris veri setini kullandım. Veriyi %30 test, %70 eğitim olacak şekilde stratejik bir şekilde böldüm.

Zayıf Öğrenici Yapılandırması: AdaBoost'un temel taşı olan "Decision Stump" yapısını kurmak için tek derinlikli (max_depth=1) bir Karar Ağacı belirledim.

Topluluk Modeli (Ensemble): Belirlediğim zayıf öğreniciyi 50 farklı aşamada (n_estimators=50) eğitecek olan AdaBoostClassifier modelini inşa ettim. Bu sayede modelin her adımda bir önceki hatalarına odaklanarak kendini geliştirmesini sağladım.

Performans Analizi: Modelin tahmin gücünü accuracy_score ile ölçtüm ve sonuçları confusion_matrix kullanarak detaylandırdım.

--- Teknolojik Stack
Kütüphaneler: Scikit-learn (sklearn), Matplotlib, Seaborn

Algoritma: AdaBoost (Ensemble Learning)

Temel Model: Decision Tree (Decision Stump)

--- Nasıl Çalışır?
Kod yürütüldüğünde ilk olarak Iris veri seti yüklenir ve eğitim/test ayrımı yapılır. Ardından AdaBoost algoritması, 50 adet zayıf karar ağacını ardışık olarak eğitir; her yeni ağaç, bir öncekinin yanlış sınıflandırdığı verilere daha fazla ağırlık vererek hataları telafi etmeye çalışır. Son aşamada ise test seti üzerindeki doğruluk oranı hesaplanarak terminale yazdırılır ve sınıflandırma başarısı görselleştirilir.
