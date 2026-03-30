from utils.validations import validate_state, validate_type_plan


def add_client(client, id_client, types):
    name_client = input("enter the name: ")
    age_client = int(input("enter the age: "))

    print("--- SELECT TYPE PLAN ---")
    for i, plan in enumerate(types["type_plan"], start=1):
        print(f"{i}. {plan}")

    option_plan = int(input("select type plan: "))

    if not validate_type_plan(types, option_plan):
        print("invalid option for type plan")
        return

    type_plan = types["type_plan"][option_plan - 1]

    client.append(
        {
            "id": id_client,
            "name": name_client,
            "age": age_client,
            "type_plan": type_plan,
            "state": "active",
        }
    )


def show_client(client):
    if not client:
        print("no data")
        return

    for i, x in enumerate(client, start=1):
        print(
            f"{i}. ID:{x['id']} | "
            f"Name:{x['name']} | "
            f"Age:{x['age']} | "
            f"Plan:{x['type_plan']} | "
            f"State:{x['state']}"
        )


def search_client(client):
    if not client:
        print("no data")
        return

    print("--- SEARCH CLIENT ---")
    print("1. search by ID")
    print("2. search by name")

    option = int(input("select option: "))

    match option:
        case 1:
            id_client = int(input("enter client ID: "))

            for person in client:
                if person["id"] == id_client:
                    print("--- CLIENT FOUND ---")
                    print(
                        f"ID:{person['id']} | "
                        f"Name:{person['name']} | "
                        f"Age:{person['age']} | "
                        f"Plan:{person['type_plan']} | "
                        f"State:{person['state']}"
                    )
                    return

            print("client not found")

        case 2:
            name_client = input("enter client name: ").strip().lower()

            found = False
            for person in client:
                if person["name"].strip().lower() == name_client:
                    print("--- CLIENT FOUND ---")
                    print(
                        f"ID:{person['id']} | "
                        f"Name:{person['name']} | "
                        f"Age:{person['age']} | "
                        f"Plan:{person['type_plan']} | "
                        f"State:{person['state']}"
                    )
                    found = True

            if not found:
                print("client not found")

        case _:
            print("invalid option")


def update_client(client, types):
    id_client = int(input("enter client ID to update: "))

    for person in client:
        if person["id"] == id_client:
            print("--- WHAT DO YOU WANT TO UPDATE? ---")
            print("1. state")
            print("2. client info")

            option_update = int(input("select option: "))

            match option_update:
                case 1:
                    update_state(person, types)
                    return

                case 2:
                    update_info(person, types)
                    return

                case _:
                    print("invalid option")
                    return

    print("client not found")


def update_state(person, types):
    print(f"current state: {person['state']}")
    print("--- SELECT NEW STATE ---")

    for i, state in enumerate(types["state"], start=1):
        print(f"{i}. {state}")

    option_state = int(input("select new state: "))
    if not validate_state(types, option_state):
        print("invalid option for type plan")
        return

    person["state"] = types["state"][option_state - 1]
    print("state updated successfully")


def update_info(person, types):
    person["id"] = int(input("enter new ID:"))
    person["name"] = input("enter new name: ")
    person["age"] = int(input("enter new age: "))

    print("--- SELECT NEW TYPE PLAN ---")
    for i, plan in enumerate(types["type_plan"], start=1):
        print(f"{i}. {plan}")

    option_plan = int(input("select new type plan: "))
    if not validate_type_plan(types, option_plan):
        print("invalid option for type plan")
        return

    person["type_plan"] = types["type_plan"][option_plan - 1]
    print("client info updated successfully")


def delete_client(client):
    print("--- DELETE CLIENT ---")
    id_client = int(input("enter client ID to delete: "))
    for i, person in enumerate(client):
        if person["id"] == id_client:
            client.pop(i)
            print("client deleted successfully")
            return
    print("client not found")
