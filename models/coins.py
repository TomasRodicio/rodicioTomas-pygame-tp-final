# 24
import pygame
from auxiliar.constantes import *
from auxiliar.auxiliar import SurfaceManager as sm

class Coins(pygame.sprite.Sprite):
    def __init__(self, pos, size, stage_dict_configs: dict, frame_rate = 40) -> None:
        super().__init__()

        self.__spin = sm.get_surface('./assets/img/items/GoldCoinSpinning.png', 24, 1)
        self.__coins_configs = stage_dict_configs.get('coins')
        self.__frame_rate = frame_rate
        self.__coin_animation_time = 0
        self.__initial_frame = 0
        self.__actual_img_animation = self.__spin[self.__initial_frame]
        self.image = self.__actual_img_animation
        self.__size = size
        self.image = pygame.transform.scale(self.image, (self.__size / 2, self.__size / 2))
        self.rect = self.image.get_rect(topleft=pos)
        self.__value = self.__coins_configs['value']

    
    @property
    def value(self):
        return self.__value


    


    def do_animation(self, delta_ms):
        self.__coin_animation_time += delta_ms
        if self.__coin_animation_time >= self.__frame_rate:
            self.__coin_animation_time = 0
            if self.__initial_frame < len(self.__spin) - 1:
                self.__initial_frame += 1
            else:
                self.__initial_frame = 0
    


    def draw(self, screen: pygame.surface.Surface):
        if DEBUG:
            pygame.draw.rect(screen, 'yellow', self.rect)
        self.__actual_img_animation = self.__spin[self.__initial_frame]
        self.__actual_img_animation = pygame.transform.scale(self.__actual_img_animation, (self.__size / 2, self.__size / 2))
        screen.blit(self.__actual_img_animation, self.rect)  


    def update(self, delta_ms, screen: pygame.surface.Surface):
        self.do_animation(delta_ms)
        self.draw(screen)