import urllib.request
import urllib.parse
import time

url = 'http://trash.lhsr.cn/sites/feiguan/trashTypes/dyn/Handler/Handler.ashx'
kwd = dict()

with open('chars.txt', 'r') as f:
	chars = f.read()
	chars_valid = list()

for char in chars:
	data = urllib.parse.urlencode({'a':'Keywords_Get', 's_kw':char}).encode('ascii')
	try:
		with urllib.request.urlopen(url, data) as f:
			res = f.read().decode('utf-8')
	except:
		print(char, 'Error')
	else:
		if len(res) > 0:
			kws = eval(res)
			print(char, kws)
			chars_valid.append(char)
			for kw in kws:
				kwd[kw.strip()] = 0
		else:
			print(char, 'No Keywords')
	time.sleep(1)

with open('keywords.txt', 'w') as f:
	for kw in kwd.keys():
		f.write(kw)
		f.write('\n')

with open('chars_valid.txt', 'w') as f:
	f.write(''.join(chars_valid))