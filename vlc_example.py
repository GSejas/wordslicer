import vlc
import time
player = vlc.MediaPlayer("sicher.xspf")
player.play()

time.sleep(10)