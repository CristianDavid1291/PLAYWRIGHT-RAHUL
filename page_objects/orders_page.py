from locators import OrdersLocators
from .details_order_page import DetailsOrderPage


class OrdersPage:

    def __init__(self, page):
        self.page = page

    
    def select_order(self, order_id):
        """Selecciona una orden específica haciendo click en el botón View"""
        OrdersLocators.get_view_button_for_order(self.page, order_id).click()
        return DetailsOrderPage(self.page)




