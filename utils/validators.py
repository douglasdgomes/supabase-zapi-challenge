def is_valid_phone(phone: str) -> bool:

    if not phone:
        return False

    return (
        phone.startswith("55")
        and phone.isdigit()
        and len(phone) >= 12
    )