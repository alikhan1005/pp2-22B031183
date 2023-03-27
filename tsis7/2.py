import pygame 
import os 

pygame.init() 

screen = pygame.display.set_mode((500, 300)) 
pygame.display.set_caption("Music Player") 
 
font = pygame.font.Font(None, 30) 
 
music_dir = "/Users/alikhankudaibergen/Documents/music/" 
songs = os.listdir(music_dir) 
current_song_index = 0
pygame.mixer.music.load(os.path.join(music_dir, songs[current_song_index])) 

def play(): 
    pygame.mixer.music.play() 
 
def stop(): 
    pygame.mixer.music.stop() 

def next_song(): 
    global current_song_index 
    current_song_index = (current_song_index + 1) % len(songs) 
    pygame.mixer.music.load(os.path.join(music_dir, songs[current_song_index])) 
    pygame.mixer.music.play() 
 
def prev_song(): 
    global current_song_index 
    current_song_index = (current_song_index - 1) % len(songs) 
    pygame.mixer.music.load(os.path.join(music_dir, songs[current_song_index])) 
    pygame.mixer.music.play() 
 
running = True 
while running: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_SPACE: 
                play() 
            elif event.key == pygame.K_DOWN: 
                stop() 
            elif event.key == pygame.K_RIGHT: 
                next_song() 
            elif event.key == pygame.K_LEFT: 
                prev_song() 

    screen.fill((0, 255, 0)) 
 
    song_name = font.render(songs[current_song_index], True, (0, 0, 0)) 

    screen.blit(song_name, (10, 10)) 

    pygame.display.flip() 