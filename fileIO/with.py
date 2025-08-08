'''

Reference Source: https://realpython.com/python-with-statement/


'''








import pathlib
import logging
import os

def no_with():
    file = open("hello.txt", "w")
    try:
        file.write("Hello asd!")
    except Exception as e:
        print(f"An error ocured while writing to the file: {e}")
    finally:
        file.close()

def yes_with():
    '''
    Use a context manager: An object that implemetns the context management protocol (which are the methods __enter__() and __exit__())

    Syntax: with expression as targe_var:
                do_something(target_var)
    return value of .__enter__() is bound to target_var if as is included

    Can supply multiple context managers:
    with A() as a, B() as b:
        pass
        
    Be careful of the following ERROR:
        file = open("hello.txt", mode = "w")
        with file:
            file.write("Hello World")
        #   context manager CLOSES file here. So file is closed!
            
        with file:
            file.write("Welcome")
    '''
    with open("hello.txt", mode="w") as file:
        file.write("Helloadsasd World!")


def using_pathlib():
    file_path = pathlib.Path("hello.txt")

    with file_path.open("w") as file:
        file.write("Hello, World! with using_pathlib!")

''' General format: 
    import pathlib
    import logging '''

def general_format():
    file_path = pathlib.Path("hello.txt")
    try:
        with file_path.open(mode="w") as file:
            file.write("General format: Hello World")
    except OSError as error:
        logging.error(f"Writing to file {file_path} failed due to: {error}")


def using_os():
    with os.scandir(r"..") as entries:        #   returns iterator that supports context management protocol (i.e. the iterator is a context manager)
        for entry in entries:
            print(f"{entry.name} -> {entry.stat().st_size} bytes")


''' 

async with: Requires aysynchronous context manager, used with async def function_name(...)



'''

yes_with()
using_pathlib()
general_format()
using_os()