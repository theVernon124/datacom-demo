from playwright.sync_api import Page, expect
import pytest
import pytest_check as check
from pages.bugs_form_page import BugsFormPage
from data.user_data import (
    RANDOM_VALID_USER,
    VALID_USER,
    USER_WITH_EMPTY_LAST_NAME,
    USER_WITH_EMPTY_PHONE_NUMBER,
    USER_WITH_SHORT_PHONE_NUMBER,
    USER_WITH_NON_NUMERICAL_PHONE_NUMBER,
    USER_WITH_EMPTY_EMAIL,
    USER_WITH_INVALID_EMAIL_SYNTAX,
    USER_WITH_EMPTY_PASSWORD,
    USER_WITH_SHORT_PASSWORD,
    USER_WITH_LONG_PASSWORD,
)


@pytest.fixture(scope="function", autouse=True)
def before_each_test(page: Page):
    page.goto("https://qa-practice.netlify.app/bugs-form")


def test_terms_and_conditions_checkbox_must_be_enabled(page: Page):
    bugs_form_page = BugsFormPage(page)
    bugs_form_page.page.get_by_role(
        "checkbox", name="I agree with the terms and conditions"
    ).check()  # This will fail because the checkbox is disabled
    expect(
        bugs_form_page.page.get_by_role(
            "checkbox", name="I agree with the terms and conditions"
        )
    ).to_be_checked()


def test_first_name_should_be_optional(page: Page):
    bugs_form_page = BugsFormPage(page)
    user_data = RANDOM_VALID_USER
    bugs_form_page.fill_registration_form(user_data)
    bugs_form_page.submit_form()

    # Intentionally using soft assertions to capture all possible bugs
    check.is_true(bugs_form_page.is_success_message_visible())
    check.equal(
        bugs_form_page.get_result_first_name().text_content(),
        f"First Name: {user_data['first_name']}",
    )
    check.equal(
        bugs_form_page.get_result_last_name().text_content(),
        f"Last Name: {user_data['last_name']}",
    )  # This will fail due to input and output last name value mismatch
    check.equal(
        bugs_form_page.get_result_phone_number().text_content(),
        f"Phone Number: {user_data['phone_number']}",
    )  # This will fail due to input and output phone number value mismatch
    check.equal(
        bugs_form_page.get_result_country().text_content(),
        f"Country: {user_data['country']}",
    )
    check.equal(
        bugs_form_page.get_result_email().text_content(),
        f"Email: {user_data['email']}",
    )


def test_last_name_should_be_required(page: Page):
    bugs_form_page = BugsFormPage(page)
    bugs_form_page.fill_registration_form(USER_WITH_EMPTY_LAST_NAME)
    bugs_form_page.submit_form()

    # Intentionally using soft assertions to capture all possible bugs
    # These will fail because the form allows submission even if the last name is missing
    check.is_false(bugs_form_page.is_success_message_visible())
    check.is_false(bugs_form_page.get_result_first_name().is_visible())
    check.is_false(bugs_form_page.get_result_last_name().is_visible())
    check.is_false(bugs_form_page.get_result_phone_number().is_visible())
    check.is_false(bugs_form_page.get_result_country().is_visible())
    check.is_false(bugs_form_page.get_result_email().is_visible())


def test_phone_number_should_be_required(page: Page):
    bugs_form_page = BugsFormPage(page)
    bugs_form_page.fill_registration_form(USER_WITH_EMPTY_PHONE_NUMBER)
    bugs_form_page.submit_form()

    # Intentionally using soft assertions to capture all possible bugs
    check.is_true(bugs_form_page.is_phone_error_message_visible())
    check.is_false(bugs_form_page.get_result_first_name().is_visible())
    check.is_false(bugs_form_page.get_result_last_name().is_visible())
    check.is_false(bugs_form_page.get_result_phone_number().is_visible())
    check.is_false(bugs_form_page.get_result_country().is_visible())
    check.is_false(bugs_form_page.get_result_email().is_visible())


def test_phone_number_should_be_at_least_10_characters(page: Page):
    bugs_form_page = BugsFormPage(page)
    bugs_form_page.fill_registration_form(USER_WITH_SHORT_PHONE_NUMBER)
    bugs_form_page.submit_form()

    # Intentionally using soft assertions to capture all possible bugs
    check.is_true(bugs_form_page.is_phone_error_message_visible())
    check.is_false(bugs_form_page.get_result_first_name().is_visible())
    check.is_false(bugs_form_page.get_result_last_name().is_visible())
    check.is_false(bugs_form_page.get_result_phone_number().is_visible())
    check.is_false(bugs_form_page.get_result_country().is_visible())
    check.is_false(bugs_form_page.get_result_email().is_visible())


def test_phone_number_should_be_numerical(page: Page):
    bugs_form_page = BugsFormPage(page)
    bugs_form_page.fill_registration_form(USER_WITH_NON_NUMERICAL_PHONE_NUMBER)
    bugs_form_page.submit_form()

    # Intentionally using soft assertions to capture all possible bugs
    # These will fail because the form allows non-numerical phone numbers
    check.is_true(bugs_form_page.is_phone_error_message_visible())
    check.is_false(bugs_form_page.get_result_first_name().is_visible())
    check.is_false(bugs_form_page.get_result_last_name().is_visible())
    check.is_false(bugs_form_page.get_result_phone_number().is_visible())
    check.is_false(bugs_form_page.get_result_country().is_visible())
    check.is_false(bugs_form_page.get_result_email().is_visible())


def test_email_should_be_required(page: Page):
    bugs_form_page = BugsFormPage(page)
    bugs_form_page.fill_registration_form(USER_WITH_EMPTY_EMAIL)
    bugs_form_page.submit_form()

    # Intentionally using soft assertions to capture all possible bugs
    # These will fail because the form allows submission even if the email is missing
    check.is_false(bugs_form_page.is_success_message_visible())
    check.is_false(bugs_form_page.get_result_first_name().is_visible())
    check.is_false(bugs_form_page.get_result_last_name().is_visible())
    check.is_false(bugs_form_page.get_result_phone_number().is_visible())
    check.is_false(bugs_form_page.get_result_country().is_visible())
    check.is_false(bugs_form_page.get_result_email().is_visible())


def test_email_should_have_the_correct_syntax(page: Page):
    bugs_form_page = BugsFormPage(page)
    bugs_form_page.fill_registration_form(USER_WITH_INVALID_EMAIL_SYNTAX)
    bugs_form_page.submit_form()

    # Intentionally using soft assertions to capture all possible bugs
    # These will fail because the form allows submission even if the email syntax is incorrect
    check.is_false(bugs_form_page.is_success_message_visible())
    check.is_false(bugs_form_page.get_result_first_name().is_visible())
    check.is_false(bugs_form_page.get_result_last_name().is_visible())
    check.is_false(bugs_form_page.get_result_phone_number().is_visible())
    check.is_false(bugs_form_page.get_result_country().is_visible())
    check.is_false(bugs_form_page.get_result_email().is_visible())


def test_password_should_be_required(page: Page):
    bugs_form_page = BugsFormPage(page)
    bugs_form_page.fill_registration_form(USER_WITH_EMPTY_PASSWORD)
    bugs_form_page.submit_form()

    # Intentionally using soft assertions to capture all possible bugs
    check.is_true(bugs_form_page.is_password_error_message_visible())
    check.is_false(bugs_form_page.get_result_first_name().is_visible())
    check.is_false(bugs_form_page.get_result_last_name().is_visible())
    check.is_false(bugs_form_page.get_result_phone_number().is_visible())
    check.is_false(bugs_form_page.get_result_country().is_visible())
    check.is_false(bugs_form_page.get_result_email().is_visible())


def test_password_should_be_at_least_6_characters(page: Page):
    bugs_form_page = BugsFormPage(page)
    bugs_form_page.fill_registration_form(USER_WITH_SHORT_PASSWORD)
    bugs_form_page.submit_form()

    # Intentionally using soft assertions to capture all possible bugs
    check.is_true(bugs_form_page.is_password_error_message_visible())
    check.is_false(bugs_form_page.get_result_first_name().is_visible())
    check.is_false(bugs_form_page.get_result_last_name().is_visible())
    check.is_false(bugs_form_page.get_result_phone_number().is_visible())
    check.is_false(bugs_form_page.get_result_country().is_visible())
    check.is_false(bugs_form_page.get_result_email().is_visible())


def test_password_should_be_at_most_20_characters(page: Page):
    bugs_form_page = BugsFormPage(page)
    bugs_form_page.fill_registration_form(USER_WITH_LONG_PASSWORD)
    bugs_form_page.submit_form()

    # Intentionally using soft assertions to capture all possible bugs
    check.is_true(bugs_form_page.is_password_error_message_visible())
    check.is_false(bugs_form_page.get_result_first_name().is_visible())
    check.is_false(bugs_form_page.get_result_last_name().is_visible())
    check.is_false(bugs_form_page.get_result_phone_number().is_visible())
    check.is_false(bugs_form_page.get_result_country().is_visible())
    check.is_false(bugs_form_page.get_result_email().is_visible())


def test_password_field_should_be_masked(page: Page):
    bugs_form_page = BugsFormPage(page)
    bugs_form_page.password_input.fill("Test123!")
    check.equal(
        bugs_form_page.password_input.input_value(), "••••••••"
    )  # This will fail because the password field is not masked


# Styling/Visual tests should ideally be via tools like Applitools, Percy, etc., but including them here anyway for completeness
def test_success_message_background_color_should_be_green(page: Page):
    bugs_form_page = BugsFormPage(page)
    bugs_form_page.fill_registration_form(RANDOM_VALID_USER)
    bugs_form_page.submit_form()

    expect(bugs_form_page.success_message).to_have_css(
        "background-color", "rgb(0, 255, 0)"
    )  # Just some arbitrary shade of green; This will fail because the success message background color is not green


# Styling/Visual tests should ideally be via tools like Applitools, Percy, etc., but including them here anyway for completeness
def test_error_message_background_color_should_be_red(page: Page):
    bugs_form_page = BugsFormPage(page)
    bugs_form_page.fill_registration_form(USER_WITH_EMPTY_PHONE_NUMBER)
    bugs_form_page.submit_form()

    expect(bugs_form_page.phone_error_message).to_have_css(
        "background-color", "rgb(248, 215, 218)"
    )
