from cryptography.fernet import Fernet, InvalidToken

# key = Fernet.generate_key()
# fernet = Fernet(key)

key = b'Md9MwbLKdRl6EqocTWqdPIOBum6HsrSD10a5W--0fvk='
fernet = Fernet(key)

def encrypt_pass(input_pass):
    
    if type(input_pass) != bytes:
        input_pass_bytes = input_pass.encode('utf-8')
    else:
        input_pass_bytes = input_pass
    
    encrypted_pass = fernet.encrypt(input_pass_bytes)
    return encrypted_pass.decode('utf-8')

def decrypt_pass(encrypted_data):
    
    if type(encrypted_data) != bytes:
        encrypted_data_bytes = encrypted_data.encode('utf-8')
    else:
        encrypted_data_bytes = encrypted_data
    try:
        decrypted_data = fernet.decrypt(encrypted_data_bytes)
    except InvalidToken:
        return 'Token Invalido!!!'
    return decrypted_data.decode('utf-8')

if __name__ == '__main__':
    x = decrypt_pass('gAAAAABjL0bzOnba-OHH0cVphK5fYUen_x8h5Z6y37fB9xwqiKDH6H4VgeE9k_b_ii5bS-ju3YnY83MAwl_PPHb8JEUaZVG8rQ==')