def list_string_parser(file_name: str) -> [str]:
    with open(file_name, "r") as file:
        data = file.read().splitlines()
    return data


def text_parser(file_name: str) -> [str]:
    with open(file_name, "r") as file:
        data = file.read()
    return data


def block_parser(file_name: str) -> [str]:
    with open(file_name, "r") as file:
        data = file.read()
        blocks = [block.strip() for block in data.split("\n\n") if block.strip()]
        return blocks
