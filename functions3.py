# here we call functions from functions

def introduce(name):
    """

    :param name a regular string
    :return: prints the name
    """
    print("The name is:", name)


def bond(first_name="james", last_name="bond"):
    """
    Cool function
    :param first_name: first name, default "james"
    :param last_name: last name, default"bond
    :return: returns the cool introduction
    """
    first_name = first_name.capitalize()
    last_name = last_name.capitalize()
    return f"{last_name}, {first_name} {last_name}"


introduce(bond())
introduce(bond("amir", "foox"))
introduce(bond(last_name="Johnson"))
introduce(bond(first_name="John"))
