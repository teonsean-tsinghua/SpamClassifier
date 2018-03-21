count = 64620
root_dir = '.\\data\\data_cut\\'
labels = list()
fp = open('data\\label\\index', 'r')
for line in fp.readlines():
	if line[0] == 's':
		labels.append(True)
	else:
		labels.append(False)

def is_spam(n):
	if n >= count:
		return None
	return labels[n]

def numberToStr3(n):
	return '%03d' % n

def getFilenameByNumber(n):
	return root_dir + numberToStr3(n // 300) + '\\' + numberToStr3(n % 300)

def filterCharacter(content):
	re = ''
	has_space = False
	for i in range(len(content)):
		uchar = content[i]
		if uchar >= u'\u4e00' and uchar <= u'\u9fa5':
			re = re + uchar
			has_space = False
		elif not has_space:
			re = re + u' '
			has_space = True
	return re

def getWords(n):
	if n >= count:
		return None
	fp = open(getFilenameByNumber(n), encoding='utf-8')
	words = filterCharacter(fp.read()).split(' ')
	words = [word for word in words if not word == '']
	return words
