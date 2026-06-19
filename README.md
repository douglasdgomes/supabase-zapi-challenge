# Supabase + Z-API Challenge

Projeto desenvolvido para ler contatos cadastrados no Supabase e enviar uma mensagem personalizada via Z-API utilizando WhatsApp

## Tecnologias

* Python
* Supabase
* Z-API

## Configuração

### 1. Criar as contas no Supabase e Z-API

Criar uma conta no Supabase e obter a SUPABASE_URL e SUPABASE_KEY.
Criar uma conta na Z-API, criar uma instância, conectar o WhatsApp e obter o ZAPI_INSTANCE_ID, ZAPI_TOKEN e ZAPI_CLIENT_TOKEN.

### 2. Criar o arquivo `.env`

```env
SUPABASE_URL=
SUPABASE_KEY=

ZAPI_INSTANCE_ID=
ZAPI_TOKEN=
ZAPI_CLIENT_TOKEN=

```

### 3. Criar a tabela no Supabase e inserir contatos de exemplo

```sql
CREATE TABLE contacts (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name TEXT NOT NULL,
    phone TEXT NOT NULL
);

INSERT INTO contacts (name, phone) 
VALUES 
('Contato 1', '5531999999999'), 
('Contado 2', '5531888888888'), 
('Contato 3', '5531777777777');

```

### 4. Instalar dependências

```bash
pip install -r requirements.txt
```

### 5. Executar

```bash
python main.py
```

## Funcionalidades

* Busca contatos no Supabase
* Limita a quantidade de contatos processados
* Envia mensagens personalizadas via Z-API
* Valida números de telefone
* Possui logs e tratamento de erros