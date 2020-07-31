from Background import background 
from Person import person
from colorama import Fore, Back, Style
class mandalorian(person):
    def __init__(self):
        self._dim_x=4
        self._dim_y=2
        self._x_cor=0
        self._y_cor=0
        self._name='p'
        self.__boss_lives=50
        self.__score=0
        self._bullet_list=[]
        self._vel_x=0
        self._vel_y=0
        self._shape=[]
        self.__normal_shape=[]
        self.__fly_shape=[]
        self.__shield_time=0
        self.__shield_state='inactive'

        ''' gets shapes from files '''        
        f=open('ascii_arts/mandalorian.txt','r')
        st=f.read()
        st=st.split('\n')
        for s in st:
            s=[char for char in s+Style.RESET_ALL+Back.BLACK]
            self.__normal_shape.append(s)
        
        f=open('ascii_arts/flying_mandalorian.txt','r')
        st=f.read()
        st=st.split('\n')
        for s in st:
            s=[char for char in s+Style.RESET_ALL+Back.BLACK]
            self.__fly_shape.append(s)
        self.__fly_shape[3][0]=Fore.RED+'|'+Style.RESET_ALL+Back.BLACK
        self.__fly_shape[2][0]=Fore.RED+'|'+Style.RESET_ALL+Back.BLACK
        self._shape=self.__normal_shape 

    ''' getters and setters '''

    def get_shield_state(self):
        return self.__shield_state
        
    def set_shield_time(self,val):
        self.__shield_time=val
    
    def set_shield_state(self,val):
        self.__shield_state=val

    def get_normal_shape(self):
        return self.__normal_shape
    
    def get_fly_shape(self):
        return self.__fly_shape

    def get_shield_time(self):
        return self.__shield_time
    
    def get_boss_lives(self):
        return self.__boss_lives
    
    def dec_boss_lives(self):
        self.__boss_lives-=1
    
    def get_bullet_list(sel):
        return self.__bullet_list
    

# m=mandalorian()    