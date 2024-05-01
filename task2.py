#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import collections
from task1 import caesar_cipher, caesar_decipher

english_frequencies = {
    'E': 12.02, 'T': 9.10, 'A': 8.12, 'O': 7.68, 'I': 7.31,
    'N': 6.95, 'S': 6.28, 'R': 6.02, 'H': 5.92, 'D': 4.32,
    'L': 3.98, 'U': 2.88, 'C': 2.71, 'M': 2.61, 'F': 2.30,
    'Y': 2.11, 'W': 2.09, 'G': 2.03, 'P': 1.82, 'B': 1.49,
    'V': 1.11, 'K': 0.69, 'X': 0.17, 'Q': 0.11, 'J': 0.10,
    'Z': 0.07
}

def caesar_break_cipher(encrypted_text):
    counter = collections.Counter(encrypted_text)
    
    # Поиск самого частого символа
    most_common_char = counter.most_common(1)[0][0]
    #Приписываем ему Е
    shift = ord('E') - ord(most_common_char)
    #Вычисляем сдвиг по разнице
    decrypted_text = caesar_decipher(encrypted_text, shift)
    return decrypted_text

# Пример использования
def main():
    encrypted_text = input("Введите зашифрованный текст: ")
    decryption = caesar_break_cipher(encrypted_text)
    print("Возможное оригинальное сообщение: ", decryption)
    
if __name__ == "__main__":
    main()
