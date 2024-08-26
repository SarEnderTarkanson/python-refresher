def search(sequence, expected, finder):
    for elem in sequence:
        if finder(elem) == expected:
            return elem
    raise RuntimeError(f"Could not find an element with {expected}.")

friends = [
    {"name": "Bob", "age": 24},
    {"name": "Rolf", "age": 30},
    {"name": "Jen", "age": 27}
]

def get_friend_name(friend):
    return friend["name"]


print(search(friends, "Alpy", get_friend_name))