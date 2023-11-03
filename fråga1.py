username_and_password = {
    'KalleAnka': '1234asdf', 
    'Mimmi_PIG': 'Hösten2023', 
    'Jann3Langben': 'password', 
    'Sebastianmentor': 'PyAi23Masters'
}


def login():
    username = input("användarnamn: ")
    password = input("lösenord: ")

    if (username in username_and_password
    and username_and_password[username] == password):
        print("Woop woop, du är inloggad")


def register():
    username = input("användarnamn: ")

    if username in username_and_password:
        print("Användarnamnet är redan taget!")
        return

    password = input("lösenord: ")
    if len(password) <= 6:
        print("Lösenord måste vara längre än 6 karakterer!")
        return

    if password==input("Validera lösenord: "):
        print("Nytt konto registrerat!")
        username_and_password[username] = password


def main():
    while True:
        print('1. Logga in!')
        print('2. Skapa ny användare!')
        print('3. Avsluta')

        choice = input('>>>')

        if choice == '1':
            login()
        elif choice == '2':
            register()
        elif choice == '3':
            break
        else:
            print('Felaktigt val')


if __name__ == "__main__":
    main()