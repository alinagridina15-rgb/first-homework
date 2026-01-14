import logging
from logging_file import log_event

def test_log_event_success(caplog):
    with caplog.at_level(logging.INFO):
        log_event("admin", "success")
    assert any("Username: admin, Status: success" in rec.message and rec.levelname == "INFO"
               for rec in caplog.records)

def test_log_event_expired(caplog):
    with caplog.at_level(logging.WARNING):
        log_event("user", "expired")
    assert any("Username: user, Status: expired" in rec.message and rec.levelname == "WARNING"
               for rec in caplog.records)

def test_log_event_failed(caplog):
    with caplog.at_level(logging.ERROR):
        log_event("unknown", "failed")
    assert any("Username: unknown, Status: failed" in rec.message and rec.levelname == "ERROR"
               for rec in caplog.records)
