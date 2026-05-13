Bu projede, bir yapay zeka ajanının deneme-yanılma yoluyla bir ortamda nasıl karar vermesi gerektiğini öğrendiği Takviyeli Öğrenme modelini uyguladım. Ajan, çevreyle etkileşime girerek ödülleri maksimize etmeyi öğrenen bir Q-Learning algoritması kullanmaktadır.

--- Neler Yaptım?

Ortam Tasarımı (Grid World): Ajan için $5 \times 5$ boyutunda bir oyun alanı kurguladım. Sol üst köşeyi başlangıç, sağ alt köşeyi ise yüksek ödüllü hedef noktası olarak belirledim. Her adımın küçük bir negatif puan (-1) getirdiği bu yapıda ajanı en kısa yolu bulmaya zorladım.

Q-Tablosu ve Öğrenme Mekanizması: Ajanın hafızasını temsil eden bir Q-Tablosu (Q-Table) oluşturdum. Öğrenme oranı (alpha), indirim faktörü (gamma) ve epsilon gibi hiperparametreleri kullanarak ajanın geçmiş tecrübelerinden ders çıkarmasını sağladım.

Epsilon-Greedy Stratejisi: Ajanın sadece bildiği yoldan gitmek yerine yeni yollar keşfetmesi için %20 ihtimalle rastgele hareket ettiği (exploration) bir mekanizma entegre ettim.Eğitim Döngüsü: Sistemi 1000 iterasyon boyunca çalıştırarak ajanın hedefe ulaşma konusundaki karar verme sürecini stabilize ettim ve öğrenme sürecini fonksiyonel bir yapıyla optimize ettim.

--- Teknolojik Stack 

Kütüphaneler: NumPy (Matematiksel işlemler ve Q-Tablosu yönetimi), Matplotlib (Öğrenme sürecinin görselleştirilmesi için altyapı), Random.

Algoritma: Q-Learning (Off-policy Reinforcement Learning).Yöntem: Takviyeli Öğrenme (Reinforcement Learning).

--- Nasıl Çalışır? 

Ajan başlangıçta dünyayı bilmez ve tamamen rastgele hareketler yapar. Her adımda çevreye bir eylem gönderir ve karşılığında bir ödül ile yeni bir durum (state) bilgisi alır. Aldığı ödüllere göre Q-Tablosundaki değerleri güncelleyerek hangi durumda hangi eylemin (yukarı, aşağı, sol, sağ) daha karlı olduğunu hafızasına kazır. Eğitim süreci ilerledikçe ajan rastgele hareketleri bırakır ve Q-Tablosundaki verilere dayanarak başlangıçtan hedefe giden en optimize rotayı izlemeye başlar.
