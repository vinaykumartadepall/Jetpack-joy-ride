from colorama import Fore,Back,Style
from Objects import objects
class beams(objects):
    def __init__(self):
        self._name='o'
        self.__hor_shape=[]
        self.__ver_shape=[]
        self.__tilt_shape=[]
        self._arr=[]
        self._count=10

        ''' get shapes from files '''

        f=open('ascii_arts/h_beam.txt','r')
        __st=f.read()
        __st=__st.split('\n')
        for s in __st:
            s=[Fore.RED+char +Style.RESET_ALL+Back.BLACK for char in s]
            self.__hor_shape.append(s)

        f=open('ascii_arts/v_beam.txt','r')
        __st=f.read()    
        __st=__st.split('\n')
        for s in __st:
            s=[Fore.RED+char +Style.RESET_ALL+Back.BLACK for char in s]
            self.__ver_shape.append(s)

        f=open('ascii_arts/slant_beam.txt','r')
        __st=f.read()    
        __st=__st.split('\n')
        for s in __st:
            s=[Fore.RED+char +Style.RESET_ALL+Back.BLACK for char in s]
            self.__tilt_shape.append(s)
        
    ''' getters and setters ''' 

    def get_ver_shape(self):
        return self.__ver_shape
    
    def get_hor_shape(self):
        return self.__hor_shape

    def get_tilt_shape(self):
        return self.__tilt_shape
    
    # print(tilt_shape)

    
    # for i in hor_shape:
    #     st=''
    #     for j in i:
    #         st=st+j
    #     print(st)
#     for i in ver_shape:
#         st=''
#         for j in i:
#             st=st+j
#         print(st)
#     for i in tilt_shape:
#         st=''
#         for j in i:
#             st=st+j
#         print(st)
    
h=beams()