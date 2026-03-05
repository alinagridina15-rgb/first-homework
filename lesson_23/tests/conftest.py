import logging
import pytest
import requests
from requests.auth import HTTPBasicAuth

BASE_URL = "http://127.0.0.1:8080"
USERNAME = "test_user"
PASSWORD = "test_pass"


def _configure_logger() -> logging.Logger:
    logger = logging.getLogger("test_search")
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        fmt = logging.Formatter("%(asctime)s | %(levelname)s | %(name)s | %(message)s")

        sh = logging.StreamHandler()
        sh.setLevel(logging.INFO)
        sh.setFormatter(fmt)

        fh = logging.FileHandler("test_search.log", mode="w", encoding="utf-8")
        fh.setLevel(logging.INFO)
        fh.setFormatter(fmt)

        logger.addHandler(sh)
        logger.addHandler(fh)

    return logger


@pytest.fixture(scope="session")
def logger():
    return _configure_logger()


@pytest.fixture(scope="class")
def auth_session(logger):
    session = requests.Session()

    url = f"{BASE_URL}/auth"
    logger.info(f"AUTH -> POST {url} as {USERNAME}")

    resp = session.post(url, auth=HTTPBasicAuth(USERNAME, PASSWORD), timeout=10)
    logger.info(f"AUTH <- status={resp.status_code}, body={resp.text}")

    assert resp.status_code == 200, "Auth failed"
    token = resp.json().get("access_token")
    assert token, "No access_token in response"

    session.headers.update({"Authorization": f"Bearer {token}"})
    yield session
    session.close()