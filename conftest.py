"""Fixtures de Pytest para la suite de control de calidad de Barterflip.

Este módulo contiene fixtures para cargar variables de entorno, lanzar un navegador
Playwright durante la sesión de prueba y proporcionar un objeto de página nueva
por prueba. Mantener el navegador en el ámbito de la sesión
acelera la suite mientras que todavía da a cada prueba de aislamiento a través de
contextos individuales.
"""
import os
import pytest
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright, Browser, Page

@pytest.fixture(scope="session")
def env() -> dict:
    """Carga variables de entorno desde el archivo .env.

    Devuelve un diccionario con la URL base y las credenciales. Si se añade
    configuración adicional al archivo .env también estará
    disponible a través de este accesorio.
    """
    load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), ".env"))
    return {
        "BASE_URL": os.getenv("BASE_URL"),
        "USER_EMAIL": os.getenv("USER_EMAIL"),
        "USER_PASSWORD": os.getenv("USER_PASSWORD"),
    }

@pytest.fixture(scope="session")
def browser() -> Browser:
    """Inicie un navegador Chromium headless durante toda la sesión de prueba."""
    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=True)
        yield browser
        browser.close()

@pytest.fixture(scope="function")
def page(browser: Browser) -> Page:
    """Proporcione un nuevo contexto de navegador y una nueva página para cada prueba.

    El uso de un nuevo contexto asegura que las cookies, localStorage y otros datos de la sesión
    estén aislados entre pruebas. La página se cierra después de la prueba.
    """
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()