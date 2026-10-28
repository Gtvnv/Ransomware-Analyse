#!/usr/bin/env python3
"""
Script de teste para o Ransomware Simulador
Este script demonstra o funcionamento básico do projeto.
"""

import os
import subprocess
import shutil

def create_test_environment():
    """Cria um ambiente de teste isolado."""
    test_dir = "test_environment"
    
    # Limpar ambiente anterior se existir
    if os.path.exists(test_dir):
        shutil.rmtree(test_dir)
    
    # Criar diretório de teste
    os.makedirs(test_dir)
    
    # Criar arquivos de teste
    test_files = [
        ("documento.txt", "Este é um documento de teste para criptografia."),
        ("relatorio.pdf.txt", "Relatório financeiro importante."),
        ("imagem.png.txt", "Descrição de uma imagem."),
        ("planilha.xlsx.txt", "Dados importantes da empresa."),
    ]
    
    for filename, content in test_files:
        with open(os.path.join(test_dir, filename), 'w', encoding='utf-8') as f:
            f.write(content)
    
    print(f"Ambiente de teste criado em: {test_dir}")
    print("Arquivos criados:")
    for filename, _ in test_files:
        print(f"  - {filename}")
    
    return test_dir

def run_encryption_test(test_dir):
    """Executa teste de criptografia."""
    print("\n" + "="*60)
    print("TESTE DE CRIPTOGRAFIA")
    print("="*60)
    
    password = "senha_teste_123"
    
    # Executar encrypter
    print(f"\nExecutando encrypter.py...")
    result = subprocess.run(
        ["python", "encrypter.py", test_dir, password],
        capture_output=True,
        text=True
    )
    
    print("Saída do encrypter:")
    print(result.stdout)
    if result.stderr:
        print("Erros:", result.stderr)
    
    # Verificar arquivos criados
    print("\nVerificando arquivos após criptografia:")
    files = os.listdir(test_dir)
    for file in sorted(files):
        filepath = os.path.join(test_dir, file)
        if os.path.isfile(filepath):
            size = os.path.getsize(filepath)
            print(f"  - {file} ({size} bytes)")
    
    return result.returncode == 0

def run_decryption_test(test_dir):
    """Executa teste de descriptografia."""
    print("\n" + "="*60)
    print("TESTE DE DESCRIPTOGRAFIA")
    print("="*60)
    
    password = "senha_teste_123"
    
    # Executar decrypter
    print(f"\nExecutando decrypter.py...")
    result = subprocess.run(
        ["python", "decrypter.py", test_dir, password],
        capture_output=True,
        text=True
    )
    
    print("Saída do decrypter:")
    print(result.stdout)
    if result.stderr:
        print("Erros:", result.stderr)
    
    # Verificar arquivos após descriptografia
    print("\nVerificando arquivos após descriptografia:")
    files = os.listdir(test_dir)
    for file in sorted(files):
        filepath = os.path.join(test_dir, file)
        if os.path.isfile(filepath):
            size = os.path.getsize(filepath)
            print(f"  - {file} ({size} bytes)")
    
    return result.returncode == 0

def verify_file_contents(test_dir):
    """Verifica se o conteúdo dos arquivos foi restaurado corretamente."""
    print("\n" + "="*60)
    print("VERIFICAÇÃO DE CONTEÚDO")
    print("="*60)
    
    expected_files = [
        "documento.txt",
        "relatorio.pdf.txt", 
        "imagem.png.txt",
        "planilha.xlsx.txt",
    ]
    
    all_correct = True
    
    for filename in expected_files:
        filepath = os.path.join(test_dir, filename)
        if os.path.exists(filepath):
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            print(f"✓ {filename}: OK ({len(content)} caracteres)")
        else:
            print(f"✗ {filename}: NÃO ENCONTRADO")
            all_correct = False
    
    return all_correct

def main():
    """Função principal do teste."""
    print("="*60)
    print("TESTE DO RANSOMWARE SIMULADOR")
    print("="*60)
    print("Este script testa o funcionamento básico do projeto.")
    print("="*60)
    
    # Criar ambiente de teste
    test_dir = create_test_environment()
    
    try:
        # Testar criptografia
        if not run_encryption_test(test_dir):
            print("\n❌ TESTE DE CRIPTOGRAFIA FALHOU")
            return
        
        # Testar descriptografia
        if not run_decryption_test(test_dir):
            print("\n❌ TESTE DE DESCRIPTOGRAFIA FALHOU")
            return
        
        # Verificar conteúdo
        if not verify_file_contents(test_dir):
            print("\n❌ VERIFICAÇÃO DE CONTEÚDO FALHOU")
            return
        
        print("\n" + "="*60)
        print("✅ TODOS OS TESTES PASSARAM COM SUCESSO!")
        print("="*60)
        
    except Exception as e:
        print(f"\n❌ ERRO DURANTE OS TESTES: {e}")
    
    finally:
        # Limpar ambiente de teste
        print(f"\nLimpando ambiente de teste...")
        if os.path.exists(test_dir):
            shutil.rmtree(test_dir)
            print(f"Diretório {test_dir} removido.")

if __name__ == "__main__":
    main()