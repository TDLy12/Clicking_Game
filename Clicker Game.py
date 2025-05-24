import pygame
import random
import time

from pygame.examples.vgrade import timer

black = (0, 0, 0)
cyan = (0, 155, 200)
dark_blue = (0, 40, 225)
yellow = (255, 255, 0)
green = (0, 255, 0)
red = (255, 0, 0)

pygame.init()
window = pygame.display.set_mode((500,500)) #Creating the window
window.fill(cyan) #Color the background

clock = pygame.time.Clock()

class Area:
    def __init__(self, x=0, y=0, width=10, height=10, color=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color

    def set_new_color(self, new_color):
        self.color = new_color

    def fill(self):
        pygame.draw.rect(window, self.color, self.rect)

    def outline(self, frame_color, thickness):
        pygame.draw.rect(window, frame_color, self.rect, thickness)



class Card(Area):
    def set_text(self, text, text_size, text_color = black):
        font1 = pygame.font.SysFont("verdana", text_size)
        self.image = font1.render(text, True, text_color) #blueprint

    def write_text(self, shift_x=0, shift_y=0):
        self.fill()
        #The position of text depends on the position of the rectangle
        window.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))

    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)




class Image(Area):
    pass


first_card = Card(45,200,90, 100, yellow)
first_card.outline(black, 10)
first_card.set_text("CLICK", 20)

second_card = Card(150,200,90, 100, yellow)
second_card.outline(black, 10)
second_card.set_text("CLICK", 20)

third_card = Card(255,200,90, 100, yellow)
third_card.outline(black, 10)
third_card.set_text("CLICK", 20)

fourth_card = Card(360,200,90, 100, yellow)
fourth_card.outline(black, 10)
fourth_card.set_text("CLICK", 20)

cards = []
cards.append(first_card)
cards.append(second_card)
cards.append(third_card)
cards.append(fourth_card)

wait = 0
score = 0
start_time = time.time()

win_label = Card(250,250, 100, 100, green)

lose_label = Card(250,250, 100, 100, green)

score_label = Card(430,55,60,40,black)
score_label.set_text("0",25,green)
score_label.write_text(0,0)

timer_label = Card(30,55,60,40,black)
timer_label.set_text("0",25,red)
timer_label.write_text(0,0)


while True:
    if wait == 0:
        wait = 60
        random_pos = random.randint(0,4) #randomize position

        for i in range(4):
            cards[i].set_new_color(yellow)
            if i+1 == random_pos:
                cards[i].write_text(10,10)
            else:
                cards[i].fill()
    else:
        wait += -1



    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            for i in range(4):
                if cards[i].collidepoint(x,y): #When the card is clicked
                    if i+1 == random_pos: #Check that whether the text will still show up on the same card
                        cards[i].write_text(10,10)
                        cards[i].set_new_color(green)
                        score = score + 1
                        score_label.set_text(str(score),25,green)
                        score_label.write_text(0,0)
                    else:
                        cards[i].set_new_color(red)
                        score = score - 1
                    cards[i].fill()

    current_time = time.time()
    timer = round(current_time - start_time, 2)
    timer_label.set_text(str(timer),25,red)
    timer_label.write_text(0,0)

    if current_time - start_time > 10:
        print("Time Out!")
        lose_label.set_text("Lost!", 75, red)
        lose_label.write_text(0, 0)
        break


    if score > 5:
        print("win")
        win_label.set_text("Win!", 75, green)
        win_label.write_text(0, 0)
        break


    print("-------")
    print("| Timer:", timer, "|")
    print("| Score", score, "|")
    print("-------")



    pygame.display.update()  # Updating the frames
    clock.tick(60)  # 60 FPS

pygame.display.update() 

