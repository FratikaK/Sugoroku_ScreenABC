import pygame
import Screen_abc as SC

effect_group = pygame.sprite.Group()


def draw_effect():
    effect_group.draw(SC.screen)
    effect_group.update()


# 画面遷移を行う時に表示するエフェクト
class ScreenChangeEffect(pygame.sprite.Sprite):
    def __init__(self, next_screen_id: int):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("img/screen_change.png")
        self.rect = self.image.get_rect()
        self.rect.x = 1280
        self.rect.y = 0
        self.next_screen_id = next_screen_id
        self.wait_time = 10

    def update(self):
        if self.rect.x > 1100:
            self.rect.x -= 50
        elif 80 < self.rect.x <= 1100:
            self.rect.x -= 200
            if self.rect.x <= 0:
                self.rect.x = 0
        elif self.rect.x > 0:
            self.rect.x -= 50
            if self.rect.x <= 0:
                self.rect.x = 0

        elif self.rect.x <= 0:
            if SC.ScreenNum != self.next_screen_id:
                SC.ScreenNum = self.next_screen_id
            if self.wait_time > 0:
                if self.rect.x <= 0:
                    self.rect.x = 0
                self.wait_time -= 1
            else:
                if self.rect.x > -50:
                    self.rect.x -= 10
                elif -1800 < self.rect.x <= -50:
                    self.rect.x -= 300
                else:
                    self.rect.x -= 10

            if self.rect.x < -1300:
                self.remove(effect_group)

    def draw(self, screen):
        screen.blit(self.image, self.rect)


# コインが増減する時に出現させるエフェクト
class CoinNumFontEffect(pygame.sprite.Sprite):
    def __init__(self, num: int, x_location, y_location):
        pygame.sprite.Sprite.__init__(self)
        if num > 0:
            self.color = (0, 255, 255)
            self.message = "+ " + str(num)
        else:
            self.color = (255, 0, 0)
            self.message = "- " + str(abs(num))
        self.font = pygame.font.SysFont("yugothicyugothicuisemiboldyugothicuibold", 30)
        self.image = self.font.render(self.message, True, self.color)
        self.rect = self.image.get_rect()
        self.rect.center = (x_location, y_location)
        self.move_amount = 50

    def update(self):
        if self.move_amount >= 20:
            self.rect.y -= 20
            self.move_amount -= 20
        else:
            self.rect.y -= 1
            self.move_amount -= 1
            if self.move_amount < 0:
                self.remove(effect_group)

    def draw(self, screen):
        screen.blit(self.image, self.rect)


# 文字を右から左へ移動させるアニメーション
class ScreenLineFontEffect(pygame.sprite.Sprite):
    def __init__(self, message: str, color=(255, 255, 255)):
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.SysFont("yugothicyugothicuisemiboldyugothicuibold", 70)
        self.image = self.font.render(message, True, color)
        self.rect = self.image.get_rect()
        self.rect.x = 1300
        self.rect.y = 280

    def update(self):
        if self.rect.x > 600:
            self.rect.x -= 100
        elif 500 <= self.rect.x <= 600:
            self.rect.x -= 5
        else:
            self.rect.x -= 200
        if self.rect.x < -300:
            self.remove(effect_group)

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
            self.remove(effect_group)
            return
        self.image = self.uma_images[self.index]
        self.index += 1

    def draw(self, screen):
        screen.blit(self.image, self.rect)


# 氷が出現して砕けるアニメーション
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
