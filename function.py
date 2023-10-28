FILEPATH = "C:/Users/User/Documents/Python lectures/webapp1/todos.txt"


def get_todos(filepath=FILEPATH):
    """This reads a text file and return todo list"""
    with open(filepath, 'r') as file_local:
        list_todo_local = file_local.readlines()
    return list_todo_local


def write_todos(list_todos_arg, filepath=FILEPATH):
    """Writes the todo item in the text file"""
    with open(filepath, 'w') as file_local:
        file_local.writelines(list_todos_arg)


if __name__ == "__main__":
    print("whadup doc my man")
    print(get_todos())
