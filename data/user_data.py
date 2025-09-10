VALID_USER = {
    "first_name": "",
    "last_name": "Cenzon",
    "phone_number": "1234567890",
    "country": "Philippines",
    "email": "test@test.com",
    "password": "Test123!",
}

USER_WITH_EMPTY_LAST_NAME = {
    "first_name": "",
    "last_name": "",
    "phone_number": "1234567890",
    "country": "Philippines",
    "email": "test@test.com",
    "password": "Test123!",
}

USER_WITH_EMPTY_PHONE_NUMBER = {
    "first_name": "",
    "last_name": "Cenzon",
    "phone_number": "",
    "country": "Philippines",
    "email": "test@test.com",
    "password": "Test123!",
}

USER_WITH_SHORT_PHONE_NUMBER = {
    "first_name": "",
    "last_name": "Cenzon",
    "phone_number": "1",
    "country": "Philippines",
    "email": "test@test.com",
    "password": "Test123!",
}

USER_WITH_NON_NUMERICAL_PHONE_NUMBER = {
    "first_name": "",
    "last_name": "Cenzon",
    "phone_number": "qwertyuiop",
    "country": "Philippines",
    "email": "test@test.com",
    "password": "Test123!",
}

USER_WITH_EMPTY_EMAIL = {
    "first_name": "",
    "last_name": "Cenzon",
    "phone_number": "1234567890",
    "country": "Philippines",
    "email": "",
    "password": "Test123!",
}

USER_WITH_INVALID_EMAIL_SYNTAX = {
    "first_name": "",
    "last_name": "Cenzon",
    "phone_number": "1234567890",
    "country": "Philippines",
    "email": "incorrectemailsyntax",
    "password": "Test123!",
}

USER_WITH_EMPTY_PASSWORD = {
    "first_name": "",
    "last_name": "Cenzon",
    "phone_number": "1234567890",
    "country": "Philippines",
    "email": "test@test.com",
    "password": "",
}

USER_WITH_SHORT_PASSWORD = {
    "first_name": "",
    "last_name": "Cenzon",
    "phone_number": "1234567890",
    "country": "Philippines",
    "email": "test@test.com",
    "password": "`",
}

USER_WITH_LONG_PASSWORD = {
    "first_name": "",
    "last_name": "Cenzon",
    "phone_number": "1234567890",
    "country": "Philippines",
    "email": "test@test.com",
    "password": "`1234567890-=qwertyui",
}
