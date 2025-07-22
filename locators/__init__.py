# Archivo para hacer el paquete locators importable
from .login_locators import LoginLocators
from .dashboard_locators import DashboardLocators
from .orders_locators import OrdersLocators
from .details_order_locator import DetailsOrderLocators

__all__ = ['LoginLocators', 'DashboardLocators', 'OrdersLocators', 'DetailsOrderLocators']
