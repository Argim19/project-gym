def validate_id(client, id_client):
    for i in client:
        if i["id"] == id_client:
            return False
    return True


def validate_type_plan(types, option_plan):

    if option_plan < 1 or option_plan > len(types["type_plan"]):
        return False
    return True


def validate_state(types, option_state):
    if option_state < 1 or option_state > len(types["state"]):
        return False
    return True


