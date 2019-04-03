
import


width = 500
height = 500
win = demo.display.set_mode((width, height))
demo.display.set_caption("Client")

clientNumber = 0


class Player():
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x,y,width,height)
        self.vel = 3

    def draw(self, win):
        demo.draw.rect(win, self.color, self.rect)

    def move(self):
        keys = demo.key.get_pressed()

        if keys[demo.K_LEFT]:
            self.x -= self.vel

        if keys[demo.K_RIGHT]:
            self.x += self.vel

        if keys[demo.K_UP]:
            self.y -= self.vel

        if keys[demo.K_DOWN]:
            self.y += self.vel

        self.rect = (self.x, self.y, self.width, self.height)


def redrawWindow(win,player):
    win.fill((255,255,255))
    player.draw(win)
    demo.display.update()


def main():
    run = True
    p = Player(50,50,100,100,(0,255,0))
    clock = demo.time.Clock()

    while run:
        clock.tick(60)
        for event in demo.event.get():
            if event.type == demo.QUIT:
                run = False
                demo.quit()

        p.move()
        redrawWindow(win, p)

main()