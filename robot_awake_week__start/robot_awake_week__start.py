#from story import lines
from operator import ne
import os
import random
from time import sleep,asctime

class cmd_game_strture :
    def __init__(self) -> None:
        self.size = {"weith":100,"higth":100}#定义窗口大小

    def _text(self,infor,person)->str:# 基本文本框 内容，说话人
        line = f"【{person}】".center(self.size["weith"]-2,"─")#上方的人名
        un_line = self.size["weith"]*"─"
        massage = f"┌─{line}─┐\n •{infor}\n└─{un_line}─┘"
        return massage

    def Show(self,mas="",img="",type="text",ques="请选择",per="???",cho_t="A",choices={})->str:# 显示函数 消息-》text，字符图片，问题-》choice，出题人or说话人，正确选项，一些选项
        os.system('cls')#打印前清屏
        print("\033[1;32;40m",end="")#前景色 绿，背景色 黑
        self.Title()#时间头
        self.Body(img)#主体图片
        #功能分类
        if type == "text":#纯文本
            print(self._text(mas,per))
            self.event = input("按回车健（enter）以继续")#继续游戏
        if type == "choice":#选择
            flag = 1
            while flag:
                print(self._choice(ques,per,choices))
                self.event = input("你的选择:")#选项输入
                if cho_t == self.event :
                    self.is_t = True
                else :
                    self.is_t = False
                if self.choi.get(self.event.upper(),False):
                    self.next_step = self.choi[self.event.upper()][1]
                    self.next_step()#回调函数，实现分线
                    flag = 0
                else:
                    print("请输入正确选项！！！")
                    sleep(2)
                    os.system('cls')#打印前清屏
                    print("\033[1;32;40m",end="")#前景色 绿，背景色 黑
                    self.Title()#时间头
                    self.Body(img)#主体图片

        if type == None:
            pass

    def Title(self):
        a = f"{asctime()}".center(self.size["weith"]+4,"-")#中间显示现在时间
        print(a)

    def _choice(self,title,person,choices):#辅助 show 实现选择功能
        massage = title#导入问题
        self.choi = choices
        for i in choices:#导入选项
            value = choices[i][0]#dict 的值
            massage += f"\n\t{i.upper()}:{value}"
        return self._text(massage,person)#返回值格式化

    def Body(self,img):#显示图片
        print(img)

class game_main_viwe(cmd_game_strture,):
    def __init__(self) -> None:
        super().__init__()
        #开头动画
        self.start_video = [

            """

""","""
0 0 0  0  0   0   0   0   0   0    000 
""","""
0 0 0  0  0   0   0   0   00  00  00000
0 0 0  0  0   0   0   0   0   0    000
""","""

0000 00 000 0 0 0 0 0 0 0 00 000 000000
0 0 0  0  0   0   0   0   00  00  00000
0 0 0  0  0   0   0   0   0   0    000
""","""
0000000000000 000 000 000000 0000000000
000000000000000000000000000000000000000
0000 00 000 0 0 0 0 0 0 0 00 000 000000
0 0 0  0  0   0   0   0   00  00  0000
""","""
00000000000000000000000000000000000000
0000000000000 000 000 000000 0000000000
000000000000000000000000000000000000000
0000 00 000 0 0 0 0 0 0 0 00 000 000000
0 0 0  0  0   0   0   0   00  00  0000
""","""
000000000000000000000000000000000000000
00000000000000000000000000000000000000
000000000000000000000000000000000000000
0000 00 000 0 0 0 0 0 0 0 00 000 000000
0 0 0  0  0   0   0   0   00  00  00000
""","""
000000000000000000000000000000000000000
000000000000000000000000000000000000000
000000000000000000000000000000000000000
000000000000000000000000000000000000000
0000 00 000 0 0 0 0 0 0 0 00 000 000000
""","""
000000000000000000000000000000000000000
000000000000000000000000000000000000000
000000000000000000000000000000000000000
000000000000000000000000000000000000000
000000000000000000000000000000000000000
""","""
000000000000000000000000000000000000000
0■■■00■00■0000■000■00000000000000000000
0■0000■■■■000■0■0■0■0000000000000000000
0■■■00■00■00■000■000■000000000000000000
000000000000000000000000000000000000000
""","""
000000000000000000000000000000000000000
0■■■00■00■0000■000■00000000000000000000
0■0000■■■■000■0■0■0■0000000000000000000
0■■■00■00■00■000■000■000000000000000000
000000000000000000000000000000000000000
"""]
        #图片 2077
        self.img_2077 = """
        ■■■■■    ■■■■■    ■■■■■    ■■■■■       ■     ■
            ■    ■   ■        ■        ■      ■■     ■
           ■     ■   ■        ■        ■     ■ ■     ■
          ■      ■   ■        ■        ■    ■■■■■    ■
        ■■■■■    ■■■■■        ■        ■年     ■  月 ■  日
        """
        #故事剧情
        self.story = [
            {"type":"text","mas":"2077年4月1日".center(self.size["weith"]),"img":self.img_2077,"per":"SYSTEM","img":self.img_2077,'cho_t':"","choices":'','next':1,"flag":"run"},
            {"type":"text","mas":"世界跟我们开了一个大大的玩笑","img":self.img_2077,"per":"SYSTEM","img":self.img_2077,'cho_t':"","choices":'','next':2,"flag":"run"},
            {"type":"text","mas":"世界陷入了一片混乱","img":self.img_2077,"per":"SYSTEM","img":self.img_2077,'cho_t':"","choices":'','next':3,"flag":"run"},
            {"type":"text","mas":"因为一场特大的疫情","img":self.img_2077,"per":"SYSTEM","img":self.img_2077,'cho_t':"","choices":'','next':4,"flag":"run"},
            {"type":"text","mas":"让人类陷入了困境","img":self.img_2077,"per":"SYSTEM","img":"""
    本报讯 2076年12月30日，在学园  │    宏铭社电报  一方通行（大爷）的演唱
都市发现第一例感染噬菌体病毒患者... │  会 —— 恶党美学 将在2077年1月1日开幕
─────────────────────────────────────────────────────────────────────
    紧急通知，第一学区出现大规模的疫│    学园都市与美国、中国、俄罗斯的外交
情，原本在1月1日的演唱会推迟到4月1日│关系恶化
─────────────────────────────────────────────────────────────────────
    人民日报、CBM、VGTRK等多家媒体点名批评学院都市的行为
─────────────────────────────────────────────────────────────────────
    ...
─────────────────────────────────────────────────────────────────────
    学园都市理事长宣布向世界宣战
""",'cho_t':"","choices":'','next':5,"flag":"run"},
            {"type":"text","mas":"面对战争，人类是多么的无力，弱小","img":self.img_2077,"per":"SYSTEM","img":"",'cho_t':"","choices":'','next':6,"flag":"run"},
            {"type":"choice","per":"SYSTEM","quse":"所以，选择身份","chioces":{"A":["普通人",self.change_line],"B":["管理人员",self.change_line]},'next':"end","flag":"end"},
        ]
    
    def change_line(slef):#估计没用
        pass
    
    def start(self):#开头
        for f in self.start_video:
            f_n = ""
            f.join(" ").split()
            for i in f:
                if i == 0:
                    f_n += random.choice([0,1])
                else:
                    f_n += i
            self.Show(img=f_n,type=None)
            sleep(1/12)
        print("""
主办方：
    陈宏铭
编程：
    陈宏铭
鸣谢：
    农昊——剧本
    吴聿诚——剧本
        ""","""感谢游玩！！！""")
        sleep(2)
    
    def main_viwe(self):
        os.system("cls")
        self.Show(mas="屑智周：启航")
        self.Show(type="choice",
            per="SYSTEM",
            ques="主菜单",
            choices={
                "A":["新游戏",self.new_game],
                "B":["读取存档",self.read_save],
                "C":["退出",exit]
                }
        )

    def save(self):
        pass

    def new_game(self):#未作保存
        i = self.story[0]
        flag = "run"
        while 1:
            self.Show(type=i.get("type",""),mas=i.get("mas",""),img=i.get("img",""),cho_t=i.get("cho_t",""),choices=i.get("chioces",""),per=i.get("per",""),ques=i.get("quse",""))
            flag = i.get("flag","end")
            if flag == "end":
                break
            if self.event.lower() == "q" or self.event.lower() == "quit" or self.event.lower() == "exit" :
                self.save()
                break
            i = self.story[i.get("next",0)]

    def read_save(self):
        print("r_s")
        pass

#回调函数，实现分支

if __name__ == "__main__" :
    a = game_main_viwe()#创建实例
    a.start()
    a.main_viwe()
