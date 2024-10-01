import string
import itertools

def password_cracker(target_password):
    # Перебираем все символы: буквы (верхний и нижний регистр), цифры и специальные символы
    possible_chars = string.ascii_letters + string.digits + string.punctuation
    
    # Начинаем с перебора паролей минимальной длины
    for pwd_length in range(1, len(target_password) + 1):
        # Создаем все возможные комбинации символов текущей длины
        combinations = itertools.product(possible_chars, repeat=pwd_length)
        
        # Перебираем сгенерированные комбинации
        for guess in combinations:
            attempt = ''.join(guess)  # Преобразуем кортеж символов в строку
            
            print(f"Пробуем: {attempt}")
            
            # Если угадали пароль, выводим его и прекращаем перебор
            if attempt == target_password:
                print(f"Пароль найден: {attempt}")
                return attempt
    return None

# Пример использования программы
secret_psswd = "p!1/"
password_cracker(secret_psswd)
