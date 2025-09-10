from playwright.sync_api import Page, expect
import pytest
import pytest_check as check


@pytest.fixture(scope="function", autouse=True)
def before_each_test(page: Page):
    page.goto("https://qa-practice.netlify.app/bugs-form")


def test_terms_and_conditions_checkbox_must_be_enabled(page: Page):
    page.get_by_role(
        "checkbox", name="I agree with the terms and conditions"
    ).check()  # This will fail because the checkbox is disabled
    expect(
        page.get_by_role("checkbox", name="I agree with the terms and conditions")
    ).to_be_checked()


def test_first_name_should_be_optional(page: Page):
    page.get_by_role("textbox", name="First Name").fill("")
    page.get_by_role("textbox", name="Last Name* Phone nunber* Country").fill("Cenzon")
    page.get_by_role("textbox", name="Enter phone number").fill("1234567890")
    page.locator("#countries_dropdown_menu").select_option(value="Phillipines")
    page.get_by_role("textbox", name="Enter email").fill("test@test.com")
    page.get_by_role("textbox", name="Password").fill("Test123!")
    # page.get_by_role("checkbox", name="I agree with the terms and conditions").check()  # Intentionally skipping this step because it's bugged. In a real scenario, tests should not be forced to "pass" if there is a valid bug.
    page.get_by_role("button", name="Register").click()

    expect(
        page.locator(
            "#message", has_text="Successfully registered the following information"
        )
    ).to_be_visible()
    # Intentionally using soft assertions to capture all possible bugs
    check.equal(page.locator("#resultFn").text_content(), "First Name: ")
    check.equal(
        page.locator("#resultLn").text_content(), "Last Name: Cenzon"
    )  # This will fail due to input and output last name value mismatch
    check.equal(
        page.locator("#resultPhone").text_content(), "Phone Number: 1234567890"
    )  # This will fail due to input and output phone number value mismatch
    check.equal(page.locator("#country").text_content(), "Country: Phillipines")
    check.equal(page.locator("#resultEmail").text_content(), "Email: test@test.com")


def test_last_name_should_be_required(page: Page):
    page.get_by_role("textbox", name="First Name").fill("")
    page.get_by_role("textbox", name="Last Name* Phone nunber* Country").fill("")
    page.get_by_role("textbox", name="Enter phone number").fill("1234567890")
    page.locator("#countries_dropdown_menu").select_option(value="Phillipines")
    page.get_by_role("textbox", name="Enter email").fill("test@test.com")
    page.get_by_role("textbox", name="Password").fill("Test123!")
    # page.get_by_role("checkbox", name="I agree with the terms and conditions").check()  # Intentionally skipping this step because it's bugged. In a real scenario, tests should not be forced to "pass" if there is a valid bug.
    page.get_by_role("button", name="Register").click()

    # Intentionally using soft assertions to capture all possible bugs
    # These will fail because the form allows submission even if the last name is missing
    check.is_false(
        page.locator(
            "#message", has_text="Successfully registered the following information"
        ).is_visible()
    )
    check.is_false(page.locator("#resultFn").is_visible())
    check.is_false(page.locator("#resultLn").is_visible())
    check.is_false(page.locator("#resultPhone").is_visible())
    check.is_false(page.locator("#country").is_visible())
    check.is_false(page.locator("#resultEmail").is_visible())


def test_phone_number_should_be_required(page: Page):
    page.get_by_role("textbox", name="First Name").fill("")
    page.get_by_role("textbox", name="Last Name* Phone nunber* Country").fill("Cenzon")
    page.get_by_role("textbox", name="Enter phone number").fill("")
    page.locator("#countries_dropdown_menu").select_option(value="Phillipines")
    page.get_by_role("textbox", name="Enter email").fill("test@test.com")
    page.get_by_role("textbox", name="Password").fill("Test123!")
    # page.get_by_role("checkbox", name="I agree with the terms and conditions").check()  # Intentionally skipping this step because it's bugged. In a real scenario, tests should not be forced to "pass" if there is a valid bug.
    page.get_by_role("button", name="Register").click()

    # Intentionally using soft assertions to capture all possible bugs
    check.is_true(
        page.locator(
            "#message",
            has_text="The phone number should contain at least 10 characters!",
        ).is_visible()
    )
    check.is_false(page.locator("#resultFn").is_visible())
    check.is_false(page.locator("#resultLn").is_visible())
    check.is_false(page.locator("#resultPhone").is_visible())
    check.is_false(page.locator("#country").is_visible())
    check.is_false(page.locator("#resultEmail").is_visible())


def test_phone_number_should_be_at_least_10_characters(page: Page):
    page.get_by_role("textbox", name="First Name").fill("")
    page.get_by_role("textbox", name="Last Name* Phone nunber* Country").fill("Cenzon")
    page.get_by_role("textbox", name="Enter phone number").fill("1")
    page.locator("#countries_dropdown_menu").select_option(value="Phillipines")
    page.get_by_role("textbox", name="Enter email").fill("test@test.com")
    page.get_by_role("textbox", name="Password").fill("Test123!")
    # page.get_by_role("checkbox", name="I agree with the terms and conditions").check()  # Intentionally skipping this step because it's bugged. In a real scenario, tests should not be forced to "pass" if there is a valid bug.
    page.get_by_role("button", name="Register").click()

    # Intentionally using soft assertions to capture all possible bugs
    check.is_true(
        page.locator(
            "#message",
            has_text="The phone number should contain at least 10 characters!",
        ).is_visible()
    )
    check.is_false(page.locator("#resultFn").is_visible())
    check.is_false(page.locator("#resultLn").is_visible())
    check.is_false(page.locator("#resultPhone").is_visible())
    check.is_false(page.locator("#country").is_visible())
    check.is_false(page.locator("#resultEmail").is_visible())


def test_phone_number_should_be_numerical(page: Page):
    page.get_by_role("textbox", name="First Name").fill("")
    page.get_by_role("textbox", name="Last Name* Phone nunber* Country").fill("Cenzon")
    page.get_by_role("textbox", name="Enter phone number").fill("qwertyuiop")
    page.locator("#countries_dropdown_menu").select_option(value="Phillipines")
    page.get_by_role("textbox", name="Enter email").fill("test@test.com")
    page.get_by_role("textbox", name="Password").fill("Test123!")
    # page.get_by_role("checkbox", name="I agree with the terms and conditions").check()  # Intentionally skipping this step because it's bugged. In a real scenario, tests should not be forced to "pass" if there is a valid bug.
    page.get_by_role("button", name="Register").click()

    # Intentionally using soft assertions to capture all possible bugs
    # These will fail because the form allows non-numerical phone numbers
    check.is_true(
        page.locator(
            "#message",
            has_text="The phone number should contain at least 10 characters!",
        ).is_visible()
    )
    check.is_false(page.locator("#resultFn").is_visible())
    check.is_false(page.locator("#resultLn").is_visible())
    check.is_false(page.locator("#resultPhone").is_visible())
    check.is_false(page.locator("#country").is_visible())
    check.is_false(page.locator("#resultEmail").is_visible())


def test_email_should_be_required(page: Page):
    page.get_by_role("textbox", name="First Name").fill("")
    page.get_by_role("textbox", name="Last Name* Phone nunber* Country").fill("Cenzon")
    page.get_by_role("textbox", name="Enter phone number").fill("1234567890")
    page.locator("#countries_dropdown_menu").select_option(value="Phillipines")
    page.get_by_role("textbox", name="Enter email").fill("")
    page.get_by_role("textbox", name="Password").fill("Test123!")
    # page.get_by_role("checkbox", name="I agree with the terms and conditions").check()  # Intentionally skipping this step because it's bugged. In a real scenario, tests should not be forced to "pass" if there is a valid bug.
    page.get_by_role("button", name="Register").click()

    # Intentionally using soft assertions to capture all possible bugs
    # These will fail because the form allows submission even if the email is missing
    check.is_false(
        page.locator(
            "#message", has_text="Successfully registered the following information"
        ).is_visible()
    )
    check.is_false(page.locator("#resultFn").is_visible())
    check.is_false(page.locator("#resultLn").is_visible())
    check.is_false(page.locator("#resultPhone").is_visible())
    check.is_false(page.locator("#country").is_visible())
    check.is_false(page.locator("#resultEmail").is_visible())


def test_email_should_have_the_correct_syntax(page: Page):
    page.get_by_role("textbox", name="First Name").fill("")
    page.get_by_role("textbox", name="Last Name* Phone nunber* Country").fill("Cenzon")
    page.get_by_role("textbox", name="Enter phone number").fill("1234567890")
    page.locator("#countries_dropdown_menu").select_option(value="Phillipines")
    page.get_by_role("textbox", name="Enter email").fill("incorrectemailsyntax")
    page.get_by_role("textbox", name="Password").fill("Test123!")
    # page.get_by_role("checkbox", name="I agree with the terms and conditions").check()  # Intentionally skipping this step because it's bugged. In a real scenario, tests should not be forced to "pass" if there is a valid bug.
    page.get_by_role("button", name="Register").click()

    # Intentionally using soft assertions to capture all possible bugs
    # These will fail because the form allows submission even if the email syntax is incorrect
    check.is_false(
        page.locator(
            "#message", has_text="Successfully registered the following information"
        ).is_visible()
    )
    check.is_false(page.locator("#resultFn").is_visible())
    check.is_false(page.locator("#resultLn").is_visible())
    check.is_false(page.locator("#resultPhone").is_visible())
    check.is_false(page.locator("#country").is_visible())
    check.is_false(page.locator("#resultEmail").is_visible())


def test_password_should_be_required(page: Page):
    page.get_by_role("textbox", name="First Name").fill("")
    page.get_by_role("textbox", name="Last Name* Phone nunber* Country").fill("Cenzon")
    page.get_by_role("textbox", name="Enter phone number").fill("1234567890")
    page.locator("#countries_dropdown_menu").select_option(value="Phillipines")
    page.get_by_role("textbox", name="Enter email").fill("test@test.com")
    page.get_by_role("textbox", name="Password").fill("")
    # page.get_by_role("checkbox", name="I agree with the terms and conditions").check()  # Intentionally skipping this step because it's bugged. In a real scenario, tests should not be forced to "pass" if there is a valid bug.
    page.get_by_role("button", name="Register").click()

    # Intentionally using soft assertions to capture all possible bugs
    check.is_true(
        page.locator(
            "#message",
            has_text="The password should contain between [6,20] characters!",
        ).is_visible()
    )
    check.is_false(page.locator("#resultFn").is_visible())
    check.is_false(page.locator("#resultLn").is_visible())
    check.is_false(page.locator("#resultPhone").is_visible())
    check.is_false(page.locator("#country").is_visible())
    check.is_false(page.locator("#resultEmail").is_visible())


def test_password_should_be_at_least_6_characters(page: Page):
    page.get_by_role("textbox", name="First Name").fill("")
    page.get_by_role("textbox", name="Last Name* Phone nunber* Country").fill("Cenzon")
    page.get_by_role("textbox", name="Enter phone number").fill("1234567890")
    page.locator("#countries_dropdown_menu").select_option(value="Phillipines")
    page.get_by_role("textbox", name="Enter email").fill("test@test.com")
    page.get_by_role("textbox", name="Password").fill("`")
    # page.get_by_role("checkbox", name="I agree with the terms and conditions").check()  # Intentionally skipping this step because it's bugged. In a real scenario, tests should not be forced to "pass" if there is a valid bug.
    page.get_by_role("button", name="Register").click()

    # Intentionally using soft assertions to capture all possible bugs
    check.is_true(
        page.locator(
            "#message",
            has_text="The password should contain between [6,20] characters!",
        ).is_visible()
    )
    check.is_false(page.locator("#resultFn").is_visible())
    check.is_false(page.locator("#resultLn").is_visible())
    check.is_false(page.locator("#resultPhone").is_visible())
    check.is_false(page.locator("#country").is_visible())
    check.is_false(page.locator("#resultEmail").is_visible())


def test_password_should_be_at_most_20_characters(page: Page):
    page.get_by_role("textbox", name="First Name").fill("")
    page.get_by_role("textbox", name="Last Name* Phone nunber* Country").fill("Cenzon")
    page.get_by_role("textbox", name="Enter phone number").fill("1234567890")
    page.locator("#countries_dropdown_menu").select_option(value="Phillipines")
    page.get_by_role("textbox", name="Enter email").fill("test@test.com")
    page.get_by_role("textbox", name="Password").fill("`1234567890-=qwertyui")
    # page.get_by_role("checkbox", name="I agree with the terms and conditions").check()  # Intentionally skipping this step because it's bugged. In a real scenario, tests should not be forced to "pass" if there is a valid bug.
    page.get_by_role("button", name="Register").click()

    # Intentionally using soft assertions to capture all possible bugs
    check.is_true(
        page.locator(
            "#message",
            has_text="The password should contain between [6,20] characters!",
        ).is_visible()
    )
    check.is_false(page.locator("#resultFn").is_visible())
    check.is_false(page.locator("#resultLn").is_visible())
    check.is_false(page.locator("#resultPhone").is_visible())
    check.is_false(page.locator("#country").is_visible())
    check.is_false(page.locator("#resultEmail").is_visible())


def test_password_field_should_be_masked(page: Page):
    page.get_by_role("textbox", name="Password").fill("Test123!")
    check.equal(
        page.get_by_role("textbox", name="Password").input_value(), "••••••••"
    )  # This will fail because the password field is not masked


# Styling/Visual tests should ideally be via tools like Applitools, Percy, etc., but including them here anyway for completeness
def test_success_message_background_color_should_be_green(page: Page):
    page.get_by_role("textbox", name="First Name").fill("")
    page.get_by_role("textbox", name="Last Name* Phone nunber* Country").fill("Cenzon")
    page.get_by_role("textbox", name="Enter phone number").fill("1234567890")
    page.locator("#countries_dropdown_menu").select_option(value="Phillipines")
    page.get_by_role("textbox", name="Enter email").fill("test@test.com")
    page.get_by_role("textbox", name="Password").fill("Test123!")
    # page.get_by_role("checkbox", name="I agree with the terms and conditions").check()  # Intentionally skipping this step because it's bugged. In a real scenario, tests should not be forced to "pass" if there is a valid bug.
    page.get_by_role("button", name="Register").click()

    expect(
        page.locator(
            "#message", has_text="Successfully registered the following information"
        )
    ).to_have_css(
        "background-color", "rgb(0, 255, 0)"
    )  # Just some arbitrary shade of green; This will fail because the success message background color is not green


# Styling/Visual tests should ideally be via tools like Applitools, Percy, etc., but including them here anyway for completeness
def test_error_message_background_color_should_be_red(page: Page):
    page.get_by_role("textbox", name="First Name").fill("")
    page.get_by_role("textbox", name="Last Name* Phone nunber* Country").fill("Cenzon")
    page.get_by_role("textbox", name="Enter phone number").fill("")
    page.locator("#countries_dropdown_menu").select_option(value="Phillipines")
    page.get_by_role("textbox", name="Enter email").fill("test@test.com")
    page.get_by_role("textbox", name="Password").fill("Test123!")
    # page.get_by_role("checkbox", name="I agree with the terms and conditions").check()  # Intentionally skipping this step because it's bugged. In a real scenario, tests should not be forced to "pass" if there is a valid bug.
    page.get_by_role("button", name="Register").click()

    expect(
        page.locator(
            "#message",
            has_text="The phone number should contain at least 10 characters!",
        )
    ).to_have_css("background-color", "rgb(248, 215, 218)")
