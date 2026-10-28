# Ransomware Simulador - Projeto Educacional

![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Educational](https://img.shields.io/badge/projeto-educacional-orange)

Este é um projeto **EDUCACIONAL** desenvolvido para fins de estudo em cibersegurança. O objetivo é entender como funcionam os ransomwares, seus mecanismos de criptografia e como implementar medidas de segurança para se proteger contra tais ataques.

**⚠️ AVISO IMPORTANTE:**
Este código é apenas para fins educacionais e de aprendizado. NUNCA use este software para fins maliciosos. O uso indevido deste software pode resultar em consequências legais graves.

## 📋 Sobre o Projeto

Este projeto simula o funcionamento de um ransomware com as seguintes características:

- **Encrypter**: Criptografa arquivos em um diretório específico
- **Decrypter**: Descriptografa arquivos previamente criptografados
- **Educacional**: Inclui logs detalhados e confirmações para evitar uso acidental

## 🎯 Objetivos de Aprendizagem

Ao trabalhar com este projeto, você aprenderá:

1. **Criptografia Simétrica**: Uso do algoritmo Fernet (AES-128 em modo CBC)
2. **Derivação de Chaves**: PBKDF2 para gerar chaves seguras a partir de senhas
3. **Manipulação de Arquivos**: Leitura e escrita de arquivos binários em Python
4. **Segurança Cibernética**: Entendimento de como ransomwares funcionam
5. **Boas Práticas**: Implementação de medidas de segurança em software

## 🚀 Como Usar

### Pré-requisitos

```bash
# Instalar dependências
pip install cryptography
```

### Estrutura do Projeto

```
ransomware_simulador/
├── encrypter.py      # Script para criptografar arquivos
├── decrypter.py      # Script para descriptografar arquivos
├── README.md         # Documentação do projeto
├── requirements.txt  # Dependências do projeto
└── test_files/       # Diretório para testes (criar manualmente)
```

### Criptografando Arquivos

1. Primeiro, crie um diretório de teste:

```bash
mkdir test_files
echo "Conteúdo de teste" > test_files/documento.txt
echo "Outro arquivo" > test_files/relatorio.pdf.txt
```

2. Execute o encrypter:

```bash
python encrypter.py ./test_files minha_senha_secreta
```

O script irá:
- Pedir confirmação (digite "CONFIRMAR")
- Criptografar arquivos com extensões específicas (.txt, .pdf, etc.)
- Gerar arquivos `.encrypted` e `.key` para cada arquivo
- Salvar um arquivo `.salt.bin` no diretório

### Descriptografando Arquivos

```bash
python decrypter.py ./test_files minha_senha_secreta
```

O script irá:
- Verificar a senha
- Descriptografar todos os arquivos `.encrypted`
- Remover os arquivos temporários (.encrypted, .key, .salt.bin)
- Restaurar os arquivos originais

## 🔒 Funcionalidades de Segurança

Para evitar uso acidental ou malicioso, o projeto inclui:

1. **Confirmação explícita**: Requer digitar "CONFIRMAR" antes de criptografar
2. **Logs detalhados**: Mostra exatamente o que está acontecendo
3. **Extensões específicas**: Só criptografa tipos de arquivo predefinidos
4. **Mensagens educacionais**: Avisos claros sobre o uso apropriado
5. **Chaves salvas**: Permite recuperação com a senha correta

## 🛡️ Mecanismos de Criptografia

### Algoritmos Utilizados

1. **Fernet (AES-128-CBC)**: Para criptografia dos arquivos
2. **PBKDF2-HMAC-SHA256**: Para derivação de chaves a partir de senhas
3. **Salt aleatório**: 16 bytes para prevenir ataques de rainbow table

### Fluxo de Criptografia

```
Senha → PBKDF2 + Salt → Chave Mestre
Arquivo → Fernet.generate_key() → Chave de Arquivo
Arquivo + Chave de Arquivo → Arquivo.encrypted
Chave de Arquivo → Arquivo.key
```

### Fluxo de Descriptografia

```
Senha + Salt → PBKDF2 → Chave Mestre
Arquivo.key → Chave de Arquivo
Arquivo.encrypted + Chave de Arquivo → Arquivo Original
```

## 📚 Conceitos Técnicos Aprendidos

### 1. Criptografia Simétrica
- Uso do algoritmo AES através da biblioteca cryptography
- Modo de operação CBC (Cipher Block Chaining)
- Padding PKCS7

### 2. Derivação de Chaves
- PBKDF2 (Password-Based Key Derivation Function 2)
- Uso de salt para prevenir ataques de dicionário
- 100.000 iterações para tornar ataques de força bruta inviáveis

### 3. Manipulação de Arquivos Binários
- Leitura e escrita em modo binário (`'rb'` e `'wb'`)
- Criação de arquivos temporários
- Limpeza segura de arquivos após uso

### 4. Segurança em Python
- Tratamento de exceções
- Validação de entrada
- Confirmação de ações destrutivas

## ⚠️ Considerações Éticas e Legais

1. **Uso Educacional Apenas**: Este código deve ser usado apenas para aprendizado
2. **Consentimento**: Só teste em seus próprios arquivos ou com permissão explícita
3. **Responsabilidade**: Você é responsável pelo uso que faz deste software
4. **Legalidade**: Em muitos países, usar ransomware é crime

## 🔍 Como se Proteger de Ransomwares Reais

1. **Backups regulares**: Mantenha cópias offline dos seus arquivos importantes
2. **Atualizações**: Mantenha sistema operacional e software atualizados
3. **Antivírus**: Use software de segurança confiável
4. **Cautela com emails**: Não abra anexos de remetentes desconhecidos
5. **Educação**: Aprenda sobre phishing e engenharia social

## 🧪 Testando o Projeto

### Cenário de Teste Seguro

1. Crie uma máquina virtual isolada
2. Use apenas arquivos de teste sem valor
3. Documente todos os passos realizados
4. Limpe todos os arquivos após os testes

### Comandos de Teste

```bash
# Preparar ambiente de teste
mkdir -p test_env
cd test_env

# Criar arquivos de teste
echo "Teste 1" > arquivo1.txt
echo "Teste 2" > arquivo2.pdf.txt
cp /dev/null arquivo_vazio.txt

# Testar criptografia
python ../encrypter.py ./ minha_senha

# Verificar resultados
ls -la *.encrypted *.key

# Testar descriptografia
python ../decrypter.py ./ minha_senha

# Verificar se arquivos foram restaurados
cat arquivo1.txt
```

## 📁 Estrutura de Arquivos Gerados

Durante a operação, são criados:

```
arquivo.txt              # Original
arquivo.txt.encrypted    # Versão criptografada
arquivo.txt.key          # Chave de criptografia
.salt.bin                # Salt para derivação de chaves
```

## 🐛 Solução de Problemas

### Erro: "No module named 'cryptography'"
```bash
pip install cryptography
```

### Erro: "Senha incorreta"
- Verifique se está usando a mesma senha usada na criptografia
- O salt (.salt.bin) deve ser o mesmo

### Erro: "Arquivo de chave não encontrado"
- Certifique-se de que o arquivo `.key` existe
- Não delete arquivos `.key` manualmente

## 🤝 Contribuindo

Este é um projeto educacional. Se quiser contribuir:

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📄 Licença

Distribuído sob a licença MIT. Veja `LICENSE` para mais informações.

## 🙏 Agradecimentos

- [Cryptography.io](https://cryptography.io/) - Biblioteca Python para criptografia
- [DIO](https://web.dio.me/) - Plataforma de aprendizagem
- Comunidade de segurança cibernética

## 📞 Contato

Este projeto é apenas educacional. Para questões sobre segurança cibernética, consulte profissionais certificados.

---

**⚠️ LEMBRETE FINAL:** Este software é apenas para fins educacionais. O uso malicioso de ransomware é crime e causa danos reais a pessoas e organizações. Use este conhecimento para se proteger e proteger outros, nunca para causar danos.