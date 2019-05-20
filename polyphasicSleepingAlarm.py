import pygame as pg
import random

#name of the random song
song_list = ['Allegiance.mp3', 'Progenies of the Great Apocalypse.mp3', 'Lepers Among Us.mp3', 'Vredesbyrd.mp3', 'For the World to Dictate Our Death.mp3', 
			'Blood Hunger Doctrine.mp3', 'Allehelgens Dod I Helveds Rike.mp3', 'Cataclysm Children.mp3', 'Eradication Instincts Defined.mp3', 'Unorthodox Manifesto.mp3']

#select a random song from song_list
selected_song = 'songs/{}'.format(song_list[int(random.random() * 10)])

#after 20 minutes start the program
pg.time.wait(2000)						

def open_window():
	#customize the window
	(width, height) = (480, 250)
	background_colour = (105,105,105)

	#display the window
	screen = pg.display.set_mode((width, height))
	screen.fill(background_colour)
	pg.display.flip()

	#set the window's title
	pg.display.set_caption('Alarm')

	#show the name of the song
	pg.font.init()
	my_font = pg.font.SysFont('Comic Sans MS', 30)
	text_surface = my_font.render('{}'.format(selected_song[6:-4]), False, (255, 255, 255))
	screen.blit(text_surface,(27,80))

	#keep the window open
	window_running = True
	while window_running==True:
		#update the song name when the window opens
		pg.display.update()
		for event in pg.event.get():
			if event.type == pg.QUIT or event.type == pg.MOUSEBUTTONDOWN:
				window_running = False
				pg.quit()
			else:
				#set volume of the playback
				volume = 1

				play_music(selected_song, volume)
				window_running = False
				pg.quit()

def play_music(selected_song, volume=0.8):

    #set pygame's mixer
    freq = 44100
    bitsize = -16
    channels = 2
    buffer = 2048
    pg.mixer.init(freq, bitsize, channels, buffer)    
    pg.mixer.music.set_volume(volume)

    clock = pg.time.Clock()

    #check whether file is correct
    try:
        pg.mixer.music.load(selected_song)
        print('Song {} loaded!'.format(selected_song))
    except pg.error:
        print('Song {} not found! ({})'.format(selected_song, pg.get_error()))
        return

    #play the song
    pg.mixer.music.play()
    while pg.mixer.music.get_busy():
        #check if playback has finished
        clock.tick(5)

open_window()