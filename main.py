import os
local_dir = ""                               #local directory 
alien_dir = ""                               #USB directory
local_list = os.listdir(local_dir)                     
alien_list = os.listdir(alien_dir)                     
rem_list = []                                #list of items to ignore

for i in rem_list:
    local_list.remove(i)

print("USB SYNC TOOL")
print("1.LOCAL --> USB\n2. USB --> LOCAL")
try:
    ch = int(input('-->  '))
    if ch == 1:
        print_ls = []
        for i in local_list:
            if i not in alien_list:
                print_ls.append(i)
        if print_ls == []:
            print("No files found!!")
        else:
            print("Do you want to transfer these files?")
            for i in print_ls:
                print('> ', i)
            yn = input("Proceed? : ").lower()
            if yn == 'y':
                for i in print_ls:
                    cmd = f"copy \"{local_dir + i}\" \"{alien_dir}\""
                    os.system(cmd)
    elif ch == 2:
        print_ls = []
        for i in alien_list:
            if i not in local_list:
                print_ls.append(i)
        if print_ls == []:
            print("No files found!!")
        else:
            print("Do you want to transfer these files?")
            for i in print_ls:
                print('> ', i)
            yn = input("Proceed? :").lower()
            if yn == 'y':
                for i in print_ls:
                    cmd = f"copy \"{alien_dir + i}\" \"{local_dir}\""
                    os.system(cmd)
    print("ALL FILES TRANSFERED COMPLETELY")
except:
    print("Thank You!!")       
