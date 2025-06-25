#!/usr/bin/python3
import PIL.Image
import io

#lets load our PNG file using pillow
img=PIL.Image.open('toy_story.png')
#the bytes is set to empty
byte_arr=io.BytesIO()
#lets save our PNG image data to the byte array above we created using the io library
img.save(byte_arr, format='PNG')

#now lets load our JPEG file in append binary
with open('my_robot.jpg', 'ab')as f:
    #now add the img byte array creaded above into our image
    f.write(byte_arr.getvalue())

print("[+]Steg Complete")
