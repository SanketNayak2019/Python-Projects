import PIL
from PIL import Image,ImageEnhance,ImageDraw,ImageFont
from IPython import display


# read image and convert to RGB
image=Image.open("readonly/msi_recruitment.gif")
image=image.convert('RGB')

#Set up intensity values and fonts
intensities = (0.1,0.5,0.9)
myfont = ImageFont.truetype('readonly/fanwood-webfont.ttf',50)

#Add bottom black segment for text display
extender = PIL.Image.new(image.mode,(image.width,image.height + 70))
extender.paste(image,(0,0))
image = extender

#Modify image and populate images list
images=[]
for chanNum in range(3):
    for intensity in intensities:
        new_image = image.copy()
        textEdit = ImageDraw.Draw(new_image)
        textEdit.text((0.1*image.width,0.9*image.height),'channel {} intensity {}'.format(str(chanNum),str(intensity)),font=myfont)
        new_channels = list(new_image.split())
        new_channels[chanNum] = new_channels[chanNum].point(lambda v: v*intensity)
        images.append(Image.merge('RGB',new_channels))

    
# create a contact sheet from different brightnesses
first_image=images[0]
contact_sheet=PIL.Image.new(first_image.mode, (first_image.width*3,first_image.height*3))
x=0
y=0

for img in images:
    # Lets paste the current image into the contact sheet
    contact_sheet.paste(img, (x, y) )
    
    # Now we update our X position. If it is going to be the width of the image, then we set it to 0
    # and update Y as well to point to the next "line" of the contact sheet.
    if x+first_image.width == contact_sheet.width:
        x=0
        y=y+first_image.height
    else:
        x=x+first_image.width

# resize and display the contact sheet
contact_sheet = contact_sheet.resize((int(contact_sheet.width/2),int(contact_sheet.height/2) ))
display(contact_sheet)


