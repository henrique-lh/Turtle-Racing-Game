from machine import Machine
import os

def main() -> None:
    """Main function"""
    os.system('python3 registerWindow.py')

    machine = Machine()
    machine.start_machine()

if __name__ == "__main__":
    main()
