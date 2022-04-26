import pygame


class Display():
    def __init__(self):
        self.width = 720
        self.height = 640
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.font = pygame.font.SysFont("comicsans", 90)
        self.wave_font = pygame.font.SysFont("comicsans", 30)

        self.tuning = 440

    def update(self):

        self.screen.fill((210, 185, 100))

        black_keys_we = self.font.render("w e", 1, (25, 25, 25))
        black_keys_tyu = self.font.render("t y u", 1, (25, 25, 25))
        black_keys_op = self.font.render("o p", 1, (25, 25, 25))
        white_keys = self.font.render(
            "a s d f g h j k l ö", 1, (255, 255, 255))
        self.screen.blit(black_keys_we, (self.width -
                         black_keys_we.get_width()-540, 180))
        self.screen.blit(black_keys_tyu, (self.width -
                         black_keys_tyu.get_width()-250, 180))
        self.screen.blit(black_keys_op, (self.width -
                         black_keys_op.get_width()-40, 180))
        self.screen.blit(
            white_keys, (self.width - white_keys.get_width()-20, 240))

        shift_buttons = self.font.render("z x", 1, (25, 25, 25))
        self.screen.blit(shift_buttons, (50, 400))

    #oct_shift = wavefont.render(f"oct {os_screen}", 1, (30, 30, 30))
    #screen.blit(oct_shift, (70, 400))
