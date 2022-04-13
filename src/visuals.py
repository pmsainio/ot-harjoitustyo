import pygame


class Display():
    def __init__(self):
        self.WIDTH = 720
        self.HEIGHT = 640
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.font = pygame.font.SysFont("comicsans", 90)
        self.wave_font = pygame.font.SysFont("comicsans", 30)

        self.tuning = 440


    def update(self):

        self.screen.fill((210, 185, 100))

        black_keys_we = self.font.render("w e", 1, (25, 25, 25))
        black_keys_tyu = self.font.render("t y u", 1, (25, 25, 25))
        black_keys_op = self.font.render("o p", 1, (25, 25, 25))
        white_keys = self.font.render("a s d f g h j k l ö", 1, (255, 255, 255))
        self.screen.blit(black_keys_we, (self.WIDTH - black_keys_we.get_width()-540, 180))
        self.screen.blit(black_keys_tyu, (self.WIDTH - black_keys_tyu.get_width()-250, 180))
        self.screen.blit(black_keys_op, (self.WIDTH - black_keys_op.get_width()-40, 180))
        self.screen.blit(white_keys, (self.WIDTH - white_keys.get_width()-20, 240))

        pygame.draw.rect(self.screen, (195, 170, 87), pygame.Rect(45, 100, 65, 40))
        pygame.draw.rect(self.screen, (195, 170, 87), pygame.Rect(45, 145, 65, 30))
        pygame.draw.rect(self.screen, (195, 170, 87), pygame.Rect(115, 100, 107, 40))
        pygame.draw.rect(self.screen, (195, 170, 87), pygame.Rect(115, 145, 120, 32))
        sine_button = self.wave_font.render("sine", 1, (30, 30, 30))
        saw_button = self.wave_font.render("saw", 1, (30, 30, 30))
        square_button = self.wave_font.render("square", 1, (30, 30, 30))
        triangle_button = self.wave_font.render("triangle", 1, (30, 30, 30))
        self.screen.blit(sine_button, (50, 100))
        self.screen.blit(square_button, (120, 100))
        self.screen.blit(saw_button, (50, 130))
        self.screen.blit(triangle_button, (120, 130))

        shift_buttons = self.font.render("z x", 1, (25, 25, 25))
        self.screen.blit(shift_buttons, (50, 400))
        
    def variables(self):
        tuning_f = self.wave_font.render(f"tuning: A={self.tuning}", 1, (35, 35, 35))
        self.screen.blit(tuning_f, (60, 380))

    #oct_shift = wavefont.render(f"oct {os_screen}", 1, (30, 30, 30))
    #screen.blit(oct_shift, (70, 400))
    
