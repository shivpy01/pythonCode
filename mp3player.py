import pygame
import tkinter as tkr
import os


'''Create window'''
player = tkr.Tk()


'''edit window'''
player.title('Auddio Player')
player.geometry('205x340')


"""REgister Playlist"""
os.chdir(r'C:\Users\Shivam\Music')
songlist = os.listdir()


"""volume Input"""
volumeLabel = tkr.Scale(player,from_= 0.0 , to_= 1.0,orient = tkr.HORIZONTAL, resolution = 0.1)


"""Playlist Input"""
playlist = tkr.Listbox(player,highlightcolor = 'blue',selectmode = tkr.SINGLE )
print(playlist)
for item in songlist:
    pos = 0
    playlist.insert(pos,item)
    post = pos +1


"""pygame init"""
pygame.init()
pygame.mixer.init()
    
    
"""Action Event"""
def play():
    pygame.mixer.music.load(playlist.get(tkr.ACTIVE))
    var.set(playlist.get(tkr.ACTIVE))
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(volumeLabel.get())
    print(pygame.mixer.music.get_volume())
    print(volumeLabel.get())

    
def ExitPlayer():
    pygame.mixer.music.stop()
    
    
def Pause():
    pygame.mixer.music.pause()
    
    
def Unpause():
      pygame.mixer.music.unpause()

        
'''Register Buttons'''
Button1=tkr.Button(player,width = 5,height = 3,text = 'PLAY',command = play)
Button2=tkr.Button(player,width = 5,height = 3,text = 'STOP',command = ExitPlayer)
Button3=tkr.Button(player,width = 5,height = 3,text = 'PAUSE',command = Pause)
Button4=tkr.Button(player,width = 5,height = 3,text = 'UNPAUSE',command = Unpause)


"""Song Name"""
var = tkr.StringVar()
songtitle = tkr.Label(player,textvariable = var)


"""Place Widget"""
Button1.pack(fill = 'x')
Button3.pack(fill = 'x')
Button4.pack(fill = 'x')
Button2.pack(fill = 'x')
volumeLabel.pack(fill = 'x')
songtitle.pack()
playlist.pack(fill = 'both' ,expand = 'no')


"""activate"""
player.mainloop()
