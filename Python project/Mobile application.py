
# import pygame
# import os
# screen_size=[360,600]
# screen = pygame.display.set_mode(screen_size)
# background = os.path.dirname("C:/Users/user/.PyCharmCE2019.1/config/scratches/Python project/Mobile application.py")
# resource_path = os.path.join(background, 'C:/Users/user/.PyCharmCE2019.1/config/scratches/Python project/Screenshot_20190515_152033')
# screen.blit(background,[0,0])
# keep_alive = True
# while keep_alive:
#     screen.blit(background,[0,0])
#     pygame.display.update()


a=0
b=1
c=a+b
user_input=int(input("Enter a number: "))
for i in range (user_input):
    print(a)
    print(f"The sum of all these number is : c = {c} b = {b} a = {a}")
    a=b
    b=c
    c=a+b
