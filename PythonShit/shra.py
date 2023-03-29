f=open('da.txt','w')
f.write('haha!')
f.close()

s=open('net.py','w')
s.write("import os\nos.remove('da.txt')\nos.remove('net.py')")
s.close()

import os
os.startfile('da.txt')
os.startfile('net.py')
