from twisted.internet import reactor
from twisted.web.server import Site
from twisted.web.resource import Resource
import mysql.connector

class WebApp(Resource):
    isLeaf = True
    def render_GET(self, request):

        cnx = mysql.connector.connect(host='10.0.2.9', user='webapp_user', passwd='Pa$$word123', database='webappdb',auth_plugin='mysql_native_password')
        cursor = cnx.cursor()
        sql_req = b"SELECT greeting FROM webappdb.greetings WHERE name='" + request.args[b'name'][0] + b"';"
        print(sql_req)

        greeting = "".encode("utf-8")
        results = cursor.execute(sql_req, multi=True)
        if results:
            for result in results:
                if result.with_rows:
                    greeting = result.fetchall()[0][0].encode("utf-8")


        cnx.commit()
        cursor.close()
        cnx.close()
        cnx.disconnect()

        return b'' + bytearray(greeting) + b' ' + request.args[b'name'][0] + b'!'

factory = Site(WebApp())
reactor.listenTCP(8880, factory)
reactor.run()
