import urllib.request, csv, sys, re

url = 'https://www.ncbi.nlm.nih.gov{}'
filename = sys.argv[1]
results = []
tag = sys.argv[2]

with open('../pubmed-results/' + filename, 'r') as f:
	reader = csv.reader(f)
	articles = list(reader)
	count = 0

filename = filename.replace('.csv', '')

with open('../output/' + filename, 'w') as f:
	for article in articles:
		if article[0] == 'Title':
			continue
		count += 1
		print(str(count) + '. ' + article[0])
		article_page = ''.join(urllib.request.urlopen(url.format(article[1])).read().decode('utf-8').splitlines())
		doi = re.search('<a href="(?P<doi>//doi.org/[a-zA-Z0-9./-]+)" ref="aid_type=doi">', article_page)
		if doi is None:
			doi_link = ''
		else:
			doi_link = 'https:' + doi.group('doi')
		result = '\t'.join([doi_link, url.format(article[1]), ' ', tag, article[0]])
		result += '\n'
		f.write(result)