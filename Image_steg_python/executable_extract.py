#!/usr/bin/python3
#load our jpeg file containing our executable in read bytes mode
with open('elliot_mr_robot.jpg', 'rb') as f:
    #add the jpeg file bytes into a variable
    content=f.read()

    #identify the last bytes for the jpeg file
    offset=content.index(bytes.fromhex("FFD9"))

    #get the bytes of the executable after the jpeg bytes
    f.seek(offset + 2)

    #create a file to add the executable bythes, in my case "run_me.exe"
    with open("run_me.exe", "wb") as e:
        #add the bytes into the new file
        e.write(f.read())

print("[+]Executable created")
