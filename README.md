# Analisis Sentimen Postingan Diskominfos Denpasar tentang 10 Proyek Strategis

## Deskripsi Proyek
Proyek ini merupakan salah satu bentuk tugas yang dikerjakan pada **Praktik Kerja Lapangan (PKL)** di **Dinas Komunikasi, Informatika, dan Statistik Kota Denpasar**.  
Tujuan proyek adalah melakukan **analisis sentimen masyarakat terhadap komentar Instagram terkait 10 proyek strategis Kota Denpasar**.  

Sistem dikembangkan menggunakan **machine learning** dengan dua algoritma utama:  
- **Support Vector Machine (SVM)**  
- **Multinomial Naive Bayes (MNB)**  

Fokus proyek adalah **mengidentifikasi sentimen dan emosi masyarakat**, serta memberikan insight terkait persepsi masyarakat terhadap 10 proyek strategis pemkot Denpasar.

---

## Dataset
- Sumber: **Crawling komentar Instagram 10 proyek strategis**  
- Jumlah data: **103 komentar**  
- Kelas sentimen: **Positif & Negatif**

Distribusi awal:
- Negatif: 53  
- Positif: 50  

Setelah balancing (oversampling):
- Negatif: 53  
- Positif: 53  

---

## Alur Implementasi
1. Load dataset komentar
2. Pra-pemrosesan teks:
   - Pembersihan data (URL, simbol, mention, hashtag)
   - Case folding (huruf kecil)
   - Normalisasi kata slang
   - Stopword removal
   - Tokenisasi kata
   - Stemming
3. Ekstraksi fitur menggunakan **TF-IDF**
4. Pembagian data menjadi data **training (80%)** dan **testing (20%)**
5. Training model menggunakan **SVM** dan **MNB**
6. Evaluasi performa model
7. Visualisasi hasil analisis: **WordCloud**, bar plot, pie chart
8. Deteksi emosi komentar menggunakan lexicon-based
9. Prediksi sentimen dan emosi komentar baru

---

## Pra-pemrosesan Teks
Langkah-langkah:
- Bersihkan teks dari URL, simbol, mention, hashtag
- Case folding
- Normalisasi kata slang
- Stopword removal
- Tokenisasi
- Stemming

---

## Penanganan Ketidakseimbangan Kelas
Dataset awal tidak seimbang:  
- Negatif: 53  
- Positif: 50  

Dilakukan **oversampling** sehingga menjadi:  
- Negatif: 53  
- Positif: 53  

---

## Model Machine Learning

### Support Vector Machine (SVM)
- Akurasi: **91%**  
- Confusion Matrix
<img width="530" height="455" alt="image" src="https://github.com/user-attachments/assets/94a6d2a3-58a9-4796-b9b8-37a7f1fa2010" />

---

### Multinomial Naive Bayes (MNB)
- Akurasi: **91%**  
- Confusion matrix:  
<img width="591" height="470" alt="image" src="https://github.com/user-attachments/assets/b7317d1b-dd70-4fad-9df7-181eb30210df" />

---

## Visualisasi Data

### Distribusi Sentimen
- Bar plot dan pie chart distribusi komentar setelah balancing:  
<img width="562" height="455" alt="image" src="https://github.com/user-attachments/assets/f23d3d04-d6f5-434d-b43f-48765d27c51d" />
<img width="290" height="290" alt="image" src="https://github.com/user-attachments/assets/6866f829-93d3-4b0f-a793-092195f68567" />

### WordCloud
- **WordCloud Umum**:  
<img width="795" height="820" alt="image" src="https://github.com/user-attachments/assets/90cdab60-8506-4c3b-8a1f-175d5120d1a5" />

- **WordCloud Positif**:  
<img width="795" height="820" alt="image" src="https://github.com/user-attachments/assets/6193206f-fa87-41bd-a6e5-e08dd104c61c" />

- **WordCloud Negatif**:  
<img width="795" height="820" alt="image" src="https://github.com/user-attachments/assets/f2f520bd-f0e2-4c9d-be13-d7dadb6a1c97" />

---

## Analisis Emosi
Lexicon-based detection menghasilkan distribusi emosi sebagai berikut:

| Emosi       | Jumlah |
|------------|--------|
| Senang     | 44     |
| Biasa saja | 26     |
| Sedih      | 19     |
| Kritis     | 6      |
| Ragu-ragu  | 5      |
| Optimis    | 3      |
| Marah      | 3      |

**Insight:**
- Mayoritas komentar bersifat **positif atau senang**, mendukung proyek strategis.  
- Komentar **negatif dan sedih** terkait infrastruktur.  
- Emosi **kritis** muncul pada komentar yang meminta perhatian dan koordinasi pemerintah.

---

## Inference Hasil menggunakan Fungsi Prediksi

### Model SVM
<img width="526" height="215" alt="image" src="https://github.com/user-attachments/assets/5eea8bd4-282c-4b49-bf0c-141ddbc169a9" />

### Model MNB
<img width="536" height="214" alt="image" src="https://github.com/user-attachments/assets/4612866d-d801-497e-8d53-33499d3f7924" />
