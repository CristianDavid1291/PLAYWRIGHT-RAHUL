class DetailsOrderLocators:

    _TOP_DIV_MESSAGE_SELECTOR = ".tagline"

    @staticmethod
    def get_top_div_message(page):
        return page.locator(DetailsOrderLocators._TOP_DIV_MESSAGE_SELECTOR)
