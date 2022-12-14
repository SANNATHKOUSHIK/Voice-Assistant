import os
while True:
    cmdlist = os.system('cmd /k"tasklist"')
    if "explorer.exe" in cmdlist:
        break
    

