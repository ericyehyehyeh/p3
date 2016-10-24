

import os
path = "cd /Desktop/vagrant/Eecs485/p1/"
dirs = os.listdir(path)


import hashlib


for file in dirs:
	category_in = file.split('_')
	if category_in[0] == 'football':
		albumid_in = 2
		filename = file
		m = hashlib.md5()
		m.update(str(albumid_in))
		m.update(filename)
		print albumid_in
		print m.hexdigest()
		category_in[0] = m.hexidigest()
	elif category_in[0] == 'space':
		albumid_in = 4
		filename = file
		m = hashlib.md5()
		m.update(str(albumid_in))
		m.update(filename)
		print albumid_in
		print m.hexdigest()
		category_in[0] = m.hexidigest()
	elif category_in[0] == 'sports':
		albumid_in = 1
		filename = file
		m = hashlib.md5()
		m.update(str(albumid_in))
		m.update(filename)
		print albumid_in
		print m.hexdigest()
		category_in[0] = m.hexidigest()
	elif category_in[0] == 'world':
		albumid_in = 3
		filename = file
		m = hashlib.md5()
		m.update(str(albumid_in))
		m.update(filename)
		print albumid_in
		print m.hexdigest()
		category_in[0] = m.hexidigest()





#url_for('albums.albums_route')

#<picid>.<format>

#<id="album_{{albumid}}_link">
#(albumid is the name of the variable you sent in your python code)