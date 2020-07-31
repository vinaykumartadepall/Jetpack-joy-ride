from Background import background
from random import randint
from colorama import Fore,Back,Style
from Objects import objects
class coins(objects):
    def __init__(self):
        self._name='$'
        self._shape='$'
        self._count=15
        self._arr=[]
        self._x_cor=0
        self._y_cor=0
    def generate(self):
        ''' generate coins randomly '''
        for i in range(self._count):
            coin=coins()
            # __lis=[]
            # __lis.append(randint(1,48))
            # __lis.append(randint(0,400))
            # __lis.append(randint(0,1))
            # __lis.append(randint(5,10))
            coin._x_cor=randint(1,40)
            coin._y_cor=randint(0,400)
            if randint(0,1)==0:
                coin._dim_x=randint(5,10)
                coin._dim_y=1
            else:
                coin._dim_y=randint(5,10)
                coin._dim_x=1
            self._arr.append(coin)
            # self._arr.append(__lis)
    def place(self):
        # i=1
        ''' places coins '''
        for obj in self._arr:
            for i in range(0,obj._dim_x):
                for j in range(0,obj._dim_y):
                    if i+obj._x_cor < 49:
                        background.set_arr(i+obj._x_cor,j+obj._y_cor,Fore.YELLOW+self._shape+Style.RESET_ALL+Back.BLACK) 
                        background.set_located(i+obj._x_cor,j+obj._y_cor,self._name)
        # for lis in self._arr:
            # print(lis)

            # if lis[2]==0:
            #     for i in range(lis[3]):
            #         if lis[1]+i<350:
            #             # print(str(lis[0])+' '+str(lis[1]+i))
            #             # background.arr[lis[0]][lis[1]+i]=Fore.YELLOW+self.shape+Style.RESET_ALL+Back.BLACK
            #             background.set_arr(lis[0],lis[1]+i,Fore.YELLOW+self._shape+Style.RESET_ALL+Back.BLACK)
            #             background.set_located(lis[0],lis[1]+i,self._name)
            # if lis[2]==1:
            #     for i in range(lis[3]):
            #         if lis[0]+i<48:
            #             # print(str(lis[0]+i)+' '+str(lis[1]))
            #             background.set_arr(lis[0]+i,lis[1],Fore.YELLOW+self._shape+Style.RESET_ALL+Back.BLACK)
            #             background.set_located(lis[0]+i,lis[1],self._name)
