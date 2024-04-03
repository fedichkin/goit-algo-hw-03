from datetime import datetime
import random
import re


# date must have format YYYY-MM-DD
def get_days_from_today(date: str):
    try:
        current_date = datetime.today()
        second_date = datetime.strptime(date, '%Y-%m-%d')

        return current_date.toordinal() - second_date.toordinal()
    except ValueError:
        print('Incorrect format of date')


def get_numbers_ticket(min: int, max: int, quantity: int):
    if min < 1 or max > 1000 or min > max or quantity > (max - min):
        return []

    result = set()

    while len(result) < quantity:
        result.add(random.randint(min, max))

    return sorted(result)


def normalize_phone(phone_number: str):
    result = re.sub(r'[^\d+]', '', phone_number)

    if result.startswith('38'):
        result = '+' + result
    elif result.startswith('0'):
        result = '+38' + result

    return result
