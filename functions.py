FILEPATH = 'todos.txt'

def get_todos(filepath=FILEPATH):
    """ reads selected file and returns the list of to-do items. THIS IS AN EXAMPLE OF A DOC STRING."""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg, filepath=FILEPATH):
    """ Writes to end of filepath what is written in todos_arg """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

# print(__name__)
# if __name__ == "__main__":
#     print("hello")
#     print(get_todos())