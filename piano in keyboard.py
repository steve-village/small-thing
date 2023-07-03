import winsound
import sys
import pygame
import os
pygame.init()
screen = pygame.display.set_mode((1200,800))
screen.fill((255,250,240))
pygame.display.set_caption('钢琴键盘')

my_font = pygame.font.SysFont(['方正粗黑宋简体','microsoftsansserif'],35)
text1 = my_font.render("1",True,(255,0,0),None)
text2 = my_font.render("2",True,(255,0,0),None)
text3 = my_font.render("3",True,(255,0,0),None)
text4 = my_font.render("4",True,(255,0,0),None)
text5 = my_font.render("5",True,(255,0,0),None)
text6 = my_font.render("6",True,(255,0,0),None)
text7 = my_font.render("7",True,(255,0,0),None)
text8 = my_font.render("8",True,(255,0,0),None)
text9 = my_font.render("9",True,(255,0,0),None)
text10 = my_font.render("0",True,(255,0,0),None)
text11 = my_font.render("-",True,(255,0,0),None)
text12 = my_font.render("=",True,(255,0,0),None)
text21 = my_font.render("do",True,(0,0,255),None)
text22 = my_font.render("re",True,(0,0,255),None)
text23 = my_font.render("mi",True,(0,0,255),None)
text24 = my_font.render("fa",True,(0,0,255),None)
text25 = my_font.render("sol",True,(0,0,255),None)
text26 = my_font.render("la",True,(0,0,255),None)
text27 = my_font.render("si",True,(0,0,255),None)
face1 = pygame.Surface((1200,300),flags=pygame.HWSURFACE)
face2 = pygame.Surface((3,300),flags=pygame.HWSURFACE)
face3 = pygame.Surface((80,250),flags=pygame.HWSURFACE)
face4 = pygame.Surface((1200,3),flags=pygame.HWSURFACE)
face1.fill(color='white')
screen.blit(face1, (0,500))
screen.blit(face2,(95,500))
screen.blit(face2,(195,500))
screen.blit(face2,(295,500))
screen.blit(face2,(395,500))
screen.blit(face2,(495,500))
screen.blit(face2,(595,500))
screen.blit(face2,(695,500))
screen.blit(face2,(795,500))
screen.blit(face2,(895,500))
screen.blit(face2,(995,500))
screen.blit(face2,(1095,500))
screen.blit(face3,(60,400))
screen.blit(face3,(160,400))
screen.blit(face3,(360,400))
screen.blit(face3,(460,400))
screen.blit(face3,(560,400))
screen.blit(face3,(760,400))
screen.blit(face3,(860,400))
screen.blit(face3,(1060,400))
screen.blit(face4,(0,500))
screen.blit(text1,(30,650))
screen.blit(text2,(130,650))
screen.blit(text3,(230,650))
screen.blit(text4,(330,650))
screen.blit(text5,(430,650))
screen.blit(text6,(530,650))
screen.blit(text7,(630,650))
screen.blit(text8,(730,650))
screen.blit(text9,(830,650))
screen.blit(text10,(930,650))
screen.blit(text11,(1030,650))
screen.blit(text12,(1130,650))
screen.blit(text21,(30,700))
screen.blit(text22,(130,700))
screen.blit(text23,(230,700))
screen.blit(text24,(330,700))
screen.blit(text25,(430,700))
screen.blit(text26,(530,700))
screen.blit(text27,(630,700))
screen.blit(text21,(730,700))
screen.blit(text22,(830,700))
screen.blit(text23,(930,700))
screen.blit(text24,(1030,700))
screen.blit(text25,(1130,700))
face5 = pygame.Surface((250,100),flags=pygame.HWSURFACE)
face5.fill(color=(255,242,226))
screen.blit(face5, (950,200))
my_font2 = pygame.font.SysFont('FZZJ-ZHRXKJW.ttf',70)
text31 = my_font2.render("Record",True,(0,0,255),None)
screen.blit(text31,(1000,230))
myfont3 = pygame.font.Font('FZZJ-ZHRXKJW.ttf',100)
text32 = myfont3.render("钢 琴 键 盘",True,(247,200,207),None)
screen.blit(text32,(350,150))
text33 = my_font2.render("Stop",True,(0,0,255),None)
face6 = pygame.Surface((250,100),flags=pygame.HWSURFACE)
face6.fill(color=(255,242,226))
screen.blit(face5, (950,50))
screen.blit(text33,(1000,75))
flag = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx,my = event.pos
            if mx>=950 and mx <=1200:
                if my>=200 and my <=300:
                    f = open('record.txt','w')
                    flag = True
                if my >= 50 and my<=150:
                    f.close()
                    flag = False
            pygame.display.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                winsound.Beep(262,400)
                if flag:
                    f.write('1 do ')
            if event.key == pygame.K_2:
               winsound.Beep(294,400)
               if flag:
                    f.write('2 re ')
            if event.key == pygame.K_3:
                winsound.Beep(330,400)
                if flag:
                    f.write('3 mi ')
            if event.key == pygame.K_4:
               winsound.Beep(349,400)
               if flag:
                    f.write('4 fa ')
            if event.key == pygame.K_5:
                winsound.Beep(392,400)
                if flag:
                    f.write('5 so ')
            if event.key == pygame.K_6:
               winsound.Beep(440,400)
               if flag:
                    f.write('6 la ')
            if event.key == pygame.K_7:
                winsound.Beep(494,400)
                if flag:
                    f.write('7 si ')
            if event.key == pygame.K_8:
               winsound.Beep(523,400)
               if flag:
                    f.write('8 do\' ')
            if event.key == pygame.K_9:
                winsound.Beep(587,400)
                if flag:
                    f.write('9 re\' ')
            if event.key == pygame.K_0:
               winsound.Beep(659,400)
               if flag:
                    f.write('0 mi\' ')
            if event.key == pygame.K_KP_MINUS:
                winsound.Beep(698,400)
                if flag:
                    f.write('- fa\' ')
            if event.key == pygame.K_KP_EQUALS:
               winsound.Beep(784,400)
               if flag:
                    f.write('= so\' ')
    pygame.display.flip()