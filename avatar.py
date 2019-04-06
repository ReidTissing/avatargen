from PIL import Image
import cv2

#get input
print("*Building your Avatar*\nEnter 0 for 'No' and 1 for 'Yes'")
pants_option = input("do you want pants? ")
shirt_option = input("do you want a shirt? ")
# print(pants)
body = Image.open("./img/body.png")
head = Image.open("./img/head.png")
pants = Image.open("./img/pants.png")
briefs = Image.open("./img/briefs.png")
shirt = Image.open("./img/shirt.png")

#build a body
Image.alpha_composite(body, head).save("avatar.png")
tmp = Image.open("avatar.png")
Image.alpha_composite(tmp,briefs).save("avatar.png")
if(pants_option == 1):
	tmp = Image.open("avatar.png")
	Image.alpha_composite(tmp, pants).save("avatar.png")
if(shirt_option == 1):
	tmp = Image.open("avatar.png")
	Image.alpha_composite(tmp, shirt).save("avatar.png")
if(shirt_option != 1 and pants_option != 1):
	print("okay, well at least you're wearing underwear.\n")
print("Avatar saved to 'avatar.png'")