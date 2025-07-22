class DashboardLocators:
    """
    Clase que contiene los locators completos para los elementos del dashboard
    Cumple con el principio de responsabilidad única: solo gestiona locators del dashboard
    Incluye la función completa de Playwright para encontrar los elementos
    """
    
    # Constantes privadas - solo para uso interno de la clase
    _ORDERS_BUTTON_NAME = "ORDERS"
    
    @staticmethod
    def get_orders_button(page):
        """Retorna el locator completo para el botón ORDERS"""
        return page.get_by_role("button", name=DashboardLocators._ORDERS_BUTTON_NAME)