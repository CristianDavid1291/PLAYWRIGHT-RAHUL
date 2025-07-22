from locators import DetailsOrderLocators


class DetailsOrderPage:

    def __init__(self, page):
        self.page = page

    def get_message(self):
        """Obtiene el mensaje de la página de detalles de la orden"""
        return DetailsOrderLocators.get_top_div_message(self.page)
