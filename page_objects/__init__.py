"""
Page Objects Initialization Module
Centralized page object management for playwright test framework
"""
from .login_page import LoginPage
from .dashboard_page import DashboardPage
from .orders_page import OrdersPage
from .details_order_page import DetailsOrderPage


__all__ = [
    'LoginPage',
    'DashboardPage',
    'OrdersPage',
    'DetailsOrderPage'
]