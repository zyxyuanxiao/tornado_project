# 此文件为程序的入口文件
import tornado.ioloop
import tornado.options
import tornado.httpserver

from application import application

from tornado.options import define, options
import configparser

cf = configparser.ConfigParser()
cf.read("conf/default.conf")

define("port", default=cf.get("server", "port"), help="run on th given port", type=int)


def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    print('Development server is running at http://127.0.0.1:{}'.format(options.port))
    print('Quit the server with Control-C')
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()
