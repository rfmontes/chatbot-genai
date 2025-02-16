# 📚 Chatbot com Gemini API

Este é um chatbot baseado na API **Gemini** do Google, projetado para responder perguntas de forma dinâmica. Ele busca respostas de um arquivo **JSON** com perguntas pré-definidas e, caso não encontre, utiliza a IA do Gemini para fornecer uma resposta.

---

## 🚀 Funcionalidades

✅ **Responde perguntas pré-cadastradas** com base no arquivo JSON.  
✅ **Interage com a API Gemini** caso a resposta não esteja no JSON.  
✅ **Histórico de conversa** mantido durante a sessão (Somente na versão Terminal).  
✅ **Versão terminal e versão web**.

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**
- **Google Gemini API**
- **Dotenv** (para gerenciar variáveis de ambiente)
- **JSON** (para armazenar perguntas e respostas)

---

## 📂 Estrutura do Projeto (Versão Terminal)

```
📁 chatbot-genai/
├── 📄 app.py                # Código da aplicação Flask
├── 📄 chatbot.py            # Código principal do chatbot
├── 📄 perguntas_escolares_com_respostas.json  # Base de perguntas e respostas
├── 📄 requirements.txt      # Dependências do projeto
├── 📄 .env.example          # Exemplo do arquivo de variáveis de ambiente
├── 📂 templates/            # Arquivos HTML para a interface web
│   ├── 📄 index.html        # Página principal
├── 📄 README.md             # Documentação do projeto
```

---

## 🔧 Configuração e Execução

### 1️⃣ Clonar o Repositório

```bash
git clone https://github.com/rfmontes/chatbot-genai.git
cd chatbot-genai
```

### 2️⃣ Criar um Ambiente Virtual (Opcional, mas Recomendado)

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate  # Windows
```

### 3️⃣ Instalar Dependências

```bash
pip install -r requirements.txt
```

### 4️⃣ Configurar Variáveis de Ambiente

Crie um arquivo `.env` com a chave da API do Gemini:

```ini
GEMINI_API_KEY=SUA_CHAVE_AQUI
```

Você pode usar o arquivo **.env.example** como referência.

### 5️⃣ Executar o Chatbot

## (Modo Web)

```bash
python app.py
```

## (Modo Terminal)

```bash
python chatbot.py
```

---

## 📝 Exemplo de Uso

```
Faça uma pergunta (ou digite 'sair' para encerrar): O que é um substantivo?
Substantivo é a classe de palavras que dá nome aos seres, objetos, lugares, sentimentos, etc.
```

Caso a pergunta não esteja no JSON, o chatbot usará a API do Gemini para responder.

---

## 🤝 Contribuições

Sinta-se à vontade para contribuir! Abra uma **issue** ou envie um **pull request**. 😊
