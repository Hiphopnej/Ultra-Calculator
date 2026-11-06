from InquirerPy import inquirer

def inquirer_input(message_param, options):
    choice = inquirer.select(
        message=message_param,
        choices=options
    ).execute()
    return choice

def get_valid_input(message, conversion_func, validation_func=None, error_message="Invalid input. Please try again."):
    while True:
        try:
            value = conversion_func(input(message))
        except (ValueError, TypeError):
            print(error_message)
            continue

        if validation_func is not None and not validation_func(value):
            print(error_message)
            continue

        return value