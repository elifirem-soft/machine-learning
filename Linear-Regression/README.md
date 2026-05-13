Bu bölümde, doğrusal regresyon modelini istatistiksel analizden manuel matematiksel hesaplamaya kadar üç farklı yöntemle ele aldım.

1. Statistical Linear Regression (SciPy)

linear_regression.py dosyasında, veriler arasındaki korelasyonu ve regresyon katsayılarını istatistiksel bir perspektifle inceledim.

--- Neler Yaptım? SciPy kütüphanesinin stats.linregress metodunu kullanarak eğim (slope), kesişim (intercept) ve korelasyon katsayısı ($r$) değerlerini hesapladım. Belirlediğim bir girdi değeri için geleceğe yönelik tahmin yürüten bir fonksiyon kurguladım ve sonuçları dağılım grafiği üzerinde görselleştirdim.

2. Predictive Modeling (Scikit-Learn)

linear_regression_2.py dosyasında, araç kilometresi ve fiyatı arasındaki ilişkiyi makine öğrenmesi iş akışına uygun şekilde modelledim.-

--- Neler Yaptım? Veri setini train_test_split ile eğitim ve test gruplarına ayırarak modelin genelleme yeteneğini test ettim. LinearRegression sınıfı ile modeli eğittim ve belirleme katsayısını ($R^2$) hesaplayarak modelin veriyi açıklama gücünü ölçümledim.

3. Mathematical Foundations & Evaluation

linear_regression_3.py dosyasında, algoritmanın arka planındaki matematiksel formülleri koda dökerek kapsamlı hata analizleri gerçekleştirdim.

--- Neler Yaptım? Eğim ve kesişim değerlerini herhangi bir kütüphane kullanmadan, doğrudan varyans ve kovaryans formülleriyle (Numerator/Denominator) manuel olarak hesapladım. Model performansını değerlendirmek için MAE, MSE, RMSE ve $R^2$ metriklerini entegre ederek tahminlerin hata payını detaylıca analiz ettim.Teknolojik Stack: Python, NumPy, Matplotlib, Scikit-learn, SciPy.

Teknolojik Stack: Python, NumPy, Matplotlib, Scikit-learn, SciPy.
