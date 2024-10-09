# daftar_buku = {
# "Buku1" : "Harry Potter",
# "Buku2" : "percy jackson",
# "Buku3" : "Twillight"
# }
# print(daftar_buku["Buku1"])
# print(daftar_buku["Buku2"])
# print(daftar_buku["Buku3"])

# Biodata = {
#     "Nama" : "Aldy Ramadhan Syahputra",
#     "NIM" : 2109106079,
#     "KRS" : ["Program Web", "Struktur Data", "Basis Data"],
#     "Mahasiswa_Aktif" :True,
#     "Social Media" : {
#          "Instagram" : "@aldyrmdhns_",
#          "Discord" : "\'Izanami#6848"
#     }
# }

# print(biodata["Social Media"]["Discord"])

# games = dict(Sekiro = "Action", Pokemon = "Adventure",
# Valorant = {"nama":{123:"Informatika"}})
# print(games['Valorant']['nama'][123])


# Games ={
#     "Game1" : "PUBG MOBILE",
#     "Game2" : " Mobile Legend",
#     "Game3" : {
#         "nama" : "COC",
#         "genre" : "strategy"
#     }
# }
# print((Games.get('Game3')).get('genre'))

# Nilai = {
# "Matematika" : 80,
# "B. Indonesia" : 90,
# "B. Inggris" : 81,
# "Kimia" : 78,
# "Fisika" : 80
# }
# #tanpa menggunakan items
# for i,in Nilai:
#     print(i)
# print("")

# #menggunakan items
# for mapel, nilai in Nilai.items():
#     print(f"Nilai {mapel} anda adalah {nilai}")

# Film = {
# "Avenger Endgame" : "Action",
# "Sherlock Holmes" : "Mystery",
# "The Conjuring" : "Horror"
# }
# #Sebelum Ditambah
# print(Film)

# Film["Zombieland"] = "Comedy"
#   Film.update({"Hours" : "Thriller",
#               "Rush hours" : "Comedy",
#               "oblivion" : "Science Fiction"})

#  #Setelah Ditambah

#  #penggunaan del
#  #del Film['Avenger Endgame']

#  simpan = film.pop('Hours')
#  Film.Clear()
#  print(Film)
#  Film["Hours"] = simpan
# print(simpan)

#  print("Jumlah Data = ", len(Film))
#   movies = Film.copy()
#  print (movies)
#  print("Jumlah Film ="), len(movies)

# key = "apel", "jeruk", "mangga"
# value = 1
# buah = dict.fromkeys(key, value)
# print(buah)

# Nilai = {
# "Matematika" : 80,
# "B. Indonesia" : 90,
# "B. Inggris" : 81
# }
# #sebelum Setdefault
# print(Nilai)
# print("")
# #menggunakan setdefault
# print("Nilai : ", Nilai.setdefault("Kimia", 70))
# print("")
# #setelah menggunakan setdefault
# print(Nilai)

# Musik = {
# "The Chainsmoker" : ["All we Know", "TheParis"],
# "Alan Walker" : ["Alone", "Lily"],
# "Neffex" : ["Best of Me", "Memories"]
# }
# for i, j in Musik.items():
#     print(f"Musik milik {i} adalah : ")
#     for song in j:
#         print(song)
# print("")

# mahasiswa = {
# 101 : {"Nama" : "Aldy", "Umur" : 19},
# 111 : {"Nama" : "Abdul", "Umur" : 18}
# }
# for key, value in mahasiswa.items():
#     print("ID Mahasiswa : ", key)
#     for key_a, value_a in value.items():
#         print (key_a, " : ", value_a)
# print("")


# Membuat dictionary awal
# data_mahasiswa = {
#     "Nama": "Budi",
#     "Umur": 20,
#     "NIM": "123456",
#     "Jurusan": "Teknik Informatika",
#     "Angkatan": 2022
# }

# # Fungsi untuk menampilkan menu
# def menu():
#     print("\nMenu:")
#     print("1. Tambah item baru")
#     print("2. Ubah item")
#     print("3. Hapus item")
#     print("4. Tampilkan data")
#     print("5. Keluar")

# # Fungsi untuk menambah item baru
# def tambah_item():
#     key = input("Masukkan key baru: ")
#     value = input("Masukkan value untuk key '{}': ".format(key))
#     data_mahasiswa[key] = value
#     print(f"Item '{key}' berhasil ditambahkan.")

# # Fungsi untuk mengubah item
# def ubah_item():
#     key = input("Masukkan key yang ingin diubah: ")
#     if key in data_mahasiswa:
#         value = input("Masukkan value baru untuk key '{}': ".format(key))
#         data_mahasiswa[key] = value
#         print(f"Item '{key}' berhasil diubah.")
#     else:
#         print(f"Key '{key}' tidak ditemukan.")

# # Fungsi untuk menghapus item
# def hapus_item():
#     key = input("Masukkan key yang ingin dihapus: ")
#     if key in data_mahasiswa:
#         del data_mahasiswa[key]
#         print(f"Item '{key}' berhasil dihapus.")
#     else:
#         print(f"Key '{key}' tidak ditemukan.")

# # Fungsi untuk menampilkan data
# def tampilkan_data():
#     print("\nData Mahasiswa:")
#     for key, value in data_mahasiswa.items():
#         print(f"{key}: {value}")

# # Loop utama
# while True:
#     menu()
#     pilihan = input("Pilih opsi (1-5): ")
    
#     if pilihan == '1':
#         tambah_item()
#     elif pilihan == '2':
#         ubah_item()
#     elif pilihan == '3':
#         hapus_item()
#     elif pilihan == '4':
#         tampilkan_data()
#     elif pilihan == '5':
#         print("Terima kasih! Program selesai.")
#         break
#     else:
#         print("Pilihan tidak valid. Silakan coba lagi.")


# Membuat dictionary dengan data mata pelajaran dan nilainya
nilai_mata_pelajaran = {
    "Matematika": 90,
    "Fisika": 80,
    "Biologi": 80,
    "Kimia": 70
}

# Menghitung total nilai
total_nilai = sum(nilai_mata_pelajaran.values())

# Menghitung rata-rata nilai
jumlah_mapel = len(nilai_mata_pelajaran)
rata_rata_nilai = total_nilai / jumlah_mapel

# Menampilkan hasil
print("Jumlah Total Nilai:", total_nilai)
print("Rata-rata Nilai:", rata_rata_nilai)