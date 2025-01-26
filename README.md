# API Gerenciadora de Contatos

Esta é uma API simples para gerenciamento de contatos desenvolvida com Python e Flask. Ela fornece endpoints para criar, recuperar, atualizar e deletar informações de contatos.

## Funcionalidades
- Criar um novo contato
- Listar todos os contatos
- Recuperar um contato específico por ID
- Atualizar um contato existente
- Deletar um contato

## Pré-requisitos
- Python 3.7+
- Flask instalado (`pip install flask`)

## Instalação
1. Clone este repositório ou faça o download do código-fonte.
2. Navegue até o diretório do projeto.
3. Instale as dependências necessárias:
   ```bash
   pip install flask
   ```

## Uso
1. Execute a aplicação:
   ```bash
   python app.py
   ```
2. A API estará acessível em `http://127.0.0.1:5000`.

## Endpoints

### 1. Endpoint Raiz
**GET /**
- Descrição: Exibe uma mensagem de boas-vindas para confirmar que a API está funcionando.
- Resposta:
  ```json
  {
      "message": "Welcome to the Contact Manager API!"
  }
  ```

### 2. Listar Todos os Contatos
**GET /contacts**
- Descrição: Retorna a lista de todos os contatos.
- Resposta:
  ```json
  [
      {
          "id": 1,
          "name": "John Doe",
          "email": "john.doe@example.com",
          "phone": "123456789"
      }
  ]
  ```

### 3. Criar um Novo Contato
**POST /contacts**
- Descrição: Adiciona um novo contato.
- Corpo da Requisição:
  ```json
  {
      "name": "Jane Doe",
      "email": "jane.doe@example.com",
      "phone": "987654321"
  }
  ```
- Resposta:
  ```json
  {
      "id": 2,
      "name": "Jane Doe",
      "email": "jane.doe@example.com",
      "phone": "987654321"
  }
  ```

### 4. Recuperar um Contato por ID
**GET /contacts/<int:contact_id>**
- Descrição: Retorna os detalhes de um contato específico pelo ID.
- Resposta:
  ```json
  {
      "id": 1,
      "name": "John Doe",
      "email": "john.doe@example.com",
      "phone": "123456789"
  }
  ```

### 5. Atualizar um Contato
**PUT /contacts/<int:contact_id>**
- Descrição: Atualiza os detalhes de um contato específico.
- Corpo da Requisição:
  ```json
  {
      "name": "John Smith",
      "email": "john.smith@example.com"
  }
  ```
- Resposta:
  ```json
  {
      "id": 1,
      "name": "John Smith",
      "email": "john.smith@example.com",
      "phone": "123456789"
  }
  ```

### 6. Deletar um Contato
**DELETE /contacts/<int:contact_id>**
- Descrição: Deleta um contato específico pelo ID.
- Resposta:
  ```json
  {
      "message": "Contact deleted successfully."
  }
  ```

## Notas
- Os dados são armazenados em memória e serão resetados quando a aplicação for reiniciada.
- Esta aplicação é apenas para fins de demonstração e não inclui autenticação ou armazenamento persistente.


