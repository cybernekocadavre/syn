#!/usr/bin/env python
# coding: cp-1251

# In[ ]:


def caesar_cipher(text, shift):
    
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

def main():
    text = input("Введите текст для зашифровки: ")
    
    while True:
        shift = int(input("Введите значение сдвига: "))
        try:
            shift = int(shift)
            break
        except ValueError:
            print("Вводимый сдвиг должен быть типа int!")
        
    encrypted_text = caesar_cipher(text, shift)
    print("Зашифрованное сообщение:", encrypted_text)
    decrypted_text = caesar_decipher(encrypted_text, shift)
    print("Расшифрованное сообщение:", decrypted_text)
    
if __name__ == "__main__":
    main()

