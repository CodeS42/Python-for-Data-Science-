def all_thing_is_obj(object: any) -> int:
    object_type =  str(type(object))
    if isinstance(object, list):
        display = "List : " + object_type
    elif isinstance(object, tuple):
        display = "Tuple : " + object_type
    elif isinstance(object, set):
        display = "Set : " + object_type
    elif isinstance(object, dict):
        display = "Dict : " + object_type
    elif isinstance(object, str):
        display = object + " is in the kitchen : " + object_type
    else:
        display = "Type not found"
    print(display)
    return 42