def naive_parser(file_name: str) -> [str]:
    with open(file_name, "r") as file:
        data = file.read().splitlines()
    return data
