"""Objeto de página base que contiene ayudantes comunes para las páginas de Barterflip"""
from playwright.sync_api import Page, expect


class BasePage:
    """Encapsula las operaciones genéricas realizadas en las páginas.

    Todos los objetos de página del conjunto heredan de esta clase para obtener
    ayudas sencillas de navegación y aserción. Mantener la lógica común aquí
    centraliza el mantenimiento y fomenta la coherencia entre las pruebas.
    """

    def __init__(self, page: Page) -> None:
        self.page: Page = page

    def goto(self, url: str) -> None:
        """Navega a la URL indicada y espera hasta que la red esté inactiva."""
        self.page.goto(url)
        # Espere a que la red inicial se asiente para evitar condiciones de carrera.
        self.page.wait_for_load_state("networkidle")

    def assert_text_visible(self, text: str) -> None:
        """Asegúrese de que el texto dado es visible en algún lugar de la página."""
        expect(self.page.get_by_text(text)).to_be_visible()