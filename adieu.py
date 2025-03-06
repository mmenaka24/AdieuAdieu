import inflect


def get_names_list():
    names_list = []

    while True:
        try:
            names_list.append(input("Name: "))
        except EOFError:
            print("\n")
            break

    return names_list


def main():
    p = inflect.engine()

    names = get_names_list()

    print("Adieu, adieu, to " + p.join(names))


if __name__ == "__main__":
    main()
