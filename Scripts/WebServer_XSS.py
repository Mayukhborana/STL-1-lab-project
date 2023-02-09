from twisted.internet import reactor
from twisted.web.server import Site
from twisted.web.resource import Resource

class WebApp(Resource):
    isLeaf = True
    def render_GET(self, request):
        return b'Hello!'

factory = Site(WebApp())
reactor.listenTCP(8880, factory)
reactor.run()