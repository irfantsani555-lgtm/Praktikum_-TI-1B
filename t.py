
# ==================================
# PROGRAM KASIR MINIMARKET ALFAMART
# ==================================

print("=" * 45)
print("       SELAMAT DATANG DI ALFAMART")
print("=" * 45)

# Daftar barang
barang = {
    "1": ["Indomie Goreng", 3500],
    "2": ["Aqua 600ml", 4000],
    "3": ["Chitato", 12000],
    "4": ["SilverQueen", 15000],
    "5": ["Susu Ultra Milk", 6000],
    "6": ["Roti Tawar", 14000],
    "7": ["Sabun Lifebuoy", 5000],
    "8": ["Teh Pucuk", 4000],
    "9": ["Beras 5kg", 75000],
    "10": ["Minyak Goreng", 18000]
}

keranjang = []
total = 0

# Menampilkan daftar barang
print("\nDAFTAR BARANG")
print("-" * 45)
print(f"{'Kode':<8}{'Nama Barang':<22}{'Harga':>12}")
print("-" * 45)

for kode, data in barang.items():
    print(f"{kode:<8}{data[0]:<22}Rp{data[1]:>9,}")

print("-" * 45)

# Proses pembelian
while True:
    kode = input("\nMasukkan kode barang (0 untuk selesai): ")

    if kode == "0":
        break

    if kode in barang:
        nama = barang[kode][0]
        harga = barang[kode][1]

        jumlah = int(input("Masukkan jumlah barang: "))

        if jumlah <= 0:
            print("Jumlah harus lebih dari 0!")
            continue

        subtotal = harga * jumlah
        total += subtotal

        keranjang.append([nama, harga, jumlah, subtotal])

        print(f"{nama} berhasil ditambahkan!")
        print(f"Subtotal: Rp{subtotal:,}")

    else:
        print("Kode barang tidak ditemukan!")

# Menghitung diskon
print("\n" + "=" * 45)
print("             STRUK BELANJA")
print("=" * 45)

print("             ALFAMART")
print("       Belanja Puas Harga Pas!")
print("-" * 45)

for item in keranjang:
    print(f"{item[0]}")
    print(f"  {item[2]} x Rp{item[1]:,} = Rp{item[3]:,}")

print("-" * 45)

print(f"Total Belanja : Rp{total:,}")

# Diskon 5% jika belanja minimal Rp100.000
if total >= 100000:
    diskon = total * 5 // 100
else:
    diskon = 0

total_bayar = total - diskon

print(f"Diskon        : Rp{diskon:,}")
print(f"Total Bayar   : Rp{total_bayar:,}")

# Proses pembayaran
if total_bayar > 0:
    while True:
        uang = int(input("\nMasukkan uang pembayaran: Rp"))

        if uang >= total_bayar:
            break
        else:
            print("Uang tidak mencukupi!")
            print(f"Kekurangan: Rp{total_bayar - uang:,}")

    kembalian = uang - total_bayar

    print("-" * 45)
    print(f"Uang Tunai    : Rp{uang:,}")
    print(f"Kembalian     : Rp{kembalian:,}")

print("=" * 45)
print("       TERIMA KASIH TELAH BERBELANJA")
print("           DI ALFAMART!")
print("=" * 45)
