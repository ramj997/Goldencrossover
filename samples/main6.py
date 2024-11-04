d = {
    'a': {
        'b': 5,
        'c': {
            'd': "Hello",
            'e': 10
        }
    },
    'e': [1, 2, 3]
}

flattened_dict = {}

def flatten(current, key=""):
    if isinstance(current, dict):
        for k, v in current.items():
            flatten(v, key + k + ".")  # Concatenate keys with '.'
    else:
        flattened_dict[key[:-1]] = current  # Add to flattened_dict without trailing '.'

flatten(d)  # Start flattening from the root dictionary
print(flattened_dict)
