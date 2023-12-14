from PIL import Image, ImageEnhance

# TODO 1: Buka gambar dengan pillow
image = Image.open("D:\SEMESTER 5\Modul6\inibg.jpg")

# TODO 2: Ubah tingkat kecerahan (brightness) dan kontras (contrast)
enhancer = ImageEnhance.Brightness(image)
brightness_image = enhancer.enhance(1.5)

enhancer = ImageEnhance.Contrast(brightness_image)
final_image = enhancer.enhance(1.2)

# TODO 3: Simpan gambar hasil edit
final_image.save("brightness_contrast_image.jpg")

# TODO 4: Tampilkan hasil
final_image.show()
