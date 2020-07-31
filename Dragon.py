from Person import person
from colorama import Back,Fore,Style
from Background import background

class dragon(person):
    def __init__(self):
        self._dim_x=15
        self._dim_y=39
        self._name='V'
        self._x_cor=0
        self._y_cor=0
        self._shape=[]
        self.__shield_state='inactive'
        self.__ball_list=[]
        self.__count=0
        f=open('ascii_arts/dragon.txt','r')
        __st=f.read()
        __st=__st.split('\n')
        for s in __st:
            s=[Fore.RED+char+Style.RESET_ALL+Back.BLACK for char in s]
            self._shape.append(s)

    ''' setters and getters '''

    def get_shield_state(self):
        return self.__shield_state
        
    def get_shield_time(self):
        return self.shield_time
    
        
    def shoot(self):
        ''' shoots a bullet (adds a bullet to the bullet list) '''
        __lis=[]
        __lis.append(self._x_cor+12)
        __lis.append(self._y_cor-2)
        self.__ball_list.append(__lis)
        __lis=[]
        __lis.append(self._x_cor+3)
        __lis.append(self._y_cor-2)
        self.__ball_list.append(__lis)
    
    def move_bullets(self):
        ''' moves bullets and checks collisions '''
        fl=0
        for i in self.__ball_list:
            if i[1]>0:
                if background.get_located(i[0],i[1]-1)=='p':
                    i[1]=-1
                    fl=1
                i[1]=i[1]-1
        if fl==1:
            return 'killed'            
        return 'normal'

    def remove_bullets(self):
        ''' removes a bullets and places in next position'''
        for i in self.__ball_list:
            if i[1]>0:
                if background.get_located(i[0],i[1])=='*':
                    background.set_arr(i[0],i[1],' '+Back.BLACK)
                    background.set_located(i[0],i[1],'N')

    def print_bullets(self):
        ''' places bullet in it's current location '''
        for i in self.__ball_list:
            if i[1]>0:
                if background.get_located(i[0],i[1])=='N':
                    background.set_arr(i[0],i[1],Fore.WHITE+'*'+Style.RESET_ALL+Back.BLACK)
                    background.set_located(i[0],i[1],'*')

        # print(len(s))
    # print(shape.count)
    # for __lis in shape:
    #     __st=''
    #     for c in __lis:
    #         __st+=c
    #     print(__st)

# d=dragon()