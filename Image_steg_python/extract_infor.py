#!/usr/bin/python3

#we now load our image in read bytes
with open('my_robot.jpg', 'rb') as f:
    #lets save the byte contents of the JPEG file into a variable
    content=f.read()  

    #lets look where the end of the jpeg file occurs and convert to bytes from hex
    offset=content.index(bytes.fromhex('FFD9'))

    #lets get the end of the jpeg file and read what comes after
    f.seek(offset+2)

    print(f.read())


