#第一个函数名称为x1(a,b)
#分数加减变成x2（a，b）
#把题目数量定为了_n
#把数字的范围定义成了_r
import random
from fractions import Fraction
##随机生成两个分数
print("输入数字的范围")
_r= int(input())
def createF():
    fz1 = random.randint(0, _r)
    if fz1 == 0:
        fm1 = random.randint(1,_r )
    else:
        fm1 = random.randint(1, _r)
    f1 = Fraction(fz1, fm1)
    fz2 = random.randint(1, _r)
    fm2 = random.randint(20, 20)
    f2 = Fraction(fz2, fm2)
    return f1, f2

def f(f):#分数的转换
    a=f.numerator #分子
    b=f.denominator #分母
    if a%b==0:#为整数
        return '%d'%(a/b)
    elif a<b:#为真分数
        return '%d%s%d' % (a,'/',b)
    else:#为带分数
        c=int(a/b)
        a = a - c * b
        return '%d%s%d%s%d' % (c,'’',a,'/',b)


#两个分数的四则运算
def x2(q,ans):
    symbol = random.choice(['+','-','*','/'])
    f1,f2 = createF()
    if symbol =='+':
        while f1+f2>1:
            f1,f2 = createF()
        q.append(str(f1)+'+'+str(f2)+'=')
        ans.append(f1+f2)
    elif symbol =='-':
        f1,f2 = max(f1,f2),min(f1,f2)#防止出现负数
        q.append(str(f1)+'-'+str(f2)+'=')
        ans.append(f1-f2)
    elif symbol == '*':
        while f1*f2>1:
            f1,f2 = createF()
        q.append(str(f1)+'×'+str(f2)+'=')
        ans.append(f1*f2)
    else:
        while f1/f2>1:
            f1,f2=createF()
        q.append(str(f1)+'÷'+str(f2)+'=')
        ans.append(Fraction(f1,f2))

#两个整数的四则运算
def x1(a,b):
    symbol = random.choice(['+', '-', '*', '/'])  # 生成随机符号
    if symbol == '+':
        n1 = random.randint(0, _r)
        n2 = random.randint(0, _r)
        a.append(str(n1) + '+' + str(n2) + '=')
        b.append(n1 + n2)
    elif symbol == '-':
        n1 = random.randint(0, _r)
        n2 = random.randint(0, _r)
        n1,n2 = max(n1,n1),min(n1,n2)#防止出现负数
        a.append(str(n1) + '-' + str(n2) + '=')
        b.append(n1 - n2)
    elif symbol == '*':
        n1 = random.randint(0, _r)
        n2 = random.randint(0, _r)
        a.append(str(n1) + '×' + str(n2) + '=')
        b.append(n1 * n2)
    else:
        n1 = random.randint(0, _r)
        if n1 == 0:
            n2 = random.randint(1, _r)
        else:
            n2 = random.randint(1, n1 + 1)
        a.append(str(n1) + '÷' + str(n2) + '=')
        b.append(Fraction(n1, n2))

def main():
    while 1:
        print("输入题目的数量:", end='  ')
        _n = int(input())
        p = 100 / _n
        s = 0
        a = []
        b = []
        c = []
        for i in range(_n):
            n = random.randint(1, 4)
            if n == 1:
                x1(a,b)
                g=Fraction(b[i])
                c.append(f(g))
            else:
                x2(a, b) #c2(q,ans)
                g = Fraction(b[i])
                c.append(f(g))#记录带分数答案
        for i in range(_n):
            z = open("exersices.txt", "a+")  # open-close写入
            z.write(str(i))
            z.close
        for i in range(_n):
            print("第{}题：{}".format(i + 1, a[i]), end="  ")
            a1 = input()       #a
            if a1 == str(b[i]):
                s = s + p
        print("所得的分数为：{}".format(s))
        print("正确答案：", end="  ")
        for i in range(_n):
            if str(b[i]) == str(c[i]):
                print(a[i] + str(b[i]))
            else:
                print("{}{}或{}".format(q[i],str(c[i]),str(b[i])))
        for i in range(_n):
            z = open("answer.txt", "a+")  # open-close写入
            z.write(str(i))
            z.close
if __name__ == '__main__':
    main()