import numpy as np
import scipy.integrate as integrate
import matplotlib.pyplot as plt

# Data kasus perceraian dari tahun 2019 hingga 2023
tahun = np.array([2019, 2020, 2021, 2022, 2023])
kasus_perceraian = np.array([438013, 219677, 477743, 448128, 408347])

# Fungsi prediksi berbasis parameter manual
def fungsi_manual(t):
    # Parameter a dan b harus disesuaikan untuk mendekati hasil manual
    a = 67500  # Sesuaikan nilai ini
    b = -134000000  # Sesuaikan nilai ini
    return a * t + b

# Menghitung integral dari fungsi manual untuk prediksi dari tahun 2024 hingga 2026
tahun_awal = 2024
tahun_akhir = 2026

# Menghitung integral dari fungsi manual
integral_total, error = integrate.quad(fungsi_manual, tahun_awal, tahun_akhir)

# Menampilkan hasil integral (total jumlah perceraian dari 2024 hingga 2026)
print(f"Prediksi total jumlah perceraian dari {tahun_awal} hingga {tahun_akhir}: {int(integral_total)} kasus")

# Plot data aktual dan fungsi prediksi manual
tahun_plot = np.linspace(2019, 2027, 100)
kasus_plot = fungsi_manual(tahun_plot)

plt.scatter(tahun, kasus_perceraian, color='blue', label='Data Aktual')
plt.plot(tahun_plot, kasus_plot, color='red', label='Fungsi Prediksi Manual')
plt.fill_between(np.arange(2024, 2027), 0, fungsi_manual(np.arange(2024, 2027)), color='green', alpha=0.2, label='Area Prediksi (2024-2026)')
plt.xlabel('Tahun')
plt.ylabel('Jumlah Perceraian')
plt.legend()
plt.show()
