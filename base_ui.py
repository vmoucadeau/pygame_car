import pygame

scr_size = (1000, 600)
scr = pygame.display.set_mode(scr_size)

def UI_drawbackground():
    background_color = (125, 125, 125)
    bg = pygame.Surface(scr_size)
    bg.fill(background_color)
    return bg

def UI_drawcar(pos_x, pos_y):
    img_path = "sprites/Audi.png"
    car = pygame.image.load(img_path).convert_alpha()
    car = pygame.transform.scale(car,(80,80))
    car_table = [car, pos_x, pos_y]
    return car_table

def UI_Init(screen, elements):
    pygame.init()
    done = False
    clock = pygame.time.Clock()
    screen_bg = UI_drawbackground()
    screen_car = UI_drawcar(100, 100)
    while not done:
        screen.blit(screen_bg, (0,0))
        screen.blit(screen_car[0], (screen_car[1], screen_car[2]))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        
        
        pygame.display.flip()
        clock.tick(73)

UI_Init(scr, [])