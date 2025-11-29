def NULL_not_found(object: any) -> int:
    if isinstance(object, float):
        display = f"Cheese: {object} {type(object)}"
    elif isinstance(object, bool):
        display = f"Fake: {object} {type(object)}"
    elif isinstance(object, int):
        display = f"Zero: {object} {type(object)}"
    elif object is None:
        display = f"Nothing: {object} {type(object)}"
    elif isinstance(object, str) and not object:
        display = f"Empty: {type(object)}"
    else:
        display = "Type not Found"
        
    print(display)
    return 1
