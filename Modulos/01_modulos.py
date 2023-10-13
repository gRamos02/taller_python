import sys
print(sys.version)

import re
text = 'Mi numero de telefono es 871 123 321, el codigo de pais es 52, mi numero de la suerte el 6'
result = re.findall('[0-9]+',text)
print(result)

import time
timestamp = time.time()
local = time.localtime()
result_time = time.asctime(local)
print(timestamp)
print(result_time)

import collections
numbers = [1,1,2,1,2,1,3,3,4,5,21,3]
counter = collections.Counter(numbers)
print(counter)