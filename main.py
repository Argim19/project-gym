from services.services import (
    add_client,
    delete_client,
    search_client,
    show_client,
    update_client,
)
from utils.data import load_clients, save_clients
from utils.validations import validate_id


def show_menu():
    print("")
    print("--- Welcon to program GYM ---")
    print("")
    print("1. add client")
    print("2. show clients")
    print("3. search client")
    print("4. uptade info client")
    print("5. delete client")
    print("6. exit")


def run():

    client = load_clients()
    types = {
        "type_plan": ["mensual", "trimestral", "anual"],
        "state": ["active", "inactive"],
    }

    while True:
        try:
            show_menu()
            option = int(input("enter option:"))
            match option:
                case 1:
                    print("--- ADD CLIENT ---")
                    id_client = int(input("enter the ID: "))
                    if not validate_id(client, id_client):
                        print("ID already exists")
                        continue

                    add_client(client, id_client, types)
                    save_clients(client)

                case 2:
                    show_client(client)

                case 3:
                    search_client(client)

                case 4:
                    update_client(client, types)
                    save_clients(client)

                case 5:
                    delete_client(client)
                    save_clients(client)

                case 6:
                    break

                case _:
                    print("invalid option")

        except ValueError:
            print("error")


if __name__ == "__main__":
    run()
