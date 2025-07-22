class LoginLocators:
    """
    Clase que contiene los locators completos para los elementos de login
    Cumple con el principio de responsabilidad única: solo gestiona locators de email y password
    Incluye la función completa de Playwright para encontrar los elementos
    """
    
    # Constantes privadas - solo para uso interno de la clase
    _EMAIL_SELECTOR = "#userEmail"
    _PASSWORD_SELECTOR = "#userPassword"
    _LOGIN_BUTTON_NAME = "Login"
    
    @staticmethod
    def get_email_input(page):
        """Retorna el locator completo para el campo de email"""
        return page.locator(LoginLocators._EMAIL_SELECTOR)
    
    @staticmethod
    def get_password_input(page):
        """Retorna el locator completo para el campo de password"""
        return page.locator(LoginLocators._PASSWORD_SELECTOR)
    
    @staticmethod
    def get_login_button(page):
        """Retorna el locator completo para el botón de login"""
        return page.get_by_role("button", name=LoginLocators._LOGIN_BUTTON_NAME)
