import os
import shutil
import zipfile

def papka_backuplash(papka_nomi):
    # Papka mavjudligini tekshiramiz
    if not os.path.exists(papka_nomi):
        print(f"Papka {papka_nomi} mavjud emas.")
        return

    # Papka nomini oling
    papka_ismi = os.path.basename(papka_nomi)

    # Zip arxivini yaratamiz
    zip_ismi = f"{papka_ismi}.zip"
    zip_fayl = zipfile.ZipFile(zip_ismi, 'w')

    # Papka ichidagi fayllarni zip arxiviga yuklaymiz
    for root, dirs, files in os.walk(papka_nomi):
        for file in files:
            file_path = os.path.join(root, file)
            rel_path = os.path.relpath(file_path, papka_nomi)
            zip_fayl.write(file_path, rel_path)

    # Zip arxivini yopamiz
    zip_fayl.close()

    print(f"Papka {papka_nomi} backup qilindi.")

# Backup qilish uchun papka nomini kiritamiz
papka_nomi = input("Papka nomini kiriting: ")
papka_backuplash(papka_nomi)
