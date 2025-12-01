def read_input(path: str) -> str:
    with open(path, "r") as f:
        return f.read()

def lines(data: str):
    return data.splitlines()
