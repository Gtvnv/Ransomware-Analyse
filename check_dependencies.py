#!/usr/bin/env python3
"""
Verifica se todas as dependências estão instaladas corretamente.
"""

import sys
import subprocess

def check_python_version():
    """Verifica a versão do Python."""
    version = sys.version_info
    print(f"Python versão: {version.major}.{version.minor}.{version.micro}")
    
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print("❌ Versão do Python muito antiga. Necessário Python 3.8+")
        return False
    else:
        print("✅ Versão do Python OK")
        return True

def check_cryptography():
    """Verifica se a biblioteca cryptography está instalada."""
    try:
        from cryptography.fernet import Fernet
        from cryptography.hazmat.primitives import hashes
        from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2
        
        # Testar funcionalidades básicas
        key = Fernet.generate_key()
        fernet = Fernet(key)
        test_data = b"Teste de criptografia"
        encrypted = fernet.encrypt(test_data)
        decrypted = fernet.decrypt(encrypted)
        
        if decrypted == test_data:
            print("✅ Biblioteca cryptography instalada e funcionando")
            return True
        else:
            print("❌ Biblioteca cryptography com problemas")
            return False
            
    except ImportError as e:
        print(f"❌ Biblioteca cryptography não encontrada: {e}")
        print("Instale com: pip install cryptography")
        return False
    except Exception as e:
        print(f"❌ Erro ao testar cryptography: {e}")
        return False

def check_requirements_file():
    """Verifica se o arquivo requirements.txt existe."""
    try:
        with open('requirements.txt', 'r') as f:
            content = f.read().strip()
            if content:
                print(f"✅ Arquivo requirements.txt encontrado:")
                print(f"   Conteúdo: {content}")
                return True
            else:
                print("❌ Arquivo requirements.txt vazio")
                return False
    except FileNotFoundError:
        print("❌ Arquivo requirements.txt não encontrado")
        return False

def check_main_scripts():
    """Verifica se os scripts principais existem."""
    scripts = ['encrypter.py', 'decrypter.py']
    all_exist = True
    
    for script in scripts:
        try:
            with open(script, 'r') as f:
                first_line = f.readline()
                if 'python' in first_line.lower() or '#!/' in first_line:
                    print(f"✅ {script} encontrado e parece ser um script Python")
                else:
                    print(f"⚠️  {script} encontrado mas não parece ser um script Python")
                    all_exist = False
        except FileNotFoundError:
            print(f"❌ {script} não encontrado")
            all_exist = False
    
    return all_exist

def check_example_files():
    """Verifica se os arquivos de exemplo existem."""
    import os
    
    example_dir = 'exemplo'
    if os.path.exists(example_dir) and os.path.isdir(example_dir):
        files = os.listdir(example_dir)
        if len(files) >= 2:
            print(f"✅ Diretório de exemplo encontrado com {len(files)} arquivos")
            return True
        else:
            print(f"⚠️  Diretório de exemplo encontrado mas com poucos arquivos ({len(files)})")
            return False
    else:
        print("⚠️  Diretório de exemplo não encontrado")
        return False

def main():
    """Função principal."""
    print("=" * 60)
    print("VERIFICAÇÃO DE DEPENDÊNCIAS - RANSOMWARE SIMULADOR")
    print("=" * 60)
    
    checks = [
        ("Versão do Python", check_python_version),
        ("Biblioteca cryptography", check_cryptography),
        ("Arquivo requirements.txt", check_requirements_file),
        ("Scripts principais", check_main_scripts),
        ("Arquivos de exemplo", check_example_files),
    ]
    
    results = []
    
    for check_name, check_function in checks:
        print(f"\n📋 Verificando: {check_name}")
        print("-" * 40)
        try:
            result = check_function()
            results.append((check_name, result))
        except Exception as e:
            print(f"❌ Erro durante verificação: {e}")
            results.append((check_name, False))
    
    print("\n" + "=" * 60)
    print("RESUMO DA VERIFICAÇÃO")
    print("=" * 60)
    
    success_count = sum(1 for _, result in results if result)
    total_count = len(results)
    
    for check_name, result in results:
        status = "✅" if result else "❌"
        print(f"{status} {check_name}")
    
    print(f"\nTotal: {success_count}/{total_count} verificações passaram")
    
    if success_count == total_count:
        print("\n🎉 TUDO PRONTO! Você pode começar a usar o projeto.")
        print("\nComandos para testar:")
        print("1. python encrypter.py ./exemplo senha_teste")
        print("2. python decrypter.py ./exemplo senha_teste")
        print("3. python test_script.py (teste completo)")
    elif success_count >= 3:
        print("\n⚠️  ALGUMAS VERIFICAÇÕES FALHARAM, mas o projeto pode funcionar.")
        print("   Verifique as mensagens de erro acima.")
    else:
        print("\n❌ MUITAS VERIFICAÇÕES FALHARAM. O projeto pode não funcionar.")
        print("   Siga as instruções no README.md para instalação.")

if __name__ == "__main__":
    main()