# Supabase + Z-API Challenge

Projeto desenvolvido para ler contatos cadastrados no Supabase e enviar uma mensagem personalizada via Z-API utilizando WhatsApp

## Tecnologias

* Python
* Supabase
* Z-API

## Configuração

### 1. Criar o arquivo `.env`

```env
SUPABASE_URL=
SUPABASE_KEY=

ZAPI_INSTANCE_ID=
ZAPI_TOKEN=
ZAPI_CLIENT_TOKEN=

```

### 2. Criar a tabela no Supabase

```sql
CREATE TABLE contacts (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name TEXT NOT NULL,
    phone TEXT NOT NULL
);
```

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

### 4. Executar

```bash
python main.py
```

## Funcionalidades

* Busca contatos no Supabase
* Limita a quantidade de contatos processados
* Envia mensagens personalizadas via Z-API
* Valida números de telefone
* Possui logs e tratamento de erros