

settings = {
    'upper': True,
    'lower': True,
    'space': False,
    'symbol': True,
    'number': True,
    'length': 8  # Corrected from 'lentgh' to 'length'
}


def get_user_length(option, default):
    while True:
        user_input = input('Enter password length: ')
        if user_input == '':
            return default
        if user_input.isdigit() and int(user_input) > 2:
            return int(user_input)
        print('Invalid input, please enter a number greater than 2.')


def yes_or_no(option, default):
    while True:
        user_input = input(f'Include {option} (default {default})(y:yes, n:no): ')
        if user_input == '':
            return default
        if user_input in ['y', 'n']:
            return user_input == 'y'
        print('Invalid input, please try again.')


def get_settings_from_users(settings):
    for option, default in settings.items():
        if option != 'length':
            user_choice = yes_or_no(option, default)
            print(f'{option}: {user_choice}')
        else:
            user_input_length = get_user_length(option, default)
            print(f'{option}: {user_input_length}')


get_settings_from_users(settings)
