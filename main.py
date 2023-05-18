class InvalidPasswordError(Exception):
    def __init__(self , password):
        self.password = password
class InvalidPasswordIntError(Exception):
    def __init__(self , password):
        self.password = password
def validate_password(password):
     if len(password) < 8 :
        raise InvalidPasswordError(password)
     elif not any(i.isdigit() for i in password):
         raise InvalidPasswordIntError(password)
     else:
        print("Вас зарегестривано")
try:
    password = input("Введіть пароль: ")
    validate_password(password)
except InvalidPasswordError as a:
    print(f"Не вірний пароль '{a.password}'"
          f"\nТреба мінімум 8 символів")
except InvalidPasswordIntError as b:
    print(f"Не вірний пароль '{b.password}'"
          f"\nТреба хочаб 1 цифру")