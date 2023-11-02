#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    defined_names = dir(hidden_4)
    for names in defined_names:
        if not names.startswith("__"):
            print(names)

