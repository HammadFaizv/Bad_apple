import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

# Loop through each file and print its contents
for i in range(1,6573):
    file_name = "./Ascii_Frames/Aframe_" + str(i) + ".txt"
    with open(file_name, 'r') as file:
        file_contents = file.read()
        print(file_contents)
    
    # Clear the console before proceeding to the next file
    clear_console()