# this is made to modiy your existing filess names...to look them prettier
#
# take folder path as input  as a string...
#
# it will all depends upon user's input which operations he wants to do.


# from posix import listdir
from tqdm import tqdm
import os

# verified and tested
def ask_low_cap():
    while True:
        inp = input("\nYou want to :\n\t1.Capatialize first letter of the file\n\t2.Lowerize first letter of the file.")

        if inp.isnumeric():

            inp = int(inp)
            if inp < 3:
                return inp
                break
            else:
                print("\nchoose from the given choices...")
        else:
            print("\nonly integers are accepted Sir...")

# verified and tested
def lower_first():
    print(f"folder contents are :\n\t {os.listdir()}")

    for ele in tqdm(dir_list, desc="Changing first letter to lowercase"):
        if filess:
            if os.path.isfile(ele):
                finame = ele[0].lower() + ele[1:]
                os.rename(ele, finame)

        if folder:
            if os.path.isdir(ele):
                foname = ele[0].lower() + ele[1:]
                os.rename(ele, foname)

def cap_first():
    print(f"folder contents are : {os.listdir()}")
    for ele in tqdm(dir_list, desc="Changing first letter to uppercase"):
        # print("**********entered in for loop")        #for debbuging use only
        if filess:
            # print("**********entered in fileeessss ") #for debbuging use only
            # print(f"\n{os.getcwd()}")                 #for debbuging use only
            if os.path.isfile(ele):
                # print("**********entered file type approved 1")
                finame = ele[0].upper() + ele[1:]
                # print(finame)
                os.rename(ele, finame)
                print(f"--> file name changed successfully...")

        if folder:
            # print("**********entered in folder")      #for debbuging use only
            print(f"\n{os.getcwd()}")
            if os.path.isdir(ele):
                # print("**********FOLDER VERIFIED")    #for debbuging use only
                foname = ele[0].upper() + ele[1:]
                os.rename(ele, foname)
                print(f"--> folder name changed successfully...")

# verified and tested
def take_path():

    while True:
        # printing the current directory of the user
        cwd = os.getcwd()
        print(f"\nyour current location is : {cwd}")

        # taking path from the user
        path = input("\nenter the full path of the folder which u want to clean : ")

        if_path_valid = os.path.exists(path)
        # checking wheather entered path is valid or not
        if if_path_valid:
            print(f"your entered path is {path}")
            return path
            break

        else:
            print("\nYour path is might be Invalid or Locked !!!")

# verified and tested
def set_flags():
    global filess
    global folder

    flag_inp = input(f"\non which you want to apply operations on : \n\t1.filess only\n\t2.on folders only\n\t3.on both filess and folders\n\tEnter you choice : ")

    if flag_inp == "1":
        filess = True
        # print(f"the value of files var is setted to true : {filess}") ## (only for debug purposes....)

    elif flag_inp == "2":
        folder = True
        # print(f"the value of files var is setted to true : {folder}")
        
    else:
        if flag_inp == "3":
            filess = True
            folder = True
            # print(f"the value of BOTH FILESSS AND FOLDER is setted to true : {filess},{folder}")
        else:
            print(f"pls enter valid input")


if __name__ == '__main__':

    work_path = take_path()
    os.chdir(work_path)   # change dir to the target directory
    
    dir_list = os.listdir(work_path)  # returns the list of the filess and folders
    # print(inp)        # for debbuging use only

    filess,folder = False,False

    lowup = ask_low_cap()

    set_flags()

    if lowup == 1:
        cap_first()
    else:
        lower_first()
