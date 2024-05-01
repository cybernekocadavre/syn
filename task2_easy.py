#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def caesar_break_cipher(encrypted_text):
    decrypted_texts = []
    for shift in range(1, 26):  # Перебираем все возможные значения сдвига
        decrypted_text = caesar_decipher(encrypted_text, shift)
        decrypted_texts.append(decrypted_text)
    return decrypted_texts

def main():
    encrypted_text = input("Введите зашифрованный текст: ")
    possible_decryptions = caesar_break_cipher(encrypted_text)
    print("Варианты оригинального сообщения:")
    for i, text in enumerate(possible_decryptions):
        print(f"Вариант {i+1}: {text}")

if __name__ == "__main__":
    main()

