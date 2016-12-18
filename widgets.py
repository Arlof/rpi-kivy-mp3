# Files Name : widgets.py

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.audio import SoundLoader
from kivy.clock import Clock			## Timing For Events
from kivy.properties import ObjectProperty, StringProperty

import os
import random
import time					## Time For Clock


#sound = SoundLoader.load('song.mp3')


class MyWidget(Widget):
    sound = SoundLoader.load('song.mp3')

    
    def update_time(self):
	self.ids.time_clock.text = time.asctime()



    def position_display(self, fuck):
	if self.sound.get_pos() != 0:
	    #print ("Sound is %.1f / %.1f seconds" % (self.sound.get_pos(),self.sound.length))
	    self.ids.track_position.text = "%.1f / %.1f seconds" % (self.sound.get_pos(),self.sound.length)
	

    def play_music(self, btn):			# btn is the object details being passed
	print(btn.text)
	btn.text = 'STOP'
        print("Play Button Pressed")
        self.sound.play()
	self.ids.label_filename.text = self.sound.source
	print(dir(self))

    def pause_music(self, btn):
	print("Pause Button Pressed")
	self.sound.stop()

    def mute_volume(self, btn):
	print("Muted Pressed")
	if self.sound.volume > 0:
	    self.sound.volume = 0
	else:
	    self.sound.volume = 1
	
 
    def exit(self, btn):
	print("Exiting")
	quit(1)

    def song_details(self):
	#print(str(self.sound.get_pos()))
	#print(self.sound.source)
	self.ids.label_filename.text = self.sound.source

    def random_song(self, btn):
	file_list = os.listdir("/home/pi/Music")
	seed = (random.randint(0,len(file_list))-1)	# Adding -1 To Offset Index
	print(seed)
	print(file_list[seed])
	rando = ('/home/pi/Music/'+file_list[seed])
	print(rando)
		
	self.sound.stop()
	self.sound.unload()
	self.sound = None

	
	#sound.stop()
        #sound.unload()
        self.sound = SoundLoader.load(rando)
	self.sound.play()
	self.ids.label_filename.text = rando

    def update_test(self, fuck):
	self.update_time()

class WidgetsApp(App):

#    def on_start(self):
#	print("StartFart\n")
#	Clock.schedule_interval(screen.update_test, 1)
#	dir(self)


    def build(self):
	
	screen = MyWidget()
	Clock.schedule_interval(screen.update_test, 1)
	Clock.schedule_interval(screen.position_display,0.1)
	return screen

#    if sound:
#	print("Sound Found at %s \n" % sound.source)
#	print("Sound is %.3f seconds" % sound.length)
	#sound.play()


if __name__=="__main__":
    WidgetsApp().run()

