import pygame
import Screen_abc as SC

effect_group = pygame.sprite.Group()


def draw_effect():
    effect_group.draw(SC.screen)
    effect_group.update()


class ScreenLineEffect(pygame.sprite.Sprite):
    def __init__(self, title_name: str):
        pygame.sprite.Sprite.__init__(self)
        self.title_name = title_name
        self.image = pygame.image.load("img/screen_line/screen_line.png")
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = -200

    def update(self):
        if self.rect.y < 200:
            self.rect.y += 100
        elif 200 <= self.rect.y <= 250:
            self.rect.y += 5
        else:
            self.rect.y += 200
        if self.rect.y > 640:
            self.kill()

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    # ウマが歩くだけのアニメーション
    class UmaEffect(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.index = 0
            self.uma_images = [pygame.image.load("img/uma/uma01.png"),
                               pygame.image.load("img/uma/uma02.png"),
                               pygame.image.load("img/uma/uma03.png"),
                               pygame.image.load("img/uma/uma04.png"),
                               pygame.image.load("img/uma/uma05.png"),
                               pygame.image.load("img/uma/uma06.png")]
            self.image = self.uma_images[self.index]
            self.rect = self.image.get_rect()
            self.rect.x = 30
            self.rect.y = 60

        def update(self):
            if self.index >= len(self.uma_images):
                self.kill()
                return
            self.image = self.uma_images[self.index]
            self.index += 1

        def draw(self, screen):
            screen.blit(self.image, self.rect)

    # 氷が出現して砕けるエフェクト
    class IceEffect(pygame.sprite.Sprite):
        def __init__(self, x_location: int, y_location: int):
            pygame.sprite.Sprite.__init__(self)
            self.index = 0
            self.effect_images = list()
            for i in range(1, 22):
                if i < 10:
                    self.effect_images.append(pygame.image.load("img/effect/sample_effect_00" + str(i) + ".png"))
                else:
                    self.effect_images.append(pygame.image.load("img/effect/sample_effect_0" + str(i) + ".png"))
            self.image = self.effect_images[self.index]
            self.rect = self.image.get_rect()
            self.rect.center = (x_location, y_location)

        def update(self):
            if self.index >= len(self.effect_images):
                self.kill()
                return
            self.image = self.effect_images[self.index]
            self.index += 1

        def draw(self, screen):
            screen.blit(self.image, self.rect)

    # 円が広がるようなエフェクトを表示する
    class CircleEffect(pygame.sprite.Sprite):
        def __init__(self, x_location: int, y_location: int):
            pygame.sprite.Sprite.__init__(self)
            self.index = 0
            self.effect_images = list()
            for i in range(1, 16):
                self.effect_images.append(pygame.image.load("img/circle/circle_effect" + str(i) + ".png"))
            self.image = self.effect_images[self.index]
            self.rect = self.image.get_rect()
            self.rect.center = (x_location, y_location)

        def update(self):
            if self.index >= len(self.effect_images):
                self.kill()
                return
            self.image = self.effect_images[self.index]
            self.index += 1

        def draw(self, screen):
            screen.blit(self.image, self.rect)
