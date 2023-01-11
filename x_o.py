def pole(f):
    num ='  0 1 2'
    print(num)
    for row,i in zip(f,num.split()): 
        print (f"{i} {' '.join(str(j) for j in row)}")

def user_vvod(f,user):
    while True:
        place=input(f"Ходит {user} .Введите координаты:").split()
        if len(place)!=2:
            print('Введите две координаты')
            continue
        #is digit str
        if not(place[0].isdigit() and place[1].isdigit()):
            print('Введите числа')
            continue
        x, y = map(int, place)
        if not(x>=0 and x<3 and y>=0 and  y<3):
            print('Вышли из диапазона')
            continue
        if f[x][y]!='-':
            print('Клетка занята')
            continue
        break
    return x,y

def position(f,user):
    f_list=[]
    print(f)
    for l in f:
        f_list+=l
    print(f_list)
    positions=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    indices = set([i for i, x in enumerate(f_list) if x == user])

    for pos in positions:
        if len(indices.intersection(set(pos)))==3:
            return True
    return False



def start(cell):

    count=0
    while True:
        pole(cell)
        if count%2==0:
            user='x'
        else:
            user = 'o'
        if count<9:
            x, y = user_vvod(cell,user)
            cell [x][y] = user

        elif count==9:
            print ('Ничья')
            break
        if position(cell,user):
            print(f"Выйграл {user}")
            break
        count+=1


cell = [['-'] * 3 for _ in range(3)]

start(cell)