import serial
import csv
from datetime import datetime

# Inisialisasi koneksi serial
ser = serial.Serial('COM4', 115200)  # Ganti 'COMX' dengan port serial yang sesuai
ser.flushInput()  # Membersihkan input buffer

# Fungsi untuk membaca nilai setelah penanda tertentu
def baca_nilai(data, penanda):
    pos_penanda = data.find(penanda)  # Cari posisi penanda dalam data
    if pos_penanda != -1:
        pos_awal = pos_penanda + len(penanda)  # Tentukan posisi awal nilai setelah penanda
        pos_koma = data.find(',', pos_awal)  # Cari posisi koma setelah nilai
        if pos_koma != -1:
            nilai = float(data[pos_awal:pos_koma])  # Ambil nilai dari pos_awal hingga pos_koma
            return nilai
    return None  # Jika tidak ada penanda yang ditemukan, kembalikan None

# Nama file CSV
nama_file = "data5.csv"

# Main loop untuk membaca dan memproses data serial
with open(nama_file, mode='w', newline='') as file_csv:
    penulis_csv = csv.writer(file_csv)
    penulis_csv.writerow(['Waktu', 'Nilai R'])  # Menulis header

    while True:
        if ser.in_waiting > 0:
            data = ser.readline().decode().strip()  # Membaca data serial dan menghapus karakter newline
            print("Data serial:", data)  # Tampilkan data serial
            
            # Mendapatkan waktu saat ini dengan format milidetik
            waktu = datetime.now().strftime('%H:%M:%S.%f')[:-3]  # Format waktu dengan milidetik (3 digit pertama)

            # Baca nilai setelah penanda 'R:'
            nilai_R = baca_nilai(data, 'R:')
            if nilai_R is not None:
                print("Nilai R:", nilai_R)  # Tampilkan nilai R
                
                # Menyimpan waktu dan nilai R ke dalam file CSV
                penulis_csv.writerow([waktu, nilai_R])
