def magic_string():
    magic_string.n = getattr(magic_string, 'n', 0) + 1
    return ", ".join(["BestSchool"] * magic_string.n)
