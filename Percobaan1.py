# TODO 0: Impor library yang diperlukan
from PIL import Image, ImageDraw, ImageFont

# TODO 1: Muat gambar ke dalam variabel
gambarku = Image.open("D:\SEMESTER 5\Modul6\download.png")

# TODO 2: Ubah gambar menjadi hitam-putih (grayscale)
gambarBW = gambarku.convert("L")

# TODO 3: Tambahkan teks sesuai kriteria
draw = ImageDraw.Draw(gambarBW)
# Tentukan jalur lengkap ke file font Arial
font_path = "D:\SEMESTER 5\Modul6\Preprak\ArialTh.ttf"
font_size = 24
font = ImageFont.truetype(font_path, font_size)
text = "Nama: Azizah Sisilia Sulandari \nNIM: 202110370311487"
# Dapatkan bounding box dari teks
text_bbox = draw.textbbox((0, 0), text, font=font)
# Hitung posisi tengah untuk teks
text_x = (gambarku.width - text_bbox[2]) // 2
text_y = (gambarku.height - text_bbox[3]) // 2
# Tambahkan teks ke gambar dengan warna hitam
draw.text((text_x, text_y), text, font=font, fill=0)  # Ubah fill menjadi 0

# TODO 4: Simpan gambar hasil edit dengan nama "percobaan_satu.jpg"
# Ubah gambar ke mode RGB sebelum menyimpan sebagai format JPEG
gambarku_bw = Image.new("RGB", gambarku.size)
gambarku_bw.paste(gambarBW)
gambarku_bw.save("percobaan_satu.jpg")

# TODO 5: Tampilkan hasil pengolahan gambar
gambarku_bw.show()
