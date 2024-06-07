# Analisis Data Perubahan Cuaca

Proyek ini bertujuan untuk menganalisis data perubahan cuaca harian sepanjang tahun 2023. Kami menggunakan tiga tabel yang berisi informasi tentang suhu, kelembaban dan curah hujan, serta kecepatan angin dan polusi udara.

## Langkah-langkah

### Persiapan

1. Pastikan Anda memiliki Python terinstal di sistem Anda. Proyek ini menggunakan Python 3.12.
2. Instal pustaka yang diperlukan:
    ```sh
    pip install pandas matplotlib
    ```

### Menjalankan Kode

1. Simpan ketiga file CSV di direktori yang sama dengan skrip Python:
    - `Suhu_Harian.csv`
    - `Kelembaban_Curah_Harian.csv`
    - `Angin_Polusi_Harian.csv`

2. Buat file Python bernama `analisis_data.py` dan salin kode berikut ke dalamnya:

    ```python
    import pandas as pd
    import matplotlib.pyplot as plt

    # Load the data
    df_suhu = pd.read_csv('Suhu_Harian.csv')
    df_kelembaban_curah = pd.read_csv('Kelembaban_Curah_Harian.csv')
    df_angin_polusi = pd.read_csv('Angin_Polusi_Harian.csv')

    # Convert 'Tanggal' to datetime
    df_suhu['Tanggal'] = pd.to_datetime(df_suhu['Tanggal'])
    df_kelembaban_curah['Tanggal'] = pd.to_datetime(df_kelembaban_curah['Tanggal'])
    df_angin_polusi['Tanggal'] = pd.to_datetime(df_angin_polusi['Tanggal'])

    # Set 'Tanggal' as index
    df_suhu.set_index('Tanggal', inplace=True)
    df_kelembaban_curah.set_index('Tanggal', inplace=True)
    df_angin_polusi.set_index('Tanggal', inplace=True)

    # Analysis and visualization
    # Suhu Harian
    plt.figure(figsize=(10, 6))
    plt.plot(df_suhu.index, df_suhu['Suhu Rata-rata (°C)'], label='Suhu Rata-rata')
    plt.plot(df_suhu.index, df_suhu['Suhu Maksimum (°C)'], label='Suhu Maksimum')
    plt.plot(df_suhu.index, df_suhu['Suhu Minimum (°C)'], label='Suhu Minimum')
    plt.title('Perubahan Suhu Harian')
    plt.xlabel('Tanggal')
    plt.ylabel('Suhu (°C)')
    plt.legend()
    plt.grid(True)
    plt.show()

    print("Statistik Suhu Harian:")
    print(df_suhu.describe())

    # Kelembaban dan Curah Hujan Harian
    plt.figure(figsize=(10, 6))
    plt.plot(df_kelembaban_curah.index, df_kelembaban_curah['Kelembaban Rata-rata (%)'], label='Kelembaban Rata-rata')
    plt.title('Perubahan Kelembaban Harian')
    plt.xlabel('Tanggal')
    plt.ylabel('Kelembaban (%)')
    plt.legend()
    plt.grid(True)
    plt.show()

    plt.figure(figsize=(10, 6))
    plt.plot(df_kelembaban_curah.index, df_kelembaban_curah['Curah Hujan (mm)'], label='Curah Hujan', color='b')
    plt.title('Perubahan Curah Hujan Harian')
    plt.xlabel('Tanggal')
    plt.ylabel('Curah Hujan (mm)')
    plt.legend()
    plt.grid(True)
    plt.show()

    print("Statistik Kelembaban dan Curah Hujan Harian:")
    print(df_kelembaban_curah.describe())

    # Kecepatan Angin dan Polusi Udara Harian
    plt.figure(figsize=(10, 6))
    plt.plot(df_angin_polusi.index, df_angin_polusi['Kecepatan Angin (km/jam)'], label='Kecepatan Angin', color='g')
    plt.title('Perubahan Kecepatan Angin Harian')
    plt.xlabel('Tanggal')
    plt.ylabel('Kecepatan Angin (km/jam)')
    plt.legend()
    plt.grid(True)
    plt.show()

    plt.figure(figsize=(10, 6))
    plt.plot(df_angin_polusi.index, df_angin_polusi['Indeks Kualitas Udara (AQI)'], label='Indeks Kualitas Udara', color='r')
    plt.title('Perubahan Indeks Kualitas Udara Harian')
    plt.xlabel('Tanggal')
    plt.ylabel('Indeks Kualitas Udara (AQI)')
    plt.legend()
    plt.grid(True)
    plt.show()

    print("Statistik Kecepatan Angin dan Polusi Udara Harian:")
    print(df_angin_polusi.describe())
    ```

3. Jalankan skrip Python:
    ```sh
    python analisis_data.py
    ```

## Pertanyaan dan Jawaban

1. **Bagaimana tren suhu rata-rata harian sepanjang tahun 2023?**
    - **Visualisasi**: Grafik garis menunjukkan perubahan suhu rata-rata harian sepanjang tahun.
    - **Jawaban**: Tren suhu rata-rata harian dapat dilihat dari grafik garis yang dihasilkan.

2. **Bagaimana perbandingan suhu maksimum dan minimum harian sepanjang tahun 2023?**
    - **Visualisasi**: Grafik garis menunjukkan suhu maksimum dan minimum harian.
    - **Jawaban**: Perbandingan dapat dilihat dari dua garis pada grafik yang mewakili suhu maksimum dan minimum.

3. **Bagaimana variasi kelembaban harian sepanjang tahun 2023?**
    - **Visualisasi**: Grafik garis menunjukkan kelembaban harian sepanjang tahun.
    - **Jawaban**: Variasi kelembaban dapat dilihat dari grafik garis kelembaban.

4. **Bagaimana curah hujan harian berubah sepanjang tahun 2023? Apakah ada bulan-bulan dengan curah hujan yang lebih tinggi?**
    - **Visualisasi**: Grafik garis menunjukkan curah hujan harian sepanjang tahun.
    - **Jawaban**: Perubahan curah hujan dan bulan-bulan dengan curah hujan lebih tinggi dapat diidentifikasi dari grafik.

5. **Bagaimana kecepatan angin harian bervariasi sepanjang tahun 2023?**
    - **Visualisasi**: Grafik garis menunjukkan kecepatan angin harian sepanjang tahun.
    - **Jawaban**: Variasi kecepatan angin dapat dilihat dari grafik garis kecepatan angin.

6. **Bagaimana indeks kualitas udara (AQI) harian berubah sepanjang tahun 2023?**
    - **Visualisasi**: Grafik garis menunjukkan indeks kualitas udara harian sepanjang tahun.
    - **Jawaban**: Perubahan AQI dapat dilihat dari grafik garis AQI.

7. **Apakah ada korelasi antara kecepatan angin dan indeks kualitas udara?**
    - **Visualisasi**: Scatter plot atau grafik garis untuk kecepatan angin dan AQI.
    - **Jawaban**: Korelasi dapat dianalisis dengan membuat scatter plot antara kecepatan angin dan AQI.

8. **Apakah ada pola musiman yang jelas dalam data suhu, kelembaban, curah hujan, kecepatan angin, atau AQI?**
    - **Visualisasi**: Grafik garis menunjukkan tren data cuaca harian sepanjang tahun.
    - **Jawaban**: Pola musiman dapat diidentifikasi dari tren pada grafik.

9. **Bagaimana kondisi cuaca pada bulan-bulan tertentu? Misalnya, bagaimana suhu, kelembaban, curah hujan, kecepatan angin, dan AQI pada bulan Januari dibandingkan dengan bulan Juli?**
    - **Visualisasi**: Grafik garis atau bar chart untuk membandingkan kondisi cuaca antara dua bulan yang berbeda.
    - **Jawaban**: Perbandingan dapat dilakukan dengan visualisasi data untuk bulan yang berbeda.

10. **Bagaimana distribusi suhu rata-rata, kelembaban, curah hujan, kecepatan angin, dan AQI sepanjang tahun 2023?**
    - **Visualisasi**: Histogram atau box plot untuk masing-masing variabel.
    - **Jawaban**: Distribusi data dapat dilihat dari histogram atau box plot.

Dengan mengikuti langkah-langkah di atas, Anda dapat menjalankan analisis dan visualisasi data cuaca harian sepanjang tahun 2023.

![Perubahan Suhu Harian](https://github.com/farrelialuthfiana/Analisis-Perubahan-Cuaca-Harian/assets/152155896/a5a70756-572b-4515-8e22-6463f6f217d1)
![Perubahan Kelembaban Harian](https://github.com/farrelialuthfiana/Analisis-Perubahan-Cuaca-Harian/assets/152155896/df2659b1-ef02-46ae-aa1b-158492e63dc3)
![Perubahan Curah Hujan Harian](https://github.com/farrelialuthfiana/Analisis-Perubahan-Cuaca-Harian/assets/152155896/d4a7ce80-7ef3-4653-8fe3-711a593f1172)
![Perubahan Kecepatan Angin Harian](https://github.com/farrelialuthfiana/Analisis-Perubahan-Cuaca-Harian/assets/152155896/cfa5676e-9317-48f1-92d3-37296ed661ec)
![Perubahan Indeks Kualitas Udara Harian](https://github.com/farrelialuthfiana/Analisis-Perubahan-Cuaca-Harian/assets/152155896/6fdeca2b-4234-49fa-a90f-a761cfeed2d9)




