import os
import time
import requests
from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.parse as urlparse


# PERFECTCOUNTER
# A hyper-basic Python relay
# For Winamp POST and mastodon
# interoperability.
# 
# Winamp ATF formatting is
# *REQUIRED* for this to 
# work. Tune at your
# liesure. 



# # # # #
# TODO:
# - Add HTTPS!
# - Add better logging!
# # # # #



os.chdir('.')

class handler(BaseHTTPRequestHandler):
    def log_message(self, format, *args):
        # Prevent this from filling stdout so we can debug properly
        pass

    def do_POST(self):
        global oldTime
        # Put your URL here
        endpoint = 'https://some.instance/api/v1/statuses'
        # Roll a bearer token and slap it in here,
        # or don't. I can't tell you what to do. 
        headers = {'Authorization':'Bearer '}
        # Clear these three to prevent bleedover if the media's changed
        track = ""
        album = ""
        artist = ""
        # Check cgi-like path parameters
        path = self.path
        print(path)
        
        #OPTIONAL:
        # This trims the path's first
        # two characters if you're like
        # me and added ?/ to it lol
        #
        # trimmedPath = path[2:]

        
        # check fields
        fields = urlparse.parse_qs(trimmedPath)
        # Debug print these to stdout
        print(fields)
        if "local" in fields['type'] and time.time() - oldTime >= 1800:
            print("Normal File")
            track = fields['track'][0]
            album = fields['album'][0]
            artist = fields['artist'][0]
            # construct the string
            constructed = "Now Playing: " + track + " ~ " + album + "\n" + artist + "\n\n#PERFECTCOUNTER ^w^"
            print(constructed)
            # set status field
            data = {'status':constructed}
            # send request, print response
            response = requests.post(endpoint, headers=headers, data=data)
            print(response)
            # 30 minute cooldown
            oldTime = time.time()
        elif "stream" in fields['type'] and time.time()- oldTime >= 1800:
            # lol
            print("Streaming via SHOUTCast/Icecast")
            track = fields['track'][0]
            # get stream URL
            url = fields['streamUrl'][0]
            constructed = "Now Streaming: " + track + "\n" + url + "\n\n#PERFECTCOUNTER ✧w✧ "
            print(constructed)
            data = {'status':constructed}
            # should 'just work'. No extra parsing required
            response = requests.post(endpoint, headers=headers, data=data)
            print(response)
            oldTime = time.time()
        elif "tracker" in fields['type'] and time.time()- oldTime >= 1800:
            print("Tracker File")
            track = fields['track'][0]
            try:
                artist = fields['artist'][0]
            except:
                pass;
            # some tracker files have artist tags
            # so we take that and run.
            if artist == "":
                constructed = "Now Playing: " + track + "\nType: Tracker File\n\n#PERFECTCOUNTER >w< "
            else:
                constructed = "Now Playing: " + track + "\n" + artist + "\nType: Tracker File\n\n#PERFECTCOUNTER >w< "
            print(constructed)
            data = {'status':constructed}
            response = requests.post(endpoint, headers=headers, data=data)
            print(response)
            oldTime = time.time()
               
        
with HTTPServer(('', 8080), handler) as server:
    # resetting the 30 minute cooldown
    # on startup.
    global oldTime
    oldTime=time.time()
    oldTime=oldTime - 1800
    server.serve_forever()
