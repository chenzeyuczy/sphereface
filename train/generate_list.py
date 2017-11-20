#! /usr/bin/env python

import os

root_folder = './data/ms_10w_resize'
dataset_name = os.path.basename(root_folder.rstrip(os.sep))
list_file = './data/{}_list.txt'.format(dataset_name)

f = open(list_file, 'w')
folders = os.listdir(root_folder)
for i in xrange(len(folders)):
	folder_path = os.path.join(root_folder, folders[i])
	filenames = os.listdir(folder_path)
	for filename in filenames:
		file_path = os.path.join(folder_path, filename)
		line = '{} {}\n'.format(file_path, i)
		f.write(line)
f.close()

