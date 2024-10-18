from controllers.swos_controller import SwOSController

def main():
    print("Welcome to MikroTik SwOS CLI")
    
    # Kérjük be az alapvető hitelesítési adatokat
    ip_address = input("Enter SwOS IP address: ")
    username = input("Enter username: ")
    password = input("Enter password: ")

    # Inicializáljuk az SwOS kontroller osztályt hitelesítéssel
    controller = SwOSController(ip_address, username, password)

    while True:
        # Parancsokat kérünk a felhasználótól
        command = input(f"{username}@{ip_address}> ")

        if command == "exit":
            break
        elif command == "show ports":
            controller.show_ports()
        else:
            print("Unknown command")

if __name__ == "__main__":
    main()
