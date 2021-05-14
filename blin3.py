import pygame, sys
from tkinter import *
from pygame import display


def test():
    num = entry.get()
    if float(num) == 0.8:
        print('Yes')
        
        class Ball():
            def __init__(self):
                self.x = 40
                self.velocity=1
            def draw(self):
                pygame.draw.circle(screen, (125, 125, 125), ((int(self.x)), 480) , 20)
                
            def move(self): 
                self.x += self.velocity
                if self.x <= 40:
                    self.velocity = -self.velocity

        class Ball1():
            def __init__(self):
                self.x = 150
                self.velocity=1
            def draw(self):
                pygame.draw.circle(screen, (125, 125, 125), ((int(self.x)), 480) , 20)
                
            def move(self):
                self.x += self.velocity
                if self.x <= 150:
                    self.velocity = -self.velocity

        def bouncing_rect():
            global other_speed
            other_speed=1
            other_rect.x += other_speed
            if other_rect.left <= 0 or other_rect.right >= screen_height:
                other_speed *= -1
                
            pygame.draw.rect(screen, (255,255,255), other_rect)


        pygame.init()
        clock = pygame.time.Clock()
        screen_width,screen_height = 500, 500
        screen = pygame.display.set_mode((screen_width,screen_height))

        other_rect = pygame.Rect(0,410,200,50)
        
        ball=Ball()
        ball1=Ball1()
        

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            screen.fill((30,30,30))
            ball.move()
            ball1.move()

            pygame.draw.rect(screen, (255,255,255), other_rect)
            ball.draw()
            ball1.draw()
                
            bouncing_rect()             
            pygame.display.flip()
            clock.tick(60)

    

    else:
        print('Uncorrect answer')
        
root = Tk()
root.geometry('500x500')
root.title("Game project")
root.config(bg='#526ED9')
lab1 = Label(root, text='Hello teacher to our project!', bg='#526ED9', fg='white', font=('Helvetica',25,'bold'))
lab1.pack()

lab2 = Label(root, text="Let's solve problem together", bg='#526ED9', fg='white', font=('Helvetica',20,'bold'))
lab2.pack()
lab5 = Label(root, text='', bg='#526ED9', fg='white', font=('Helvetica',10,'bold'))
lab5.pack()
lab3 = Label(root, text="Problem: A plank with a mass M = 6.00 kg rides on top of two", bg='#526ED9', fg='white', font=('Helvetica',10,'bold'))
lab3.pack()

lab4 = Label(root, text="identical solid cylindrical rollers that have R = 5.00 cm and m= 2.00 kg", bg='#526ED9', fg='white', font=('Helvetica',10,'bold'))
lab4.pack()

lab5 = Label(root, text="The plank is pulled by a constant horizontal force F of magnitude 6.00 N", bg='#526ED9', fg='white', font=('Helvetica',10,'bold'))
lab5.pack()

lab6 = Label(root, text="applied to the end of the plank and perpendicular to the axes of the cylinders.", bg='#526ED9', fg='white', font=('Helvetica',10,'bold'))
lab6.pack()


lab7 = Label(root, text="The cylinders roll without slipping on a flat surface.", bg='#526ED9', fg='white', font=('Helvetica',10,'bold'))
lab7.pack()

lab8 = Label(root, text="(a) Find the acceleration of the plank and of the rollers.", bg='#526ED9', fg='white', font=('Helvetica',12,'bold'))
lab8.pack()
lab9= Label(root, text='', bg='#526ED9', fg='white', font=('Helvetica',10,'bold'))
lab9.pack()
entry = Entry(root, fg='#526ED9', width = 30)
entry.pack()
lab9= Label(root, text='', bg='#526ED9', fg='white', font=('Helvetica',10,'bold'))
lab9.pack()
but = Button(root, text = "Test", fg='#526ED9', bg='white', command=test)
but.pack()
    
