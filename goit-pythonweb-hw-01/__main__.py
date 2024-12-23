from .task_1 import execute as task_1
from .task_2 import main as task_2


def main():
    while True:
        choice = (
            input("please choose task (1 or 2) or 'exit' to exit: ").strip().lower()
        )
        if choice == "1":
            task_1()
        elif choice == "2":
            task_2()
        elif choice == "exit":
            break
        else:
            print("Wrong number. Try it again.")


if __name__ == "__main__":
    main()
