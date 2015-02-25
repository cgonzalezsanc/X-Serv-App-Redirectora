#!/usr/bin/python

import webapp
import random


class otroServidor(webapp.webApp):

    def process(self, parsedRequest):

        rand = random.randint(1, 100000000)
        htmlAnswer = '<html><body><head>Estas siendo redirigido a /'
        htmlAnswer = htmlAnswer + str(rand) + '<meta http-equiv="refresh"' 
        htmlAnswer = htmlAnswer + 'content="1; url=' + str(rand) + '" />'
        return("307 Temporary Redirect", htmlAnswer)


if __name__ == "__main__":
    serv = otroServidor("localhost", 1234)
