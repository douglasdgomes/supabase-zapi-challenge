from supabase import create_client

from config.settings import (
    SUPABASE_URL,
    SUPABASE_KEY
)

from models.contact import Contact

supabase = create_client(
    SUPABASE_URL,
    SUPABASE_KEY
)

def get_contacts() -> list[Contact]:

    response = (
        supabase.table("contacts").select("*").execute()
    )

    return [
        Contact(
            id=row["id"],
            name=row["name"],
            phone=row["phone"]
        )
        for row in response.data
    ]