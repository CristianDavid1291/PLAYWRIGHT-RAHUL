from playwright.sync_api import Playwright
orders_payload = {"orders":[{"country":"Colombia","productOrderedId":"67a8dde5c0d3e6622a297cc8"},{"country":"Colombia","productOrderedId":"67a8df1ac0d3e6622a297ccb"}]}

class APIUtils:

    def get_token(self, playwright: Playwright, user_data):
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = api_request_context.post(
            "/api/ecom/auth/login",
            data={"userEmail": user_data['username'], "userPassword": user_data['password']}
        )
        assert response.ok, "Failed to get token"
        return response.json().get("token")
    
    def create_order(self, playwright: Playwright, user_data):
        token = self.get_token(playwright, user_data)
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = api_request_context.post(
            "/api/ecom/order/create-order",
            data=orders_payload,
            headers={"Authorization": token,
                     "Content-Type": "application/json"}

        )
        print(response.json())
        response_body = response.json()
        return response_body["orders"][0]

