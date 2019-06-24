fat = []
dir =[]
sector =[] 

def read_fat():
    i = 0
    ffat = open("fat.dat", "r")
    for line in ffat:
        line = line.strip("\n")
        val = int(line)
        fat.append(val)
    ffat.close
 
def save_fat():
    ffat = open("fat.dat", "w")
    for i in range(len(fat)):
        ffat.write(str(fat[i])+"\n" )
    ffat.close

#------------------------------------------
def read_dir():
    fdir = open("dir.dat", "r")
    print(fdir)
    for line in fdir:
        line = line.strip("\n")
        x = line.split(" ")
        x[1] = int(x[1])
        dir.append(x[0])
        sector.append(x[1])
    fdir.close

def save_dir():
    fdir = open("dir.dat", "w")
    for i in range(len(dir)):
        x = dir[i] + " " + str(sector[i])
        fdir.write(x + "\n" )
    fdir.close

def first_free_sector():
    for i in range(0,len(fat)):
        if fat[i] == 1:
            return i

def free_sectors():
    free_sector_count = 0
    for i in range(0,len(fat)):
        if fat[i] == 1:
            free_sector_count = free_sector_count +1
    return free_sector_count

def allocate_sectors(start_sector, n):
    
    CurrentSector = start_sector
    for i in range(start_sector + 1, len(fat)):
        if n == 1:
            fat[CurrentSector]= 0
            return
        if fat[i] == 1:
            fat[CurrentSector] = i
            CurrentSector = i
            n = n-1

def add_file_to_dir(FileName,start_sector):
    dir.append(FileName)
    sector.append(start_sector)

def deallocate_sectors(start_sector):
    Current_Sector = start_sector
    Finished = False
    while Finished != True:
        if fat[Current_Sector] == 0:
            fat[Current_Sector] = 1
            return
        temp = Current_Sector
        Current_Sector = fat[Current_Sector]
        fat[temp] = 1

def delete_file_from_dir(FileName):
    for i in range(0, len(dir)):
        if dir[i] == FileName:    
            del dir[i]
            temp = sector[i]
            del sector[i]
            return temp

def print_dir():
    for i in range(0, len(dir)):
        print(dir[i], end = " ")
        print(sector[i])

def does_file_exist_in_dir(filename):
    for i in range(0, len(dir)):
        if dir[i] == filename:
            return i
    return -1

def print_sector_chain(start_sector):
    current_sector = int(start_sector)
    while True:
        print(str(current_sector) + " ", end="")
        if fat[current_sector] == 0:
            print()
            return
        current_sector = fat[current_sector]

def main():
    read_fat()
    read_dir()
    print(fat)
    print(dir)
    print(sector)
    while True:

        command = input( ":" )
        command.lower
        if command == "":
            continue
        elif command == "quit":
            break
        cmd = command.split(" ")
        if cmd[0] =="add":
            startsector = first_free_sector()
            add_file_to_dir(cmd[1], startsector)
            allocate_sectors(startsector,int(cmd[2]))
        elif cmd[0] =="delete":
            Del_sector = delete_file_from_dir(cmd[1])
            deallocate_sectors(Del_sector)
        if cmd[0] =="sectors":
            start_sector = does_file_exist_in_dir(cmd[1])
            if start_sector != -1:
                print_sector_chain(start_sector)
            else:
                print("File does not exist")
        if command == "dir":
            print_dir()

        save_dir()
        save_fat()


main()
input()


