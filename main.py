from services.supabase_service import (
    get_contacts
)

from services.zapi_service import (
    send_message
)

from utils.validators import (
    is_valid_phone
)

from utils.logger import logger

from config.settings import SEND_MESSAGES

def main():

    success_count = 0
    error_count = 0

    contacts = get_contacts()

    logger.info(
        f"{len(contacts)} contatos encontrados"
    )

    for contact in contacts:

        if not is_valid_phone(
            contact.phone
        ):

            logger.warning(
                f"Telefone inválido: "
                f"{contact.phone}"
            )

            error_count += 1
            continue

        message = (
            f"Olá, {contact.name} "
            f"tudo bem com você?"
        )

        try:
            
            if SEND_MESSAGES:

                send_message(
                    contact.phone,
                    message
                )

                logger.info(
                    f"Mensagem enviada para "
                    f"{contact.name}"
                )

            else:

                logger.info(
                    f"[SIMULAÇÃO] "
                    f"Mensagem para "
                    f"{contact.name}: "
                    f"{message}"
                )

            success_count += 1

        except Exception as error:

            logger.error(
                f"Erro ao enviar para "
                f"{contact.name}: {error}"
            )

            error_count += 1

    logger.info("===== RESUMO =====")

    logger.info(
        f"Total de contatos: "
        f"{len(contacts)}"
    )

    logger.info(
        f"Sucesso: "
        f"{success_count}"
    )

    logger.info(
        f"Falhas: "
        f"{error_count}"
    )


if __name__ == "__main__":
    main()