import pygame


class Display():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))


def update(screen, font, wave_font, width):

    screen.fill((210, 185, 100))

    black_keys_we = font.render("w e", 1, (25, 25, 25))
    black_keys_tyu = font.render("t y u", 1, (25, 25, 25))
    black_keys_op = font.render("o p", 1, (25, 25, 25))
    white_keys = font.render("a s d f g h j k l ö", 1, (255, 255, 255))
    screen.blit(black_keys_we, (width - black_keys_we.get_width()-540, 180))
    screen.blit(black_keys_tyu, (width - black_keys_tyu.get_width()-250, 180))
    screen.blit(black_keys_op, (width - black_keys_op.get_width()-40, 180))
    screen.blit(white_keys, (width - white_keys.get_width()-20, 240))

    pygame.draw.rect(screen, (195, 170, 87), pygame.Rect(45, 100, 65, 40))
    pygame.draw.rect(screen, (195, 170, 87), pygame.Rect(45, 145, 65, 30))
    pygame.draw.rect(screen, (195, 170, 87), pygame.Rect(115, 100, 107, 40))
    pygame.draw.rect(screen, (195, 170, 87), pygame.Rect(115, 145, 120, 32))

    sine_button = wave_font.render("sine", 1, (30, 30, 30))
    saw_button = wave_font.render("saw", 1, (30, 30, 30))
    square_button = wave_font.render("square", 1, (30, 30, 30))
    triangle_button = wave_font.render("triangle", 1, (30, 30, 30))
    screen.blit(sine_button, (50, 100))
    screen.blit(square_button, (120, 100))
    screen.blit(saw_button, (50, 130))
    screen.blit(triangle_button, (120, 130))

    #oct_shift = wavefont.render(f"oct {os_screen}", 1, (30, 30, 30))
    #screen.blit(oct_shift, (70, 400))
    shift_buttons = font.render("z x", 1, (25, 25, 25))
    screen.blit(shift_buttons, (50, 400))
