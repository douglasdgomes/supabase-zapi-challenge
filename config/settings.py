from dotenv import load_dotenv
import os

load_dotenv()

def get_required_env(name: str) -> str:
    value = os.getenv(name)

    if not value:
        raise ValueError(f"Variável de ambiente '{name}' não configurada.")

    return value

SUPABASE_URL = get_required_env(
    "SUPABASE_URL"
)

SUPABASE_KEY = get_required_env(
    "SUPABASE_KEY"
)

ZAPI_INSTANCE_ID = get_required_env(
    "ZAPI_INSTANCE_ID"
)

ZAPI_TOKEN = get_required_env(
    "ZAPI_TOKEN"
)

ZAPI_CLIENT_TOKEN = get_required_env(
    "ZAPI_CLIENT_TOKEN"
)

MAX_CONTACTS = int(
    os.getenv("MAX_CONTACTS", "3")
)

SEND_MESSAGES = (
    os.getenv("SEND_MESSAGES", "true")
    .lower() == "true"
)