#!/usr/bin/python3
import PIL.Image
import io

#lets load our image in read binary 
with open('my_robot.jpg', 'rb') as f:
    #save image bytes into content variable
    content=f.read()

    #find the last instance of the jpeg file
    offset=content.index(bytes.fromhex('FFD9'))

    #lets get the PNG bytes now
    f.seek(offset+2)

    #save the bytes extracted to the new png file using pillow
    new_image=PIL.Image.open(io.BytesIO(f.read()))
    new_image.save("extracted_image.png")

print("[+]Image extracted successfully!!")
