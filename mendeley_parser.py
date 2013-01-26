# -*- coding:utf-8 -*-

# parses http://www.mendeley.com
# extracts articles metadata

from bs4 import BeautifulSoup
import urllib2
import os

# ============================================================= #
#
# this is initial instructions for parser
# 'theme' - theme name in url
# themes (disciplines) list are here http://www.mendeley.com/research-papers/ ("Browse disciplines" section)
# example url http://www.mendeley.com/research-papers/electrical-and-electronic-engineering/miscellaneous/a/0/
# 'letters' - for each letter in theme 
# parse from page (including) to page (excluding)
#
# ============================================================= #

theme_description = {
	'theme': 'electrical-and-electronic-engineering',
	'letters': {
		#'a':(0,1611), # DONE
		#'b':(0,240), # DONE
		#'c':(0,817), # DONE
		#'d':(0,615), # DONE
		#'e':(0,724), # DONE
		#'f':(0,396), # DONE
		#'g':(0,225), # DONE
		#'h':(0,299), # DONE
		#'i':(0,556), # DONE
		#'j':(0,20), # DONE
		#'k':(0,31), # DONE
		#'l':(0,290), # DONE
		#'m':(0,696), # DONE
		#'n':(0,332), # DONE
		#'o':(0,380), # DONE
		#'p':(521,625), # DONE
		#'q':(0,74), # DONE
		#'r':(0,468), # DONE
		#'s':(0,973), # DONE
		't':(346,913),
		#'u':(0,175),
		#'v':(0,139),
		#'w':(0,141),
		#'x':(0,8),
		#'y':(0,5),
		#'z':(0,11),
		#'other':(0,70)
	}
}

# ============================================================= #

# min year for filter articles

min_year = 2011

# ============================================================= #

def parse_page(theme, letter, page_number):
	timeout = None 
	if page_number % 10 == 0:
		timeout = 60
		print '<timout>'
	myurl = urllib2.urlopen('http://www.mendeley.com/research-papers/%s/miscellaneous/%s/%s/' % (theme, letter, str(page_number)), None, timeout)
	html_doc = myurl.read()
	outdir = './output/%s' % theme
	if not os.path.exists(outdir):
		os.makedirs(outdir)
	output = open( '%s/%s-%s.csv' % (outdir, theme, letter), 'a')

	soup = BeautifulSoup(html_doc)
	articles = soup.find_all('article')

	for article in articles:
		year = article.find('span', {'class':'year'})
		year = int(year.contents[0][1:-1])
		if year >= min_year:
			title_div = article.find('div', {'class':'title'})
			title = title_div.a.contents[0]
			
			authors_span = article.find('span', {'class':'authors'})
			author_spans = authors_span.find_all('span', {'class':'author'})
			authors = ''
			for span in author_spans:
				authors += span.contents[0]+', '
			authors = authors[:-2]

			output.write('%s\t%s\t%s\t%s\n' % (page_number, year, title.encode('utf-8'), authors.encode('utf-8')))

	myurl.close()
	output.close()
	print letter, page_number, 'DONE'

for letter in theme_description['letters']:
	pages_from, pages_to = theme_description['letters'][letter]
	for page_number in range(pages_from, pages_to):
		parse_page(theme_description['theme'], letter, page_number)




# article metadata example
'''
<article class="clearfix item document " data-doc="{&quot;title&quot;:&quot;A \&quot;flight data recorder\&quot; for enabling full-system multiprocessor deterministic replay&quot;,&quot;series&quot;:&quot;ISCA '03&quot;,&quot;identifiers&quot;:{&quot;issn&quot;:&quot;01635964&quot;,&quot;isbn&quot;:&quot;0769519458&quot;,&quot;doi&quot;:&quot;10.1145\/871656.859633&quot;},&quot;issue&quot;:&quot;2&quot;,&quot;type&quot;:&quot;journal&quot;,&quot;published_in&quot;:&quot;ACM SIGARCH Computer Architecture News&quot;,&quot;publisher&quot;:&quot;ACM&quot;,&quot;year&quot;:2003,&quot;oa_journal&quot;:false,&quot;website&quot;:&quot;http:\/\/portal.acm.org\/citation.cfm?doid=871656.859633&quot;,&quot;pages&quot;:&quot;122&quot;,&quot;url&quot;:&quot;flight-data-recorder-enabling-full-system-multiprocessor-deterministic-replay-1&quot;,&quot;volume&quot;:&quot;31&quot;,&quot;full_url&quot;:&quot;\/research\/flight-data-recorder-enabling-full-system-multiprocessor-deterministic-replay-1\/&quot;,&quot;canonicalId&quot;:&quot;482b5070-6d00-11df-a2b2-0026b95e3eb7&quot;}" id="document-482b5070-6d00-11df-a2b2-0026b95e3eb7">
<div class="item-info">
<div class="title">
<a data-dm-log-click='{"event":"click","page":"subdiscipline","data[]":["Title"]}' href="/research/flight-data-recorder-enabling-full-system-multiprocessor-deterministic-replay-1/" target="_parent" title='A "flight data recorder" for enabling full-system multiprocessor deterministic replay'>A "flight data recorder" for enabling full-system multiprocessor deterministic replay</a>
</div>
<span class="Z3988" title="ctx_ver=Z39.88-2004&amp;rfr_id=info%3Asid%2Fmendeley.com%2Fmendeley&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Ajournal&amp;rft.genre=article&amp;rft.date=2003&amp;rft.volume=31&amp;rft.issue=2&amp;rft.pages=122&amp;rft.atitle=A+%22flight+data+recorder%22+for+enabling+full-system+multiprocessor+deterministic+replay&amp;rft.jtitle=ACM+SIGARCH+Computer+Architecture+News&amp;rft.title=ACM+SIGARCH+Computer+Architecture+News&amp;rft.aulast=Xu&amp;rft.aufirst=Min&amp;rft.au=Bodik%2C+Rastislav&amp;rft.au=Hill%2C+Mark+D&amp;rft_id=info%3Adoi%2F10.1145%2F871656.859633&amp;rft.issn=01635964&amp;rft.isbn=0769519458"></span>
<div class="metadata">
<span class="authors">
<span class="author">Min Xu</span><span class="sep">, </span> <span class="author">Rastislav Bodik</span><span class="sep">, </span> <span class="author">Mark D Hill</span> </span>
<span class="sep">in</span> <span class="publication">ACM SIGARCH Computer Architecture News</span>
<span class="year">(2003)</span> </div>
<div class="abstract">Debuggers have been proven indispensable in improving software reliability. Unfortunately, on most real-life software, debuggers fail to deliver their most essential feature a faithful replay of the execution. The reason is non-determinism caused by…</div>
<div class="item-footer article-footer unfloat">
<span class="actions">
<a class="add_button addbtn_482b5070-6d00-11df-a2b2-0026b95e3eb7" data-addedtolibrary="Mendeley.Collection.handleCanonicalDocumentAddList" data-dm-log-click='{"event":"click","page":"subdiscipline","data[]":["AddToLibrary"]}' data-join-overlay="document-add-to-library" href="#">
<span class="addlib addtext_482b5070-6d00-11df-a2b2-0026b95e3eb7"><strong>Save reference</strong> to library</span>
</a>
<span class="slug">·</span> <a data-dm-log-click='{"event":"click","page":"subdiscipline","data[]":["MoreLikeThis"]}' href="/research-papers/?rec=flight-data-recorder-enabling-full-system-multiprocessor-deterministic-replay-1" rel="nofollow">
<span><strong>Related</strong> research</span>
</a>
</span>
<span class="counts">
<span class="reader-count" title="27 readers on Mendeley"><strong>27</strong> readers</span>
</span>
</div>
</div>
</article>
'''