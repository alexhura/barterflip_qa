"""Objeto de página para la página de inicio de sesión de Barterflip"""
from typing import Optional
from playwright.sync_api import expect
from .base_page import BasePage


class LoginPage(BasePage):
    """Representa la página de inicio de sesión para el CMS Barterflip.

    Esta clase expone acciones de alto nivel como introducir las credenciales de
    y enviar el formulario. Las definiciones del selector viven
    centralmente en esta clase para que las pruebas sigan siendo legibles y resistentes
    contra los cambios de marcado.
    """

    # Selectores CSS para los elementos de la página de inicio de sesión. En caso de que un selector
    # cambio en la interfaz de usuario, actualícelo aquí y las pruebas seguirán funcionando.
    EMAIL_INPUT = "input[type='Email']"
    PASSWORD_INPUT = "input[type='Password']"
    LOGIN_BUTTON = "button:has-text('Login')"
    DASHBOARD_UNIQUE = "text=Dashboard"

    def login(self, base_url: str, email: str, password: str) -> None:
        """Realiza el flujo de inicio de sesión con las credenciales suministradas.

        Navega a la URL base, rellena los campos de correo electrónico y contraseña
        y envía el formulario. El método espera hasta que aparece el panel de control
        para asegurarse de que el inicio de sesión se ha realizado correctamente.
        """
        self.goto(base_url)
        self.page.fill(self.EMAIL_INPUT, email)
        self.page.fill(self.PASSWORD_INPUT, password)
        self.page.click(self.LOGIN_BUTTON)
        # Espere a que finalice la navegación. El panel de control debería cargarse.
        self.page.wait_for_load_state("networkidle")
        # Afirmar que aparece un elemento conocido del salpicadero.
        expect(self.page.get_by_text("Dashboard")).to_be_visible()