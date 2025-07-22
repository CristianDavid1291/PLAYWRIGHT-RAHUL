class OrdersLocators:
    """
    Clase que contiene los locators completos para los elementos de la página de órdenes
    Cumple con el principio de responsabilidad única: solo gestiona locators de órdenes
    Incluye la función completa de Playwright para encontrar los elementos
    """
    
    # Constantes privadas - solo para uso interno de la clase
    _VIEW_BUTTON_NAME = "View"
    
    @staticmethod
    def get_order_row_by_id(page, order_id):
        """Retorna el locator completo para una fila de orden específica por ID"""
        return page.locator("tr").filter(has_text=order_id)
    
    @staticmethod
    def get_view_button_for_order(page, order_id):
        """Retorna el locator completo para el botón View de una orden específica"""
        return OrdersLocators.get_order_row_by_id(page, order_id).get_by_role("button", name=OrdersLocators._VIEW_BUTTON_NAME)
