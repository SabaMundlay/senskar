import gzip 
import urllib.request

request = urllib.request.Request(
	"https://www.autodraw.com/assets/stencils.json", 
	headers = {
		"Accept-encoding": "gzip",
	})

response = urllib.request.urlopen(request)
gzipFile = gzip.GzipFile(fileobj=response)
gzipFile.read()
