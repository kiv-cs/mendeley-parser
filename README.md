# Mendeley.com parser

This script parses http://www.mendeley.com and extracts articles metadata (year and title).

"Mendeley is a free reference manager and academic social network that can help you organize your research, collaborate with others online, and discover the latest research."
## Requirements

1. Python 2.7 http://www.python.org/
2. Beautiful Soup 4 python library http://www.crummy.com/software/BeautifulSoup/

## Usage
Read comments in script, configure parser and run it
<pre>
python mendeley_parser.py
</pre>
Output csv file formst:
<pre>
page_number [tab] year [tab] title [tab] author [, ] author
</pre>

---
BTW, they have API http://dev.mendeley.com/