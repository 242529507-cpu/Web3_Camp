import os

#Defini the folders we want creat
folders =[
    "00_Linux_Python",
    "01_Solidity_Basic",
    "02Foundry_Test",
    "99_Daily_Log",
]
print ("staring workspace setup...")

#Look through the list and creat folders
for folder in folders:
     #Check folder in exists
     if not os.path.exists(folder):
        os.mkdir(folder)
        print(f" Created:{folder}")
     else:
        print(f"Exists:{folder}")
print ("Workspace ready!")            
