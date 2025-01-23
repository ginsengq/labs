import pygame

pygame.init()
pygame.mixer.init()

size = width, height = 700, 700
screen = pygame.display.set_mode(size)
pygame.display.set_caption("player")
pygame.display.set_icon(pygame.image.load("lab7/imgsnd/3image.png"))

background = pygame.image.load("lab7/imgsnd/4image.jpg")

tracks = ["lab7/imgsnd/yunglean-yoshicity.mp3", "lab7/imgsnd/kanyewest-iwonder.mp3", "lab7/imgsnd/elusin-highway.mp3"]
current_track_index = 0

play = pygame.image.load("lab7/imgsnd/play.png")
play = pygame.transform.scale(play, (70, 70))
pause = pygame.image.load("lab7/imgsnd/pause.png")
pause = pygame.transform.scale(pause, (70, 70))
stop = pygame.image.load("lab7/imgsnd/stop.png")
stop = pygame.transform.scale(stop, (70, 70))
next_img = pygame.image.load("lab7/imgsnd/next.png")
next_img = pygame.transform.scale(next_img, (70, 70))
previous_img = pygame.image.load("lab7/imgsnd/previous.png")
previous_img = pygame.transform.scale(previous_img, (70, 70))

button_y = height // 2 - play.get_height() // 2
button_spacing = 20
button_total_width = play.get_width() + pause.get_width() + stop.get_width() + next_img.get_width() + previous_img.get_width() + 4 * button_spacing
start_x = (width - button_total_width) // 2

play_button_x = start_x
pause_button_x = play_button_x + play.get_width() + button_spacing
stop_button_x = pause_button_x + pause.get_width() + button_spacing
previous_button_x = stop_button_x + stop.get_width() + button_spacing
next_button_x = previous_button_x + previous_img.get_width() + button_spacing

playing = False
paused = False

def play_current_track():
    pygame.mixer.music.load(tracks[current_track_index])
    pygame.mixer.music.play()
    return True

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if play_button_x <= mouse_x <= play_button_x + play.get_width() and button_y <= mouse_y <= button_y + play.get_height():
                if not playing:
                    playing = play_current_track()
                    paused = False
            elif pause_button_x <= mouse_x <= pause_button_x + pause.get_width() and button_y <= mouse_y <= button_y + pause.get_height():
                if playing and not paused:
                    pygame.mixer.music.pause()
                    playing = False
                    paused = True
            elif stop_button_x <= mouse_x <= stop_button_x + stop.get_width() and button_y <= mouse_y <= button_y + stop.get_height():
                if playing:
                    pygame.mixer.music.stop()
                    playing = False
                    paused = False
            elif next_button_x <= mouse_x <= next_button_x + next_img.get_width() and button_y <= mouse_y <= button_y + next_img.get_height():
                if playing:
                    pygame.mixer.music.stop()
                    current_track_index = (current_track_index + 1) % len(tracks)
                    playing = play_current_track()
                    paused = False
            elif previous_button_x <= mouse_x <= previous_button_x + previous_img.get_width() and button_y <= mouse_y <= button_y + previous_img.get_height():
                if playing:
                    pygame.mixer.music.stop()
                    current_track_index = (current_track_index - 1) % len(tracks)
                    playing = play_current_track()
                    paused = False

    screen.blit(background, (0, 0))
    screen.blit(play, (play_button_x, button_y))
    screen.blit(pause, (pause_button_x, button_y))
    screen.blit(stop, (stop_button_x, button_y))
    screen.blit(previous_img, (previous_button_x, button_y))
    screen.blit(next_img, (next_button_x, button_y))
    pygame.display.flip()

pygame.quit()
