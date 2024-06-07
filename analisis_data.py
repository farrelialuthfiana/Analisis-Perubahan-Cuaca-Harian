import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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
