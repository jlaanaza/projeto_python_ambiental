### 1. Instalar Dependências

Certifique-se de ter o Python instalado. Instale as dependências necessárias usando o `pip`:

```bash
pip install flask
```

### 2. Inicializar o Banco de Dados

Execute o script para criar as tabelas no banco de dados:

```python
from banco.DatabaseConnection import inicializar_banco
inicializar_banco()
```

## Endpoints da API

### Usuários

- **Criar Usuário**: `POST /usuarios`
  - **Body**: `{ "nome": "Lucas", "cpf_cnpj": "12345678900", "tipo": "colaborador", "senha": "senha" }`

### Colaboradores

- **Criar Colaborador**: `POST /colaboradores`
  - **Body**: `{ "usuario_id": 1, "nome_colaborador": "João" }`
- **Listar Colaboradores**: `GET /colaboradores`
- **Obter Colaborador**: `GET /colaboradores/<id>`
- **Atualizar Colaborador**: `PUT /colaboradores/<id>`
  - **Body**: `{ "nome_colaborador": "João Atualizado" }`
- **Deletar Colaborador**: `DELETE /colaboradores/<id>`

### Beneficiários

- **Criar Beneficiário**: `POST /beneficiarios`
  - **Body**: `{ "usuario_id": 1, "nome_beneficiario": "Maria" }`
- **Listar Beneficiários**: `GET /beneficiarios`
- **Obter Beneficiário**: `GET /beneficiarios/<id>`

### Alimentos

- **Criar Alimento**: `POST /alimentos`
  - **Body**: `{ "nome": "Arroz", "quantidade": 10, "perecivel": true, "data_validade": "2024-12-31", "colaborador_id": 1, "endereco_id": 1 }`
- **Listar Alimentos**: `GET /alimentos`
- **Obter Alimento**: `GET /alimentos/<id>`

### Endereços

- **Criar Endereço**: `POST /enderecos`
  - **Body**: `{ "logradouro": "Rua das Flores", "cidade": "Nazaré da Mata", "estado": "PE", "cep": "55800-000" }`
- **Listar Endereços**: `GET /enderecos`
- **Obter Endereço**: `GET /enderecos/<id>`

## Executando o Projeto

1. **Rodar a Aplicação Flask**:

    ```bash
    python app.py
    ```

   O servidor Flask será iniciado em `http://localhost:5000`.

2. **Testar a API**:

   Utilize ferramentas como [Postman](https://www.postman.com/) ou [cURL](https://curl.se/) para testar os endpoints da API.

   Exemplo de cURL para criar um alimento:

    ```bash
    curl --location 'http://localhost:5000/alimentos' \
    --header 'Content-Type: application/json' \
    --data '{
        "nome": "Arroz",
        "quantidade": 10,
        "perecivel": true,
        "data_validade": "2024-12-31",
        "colaborador_id": 1,
        "endereco_id": 1
    }'
    ```

## Estrutura do Código

- **Controller**: Lida com as requisições HTTP e interage com os serviços.
- **Service**: Contém a lógica de negócio e realiza operações no banco de dados.
- **Database Connection**: Gerencia a conexão e operações no banco de dados SQLite.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para enviar pull requests ou abrir issues para melhorias.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

```