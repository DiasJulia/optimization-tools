# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os
from subprocess import run
from glob import glob

img_list = []
for img in glob('./*'):
	if img.endswith(".jpg") or img.endswith(".png") or img.endswith(".jpeg"):
		img_list.append(img.split('\\')[-1])

if(not os.path.isdir('./webp')):
	os.mkdir('./webp')

for img in img_list:
	command = 'cwebp \"'
	command += './' + img + '\" -o \"./webp/' +(img.split('.')[0])+'.webp\"'

	run(command, shell=True)
