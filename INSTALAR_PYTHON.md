# Instalação do Python - Guia para Windows

## 📥 Baixar e Instalar Python

### Método 1: Microsoft Store (Recomendado)

1. Abra a **Microsoft Store**
2. Pesquise por "Python"
3. Instale a versão mais recente (Python 3.12+)
4. Após instalar, reinicie o terminal

### Método 2: Site Oficial

1. Acesse: https://www.python.org/downloads/
2. Baixe o instalador para Windows
3. Execute o instalador
4. **IMPORTANTE**: Marque a opção "Add Python to PATH"
5. Clique em "Install Now"

## 🔧 Verificar Instalação

Após instalar, abra o PowerShell (terminal) e execute:

```powershell
# Verificar versão do Python
python --version
# ou
python3 --version

# Verificar pip (gerenciador de pacotes)
pip --version
```

Se aparecer algo como `Python 3.12.0`, a instalação foi bem-sucedida.

## 📦 Instalar Dependências do Projeto

Com o Python instalado, instale a biblioteca necessária:

```powershell
pip install cryptography
```

## 🚀 Testar Instalação

Execute o script de verificação:

```powershell
python check_dependencies.py
```

## ❓ Solução de Problemas

### "Python não é reconhecido"

Se aparecer o erro "Python não é reconhecido...", siga estes passos:

1. **Verificar se Python está no PATH**:
   ```powershell
   Get-Command python -ErrorAction SilentlyContinue
   ```

2. **Adicionar manualmente ao PATH**:
   - Pressione `Win + X` e selecione "Sistema"
   - Clique em "Configurações avançadas do sistema"
   - Clique em "Variáveis de ambiente"
   - Em "Variáveis do sistema", selecione "Path" e clique em "Editar"
   - Adicione o caminho do Python (geralmente `C:\Users\SeuUsuario\AppData\Local\Programs\Python\Python312\`)
   - Adicione também o caminho do Scripts (`C:\Users\SeuUsuario\AppData\Local\Programs\Python\Python312\Scripts\`)
   - Reinicie o terminal

### "pip não encontrado"

```powershell
# Tentar com py (instalador oficial do Windows)
py -m pip install cryptography

# Ou reinstalar Python marcando "Add Python to PATH"
```

### Erro de permissão

```powershell
# Executar como administrador
Start-Process PowerShell -Verb RunAs

# Ou usar --user
pip install --user cryptography
```

## 📚 Recursos Adicionais

- [Documentação Oficial do Python](https://docs.python.org/3/)
- [Tutorial Python para Iniciantes](https://docs.python.org/3/tutorial/)
- [Fórum da Comunidade Python](https://discuss.python.org/)

## 🎯 Próximos Passos

Após instalar o Python e as dependências:

1. Teste o projeto: `python test_script.py`
2. Experimente com seus próprios arquivos
3. Estude o código para entender como funciona
4. Documente seu aprendizado