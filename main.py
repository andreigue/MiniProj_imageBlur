'''
as per the following tutorial:
https://www.youtube.com/watch?v=2Bz-aastGk0

'''

'''
TODO:
    
add function for the repeated part
fix third image (the one is subdir)

'''


from PIL import Image, ImageFilter
import os

cwd = os.getcwd()                   #make sure have correct dir
#print("current directory: " + cwd)


#loop through all dirs and subdirs as well
for root, dirs, files in os.walk(cwd):
    for file in files:
        if file.endswith('.jpg'):
            print(os.path.join(root, file))
            image = Image.open(file)         #original image
            #image.show()                        #display image
            cropped_image = image.crop((97,91,311,307))         #crop rectangle (used MS Paint to figure out coords)
            #cropped_image.show()
            blurred_image = cropped_image.filter(ImageFilter.GaussianBlur(radius=3))    #increase radius to blur more    
            #blurred_image.show()
            image.paste(blurred_image,(97,91,311,307))      #pass image we are pasting and the coordinates
            image.show()
'''

for file in os.listdir(cwd):
    if file.endswith(".jpg"):
        print(os.path.join(cwd, file))
        image = Image.open(file)         #original image
        #image.show()                        #display image
        cropped_image = image.crop((97,91,311,307))         #crop rectangle (used MS Paint to figure out coords)
        #cropped_image.show()
        blurred_image = cropped_image.filter(ImageFilter.GaussianBlur(radius=3))    #increase radius to blur more    
        #blurred_image.show()
        image.paste(blurred_image,(97,91,311,307))      #pass image we are pasting and the coordinates
        image.show()
'''