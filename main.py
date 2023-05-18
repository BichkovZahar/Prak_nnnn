class InvalidUsernameError(Exception):
  def __init__(self, username):
    self.username = username
class InvalidSymbolError(Exception):
  def __init__(self, username):
    self.username = username
class InvalidWordError(Exception):
  def __init__(self, username):
    self.username = username
def register_user(username):
  if username == "niga":
    raise InvalidWordError(username)
  elif len(username) < 5:
    raise InvalidUsernameError(username)
  for i in username:
     if i == "!":
       raise InvalidSymbolError(username)
     elif i == "?":
       raise InvalidSymbolError(username)
     elif i == ".":
       raise InvalidSymbolError(username)
     elif i == ",":
       raise InvalidSymbolError(username)
     elif i == "@":
       raise InvalidSymbolError(username)
     elif i == "#":
       raise InvalidSymbolError(username)
  else:
    print("Вас зареєстровано")

try:
 username = input("Введіть ім'я користувача: ")
 register_user(username)
except InvalidUsernameError as a:
 print(f"Неправильне ім'я користувача {a.username} \n"
       f"Треба мінімум 5 символів")
except InvalidSymbolError as b:
    print(f"Неправильне ім'я користувача {b.username} \n"
          f"Ім'я не має містити @ # ! ? , .")
except InvalidWordError as c:
  print(f"Неправильне ім'я користувача {c.username} \n"
        f"Треба нормальне ім'я")
