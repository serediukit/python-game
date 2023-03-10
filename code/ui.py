import pygame
from settings import *

class UI:
    def __init__(self):

        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font(UI_FONT, UI_FONT_SIZE)

        self.health_bar_rect = pygame.Rect(10, 10, HEALTH_BAR_WIDTH, BAR_HEIGHT)
        self.energy_bar_rect = pygame.Rect(10, 15 + BAR_HEIGHT, ENERGY_BAR_WIDTH, BAR_HEIGHT)

        self.weapon_graphics = []
        for weapons in weapon_data.values():
            path = weapons['graphic']
            weapon = pygame.image.load(path).convert_alpha()
            self.weapon_graphics.append(weapon)

        self.magic_graphics = []
        for magics in magic_data.values():
            path = magics['graphic']
            magic = pygame.image.load(path).convert_alpha()
            self.magic_graphics.append(magic)

    def show_bar(self, current, max, bg_rect, color):
        pygame.draw.rect(self.display_surface, UI_BG_COLOR, bg_rect)

        ratio = current / max
        current_width = bg_rect.width * ratio
        current_rect = bg_rect.copy()
        current_rect.width = current_width

        pygame.draw.rect(self.display_surface, color, current_rect)
        pygame.draw.rect(self.display_surface, UI_BORDER_COLOR, current_rect, 3)

    def show_exp(self, exp):
        text_surf = self.font.render(str(int(exp)), False, TEXT_COLOR)
        x = self.display_surface.get_size()[0] - 20
        y = self.display_surface.get_size()[1] - 20
        text_rect = text_surf.get_rect(bottomright = (x,y))

        pygame.draw.rect(self.display_surface, UI_BG_COLOR, text_rect.inflate(20, 20))
        self.display_surface.blit(text_surf, text_rect)
        pygame.draw.rect(self.display_surface, UI_BORDER_COLOR, text_rect.inflate(20, 20), 3)

    def selection_box(self, left, top):
        bg_rect = pygame.Rect(left, top, ITEM_BOX_SIZE, ITEM_BOX_SIZE)
        pygame.draw.rect(self.display_surface, UI_BG_COLOR, bg_rect)
        pygame.draw.rect(self.display_surface, UI_BORDER_COLOR, bg_rect, 3)

        return bg_rect

    def weapon_overlay(self, weapon_index):
        bg_rect = []

        for i in range(5):
            bg_rect.append(self.selection_box(10 + 90 * i, 630))
            weapon_surf = self.weapon_graphics[i]
            weapon_rect = weapon_surf.get_rect(center = bg_rect[i].center)
            self.display_surface.blit(weapon_surf, weapon_rect)

        active_rect = bg_rect[weapon_index].copy()
        active_rect.width += 4
        active_rect.height += 4
        active_rect.center = bg_rect[weapon_index].center
        pygame.draw.rect(self.display_surface, UI_BORDER_COLOR_ACTIVE, bg_rect[weapon_index], 5)
        pygame.draw.rect(self.display_surface, UI_BORDER_COLOR, active_rect, 2)

    def magic_overlay(self, magic_index):
        bg_rect = []

        for i in range(2):
            bg_rect.append(self.selection_box(10 + 90 * i, 520))
            magic_surf = self.magic_graphics[i]
            magic_rect = magic_surf.get_rect(center = bg_rect[i].center)
            self.display_surface.blit(magic_surf, magic_rect)

        active_rect = bg_rect[magic_index].copy()
        active_rect.width += 4
        active_rect.height += 4
        active_rect.center = bg_rect[magic_index].center
        pygame.draw.rect(self.display_surface, UI_BORDER_COLOR_ACTIVE, bg_rect[magic_index], 5)
        pygame.draw.rect(self.display_surface, UI_BORDER_COLOR, active_rect, 2)

    def display(self, player):
        self.show_bar(player.health, player.stats['health'], self.health_bar_rect, HEALTH_COLOR)
        self.show_bar(player.energy, player.stats['energy'], self.energy_bar_rect, ENERGY_COLOR)

        self.show_exp(player.exp)

        self.weapon_overlay(player.weapon_index)
        self.magic_overlay(player.magic_index)
