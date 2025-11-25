
# 🏥 Sistema de Gestão Hospitalar (SGH) - API

📌 Descrição Geral

O Sistema de Gestão Hospitalar (SGH) é uma plataforma desenvolvida para organizar e automatizar operações essenciais de um hospital, incluindo gestão de usuários, agendamentos, consultas, prontuários, exames, farmácia, pagamentos e comunicação interna.

O sistema foi projetado para suportar múltiplos perfis de acesso, garantindo segurança, eficiência e rastreabilidade de todas as ações realizadas.

---

## 🚀 Tecnologias

* Python 3.x
* Django 5.x
* Django REST Framework
* drf-yasg (Swagger / Redoc)
* SQLite/MySQL/PostgreSQL (qualquer um pode ser configurado)

---

## 📦 Instalação

### 1. Clonar o repositório

```bash
git clone https://github.com/seu-repo/sgh-api.git
cd sgh-api
```

### 2. Criar e ativar o ambiente virtual

```bash
python -m venv venv
source venv/bin/activate    # Linux / macOS
venv\Scripts\activate       # Windows
```

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

### 4. Aplicar migrações

```bash
python manage.py migrate
```

### 5. Criar usuário administrador

```bash
python manage.py createsuperuser
```

### 6. Rodar o servidor

```bash
python manage.py runserver
```

---

## 📚 Documentação da API

As rotas padrão do projeto:

```
/api/v1/doc/         → Swagger UI  
/api/v1/doc/.json    → Schema JSON  
/api/v1/redoc/       → Redoc  
/api/v1/auth/        → Autenticação básica do DRF  
/api/v1/             → Endpoints da aplicação  
/admin/              → Área administrativa Django  
```
---

## 📌 Módulos Implementados

* **Gestão de Usuários**
  Cadastro e autenticação de pacientes, médicos e funcionários.

* **Agendamentos (Online e Presenciais)**
  Controle de disponibilidade, notificações e prevenção de conflitos de horários.

* **Consultas**
  Lista diária, atendimentos e teleconsultas.

* **Prontuários**
  Histórico clínico com acesso restrito por perfil.

* **Exames**
  Solicitação, anexos e notificação de resultados.

* **Farmácia**
  Estoque, alertas de baixo nível e registro de saídas.

* **Pagamentos**
  Registro de pagamentos, faturas e recibos.

* **Comunicação**
  Envio de notificações internas, e-mail ou SMS.

---

## ✔️ Contribuição

Pull requests são bem-vindos.
Antes de enviar contribuições: crie uma branch e abra um PR com sua proposta.
«