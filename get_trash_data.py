from bs4 import BeautifulSoup
import urllib.request
import urllib.parse
import time

base_url = 'http://trash.lhsr.cn/sites/feiguan/trashTypes_2/TrashQuery.aspx?'

kwd = dict()

with open('keywords.txt', 'r') as f:
	for l in f:
		kwd[l.strip()] = 'N/A'

for kw in kwd.keys():
	url = base_url + urllib.parse.urlencode({'kw': kw})
	try:
		with urllib.request.urlopen(url) as f:
			res = f.read().decode('utf-8')
			soup = BeautifulSoup(res, 'html.parser')
	except:
		print(kw, 'Error')
	else:
		t_info = soup.find('div', class_='info')
		if t_info is not None:
			t_info_desc = t_info.find('span').get_text()

		else:
			t_info = soup.find('p', class_='txt')
			if t_info is not None:
				if t_info.find('font') is not None:
					t_info_desc = t_info.find('font').get_text()
				else:
					t_info_desc = '非生活垃圾'
			else:
				t_info_desc = 'N/A'

		print(kw, t_info_desc)

		kwd[kw] = t_info_desc

	time.sleep(1)

with open('trash_info.csv', 'w') as f:
	for kw in kwd.keys():
		f.write(','.join([kw, kwd[kw]]))
		f.write('\n')

