import pytest

from pages.contact import ContactPage
from pages.home import HomePage


def test_contact_error(jupiter_toys: HomePage):
    contact: ContactPage = jupiter_toys.navigate_to("contact")
    contact.submit()
    contact.check_error_message()

    contact.populate_form(forename="John", email="john@email.com", message="Hello World")
    contact.submit()
    contact.check_no_errors()


@pytest.mark.parametrize(argnames="forename", argvalues=["John", "Mark", "Stacy", "Dave", "Jen"])
def test_contact_success(jupiter_toys: HomePage, forename: str):
    contact: ContactPage = jupiter_toys.navigate_to("contact")
    contact.populate_form(forename=forename, email=f"{forename}@email.com", message="Hello World")
    contact.submit()
    contact.check_success_message(forename)
