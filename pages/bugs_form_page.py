from playwright.sync_api import Page, Locator


class BugsFormPage:
    def __init__(self, page: Page):
        self.page = page
        self.first_name_input = page.get_by_role("textbox", name="First Name")
        self.last_name_input = page.get_by_role(
            "textbox", name="Last Name* Phone nunber* Country"
        )
        self.phone_number_input = page.get_by_role("textbox", name="Enter phone number")
        self.country_dropdown = page.locator("#countries_dropdown_menu")
        self.email_input = page.get_by_role("textbox", name="Enter email")
        self.password_input = page.get_by_role("textbox", name="Password")
        self.register_button = page.get_by_role("button", name="Register")
        self.success_message = page.locator(
            "#message", has_text="Successfully registered the following information"
        )
        self.phone_error_message = page.locator(
            "#message",
            has_text="The phone number should contain at least 10 characters!",
        )
        self.password_error_message = page.locator(
            "#message",
            has_text="The password should contain between [6,20] characters!",
        )

    def fill_registration_form(self, user_data: dict):
        # Intentionally skipping checking the terms and conditions checkbox because it's bugged, but in a real scenario, tests should not be forced to "pass" if there is a valid bug.
        if "first_name" in user_data:
            self.first_name_input.fill(user_data["first_name"])
        if "last_name" in user_data:
            self.last_name_input.fill(user_data["last_name"])
        if "phone_number" in user_data:
            self.phone_number_input.fill(user_data["phone_number"])
        if "country" in user_data:
            self.country_dropdown.select_option(value=user_data["country"])
        if "email" in user_data:
            self.email_input.fill(user_data["email"])
        if "password" in user_data:
            self.password_input.fill(user_data["password"])

    def submit_form(self):
        self.register_button.click()

    def is_success_message_visible(self) -> bool:
        return self.success_message.is_visible()

    def is_phone_error_message_visible(self) -> bool:
        return self.phone_error_message.is_visible()

    def is_password_error_message_visible(self) -> bool:
        return self.password_error_message.is_visible()

    def get_result_first_name(self) -> Locator:
        return self.page.locator("#resultFn")

    def get_result_last_name(self) -> Locator:
        return self.page.locator("#resultLn")

    def get_result_phone_number(self) -> Locator:
        return self.page.locator("#resultPhone")

    def get_result_country(self) -> Locator:
        return self.page.locator("#country")

    def get_result_email(self) -> Locator:
        return self.page.locator("#resultEmail")
