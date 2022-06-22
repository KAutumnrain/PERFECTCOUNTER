# PERFECTCOUNTER
A python relay to allow Winamp POST and Mastodon interoperability.

## DISCLAIMER
This isn't finished, has some niche behavior, ***and also doesn't support HTTPS yet.***
Use this only in a controlled environment for the time being, as it was written in the 
span of like an hour. 

## Usage
PERFECTCOUNTER requires Python 3.9+.
- Generate your bearer token on your mastodon instance of choice
- Put that in the headers variable, like so: {'Authorization': 'Bearer (YOUR TOKEN GOES HERE)'}
- Change the endpoint URL to whatever yours is
- If you're using WACUP or Winamp 5.666, Go to Preferences>Playback>Play Tracking> HTTP(S) POST
  and drop in the ATF string found in winampATF.txt of this repo.
- Enable the POST functionality on that same page
- Change address:port to whatever you're putting this script on
- Run it and enjoy
  
 *Theoretically* this should work without issue.


## Images
Example Mastodon output:

![image](https://user-images.githubusercontent.com/101837956/175056938-799cc119-6337-4bd6-9a68-602137d7fef4.png)


Example ATF output on [WACUP](https://getwacup.com/):

![image](https://user-images.githubusercontent.com/101837956/175054606-c23369d6-ecf7-4577-983d-64e6b8e7e5f2.png)





