from pickle import load, dump

# Read Data From Data Base And Returns List Of These Data
def read_data_base(FILE_PATH):
    objects = []
    try:
        with open(FILE_PATH, 'rb') as FILE:
            while True:
                try:
                    obj = load(FILE)
                    objects.append(obj)
                except EOFError:
                    return objects
    except FileNotFoundError: 
        raise FileNotFoundError(f"File with path {FILE_PATH} not found.")
    return objects

# Write (Delete And Rewrite) Data Into Data Base
def update_data_base(FILE_PATH : str, objects : list):
    with open(FILE_PATH, 'wb') as FILE:
        for obj in objects:
            dump(obj, FILE)