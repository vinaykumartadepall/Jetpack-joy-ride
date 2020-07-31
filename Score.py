from colorama import Back, Fore, Style
class score():
    def __init__(self):
        self.__lives=5
        self.__points=0
        self.__time=120
        self.__shield='ready'
        self.__boss=50
    def print_scores(self):
        # print(Back.GREEN+Fore.RED)
        # st='                                                                                                                                                       '
        # st1='                                                                                                                                            '
        st2='                            '
        # st3='                           '
        st4='                                                                                                                                                                                                            '
        print("\033[%d;%dH" % (0,0))
        for i in range(3):
            print(Back.YELLOW+st4)
        print("\033[%d;%dH" % (0,0))
        print(Fore.RED+Back.YELLOW+st4+'  Lives : '+str(self.__lives)+st2+'Score : '+str(self.__points)+st2+'Time Reamining : '+str(self.__time)+st2+'Shield back in : '+str(self.__shield)+st2+'Viserion lives : '+str(self.__boss))
        # print(Fore.RED+Back.BLUE+st4+'Lives : '+str(self.__lives)+st+'Score : '+str(self.__points)+st2+Style.RESET_ALL+Back.BLUE)
        # # print()
        # print(Fore.RED+'Time Reamining : '+str(self.__time)+st1+'Shield back in: '+str(self.__shield)+Style.RESET_ALL+Back.BLUE)
        # print(Style.RESET_ALL)
    
    def inc_time(self):
        self.__time=self.__time-1
        # if type(self.__shield)==int and self.__shield>0:
        #     self.__shield=self.__shield-1
        # else:
        #     self.__shield='Shield ready'
    
    def inc_points(self,val):
        self.__points=self.__points+val

    def dec_lives(self):
        self.__lives=self.__lives-1
    
    def get_lives(self):
        return self.__lives
    
    def get_score(self):
        return self.__points

    def set_shield(self,val):
        if val>0:
            self.__shield='active'
        if val<0:
            self.__shield=-val
            self.__shield=int(self.__shield/10)
        if val==0:
            self.__shield='ready'

    def set_bosses(self,val):
        self.__boss=val

    def get_time(self):
        return self.__time