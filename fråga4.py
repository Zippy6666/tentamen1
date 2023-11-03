import os


FILE_NAME_POSITIVE = os.getcwd()+"/Positiva.txt"
FILE_NAME_NEGATIVE = os.getcwd()+"/Negativa.txt"


def is_int( string ):
    if string[0] == "-":
        return string[1::].isdecimal()
    else:
        return string.isdecimal()


def append_to_file( filename, num ):
    with open(filename, "a") as f:
        f.write(str(num)+"\n")


def sort_into_files(numbers):
    used = []
    for num in numbers:
        if num in used:
            continue

        str_to_append_to_file = str(num)+f" ({numbers.count(num)} instanser)"
        append_to_file(num >= 0 and FILE_NAME_POSITIVE or FILE_NAME_NEGATIVE, str_to_append_to_file)
        
        used.append(num)



def main():
    numbers = []


    if os.path.isfile(FILE_NAME_POSITIVE):
        os.remove(FILE_NAME_POSITIVE)

    if os.path.isfile(FILE_NAME_NEGATIVE):
        os.remove(FILE_NAME_NEGATIVE)


    while True:
        inp = input("num: ")

        if inp == "q":
            break

        if is_int(inp):
            num = int(inp)
            numbers.append(num)
    
    

    sort_into_files( sorted(numbers) )


if __name__ == "__main__":
    main()