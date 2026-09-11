import pytest
from guara import it
from guara.application import Application

from tests.fixtures.driver import driver  # noqa: F401
from tests.transactions.add_to_cart_transaction import AddProductToCart
from tests.transactions.checkout_transaction import TheUSerDoesACheckoutWith
from tests.transactions.finish_order_transaction import FinishOrder
from tests.transactions.login_transaction import LoginWith


@pytest.mark.smoke
def test_checkout_ptp(driver):  # noqa: F811
    app = Application(driver)
    app.given(
        LoginWith,
        url="https://www.saucedemo.com",
        user="standard_user",
        password="secret_sauce",
    ).then(it.Contains, "inventory")

    app.when(AddProductToCart).asserts(it.Contains, "cart")

    app.when(
        TheUSerDoesACheckoutWith, name="Douglas", last="Teste", zip_code="12345"
    ).asserts(it.Contains, "checkout-step-two")

    app.when(FinishOrder).asserts(it.Contains, "Thank you")
