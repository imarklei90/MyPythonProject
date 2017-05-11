import urllib2
import re

webPage = urllib2.urlopen('http://www.python.org')

content = webPage.read()
m = re.search('<a href="([^"]+)" .*?>about</a>', content, re.IGNORECASE)
print  m.group(1)


