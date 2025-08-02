# Sentiment Analysis using Machine Learning

Proyek ini bertujuan untuk melakukan analisis sentimen terhadap data teks dengan memanfaatkan berbagai algoritma machine learning. Model yang digunakan mengklasifikasikan teks ke dalam dua kategori sentimen: positif, dan negatif.

## Deskripsi Proyek
Proyek ini melakukan beberapa langkah utama:
- Preprocessing Data: Membersihkan data teks, mengonversi semua karakter dalam teks menjadi huruf kecil, membagi teks menjadi daftar kata atau token, menghapus kata-kata berhenti (stopwords) dalam teks, dan menerapkan stemming pada teks.
- Pelabelan kelas negatif dan positif
- Modeling menggunakan: Naive Bayes, Random Forest, Logistic Regression, Decision Tree, SVM, Random Forest With TF-IDF, dan RNN
 
## Cara Menjalankan

### 1. Clone Repository
```
git clone https://github.com/username/Sentiment_Analysis_using_Machine_Learning.git
cd Sentiment_Analysis_using_Machine_Learning
```
### 2. Install Dependencies
```
pip install -r requirements.txt
```

### 3. Buka ```Sentiment_Analysis_using_Machine_Learning.ipynb``` menggunakan Jupyter Notebook atau Google Colab.

## Hasil Modelling

```
        Logistic Regression       0.886555
                        SVM       0.883498
              Random Forest       0.862830
  Random Forest With TF-IDF       0.860263
              Decision Tree       0.820828
                Naive Bayes       0.806672
                        RNN       0.478434
```