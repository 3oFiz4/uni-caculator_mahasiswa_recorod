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
