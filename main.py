# def login():
#   uname = input("What is your username?: ")
#   pwd = input("What is your password?: ")
  
#   if uname == 'akshay' and pwd == 'venkat':
#     print("Welcome to 4eplit!")
#   else:
#     print("Whoops! I don't recognize that username or password. Try again!\n")
#     login()

# login()


def login():

  while True:
    uname = input("What is your username?: ")
    pwd = input("What is your password?: ")
    if uname == 'akshay' and pwd == 'venkat':
      print("Welcome to 4eplit!")
      break
    else:
      print("Whoops! I don't recognize that username or password.Try again!\n")
      continue

login()
    

    