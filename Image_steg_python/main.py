#/usr/bin/python3

#lets open our image file as binary in our program
with open('my_robot.jpg', 'ab') as f:
    f.write(b"Hello World")

