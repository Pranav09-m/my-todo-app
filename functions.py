def get_todos(filepath='todos.txt'):
    """Read the to-do items from a file and return them as a list."""
    try:
        with open(filepath, 'r') as file:
            todos = file.readlines()
        return [todo.strip() for todo in todos]
    except FileNotFoundError:
        return []

def write_todos(todos, filepath='todos.txt'):
    """Write the provided list of to-do items to a file."""
    with open(filepath, 'w') as file:
        for todo in todos:
            file.write(f"{todo+"\n"}")