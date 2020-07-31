from Background import background
from random import randint
from colorama import Back,Fore,Style
class objects:
    def __init__(self):
        self._name=''
        self._shape=[[]]
        self._dim_x=0
        self._dim_y=0
        self._dim_z=0
        self._count=0
        self._arr=[]
        self._x_cor=0
        self._y_cor=0
    def generate(self):
        ''' generates objects randomly '''
        i=self._count-1
        while i>=0:
            lis=[]
            lis.append(randint(20,25))
            # lis.append(randint(15,400))
            lis.append(randint(26+(300/self._count)*(i+1),44+(300/self._count)*(i+1)))
            if self._name=='>':
                lis.append(randint(3,3))
                # print('\n\n\n\n\n\n\n'+str(lis[2])+'\n\n\n\n\n\n\n\n\n\n\n\n\n')
            else:
                lis.append(randint(0,2))

            # lis.append(randint(5,10))
            self._arr.append(lis)
            i-=1
            # print(lis)
        # print(self._arr)
        

    def place(self):
        ''' place an object '''
        for lis in self._arr:
            # print(lis)
            if lis[2]==0:
                self._shape=self.get_hor_shape()
                self._dim_x=2
                self._dim_y=11
            if lis[2]==1:
                self._shape=self.get_ver_shape()
                self._dim_x=6
                self._dim_y=2
            if lis[2]==2:
                self._shape=self.get_tilt_shape()
                self._dim_x=6
                self._dim_y=7
            if lis[2]==3:
                self._shape=[['>','>']]
                self._dim_x=1
                self._dim_y=2
            if lis[2]==4:
                self._shape=self.get_magnet_shape()
                self._dim_x=4
                self._dim_y=8
            for i in range(self._dim_x):
                for j in range(self._dim_y):
                    # print(str(lis[0]+i)+' '+str(lis[1]+j)+' '+str(i)+' '+str(j))
                    # print(self._shape[i][j])
                    # print(background.arr[lis[0]+i][lis[1]+j])
                    background.set_arr(lis[0]+i,lis[1]+j,self._shape[i][j])
                    background.set_details(lis[0]+i,lis[1]+j,0,lis[0])
                    background.set_details(lis[0]+i,lis[1]+j,1,lis[1])
                    background.set_details(lis[0]+i,lis[1]+j,2,self._dim_x)
                    background.set_details(lis[0]+i,lis[1]+j,3,self._dim_y)

                    if self._shape[i][j]!=Fore.RED+' '+Style.RESET_ALL+Back.BLACK:
                        background.set_located(lis[0]+i,lis[1]+j,self._name)