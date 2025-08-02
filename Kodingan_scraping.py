# Mengimpor pustaka google_play_scraper untuk mengakses ulasan dan informasi aplikasi dari Google Play Store.
import csv
from google_play_scraper import app, reviews_all, Sort
import pandas as pd

# Mengambil semua ulasan dari aplikasi dengan ID 'id.bmri.livin' di Google Play Store.
scrapreview = reviews_all(
    'id.bmri.livin',          # ID aplikasi
    lang='id',             # Bahasa ulasan (default: 'en')
    country='id',          # Negara (default: 'us')
    sort=Sort.MOST_RELEVANT, # Urutan ulasan (default: Sort.MOST_RELEVANT)
    count=10000            # Jumlah maksimum ulasan yang ingin diambil
)

# Menyimpan ulasan dalam file CSV

with open('review_livin.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Review']) 
    for review in scrapreview:
        writer.writerow([review['content']])  
        
app_reviews_df = pd.DataFrame(scrapreview)
app_reviews_df.shape
app_reviews_df.head()
app_reviews_df.to_csv('review_livin.csv', index=False)