import random


def generate_password(length, use_lowercase=True, use_uppercase=True, use_digits=True, use_cyrillic=True):
    lowercase = 'abcdefghijklmnopqrstuvwxyz' if use_lowercase else ''
    uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' if use_uppercase else ''
    digits = '0123456789' if use_digits else ''
    cyrillic_lowercase = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя' if use_cyrillic and use_lowercase else ''
    cyrillic_uppercase = cyrillic_lowercase.upper() if use_cyrillic and use_uppercase else ''

    characters = lowercase + uppercase + digits + cyrillic_lowercase + cyrillic_uppercase

    if not characters:
        raise ValueError("Необхідно вибрати принаймні один тип символу.")

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def get_user_input(prompt, allowed_values=('y', 'n')):
    while True:
        user_input = input(prompt).lower()
        if user_input in allowed_values:
            return user_input
        print("Помилка вводу. Введіть будь-ласка 'y' чи 'n'.")

def start_generate_password():
    length = int(input("Введіть бажану довжину пароля: "))
    use_lowercase = get_user_input("Додати нижній регістр? (y/n): ")
    use_uppercase = get_user_input("Додати верхній регістр? (y/n): ")
    use_digits = get_user_input("Додати цифри? (y/n): ")
    use_cyrillic = get_user_input("Додати Кирилицю? (y/n): ")

    use_lowercase = use_lowercase == 'y'
    use_uppercase = use_uppercase == 'y'
    use_digits = use_digits == 'y'
    use_cyrillic = use_cyrillic == 'y'

    password = generate_password(length, use_lowercase, use_uppercase, use_digits, use_cyrillic)
    print("Сгенерований пароль:", password)


start_generate_password()
