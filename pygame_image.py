import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    kouka_img = pg.image.load("ex01/fig/3.png")
    kouka_img = pg.transform.flip(kouka_img, True, False)
    kouka_img_2 = pg.transform.rotozoom(kouka_img, 10, 1.0)
    kouka_img_lis = [kouka_img, kouka_img_2]
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        x = tmr%1600 
        
        screen.blit(bg_img, [-x, 0])
        screen.blit(bg_img, [1600-x, 0])
        screen.blit(kouka_img_lis[tmr%2], [300, 200])
        pg.display.update()
        tmr += 1        
        clock.tick(100)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()