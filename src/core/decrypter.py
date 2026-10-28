import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding

# CONFIGURAÇÕES
TARGET_DIR = "./test_folder"
PRIVATE_KEY_PATH = "private_key.pem"
SESSION_KEY_PATH = "session.key"
EXTENSION = ".locked"

def load_private_key():
    with open(PRIVATE_KEY_PATH, "rb") as key_file:
        return serialization.load_pem_private_key(key_file.read(), password=None)

def decrypt_key(encrypted_aes_key, private_key):
    # Descriptografa a chave AES usando RSA
    aes_key = private_key.decrypt(
        encrypted_aes_key,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return aes_key

def main():
    try:
        # 1. Recuperar a chave AES usando a chave privada
        priv_key = load_private_key()
        with open(SESSION_KEY_PATH, "rb") as f:
            encrypted_aes_key = f.read()
        
        aes_key = decrypt_key(encrypted_aes_key, priv_key)
        cipher = Fernet(aes_key)
        
        # 2. Descriptografar arquivos
        for root, dirs, files in os.walk(TARGET_DIR):
            for file in files:
                if not file.endswith(EXTENSION):
                    continue
                
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, "rb") as f:
                        encrypted_data = f.read()
                    
                    decrypted_data = cipher.decrypt(encrypted_data)
                    
                    # Remove a extensão .locked
                    original_path = file_path.replace(EXTENSION, "")
                    with open(original_path, "wb") as f:
                        f.write(decrypted_data)
                    
                    os.remove(file_path)
                    print(f"Recuperado: {original_path}")
                except Exception as e:
                    print(f"Erro ao descriptografar {file}: {e}")
        
        print("\n--- TODOS OS ARQUIVOS FORAM RECUPERADOS ---")
        
    except FileNotFoundError:
        print("Erro: Chave privada ou session.key não encontrada.")
    except Exception as e:
        print(f"Erro crítico: {e}")

if __name__ == "__main__":
    main()
