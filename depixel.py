import sys
import os

for i in sys.argv[1:]:
	os.system("potrace -b svg -b pdf " + str(i))