import inflect


def collect_names():
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

    names = collect_names()

    print("Adieu, adieu, to " + p.join(names))


if __name__ == "__main__":
    main()
