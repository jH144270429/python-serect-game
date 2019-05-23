import random

class game() :
    def serectgame(self):
        serect = random.randint(1,10)
        time = 0
        print('\n')
        print("猜1到1000以内的数字.")
        temp = input("请输入你要猜的数字：")
        number = int(temp)

        while 1:
            time += 1

            if number > 1000 or number < 1:
                print("请输入1到1000内的数")
                print('\n')

            elif number != serect:
                print('\n')
                print("你猜错啦！")

                if number > serect:
                    print('\n')
                    print("数字猜的大了一丢丢！")
                if number < serect:
                    print('\n')
                    print("数字猜的小了一丢丢！")
            else:
                print('\n')
                print("恭喜你猜对了，猜对了也没有奖励！哈哈哈！")
                break
                print('\n')
            temp = input("请重新输入你要猜的数字：")
            number = int(temp)

        return time

    def diaoyong(self):
        user = game()
        order = user.serectgame()
        if order > 10:
            print('\n')
            print("小老弟你一共猜了%d次,智商不错哈！" % order)
            print("你这个智商有点儿堪忧啊！")
        else:
            print('\n')
            print("小老弟你一共猜了%d次！" % order)


def main():

    user = game()
    user.diaoyong()

    while 1:
        print('\n')
        second = input("继续猜数请输入1，输入其他退出游戏！")
        if second == "1":
            user = game()
            user.diaoyong()
        else:
            break

    print('\n')
    print("已经成功退出管理系统")

if __name__ == '__main__':
        main()
