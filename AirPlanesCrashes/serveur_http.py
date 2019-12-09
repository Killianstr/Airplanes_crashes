#!/usr/bin/python
# -*- coding: latin-1 -*-
import http.server
import socketserver

PORT = 5432
Handler = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(("",PORT), Handler) #adresse à configurer
print("à l'écoute sur le port :", PORT)
httpd.serve_forever()

#source : wikipedia