def name_split(name: str):
    name_parts = name.split()
    if len(name_parts) == 1:
        first_name = name_parts[0]
        last_name = ""
    else:
        first_name, *_, last_name = name_parts

    return first_name, last_name