import logging

def log_event(username: str, status: str):
    log_message = f"Login event - Username: {username}, Status: {status}"

    if status == "success":
        logging.info(log_message)
    elif status == "expired":
        logging.warning(log_message)
    else:
        logging.error(log_message)
