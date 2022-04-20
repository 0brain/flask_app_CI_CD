import pytest


@pytest.fixture
def app(monkeypatch):
    from app.main import create_app

    app = create_app()

    return app


@pytest.fixture
def client(app):
    """A test client for the app."""
    app.testing = True
    return app.test_client()
