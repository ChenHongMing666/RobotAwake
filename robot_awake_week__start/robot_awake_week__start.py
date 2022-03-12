import pygame
import os
from time import sleep,asctime

class screen :
    def __init__(self) -> None:
        self.size = {"weith":40,"higth":40}

    def _text(self,infor):
        line = '──'*39
        space = '  '*(40-len(infor))
        massage = f"┌─{line}─┐\n •{infor}{space}\n└─{line}─┘"
        return massage

    def Show(self,masssage,img):
        for i in range(len(masssage)+1):
            n = os.system('cls')
            self.Title()
            self.Body(img)
            print(self._text(masssage[0:i:1]))
            sleep(1/12)
        
    def Title(self):
        a = f"{asctime()}".center(80,"-")
        print(a)
    
    def Body(self,img):
        pass



if __name__ == "__main__" :
    a = screen()
    a.Show("wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww",None)
    sleep(2)


