from random import randint
import cherrypy
def tayFact(fname):
    file = open(fname)
    content = file.readlines()
    content = [x.strip() for x in content]
    return content
@cherrypy.expose
class factGrabber(object):
    @cherrypy.tools.accept(media='text/plain')
    def GET(self):
        allFacts = tayFact('TayTayFacts.txt')
        return cherrypy.session[allFacts[randint(0,len(allFacts))]]

    def POST(self):
        theFacts = tayFact('TayTayFacts.txt')
        cherrypy.session['mystring'] = theFacts[randint(0, len(theFacts))]
        return theFacts[randint(0, len(theFacts))]
conf = {
        '/': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.sessions.on': True,
            'tools.response_headers.on': True,
            'tools.response_headers.headers': [('Content-Type', 'text/plain')],
        }
    }

cherrypy.quickstart(factGrabber(),'/',conf)
