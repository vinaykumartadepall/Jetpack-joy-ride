from colorama import Back,Fore,Style
from Objects import objects
from Background import background
from random import randint
class magnet(objects):
    def __init__(self):
        self._count=randint(1,2)
        self._name='m'
        self._arr=[]
        self.__lis=[]
        self.__magnet_shape=[]
        self.__range=40
        f=open('ascii_arts/magnet.txt','r')
        __st=f.read()
        __st=__st.split('\n')
        j=0
        for s in __st:
            lis=[]
            if j>=1:
                for i in range(0,4):
                    lis.append(Fore.RED+s[i]+Style.RESET_ALL+Back.BLACK)
                for i in range(4,8):
                    lis.append(Fore.BLUE+s[i]+Style.RESET_ALL+Back.BLACK)
            else:
                lis=[Fore.WHITE+char +Style.RESET_ALL+Back.BLACK for char in s]
            self.__magnet_shape.append(lis)
            j+=1
    
    # print(magnet_shape)
    # for i in magnet_shape:
    #     st=''
    #     for j in i:
    #         st=st+j
    #     print(Back.BLACK+st+Style.RESET_ALL)

    def generate_field(self):
        ''' generates magnetic field in its surrouding '''
        for lis in self._arr:
            lis[2]=4
            lis[0]=1
            for j in range(1,49):
                for i in range(lis[1]-self.__range,lis[1]+3):
                    background.set_field(j,i,'r')
                for i in range(lis[1]+3,lis[1]+6):
                    background.set_field(j,i,'u')
                for i in range(lis[1]+6,lis[1]+self.__range):
                    background.set_field(j,i,'l')
    
    ''' getters and setters '''
    def get_magnet_shape(self):
        return self.__magnet_shape


# m=Magnet()