"""Prueba de humo para la funcionalidad de inicio de sesión de Barterflip."""
import pytest

from ..pages.login_page import LoginPage


@pytest.mark.smoke
def test_login_success(env: dict, page) -> None:
    """Compruebe que un usuario puede iniciar sesión en el CMS y acceder al panel de control."""
    login_page = LoginPage(page)
    login_page.login(env["BASE_URL"], env["USER_EMAIL"], env["USER_PASSWORD"])
    # Después de iniciar sesión, la ruta del panel de control debe formar parte de la URL.
    assert "/dashboard" in page.url