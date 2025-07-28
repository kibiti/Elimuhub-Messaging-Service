import os
import pytest
from src.integrations.whatsapp_bsp_client import send_message

def test_send_message(monkeypatch):
    class MockResponse:
        def raise_for_status(self): pass
        def json(self): return {"success": True}
    monkeypatch.setattr("requests.post", lambda *a, **k: MockResponse())

    resp = send_message("+254700000000", "admission_template", [{"type": "text", "text": "Test"}])
    assert resp["success"]
