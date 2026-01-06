def main():
    def Calculator():
        def add(x, y):
            return x + y

        def min(x, y):
            return x - y

        def mul(x, y):
            return x * y

        def div(x, y):
            return x / y

        while True:
            print("""
    ===== MENU KALKULATOR =====
    1. Penjumlahan
    2. Pengurangan
    3. Perkalian
    4. Pembagian
    5. Keluar
                """)

            result = None
            prompt_menu = int(input("Pilih menu (1-5): "))
            if prompt_menu == 5:
                print("Keluar")
                break
            first_int = int(input("Masukan bilangan pertama: "))
            second_int = int(input("Masukan bilangan kedua: "))
            if prompt_menu == 1:
                result = add(first_int, second_int)
            elif prompt_menu == 2:
                result = min(first_int, second_int)
            elif prompt_menu == 3:
                result = mul(first_int, second_int)
            elif prompt_menu == 4:
                result = div(first_int, second_int)
            print("Hasil Penjumlahan:", result)

    def PengelolahanMahasiswa():
        path = "database_mahasiswa.txt"

        def display():
            with open(path, "r") as f:
                f.seek(0)  # Set pointer to 0
                print(f.read())

        def add(nim, name, study_program):
            with open(path, "a") as f:
                f.write(f"""
NIM: {nim}
NAMA: {name}
PROGRAM STUDI: {study_program}
                        """)

        def _normalize(lines):  # Handle blanks
            normalized = []
            empty = False

            for line in lines:
                if line.strip() == "":
                    if not empty:
                        normalized.append("\n")
                    empty = True
                else:
                    normalized.append(line)
                    empty = False

            return normalized

        def remove(nim):
            with open(path, "r", encoding="utf-8") as f:
                lines = f.readlines()
            new_lines = []
            skip = False

            for line in lines:
                if line.startswith(f"NIM: {nim}"):
                    skip = True
                    continue

                if skip:
                    if line.strip() == "":
                        skip = False
                    continue

                new_lines.append(line)

            new_lines = _normalize(new_lines)

            with open(path, "w", encoding="utf-8") as f:
                f.writelines(new_lines)

        def find(nim):
            with open(path, "r", encoding="utf-8") as f:
                found = False
                buffer = []

                for line in f:
                    if line.startswith(f"NIM: {nim}"):
                        found = True
                        buffer.append(line)
                        continue

                    if found:
                        if line.strip() == "":
                            break  # end of sibling block
                        buffer.append(line)

                if found:
                    print("".join(buffer))

        # ---------------------------------------------------pertama
        while True:
            print("""
    ===== MENU PENGELOLAHAN MAHASISWA =====
    1. Tambah Mahasiswa
    2. Tampilkan Semua Mahasiswa
    3. Cari Mahasiswa (NIM)
    4. Hapus Mahasiswa (NIM)
    5. Keluar
                """)

            prompt_menu = int(input("Pilih menu (1-5): "))
            if prompt_menu == 5:
                print("Keluar")
                break
            if prompt_menu == 1:
                prompt_nim = input("Masukan NIM: ")
                prompt_nama = input("Masukan Nama: ")
                prompt_prodi = input("Masukan Prodi: ")
                add(prompt_nim, prompt_nama, prompt_prodi)
            elif prompt_menu == 2:
                display()
            elif prompt_menu == 3:
                prompt_nim = input("Masukan NIM:")
                find(prompt_nim)
            elif prompt_menu == 4:
                prompt_nim = input("Masukan NIM: ")
                remove(prompt_nim)

    # ---------------------------------------------------------
    Calculator()
    PengelolahanMahasiswa()


if __name__ == "__main__":
    main()
