def all_thing_is_obj(object: any) -> int:
    if isinstance(object, list):
        display = f"List : {type(object)}"
    elif isinstance(object, tuple):
        display = f"Tuple : {type(object)}"
    elif isinstance(object, set):
        display = f"Set : {type(object)}"
    elif isinstance(object, dict):
        display = f"Dict : {type(object)}"
    elif isinstance(object, str):
        display = f"{object} is in the kitchen : {type(object)}"
    else:
        display = "Type not found"
    print(display)
    return 42
