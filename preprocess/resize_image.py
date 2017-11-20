#! /usr/bin/env python

from PIL import Image
import os

target_size = (96, 112)  # Width * height
root_src = 'data/ms_10w_clean'
root_dst = 'data/ms_10w_resize'
width, height = target_size

if not os.path.exists(root_dst):
	os.makedirs(root_dst)

folders  = os.listdir(root_src)
folder_num = len(folders)
for i in range(folder_num)[39700:]:
	if i % 100 == 0:
		print('Resize images in {}/{} folder.'.format(i, folder_num))

	folder = folders[i]
	folder_src = os.path.join(root_src, folder)
	folder_dst = os.path.join(root_dst, folder)

	if not os.path.exists(folder_dst):
		os.makedirs(folder_dst)

	filenames = os.listdir(folder_src)
	for filename in filenames:
		file_src = os.path.join(folder_src, filename)
		file_dst = os.path.join(folder_dst, filename)
		img = Image.open(file_src)
		img = img.resize(target_size, Image.BICUBIC)
		img.save(file_dst)

