from playwright.sync_api import expect

from pages.base import BasePage


class ContactPage(BasePage):
    def populate_form(
        self,
        forename: str | None = None,
        surname: str | None = None,
        email: str | None = None,
        telephone: str | None = None,
        message: str | None = None,
    ):
        if forename is not None:
            self.page.fill("#forename", forename)
        if surname is not None:
            self.page.fill("#surname", surname)
        if email is not None:
            self.page.fill("#email", email)
        if telephone is not None:
            self.page.fill("#telephone", telephone)
        if message is not None:
            self.page.fill("#message", message)

    def submit(self):
        self.page.locator("a", has_text="Submit").click()

    def check_error_message(self):
        expect(self.page.locator(".alert-error")).to_be_visible()
        expect(self.page.locator("#forename-err")).to_contain_text("Forename is required")
        expect(self.page.locator("#email-err")).to_contain_text("Email is required")
        expect(self.page.locator("#message-err")).to_contain_text("Message is required")

    def check_no_errors(self):
        expect(self.page.locator(".alert-error")).not_to_be_visible()
        expect(self.page.locator("#forename-err")).not_to_be_visible()
        expect(self.page.locator("#email-err")).not_to_be_visible()
        expect(self.page.locator("#message-err")).not_to_be_visible()

    def check_success_message(self, forename: str):
        expect(self.page.locator(".alert-success")).to_be_visible(timeout=15e3)
        expect(self.page.locator(".alert-success")).to_contain_text(f"Thanks {forename}")
