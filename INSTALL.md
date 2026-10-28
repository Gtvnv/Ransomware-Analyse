# Instalação e Uso Rápido

## 🚀 Começando Rápido

### 1. Instalar Dependências

```bash
pip install cryptography
```

### 2. Criar Arquivos de Teste

```bash
# Criar diretório de teste
mkdir meus_arquivos

# Criar alguns arquivos de exemplo
echo "Meu documento importante" > meus_arquivos/documento1.txt
echo "Relatório confidencial" > meus_arquivos/relatorio.pdf.txt
echo "Minhas fotos" > meus_arquivos/fotos.jpg.txt
```

### 3. Criptografar Arquivos

```bash
python encrypter.py ./meus_arquivos minha_senha_segura
```

**OBS:** Você precisará digitar "CONFIRMAR" quando solicitado.

### 4. Verificar Resultado

```bash
ls -la meus_arquivos/
```

Você verá:
- Arquivos `.encrypted` (criptografados)
- Arquivos `.key` (chaves)
- Arquivo `.salt.bin`

### 5. Descriptografar Arquivos

```bash
python decrypter.py ./meus_arquivos minha_senha_segura
```

### 6. Verificar se Arquivos Foram Restaurados

```bash
ls -la meus_arquivos/
cat meus_arquivos/documento1.txt
```

## 📋 Comandos Úteis

### Teste Completo Automático

```bash
python test_script.py
```

### Apenas Verificar Instalação

```bash
python -c "from cryptography.fernet import Fernet; print('Cryptography instalado corretamente!')"
```

## 🐛 Solução de Problemas Comuns

### Erro: "ModuleNotFoundError: No module named 'cryptography'"

```bash
# Windows
pip install cryptography

# Linux/Mac
pip3 install cryptography
```

### Erro: "Permission denied"

```bash
# No Windows, execute como administrador ou em diretório com permissão
# Ou mude para um diretório onde você tem permissão de escrita
```

### O script não pede confirmação

Verifique se está executando o encrypter.py corretamente:

```bash
python encrypter.py --help
```

## 🔧 Configuração Avançada

### Alterar Extensões de Arquivo

No arquivo `encrypter.py`, modifique a lista `extensions`:

```python
extensions = ['.txt', '.pdf', '.docx', '.jpg', '.png', '.xlsx', '.zip', '.rar']
```

### Usar em Modo Silencioso (para testes)

Modifique o encrypter.py para pular a confirmação (APENAS PARA TESTES):

```python
# Comente esta parte:
# confirm = input("Digite 'CONFIRMAR' para continuar: ")
# if confirm.upper() != "CONFIRMAR":
#     print("Operação cancelada.")
#     return
```

## 📝 Notas Importantes

1. **SEMPRE teste em arquivos sem valor primeiro**
2. **Mantenha backups** dos seus arquivos importantes
3. **Lembre-se da senha** - sem ela, os arquivos ficam inacessíveis
4. **Não compartilhe as senhas** usadas nos testes

## 🎥 Demonstração em Vídeo

Para uma demonstração visual, assista às videoaulas do curso na DIO.