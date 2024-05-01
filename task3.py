#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random

def generate_one_time_pad(message_length):
    # Генерируем случайный падающий ключ
    pad = [random.randint(0, 255) for _ in range(message_length)]
    return bytes(pad)

def vernam_encrypt(message, one_time_pad):
    # Зашифровка сообщения
    encrypted_message = bytes([m ^ k for m, k in zip(message, one_time_pad)])
    return encrypted_message

def vernam_decrypt(encrypted_message, one_time_pad):
    # Дешифровка сообщения
    decrypted_message = bytes([c ^ k for c, k in zip(encrypted_message, one_time_pad)])
    return decrypted_message

def main():
    
    message = input("Введите сообщение для шифрования: ").encode()
    one_time_pad = generate_one_time_pad(len(message))
    encrypted_message = vernam_encrypt(message, one_time_pad)
    decrypted_message = vernam_decrypt(encrypted_message, one_time_pad)
    
    print("Исходное сообщение: ", message.decode())
    print("Падающий ключ: ", one_time_pad)
    print("Зашифрованное сообщение: ", encrypted_message)
    print("Расшифрованное сообщение: ", decrypted_message.decode())

if __name__ == "__main__":
    main()

