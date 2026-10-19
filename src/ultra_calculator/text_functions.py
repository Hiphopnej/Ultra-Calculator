from InquirerPy import inquirer

def inquirer_input(message_param, options):
    choice = inquirer.select(
        message=message_param,
        choices=options
    ).execute()
    return choice