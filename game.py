from Background import background
from Person import person
from Mandalorian import mandalorian
from Score import score
from Coins import coins
from Beams import beams
from Powerup import powerup
from Dragon import dragon
from Magnet import magnet
# from Objects import objects
import subprocess as sp
import time
from colorama import Back,Fore,Style
sp.call('clear',shell=True)

''' opener '''

f=open('ascii_arts/open.txt','r')
st=f.read()
st=st.split('\n')
for s in st:
    print(s)
    # s=[Fore.RED+char +Style.RESET_ALL+Back.BLACK for char in s]
    # self.__hor_shape.append(s)
if input()=='q':
    sp.call('clear',shell=True)
    quit()

''' initializing objects '''

back=background()
player=mandalorian()
score_board=score()
coin=coins()
beam=beams()
power=powerup()
boss=dragon()
mag=magnet()
tmp=sp.call('clear',shell=True)

# print("\033[%d;%dH" % (0,0))
print("\033[%d;%dH" % (0,0))

''' generating map '''

background.generate_background()
player.place(45,0)
# score_board.print_scores()
# background.print_background()
coin.generate()
coin.place()
power.generate()
power.place()
beam.generate()
beam.place()
mag.generate()
mag.generate_field()
mag.place()
boss.place(34,450)

# for i in range(50):
#     st=''
#     for j in range(150):
#         st+=background.located[i][j][0]
#     print(st)
t=0
i=0
s=0
l=int(time.time())
while score_board.get_lives()>0 and player.get_boss_lives()>0:
    ''' game play '''

    if int(time.time())-l>=1:
        score_board.inc_time()
        l=int(time.time())
    if score_board.get_time()<=0:
        t=1
        break
    if s>0:
        
        ''' powerup activated '''
        print("\033[%d;%dH" % (0,0))
        score_board.print_scores()
        ret = player.move()
        if ret == 'killed':
            score_board.dec_lives()
            player.respawn()
        
        elif ret == 'speed':
            s=10
                
        # else:
        #     score_board.inc_points(ret)
        score_board.inc_points(player.get_score())
        background.print_background()
        # background.print_loc()

        if background.get_y()+background.get_window_size()<490:
            background.increment_y()

        # score_board.inc_time()
        score_board.set_shield(player.get_shield_time())
        score_board.set_bosses(player.get_boss_lives())
        player.adjust()

    if background.get_y()+background.get_window_size()>=450:
        boss.remove()
        if player.get_x()>34:
            boss.place(34,450)
        else:
            boss.place(player.get_x(),450)
        boss.remove_bullets()
        ret=boss.move_bullets()
        if ret == 'killed' and player.get_shield_state()=='inactive':
            score_board.dec_lives()
            player.respawn()
        boss.print_bullets()

    print("\033[%d;%dH" % (0,0))
    score_board.print_scores()
    ret=player.move()

    if ret == 'killed':
        score_board.dec_lives()
        player.respawn()
    
    elif ret == 'speed':
        s=100
            
    # else:
    #     score_board.inc_points(ret)

    score_board.inc_points(player.get_score())
    background.print_background()
    # background.print_loc()
    if i==10:
        i=0
        if background.get_y()+background.get_window_size()<490:
            background.increment_y()
        player.adjust()
        # score_board.inc_time()
        score_board.set_shield(player.get_shield_time())
        score_board.set_bosses(player.get_boss_lives())
        if background.get_y()+background.get_window_size()>=450:
            boss.shoot()
    i=i+1
    if s>0:
        s-=1



tmp=sp.call('clear',shell=True)
fl=0
f=open('.highscore.txt','a')
f.close()
f=open('.highscore.txt','r')
st=f.read()
f.close()
# st='90000'
# print(Fore.BLACK+st+Style.RESET_ALL)
if st=='' or int(st) < score_board.get_score():
    f=open('.highscore.txt','w')
    f.write(str(score_board.get_score()))
    f.close()
    fl=1
st1='                                                                                                    '
st2='                                                                                                 '
st3='                                                                                     '
st4='                                                                                    '
print(Fore.BLUE)
for i in range(0,14):
    print()

if player.get_boss_lives()==0:
    print(st4+'                 @@@@@@@@@@@')
    print(st4+'                @           @')
    print(st4+'               @  0       0  @')
    print(st4+'             @@       |       @@')
    print(st4+'               @   \_____/   @')
    print(st4+'                @           @ ')

else:
    for i in range(14,20):
        print()
print(st1+' GAME OVER!!!\n')
if player.get_boss_lives()<=0:
    print(st3+'YOU KILLED THE BOSS AND RESCUED BABY YODA!!\n')
elif t==1:
    print(st1+'  '+'TIME UP\n')
else:
    print(st1+'  '+'YOU DIED\n')
print(st2+'  '+'FINAL SCORE : '+Fore.GREEN+str(score_board.get_score())+'\n')
if fl:
    print(Fore.GREEN+st2+'High score achieved\n'+Style.RESET_ALL)
else:
    print(st2+' '+'HIGHEST SCORE : '+Fore.BLUE+st+'\n')
input(Fore.GREEN+st3+'           '+'Press enter key to exit'+Style.RESET_ALL)
print(Style.RESET_ALL)

sp.call('clear',shell=True)