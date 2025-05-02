def all_thing_is_obj(object: any) -> int:
    if object == ["Hello", "tata!"]:
        print("List : <class 'list'>")
    elif object == ("Hello", "toto!"):
        print("Tuple : <class 'tuple'>")
    elif object ==  {"Hello", "tutu!"}:
        print("Set : <class 'set'>")
    elif object ==  {"Hello" : "titi!"}:
        print("Dict : <class 'dict'>")
    elif object == "Brian":
        print("Brian is in the kitchen : <class 'str'>")
    elif object == "Toto":
        print("Toto is in the kitchen : <class 'str'>")
    else:
        print("Type not found")

    return 42