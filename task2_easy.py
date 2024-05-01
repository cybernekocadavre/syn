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

#---------------------------------------------------

def caesar_cipher(text, shift):

    # Программа написана под АНГЛИЙСКИЙ ТЕКСТ!!!
    
    encrypted_text = ""
    for char in text:
        
        # Проверяем, является ли символ буквой
        if char.isalpha():
            
            # Определяем смещение для каждой буквы
            shifted = ord(char) + shift
            
            # Если выходим за пределы алфавита, возвращаемся к его началу
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
                    
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
                    
            encrypted_text += chr(shifted)
            
        else:
            # Если символ не является буквой, просто добавляем его в зашифрованный текст
            encrypted_text += char
            
    return encrypted_text

def caesar_decipher(text, shift):
    return caesar_cipher(text, -shift)

