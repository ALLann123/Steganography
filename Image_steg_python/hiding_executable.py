#!/usr/bin/python3

#load the jpeg file in appending bytes(ap) while the executable in reading bytes
with open('elliot_mr_robot.jpg', 'ab') as f, open('add_numbers.exe', 'rb') as e:
    #lets write the executable into the jpeg file
    f.write(e.read())

print("[+]Steg worked!!")



