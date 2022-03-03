import pygame as pg
import sys

pg.mixer.pre_init
pg.init()
pg.mixer.music.load('elektro.wav')
pg.mixer.music.play()

zagruzka = pg.mixer.Sound('vkluchenie.wav')
priv1 = pg.mixer.Sound('voxworker-voice-file.mp3')
priv2 = pg.mixer.Sound('fraza2.mp3')
priv3 = pg.mixer.Sound('fraza3.mp3')
klik = pg.mixer.Sound('klik.wav')
pg.init()
screen_width = 840
screen_height = 566
screen = pg.display.set_mode([screen_width, screen_height])
zastavka = pg.image.load('zastavka2.jpg').convert()
screen.blit(zastavka, (0, 0))
pg.display.update()
clock = pg.time.Clock()
FPS = 120
#pg.time.wait(1000)
pg.font.init()
pg.font.get_fonts()

i = 0
x = 0


def nadpis_text(y, i, x, messeg):
    while i < int(len(messeg)):
        text1 = f.render(str(messeg1), False, (49, 168, 77))
        screen.blit(text1, (10, y))
        pg.display.update()
        klik.play(0, 0, 0).set_volume(0.05)
        text = f.render(str(messeg[i]), True, (49, 168, 77))
        screen.blit(text, (100 + x, y))
        pg.display.update()
        pg.time.wait(120)
        i += 1
        x += 13








zagruzka.play(-1)

while True:
    for q in pg.event.get():
        if q.type == pg.QUIT:
            sys.exit()
    messeg1 = "18F000__:"
    messeg = "Здравствуйте Александр"
    f = pg.font.Font('ConsolaMono.ttf', 15)
    priv1.play(0, 0, 0)
    nadpis_text(10, i, x, messeg)
    pg.time.wait(300)
    messeg = "приветствую вас в нашем доме"
    priv2.play(0, 0, 0)
    nadpis_text(30, i, x, messeg)
    pg.time.wait(300)
    messeg = "предлагаю малость развлечься"
    priv3.play(0, 0, 0)
    nadpis_text(50, i, x, messeg)
