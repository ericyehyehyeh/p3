import os
path = "cd ~/Desktop/vagrant/Eecs485/p2/"
dirs = os.listdir(path)


import hashlib
import uuid

algorithm = 'sha512'     
password = 'bob1pass'  #need to get info from user submit on login page  
salt = uuid.uuid4().hex 

m = hashlib.new(algorithm)
m.update(salt + password)
password_hash = m.hexdigest()

print "$".join([algorithm,salt,password_hash])
