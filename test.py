import cgi
def application(environ, start_response):
	fields = cgi.FieldStorage(environ['wsgi.input'],
	environ=environ)

	name = fields.getvalue("one")
	name2 = fields.getvalue("two")
	status = "200 OK"
	headers = [('Content-type','text/plain')]
	start_response(status, headers)

	response = ['Hello World!\n', 'Query test : %s' % name, ' and %s' % name2]
	return (line.encode('utf-8') for line in response)
