from Background import background
import signal
from alarmexception import AlarmException
from getch import _getChUnix as getChar
from colorama import Back,Fore,Style
import subprocess as sp

# from Score import score

class person(background):
    def __init__(self):
        self._name=''
        self._dim_x=0
        self._dim_y=0
        self._x_cor=0
        self._y_cor=0
        self._shape=[]
        self._bullet_list=[]
        self._vel_x=[]
        self._vel_y=[]
    def place(self,x,y):
        # print(background.arr)
        # if self.shield_state=='active':
        #     for i in range(self.dim_x):
        #         for j in range(self.dim_y):
        #             self._shape[i][j]=Fore.GREEN+self._shape[i][j]+Style.RESET_ALL

        for i in range(x,x+self._dim_x):
            for j in range(y,y+self._dim_y):
                # print(str(i)+' '+str(j)+' '+str(i-x)+' '+str(j-y))
                # print(str(background.arr[i][j])+'+'+str(self._shape[i-x][j-y]))
                # self._shape=self.normal_shape
                # print(str(i)+'+'+str(j)+'+'+str(background.arr[i][j]))
                # print(str(i-x)+'+'+str(j-y)+'+'+str(self._shape[i-x][j-y]))
                if self.get_shield_state() =='inactive':
                    background.set_arr(i,j,self._shape[i-x][j-y])
                else:
                    background.set_arr(i,j,Fore.GREEN+self._shape[i-x][j-y]+Style.RESET_ALL+Back.BLACK)
                if self._shape[i-x][j-y]!=Fore.RED+' '+Style.RESET_ALL+Back.BLACK:
                    background.set_located(i,j,self._name)
                self._x_cor=x
                self._y_cor=y
    
    def remove(self):
        # print(background.arr)
        for i in range(self._x_cor,self._x_cor+self._dim_x):
            for j in range(self._y_cor,self._y_cor+self._dim_y):
                # print(str(i)+' '+str(j)+' '+str(i-x)+' '+str(j-y))
                # print(str(background.arr[i][j])+'+'+str(self._shape[i-x][j-y]))
                background.set_arr(i,j,' ')
                background.set_located(i,j,'N')
                # self._x_cor=x
                # self._y_cor=y    

    def move_up(self):
        flag=0
        # if self._name=='p':
        # self._shape=self.get_fly_shape()
        for j in range(self._dim_y):
            if background.get_located(self._x_cor-1,self._y_cor+j)=='b' or background.get_located(self._x_cor-1,self._y_cor+j)=='m':
                flag=1
            if background.get_located(self._x_cor-1,self._y_cor+j)=='>':
                background.clear(background.get_details(self._x_cor-1,self._y_cor+j,0),background.get_details(self._x_cor-1,self._y_cor+j,1),background.get_details(self._x_cor-1,self._y_cor+j,2),background.get_details(self._x_cor-1,self._y_cor+j,3))
                return 'speed'
            if background.get_located(self._x_cor-1,self._y_cor+j)=='e' or background.get_located(self._x_cor-1,self._y_cor+j)=='o':
                if self.get_shield_state()=='inactive':
                    return 'killed'
                self._score+=25
                background.clear(background.get_details(self._x_cor-1,self._y_cor+j,0),background.get_details(self._x_cor-1,self._y_cor+j,1),background.get_details(self._x_cor-1,self._y_cor+j,2),background.get_details(self._x_cor-1,self._y_cor+j,3))
        if flag==0:
            for j in range(self._dim_y):
                # f=open('temp.txt','w')
                # f.write(background.get_located[self._x_cor-1][self._y_cor+j])
                if self._name=='p' and background.get_located(self._x_cor-1,self._y_cor+j)=='$':
                    self._score+=10
            self.remove()
            self.place(self._x_cor-1,self._y_cor)
        return 'normal'


    def move_down(self):
        flag=0
        if self._name=='p':
            self._shape=self.get_normal_shape()
        for j in range(self._dim_y):
            if background.get_located(self._x_cor+self._dim_x,self._y_cor+j)=='b' or background.get_located(self._x_cor+self._dim_x,self._y_cor+j)=='m':
                flag=1
            if background.get_located(self._x_cor+self._dim_x,self._y_cor+j)=='>':
                background.clear(background.get_details(self._x_cor+self._dim_x,self._y_cor+j,0),background.get_details(self._x_cor+self._dim_x,self._y_cor+j,1),background.get_details(self._x_cor+self._dim_x,self._y_cor+j,2),background.get_details(self._x_cor+self._dim_x,self._y_cor+j,3))
                return 'speed'
            if background.get_located(self._x_cor+self._dim_x,self._y_cor+j)=='e' or background.get_located(self._x_cor+self._dim_x,self._y_cor+j)=='o':
                if self.get_shield_state()=='inactive':
                    return 'killed'
                self._score+=25
                background.clear(background.get_details(self._x_cor+self._dim_x,self._y_cor+j,0),background.get_details(self._x_cor+self._dim_x,self._y_cor+j,1),background.get_details(self._x_cor+self._dim_x,self._y_cor+j,2),background.get_details(self._x_cor+self._dim_x,self._y_cor+j,3))
        if flag==0:
            for j in range(self._dim_y):
                if self._name=='p' and background.get_located(self._x_cor+self._dim_x,self._y_cor+j)=='$':
                    self._score+=10
            self.remove()
            self.place(self._x_cor+1,self._y_cor)
        return 'normal'

    def move_left(self):
        flag=0
        self._shape=self.get_normal_shape()
        for j in range(self._dim_x):
            if background.get_located(self._x_cor+j,self._y_cor-1)=='b' or background.get_located(self._x_cor+j,self._y_cor-1)=='m':
                flag=1
            if background.get_located(self._x_cor+j,self._y_cor-1)=='>':
                background.clear(background.get_details(self._x_cor+j,self._y_cor-1,0),background.get_details(self._x_cor+j,self._y_cor-1,1),background.get_details(self._x_cor+j,self._y_cor-1,2),background.get_details(self._x_cor+j,self._y_cor-1,3))
                return 'speed'
            if background.get_located(self._x_cor+j,self._y_cor-1)=='e' or background.get_located(self._x_cor+j,self._y_cor-1)=='o':
                if self.get_shield_state()=='inactive':
                    return 'killed'
                self._score+=25
                background.clear(background.get_details(self._x_cor+j,self._y_cor-1,0),background.get_details(self._x_cor+j,self._y_cor-1,1),background.get_details(self._x_cor+j,self._y_cor-1,2),background.get_details(self._x_cor+j,self._y_cor-1,3))

        if flag==0:
            for j in range(self._dim_x):
                if self._name=='p' and background.get_located(self._x_cor+j,self._y_cor-1)=='$':
                    self._score+=10
            self.remove()
            self.place(self._x_cor,self._y_cor-1)
        return 'normal'

    def move_right(self):
        flag=0
        self._shape=self.get_normal_shape()
        for j in range(self._dim_x):
            if background.get_located(self._x_cor+j,self._y_cor+self._dim_y)=='b' or background.get_located(self._x_cor+j,self._y_cor+self._dim_y)=='m':
                flag=1
            if background.get_located(self._x_cor+j,self._y_cor+self._dim_y)=='>':
                background.clear(background.get_details(self._x_cor+j,self._y_cor+self._dim_y,0),background.get_details(self._x_cor+j,self._y_cor+self._dim_y,1),background.get_details(self._x_cor+j,self._y_cor+self._dim_y,2),background.get_details(self._x_cor+j,self._y_cor+self._dim_y,3))
                return 'speed'
            if background.get_located(self._x_cor+j,self._y_cor+self._dim_y)=='e' or background.get_located(self._x_cor+j,self._y_cor+self._dim_y)=='o':
                if self.get_shield_state()=='inactive':
                    return 'killed'
                self._score+=25
                background.clear(background.get_details(self._x_cor+j,self._y_cor+self._dim_y,0),background.get_details(self._x_cor+j,self._y_cor+self._dim_y,1),background.get_details(self._x_cor+j,self._y_cor+self._dim_y,2),background.get_details(self._x_cor+j,self._y_cor+self._dim_y,3))

        if flag==0:
            for j in range(self._dim_x):
                if self._name=='p' and background.get_located(self._x_cor+j,self._y_cor+self._dim_y)=='$':
                    self._score+=10
            self.remove()
            self.place(self._x_cor,self._y_cor+1)
        return 'normal'


    def move(self):
        def alarmhandler(signum, frame):
            ''' input method '''
            raise AlarmException

        def user_input(timeout=0.1):
            ''' input method '''
            signal.signal(signal.SIGALRM, alarmhandler)
            signal.setitimer(signal.ITIMER_REAL, timeout)
            try:
                text = getChar()()
                signal.alarm(0)
                return text
            except AlarmException:
                pass
            signal.signal(signal.SIGALRM, signal.SIG_IGN)
            return ''

        char = user_input()
        ret=0
        self._score=0

        if self.get_shield_time()<0:
            self.set_shield_time(self.get_shield_time()+1)

        if self.get_shield_time()>0:
            # f=open('out.txt','a')
            # f.write(str(self.get_shield_time())+'\n')
            self.set_shield_time(self.get_shield_time()-1)
        
        if self.get_shield_time()==0 and self.get_shield_state()=='active':
            self.set_shield_state('inactive')
            self.set_shield_time(-600)
        self.remove_bullets()
        self.move_bullets()
        self.move_bullets()
        self.print_bullets()
        # print(self._shield_state+str(self._shield_time()))
        self._vel_x=0

        if background.get_field(self._x_cor,self._y_cor)=='l':
            self._vel_x=-1
            self._vel_y=1
        
        if background.get_field(self._x_cor,self._y_cor)=='r':
            self._vel_x=1
            self._vel_y=1

        if background.get_field(self._x_cor,self._y_cor)=='u':
            self._vel_y=1

        if char=='q':
            quit()

        if char=='w':
            ''' jump '''
            self._shape=self.get_fly_shape()
            self._vel_y=1
        
        if char!='w' and background.get_field(self._x_cor,self._y_cor)=='N':
            ''' gravity '''
            self._shape=self.get_normal_shape()
            if self._vel_y==1:
                self._vel_y=-3
            self._vel_y-=1
        if char=='a':
            ''' move left '''
            self._vel_x-=2
        
        if char=='d':
            ''' move right '''
            self._vel_x+=2

        if char==' ' and self._name=='p':
            if self.get_shield_state()=='inactive' and self.get_shield_time()==0:
                self.set_shield_time(100)
                self.set_shield_state('active')
                # print()
            # return 'shield'

        if char=='b' and self._name=='p':
            self.shoot()
        
        if self._vel_y>0:
            for i in range(0,self._vel_y):
                ret=self.move_up()
                if ret!='normal':
                    return ret

        if self._vel_y<0:
            for i in range(int(self._vel_y/5),0):
                ret=self.move_down()
                if ret!='normal':
                    return ret

        if self._vel_x>0:
            for i in range(0,self._vel_x):
                ret=self.move_right()
                if ret!='normal':
                    return ret

        if self._vel_x<0:
            for i in range(self._vel_x,0):
                ret=self.move_left()
                if ret!='normal':
                    return ret


        self.place(self._x_cor,self._y_cor)
        self.adjust()
        return 10*ret
        
    def adjust(self):
        if self._y_cor<background.get_y():
            self._y_cor=background.get_y()
            self.place(self._x_cor,self._y_cor)
            # print(str(self._y_cor)+' '+str(background.get_y()))
        if self._y_cor>background.get_window_size()+background.get_y()-self._dim_x+1:
            self.remove()
            self._y_cor=background.get_y()+background.get_window_size()-self._dim_x+1
            self.place(self._x_cor,self._y_cor)
        if background.get_located(self._x_cor,self._y_cor+1+self._dim_y)=='V':
            self.respawn()            
    def respawn(self):
        self.remove()
        self.place(45,background.get_y())
        self.set_shield_time(100)
        self.set_shield_state('active')

    def get_coor(self):
        return str(self._x_cor)+','+str(self._y_cor)
    
    def shoot(self):
        lis=[]
        lis.append(self._x_cor)
        lis.append(self._y_cor+2)
        self._bullet_list.append(lis)
    
    def move_bullets(self):
        # f=open('out.txt','a')
        # f.write(str(self._bullet_list))
        # f.write('\n')
        for i in self._bullet_list:
            if i[0]>0  and i[1]<background.get_y()+background.get_window_size():
                if background.get_located(i[0],i[1]+1)=='e' or background.get_located(i[0],i[1]+1)=='o':
                    background.clear(background.get_details(i[0],i[1]+1,0),background.get_details(i[0],i[1]+1,1),background.get_details(i[0],i[1]+1,2),background.get_details(i[0],i[1]+1,3))
                    i[0]=-1
                    self._score+=15
                
                if background.get_located(i[0],i[1]+1)=='V':
                    # print('\n\n\n\n\n\n\n\n\n\n\n\n')
                    self._score+=20
                    self.dec_boss_lives()
                    i[0]=-1
            # background.arr[i[0]][i[1]]=' '+Back.BLACK
            # background.located[i[0]][i[1]]='N'
            i[1]=i[1]+1

    def remove_bullets(self):
        for i in self._bullet_list:
            if i[0]>0  and i[1]<background.get_y()+background.get_window_size():
                if background.get_located(i[0],i[1])=='~':
                    background.set_arr(i[0],i[1],' '+Back.BLACK)
                    background.set_located(i[0],i[1],'N')
    
    def print_bullets(self):
        for i in self._bullet_list:
            # f=open('out.txt','a')
            # f.write(background.located[i[0]][i[1]])
            if i[1]<background.get_y()+background.get_window_size()  and i[0]>0:
                if background.get_located(i[0],i[1])=='N':
                    background.set_arr(i[0],i[1],Fore.CYAN+'~'+Style.RESET_ALL+Back.BLACK)
                    background.set_located(i[0],i[1],'~')
            # else:
                # print('\n\n\n\n\n\n'+str(background.located[i[0]][i[1]])+'\n\n\n\n\n')

    def get_score(self):
        return self._score

    def get_x(self):
        return self._x_cor
    
    def get_y(self):
        return self._y_cor
    