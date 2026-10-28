# Desafio DIO - Ransomware em Python

## 📝 Descrição do Desafio

Este projeto foi desenvolvido como parte do desafio da Digital Innovation One (DIO) sobre cibersegurança. O objetivo é implementar um ransomware simulador para fins educacionais, demonstrando conceitos de criptografia e segurança.

## 🎯 Objetivos Alcançados

### ✅ Requisitos do Desafio

1. **Arquivo `encrypter.py`**: ✅ Implementado
   - Criptografa arquivos em um diretório
   - Usa criptografia simétrica (Fernet/AES-128)
   - Inclui confirmação de segurança
   - Logs detalhados da operação

2. **Arquivo `decrypter.py`**: ✅ Implementado
   - Descriptografa arquivos previamente criptografados
   - Verifica senha correta
   - Restaura arquivos originais
   - Limpa arquivos temporários

3. **Documentação Completa**: ✅ Implementada
   - README.md com explicações detalhadas
   - Instruções de instalação e uso
   - Considerações éticas e legais
   - Exemplos práticos

## 🧠 Conceitos Aprendidos

### Criptografia
- **Fernet**: Algoritmo de criptografia simétrica baseado em AES-128
- **PBKDF2**: Derivação de chaves a partir de senhas
- **Salt**: Valor aleatório para prevenir ataques de rainbow table
- **Modo CBC**: Cipher Block Chaining para criptografia de blocos

### Segurança
- Confirmação explícita antes de operações destrutivas
- Validação de entrada e tratamento de exceções
- Logs detalhados para transparência
- Mensagens educacionais sobre uso ético

### Programação Python
- Manipulação de arquivos binários
- Uso da biblioteca `cryptography`
- Argumentos de linha de comando
- Percorrimento recursivo de diretórios

## 🚀 Como Entregar o Desafio

### 1. Criar Repositório no GitHub

```bash
# Inicializar repositório Git
git init
git add .
git commit -m "Desafio DIO: Ransomware Simulador em Python"
git branch -M main
```

### 2. Criar Repositório no GitHub.com
- Acesse https://github.com
- Clique em "New repository"
- Nome: `ransomware-simulador-dio`
- Descrição: "Projeto educacional de ransomware em Python para o desafio DIO"
- Público
- Não inicializar com README (já temos)

### 3. Fazer Push
```bash
git remote add origin https://github.com/seu-usuario/ransomware-simulador-dio.git
git push -u origin main
```

### 4. Adicionar Screenshots (Opcional)
Crie uma pasta `screenshots/` com:
1. Execução do encrypter
2. Execução do decrypter
3. Listagem de arquivos antes/depois

### 5. Entregar na Plataforma DIO
1. Acesse o desafio na DIO
2. Clique em "Entregar Projeto"
3. Cole o link do repositório
4. Adicione uma breve descrição

## 📊 Avaliação do Projeto

### Pontos Fortes
1. **Código bem documentado**: Comentários explicativos em todas as funções
2. **Medidas de segurança**: Confirmações e logs para prevenir uso acidental
3. **Modularidade**: Funções separadas para criptografia/descriptografia
4. **Testabilidade**: Script de teste incluído
5. **Documentação completa**: README, INSTALL, e exemplos

### Melhorias Futuras (Extras)
1. Interface gráfica simples
2. Suporte a mais algoritmos de criptografia
3. Modo de operação em rede (simulação)
4. Análise de performance
5. Testes unitários automatizados

## ⚠️ Advertências Importantes

### PARA ESTUDO APENAS
Este projeto foi desenvolvido exclusivamente para fins educacionais em um ambiente controlado. O conhecimento aqui adquirido deve ser usado para:

- Entender como ransomwares funcionam
- Aprender técnicas de defesa
- Desenvolver ferramentas de proteção
- Contribuir para a segurança cibernética

### NUNCA PARA:
- Ataques reais
- Extorsão
- Danos a sistemas de terceiros
- Qualquer atividade ilegal

## 🎓 Certificação de Conclusão

Ao completar este projeto, você demonstrou habilidades em:

- [x] Criptografia simétrica em Python
- [x] Manipulação segura de arquivos
- [x] Boas práticas de programação
- [x] Documentação de projetos
- [x] Ética em segurança cibernética
- [x] Uso do GitHub para versionamento

## 🤝 Contribuições para a Comunidade

Este projeto pode ser usado como:

1. **Material de estudo** para cursos de cibersegurança
2. **Base para pesquisas** sobre técnicas de proteção
3. **Exemplo didático** de implementação segura
4. **Template** para outros projetos educacionais

## 📞 Suporte e Dúvidas

Para dúvidas sobre o projeto:

1. Consulte a documentação (`README.md` e `INSTALL.md`)
2. Revise as videoaulas do curso DIO
3. Pesquise na comunidade de cibersegurança
4. Consulte profissionais certificados para questões avançadas

---

**Boa sorte no desafio! 🚀**

*Lembre-se: Com grandes poderes vêm grandes responsabilidades. Use este conhecimento para o bem.*