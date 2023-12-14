# TODO 0: Import beberapa library lain yang dibutuhkan
from PIL import Image

# TODO 1: Buka gambar latar belakang (background) dan gambar yang ingin
# disisipkan (overlay)
background_image = Image.open("D:\SEMESTER 5\Modul6\inibg.jpg")
overlay_image = Image.open("D:\SEMESTER 5\Modul6\Preprak\inifutsal.jpeg")

# TODO 2: Konversi overlay image ke mode RGB (menghilangkan alpha channel)
overlay_image = overlay_image.convert("RGBA").convert("RGB")

# TODO 3: Perkecil ukuran gambar overlay menggunakan method resize()
new_width = 500  # Ganti dengan lebar yang diinginkan
new_height = 500  # Ganti dengan tinggi yang diinginkan
overlay_image = overlay_image.resize((new_width, new_height))

# Tentukan/Hitung koordinat tengah untuk menempatkan overlay
x_center = (background_image.width - overlay_image.width) // 2
y_center = (background_image.height - overlay_image.height) // 2

# TODO 4: Sisipkan gambar overlay ke dalam gambar background menggunakan
# method paste()
background_image.paste(overlay_image, (x_center, y_center))

# TODO 5: Simpan gambar hasil edit
background_image.save("output_image.jpg")

# TODO 6: Tampilkan hasil
background_image.show()
