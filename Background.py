from colorama import Fore, Back, Style
import subprocess as sp

class background:
    def __init__(self):
        background.__arr=[[]]
        background.__window_size=204
        background.__y_cor=0
        background.__located=[[]]
        background.__details=[[]]
        background.__field=[[]]
    # obj=[[]]

    def generate_background():
        '''generating the background'''
        background.__arr=[[' ' for i in range(500)] for i in range(50)]
        background.__located=[['N' for i in range(500)] for i in range(50)]
        background.__details=[[[0,0,0,0]for i in range(500)]for i in range(50)]
        background.__field=[['N' for i in range(500)] for i in range(50)]
        for i in range(500):
            background.__arr[0][i]=Back.YELLOW+Fore.RED+'_'+Style.RESET_ALL
            background.__arr[49][i]=Back.YELLOW+Fore.RED+' '+Style.RESET_ALL
            background.__located[0][i]='b'
            background.__located[49][i]='b'
    
    def print_background():
        '''printing the Background'''
        # Background.make_blue()
        for i in range(50):
            st=''
            for j in range(background.__window_size):
                try:
                    st+=background.__arr[i][j+background.__y_cor]
                except:
                    # f=open('out.txt','w')
                    # f.write(str(i)+' '+str(background.__y_cor)+'+'+str(j))
                    quit()
            print(Back.BLACK+st+Style.RESET_ALL)
    
    def print_loc():
        '''printing the Background'''
        for i in range(50):
            st=''
            for j in range(background.__window_size):
                st+=background.__located[i][j+background.__y_cor]
            print(st)

    def clear(x,y,dim_x,dim_y):
        # tmp=sp.call('clear',shell=True)
        # print(str(x)+' '+str(y)+' '+str(dim_x)+' '+str(dim_y))
        # tmp=sp.call('clear',shell=True)
        ''' clear/remove an object '''
        for i in range(0,dim_x):
            for j in range(0,dim_y):
                if background.__located[x+i][y+j]=='o' or background.__located[x+i][y+j]=='e' or background.__located[x+i][y+j]=='>':
                    background.__arr[x+i][y+j]=' '
                    background.__located[x+i][y+j]='N'


    '''  Getters and setters '''

    def get_y():
        return background.__y_cor
    
    def increment_y():
        background.__y_cor=background.__y_cor+1
    
    def get_arr(x,y):
        return background.__arr[x][y]

    def set_arr(x,y,val):
        background.__arr[x][y]=val

    def set_located(x,y,val):
        background.__located[x][y]=val
        
    def get_located(x,y):
        return background.__located[x][y]

    def set_field(x,y,c):
        background.__field[x][y]=c

    def get_field(x,y):
        return background.__field[x][y]

    def get_details(x,y,z):
        return background.__details[x][y][z]
    
    def set_details(x,y,z,val):
        background.__details[x][y][z]=val
    
    def get_window_size():
        return background.__window_size 