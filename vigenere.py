# Mendefinisikan fungsi enkripsi Vigenere
def vigenere_encrypt(plain_text, key):
    encrypted_text = ""  # Variabel untuk menyimpan pesan terenkripsi
    key_length = len(key)  # Panjang kunci

    # Melakukan iterasi pada setiap karakter dalam plaintext
    for i in range(len(plain_text)):
        char = plain_text[i]  # Mengambil karakter plaintext

        # Memeriksa apakah karakter merupakan huruf alfabet
        if char.isalpha():
            key_char = key[i % key_length]  # Mengambil karakter kunci yang sesuai
            shift = ord(key_char) - ord('A') if key_char.isupper() else ord(key_char) - ord('a')  # Menghitung pergeseran berdasarkan kunci

            # Memeriksa apakah karakter plaintext adalah huruf besar atau kecil
            if char.isupper():
                # Enkripsi karakter huruf besar
                encrypted_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
            else:
                # Enkripsi karakter huruf kecil
                encrypted_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))

            # Menambahkan karakter terenkripsi ke pesan terenkripsi
            encrypted_text += encrypted_char
        else:
            # Jika karakter bukan huruf alfabet, tambahkan ke pesan terenkripsi tanpa perubahan
            encrypted_text += char

    return encrypted_text

# Mendefinisikan fungsi dekripsi Vigenere
def vigenere_decrypt(encrypted_text, key):
    decrypted_text = ""  # Variabel untuk menyimpan pesan terdekripsi
    key_length = len(key)  # Panjang kunci

    # Melakukan iterasi pada setiap karakter dalam pesan terenkripsi
    for i in range(len(encrypted_text)):
        char = encrypted_text[i]  # Mengambil karakter pesan terenkripsi

        # Memeriksa apakah karakter merupakan huruf alfabet
        if char.isalpha():
            key_char = key[i % key_length]  # Mengambil karakter kunci yang sesuai
            shift = ord(key_char) - ord('A') if key_char.isupper() else ord(key_char) - ord('a')  # Menghitung pergeseran berdasarkan kunci

            # Memeriksa apakah karakter pesan terenkripsi adalah huruf besar atau kecil
            if char.isupper():
                # Dekripsi karakter huruf besar
                decrypted_char = chr(((ord(char) - ord('A') - shift + 26) % 26) + ord('A'))
            else:
                # Dekripsi karakter huruf kecil
                decrypted_char = chr(((ord(char) - ord('a') - shift + 26) % 26) + ord('a'))

            # Menambahkan karakter terdekripsi ke pesan terdekripsi
            decrypted_text += decrypted_char
        else:
            # Jika karakter bukan huruf alfabet, tambahkan ke pesan terdekripsi tanpa perubahan
            decrypted_text += char

    return decrypted_text

# Fungsi untuk mengenkripsi pesan
def encrypt_message():
    plain_text = input("Masukkan Plaintext: ")
    key = input("Masukkan Key: ")

    # Enkripsi pesan
    encrypted_text = vigenere_encrypt(plain_text, key)
    print("Pesan Terenkripsi: ", encrypted_text)
    return encrypted_text

# Fungsi untuk mendekripsi pesan
def decrypt_message():
    encrypted_text = input("Masukkan Ciphertext: ")
    key = input("Masukkan Key: ")

    # Dekripsi pesan
    decrypted_text = vigenere_decrypt(encrypted_text, key)
    print("Pesan Terdekripsi: ", decrypted_text)

# Menu utama
while True:
    print("1. Enkripsi")
    print("2. Dekripsi")
    print("3. Keluar")
    choice = input("Pilih Menu: ")

    if choice == '1':
        encrypt_message()
    elif choice == '2':
        decrypt_message()
    elif choice == '3':
        break
    else:
        print("Pilihan tidak valid. Coba lagi !!")
