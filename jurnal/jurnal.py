import datetime

def tulis_jurnal():
    waktu_sekarang = datetime.datetime.now()
    tanggal = waktu_sekarang.strftime("%Y-%m-%d")
    jam = waktu_sekarang.strftime("%H:%M:%S")
    judul = input("Masukkan judul jurnal: ")
    isi = input("Masukkan isi jurnal: ")

    with open("jurnal.txt", "a") as file:
        file.write("Tanggal: " + tanggal + "\n")
        file.write("Jam: " + jam + "\n")
        file.write("Judul: " + judul + "\n")
        file.write("Isi: " + isi + "\n\n")

    print("Jurnal berhasil ditulis.")

tulis_jurnal()
