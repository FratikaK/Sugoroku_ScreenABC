import pygame
from pygame.locals import *

import Screen_abc as SC
from Screen_abc import Screen_abc
import sys

Ozaki_img = pygame.image.load('img/oomotosan_img/Ozaki.png')
Ozaki_Big_img = pygame.image.load('img/oomotosan_img/OzakiBig.png')
Player_img = pygame.image.load('img/oomotosan_img/Player.png')
Coin_img = pygame.image.load('img/oomotosan_img/Coin.png')
Item_img = pygame.image.load('img/oomotosan_img/Item.png')
Building1_img = pygame.image.load('img/oomotosan_img/Building1.png')
Building2_img = pygame.image.load('img/oomotosan_img/Building2.png')

# dice image
Dice1_img = pygame.image.load('img/oomotosan_img/Dice1.jpg')
Dice2_img = pygame.image.load('img/oomotosan_img/Dice2.jpg')
Dice3_img = pygame.image.load('img/oomotosan_img/Dice3.jpg')
Dice4_img = pygame.image.load('img/oomotosan_img/Dice4.jpg')
Dice5_img = pygame.image.load('img/oomotosan_img/Dice5.jpg')
Dice6_img = pygame.image.load('img/oomotosan_img/Dice6.jpg')

# マス画像
Green_img = pygame.image.load('img/oomotosan_img/Green.png')
Orange_img = pygame.image.load('img/oomotosan_img/Orange.png')
Purple_img = pygame.image.load('img/oomotosan_img/Purple.png')
Red_img = pygame.image.load('img/oomotosan_img/Red.png')
Yellow_img = pygame.image.load('img/oomotosan_img/Yellow.png')


class MainScreen(Screen_abc):

    # 画面生成
    def display(self):
        super().update()

        # 背景
        super().setBackground(SC.backImg, (0, 128, 32, 32))

        # プレイヤー情報欄
        # Rect()ではgrid[][]による座標指定不可→座標数値を直接入力
        for i in range(4):
            super().setBox(SC.Black, (i * 32 * 10, 0), 32 * 10, 32 * 3, 3)  # 外枠
            display_player_color = pygame.Rect(i * 32 * 10 + 3, 3, 32 * 10 - 3, 32 * 3 - 3)  # 背景色
            pygame.draw.rect(SC.screen, SC.White, display_player_color)  # 背景色を枠内に配置
            SC.screen.blit(pygame.image.load('img/oomotosan_img/Ozaki.png'),
                           ((32 * 2 + 16) + (i * 32 * 10), 32 + 18))  # プレイヤーアイコン
            SC.screen.blit(pygame.image.load('img/oomotosan_img/Coin.png'),
                           ((32 * 6 + 8) + (i * 32 * 10), 32 - 12))  # コインアイコン
            SC.screen.blit(pygame.image.load('img/oomotosan_img/Building1.png'),
                           ((32 * 6 + 8) + (i * 32 * 10), 32 + 18))  # 物件アイコン
            super().setText_S('Player' + str(i + 1), ((32 * 2) + (i * 32 * 10), 32 - 14), 22, SC.Black)  # プレイヤー名（仮）
            super().setText_L(str(i + 1), ((32 * 1 + 2) + (i * 32 * 10), 32 + 22), 26, SC.Black)  # 順位（仮）
            super().setText_S('0枚', ((32 * 7 + 16) + (i * 32 * 10), 32 - 16), 22, SC.Black)  # コイン数
            super().setText_S('0件', ((32 * 7 + 16) + (i * 32 * 10), 32 + 18), 22, SC.Black)  # 物件数
            i += 1
        pygame.draw.rect(SC.screen, SC.Black, pygame.Rect(32 * 40 - 3, 32 * 0, 3, 32 * 3))  # 右端の外枠線を追加

        # プレイヤー情報欄の現在のプレイヤーのカーソル（仮）
        super().setText_S('●', (32 * 1, 32 - 12), 20, SC.Red)

        # 青マスを上辺と下辺に配置
        for i in range(12):
            SC.screen.blit(pygame.image.load('img/oomotosan_img/Blue.png'), self.grid[8 + i * 2][5])
            SC.screen.blit(pygame.image.load('img/oomotosan_img/Blue.png'), self.grid[8 + i * 2][13])
            i += 1

        # 青マスを左辺と右辺に配置
        for i in range(3):
            SC.screen.blit(pygame.image.load('img/oomotosan_img/Blue.png'), self.grid[8][7 + i * 2])
            SC.screen.blit(pygame.image.load('img/oomotosan_img/Blue.png'), self.grid[30][7 + i * 2])
            i += 1

        # 赤マスを上辺と下辺に配置
        for i in range(3):
            SC.screen.blit(pygame.image.load('img/oomotosan_img/Red.png'), self.grid[12 + i * 8][5])
            SC.screen.blit(pygame.image.load('img/oomotosan_img/Red.png'), self.grid[10 + i * 8][13])
            i += 1

        # 赤マスを左辺に配置
        SC.screen.blit(pygame.image.load('img/oomotosan_img/Red.png'), self.grid[8][9])

        # 黄色マス（物件マス）を配置
        SC.screen.blit(pygame.image.load('img/oomotosan_img/Yellow.png'), self.grid[24][5])
        SC.screen.blit(pygame.image.load('img/oomotosan_img/Yellow.png'), self.grid[22][13])

        # オレンジ色マス（ボーナスマス）を配置
        SC.screen.blit(pygame.image.load('img/oomotosan_img/Orange.png'), self.grid[14][13])

        # 紫色マス（特大マイナスマス）を配置
        SC.screen.blit(pygame.image.load('img/oomotosan_img/Purple.png'), self.grid[30][9])

        # 物件を配置（仮）
        SC.screen.blit(pygame.image.load('img/oomotosan_img/Building2.png'), (32 * 24, 32 * 3 + 18))
        SC.screen.blit(pygame.image.load('img/oomotosan_img/Building2.png'), (32 * 22, 32 * 11 + 13))

        # アイテムを配置（仮）
        # SC.screen.blit(pygame.image.load('img/Item.png'), (32*29, 32*11+5))
        # SC.screen.blit(pygame.image.load('img/Item.png'), (32*20+5, 32*12))

        # マス上に各プレイヤーを配置（仮）
        SC.screen.blit(pygame.image.load('img/oomotosan_img/Ozaki.png'), self.grid[14][5])  # 現在のプレイヤー
        SC.screen.blit(pygame.image.load('img/oomotosan_img/Ozaki.png'), self.grid[26][5])
        SC.screen.blit(pygame.image.load('img/oomotosan_img/Ozaki.png'), self.grid[30][5])
        SC.screen.blit(pygame.image.load('img/oomotosan_img/Ozaki.png'), self.grid[24][13])

        # マス上の現在のプレイヤーのカーソル（仮）
        super().setText_S('▼', self.grid[14][4], 32, SC.Red)  # 現在のプレイヤー
        super().setText_S('▼', self.grid[24][12], 32, SC.Blue)

        # ターン表示欄
        # Rect()ではgrid[][]による座標指定不可→座標数値を直接入力
        display_turn_color = pygame.Rect(32 * 1, 32 * 5, 32 * 5, 32 * 9)
        pygame.draw.rect(SC.screen, SC.White, display_turn_color)
        super().setTextBox_S('', SC.Black, SC.Black, self.grid[1][5], 32 * 5, 32 * 9, 3, 25, 10, 10)
        super().setText_S('ターン', (32 * 2, 32 * 6), 35, SC.Black)
        super().setText_S('3/15', (32 * 2 + 5, 32 * 8 + 10), 45, SC.Black)
        super().setText_S('【序盤】', (32 + 12, 32 * 11 + 10), 35, SC.Black)

        # ゲーム終了ボタン
        # Rect()ではgrid[][]による座標指定不可→座標数値を直接入力
        button_color = pygame.Rect(32 * 1, 32 * 16, 32 * 5, 32 * 2)
        pygame.draw.rect(SC.screen, SC.White, button_color)
        super().setTextBox_S('', SC.Black, SC.Black, self.grid[1][16], 32 * 5, 32 * 2, 3, 25, 10, 10)
        super().setText_S('ゲーム終了', (32 * 1 + 16, 32 * 16 + 20), 25, SC.Black)

        # 説明表示欄
        # Rect()ではgrid[][]による座標指定不可→座標数値を直接入力
        display_desc_color = pygame.Rect(32 * 8, 32 * 15, 32 * 23, 32 * 4)
        pygame.draw.rect(SC.screen, SC.White, display_desc_color)
        text = ['アイテム名：BBBBB', '　アイテムの説明']
        super().setTextBox_S(text, SC.Black, SC.Black, self.grid[8][15], 32 * 23, 32 * 4, 3, 30, 20, 20)

        # サイコロ表示欄
        SC.screen.blit(pygame.image.load('img/oomotosan_img/Dice1.jpg'), self.grid[35][5])

        # アイテム表示欄
        # Rect()ではgrid[][]による座標指定不可→座標数値を直接入力
        super().setText_L('アイテム', (32 * 35, 32 * 10), 24, SC.Black)
        display_item_color = pygame.Rect(32 * 34, 32 * 11, 32 * 5, 32 * 3)
        pygame.draw.rect(SC.screen, SC.White, display_item_color)
        text = ['▼AAAAA', '▼BBBBB', '▼CCCCC']
        super().setTextBox_S(text, SC.Black, SC.Black, self.grid[34][11], 32 * 5, 32 * 3, 3, 25, 10, 10)
        super().setText_S('←', (32 * 37 + 12, 32 * 12 + 2), 30, SC.Red)

    # イベント処理
    def getEvent(self):
        for event in pygame.event.get():
            # 終了用のイベント処理
            if event.type == QUIT:  # 閉じるボタンが押されたとき
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:  # キーを押したとき
                if event.key == K_ESCAPE:  # Escキーが押されたとき
                    pygame.quit()
                    sys.exit()
                if event.key == K_SPACE:
                    SC.ScreenNum = 1
