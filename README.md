# 📇 Agenda de Contatos

Bem-vindo! Este é um projeto de agenda de contatos desenvolvido com Django, oferecendo uma forma prática e organizada de gerenciar seus contatos.
OBS: Criado a partir de um modelo do Otávio Miranda.
---

## 📋 Sobre o Projeto

Se você tem muitos contatos no telefone e precisa procurar emails, telefones ou informações específicas, este site facilita sua vida. Com a **Agenda de Contatos**, você pode:

- Pesquisar contatos rapidamente por nome, sobrenome, email ou telefone
- Adicionar fotos e descrições personalizadas
- Organizar tudo em um só lugar com segurança

---

## 🎯 Recursos

- ✅ Adicionar e excluir contatos
- 📸 Upload de foto de perfil para cada contato
- 📝 Adicionar descrição/bio personalizada
- 🔍 Pesquisa centralizada por múltiplos critérios
- 🔐 Sistema de login seguro
- 👨‍💼 Painel administrativo

---

## 🛠️ Tecnologias Utilizadas

- **Python** 3.10+
- **Django** 4.2+
- **SQLite** (banco de dados padrão)
---

## 🚀 Como Rodar o Projeto

### Pré-requisitos

- Python 3.10 ou superior instalado
- pip (gerenciador de pacotes do Python)

### Instalação

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/agenda-contatos.git
cd agenda-contatos
```

2. Crie e ative um ambiente virtual:
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Execute as migrações do banco de dados:
```bash
python manage.py migrate
```

5. Crie um superusuário para acessar o admin:
```bash
python manage.py createsuperuser
```

6. Inicie o servidor de desenvolvimento:
```bash
python manage.py runserver
```

7. Acesse no navegador:
```
http://127.0.0.1:8000
```

---

## 📂 Estrutura do Projeto
```
agenda-contatos/
├── contacts/          # App principal de contatos
├── static/            # Arquivos CSS, JS e imagens
├── templates/         # Templates HTML
├── media/             # Upload de fotos dos contatos
├── manage.py
└── requirements.txt
```

---

## 📸 Screenshots

<img width="1406" height="729" alt="image" src="https://github.com/user-attachments/assets/c82906ce-7f6e-4dc2-bcc0-c2995ea27997" />


---


## 👤 Autor

Desenvolvido por **[Augusto César]**

- GitHub: [@Fa1kerXd](https://github.com/Fa1kerXd)
- LinkedIn: [@Augusto Cesar](https://www.linkedin.com/in/augusto-cesar-323662293/)

---

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.
