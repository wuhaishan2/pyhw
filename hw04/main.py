import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):

        
        html='''
        <html>
        <body>
        <table>
        '''
        for i in range(1, 10):
            html +='<TR>'
            for j in range(1,i+1):
                html +='<TD>%d*%d=%d</TD>' % (i,j,i*j)
                
                
            html +='</TR>'

        html += '''
        </table>
        </body>
        </html>
        '''


        self.write(html)

application = tornado.web.Application([
    (r"/", MainHandler),
], debug=True)

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()

    
