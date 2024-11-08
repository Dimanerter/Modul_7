from contextlib import contextmanager

@contextmanager
def my_context_manager():
    # Ініціалізація ресурсу
    print("Enter the block")
    try:
        yield  # Місце виконання блоку `with`
    except Exception as e:
        # Обробка виключень
        print(f"Error detected: {e}")
        # Можна ре-підняти виключення або вирішити його тут
        raise
    finally:
        # Звільнення ресурсу
        print("Exit the block")

# Використання
with my_context_manager():
    print("Inside the block")
    raise Exception("Something went wrong")
