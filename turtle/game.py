import turtle
import random
import math

wn = turtle.Screen()
turtle.setup(500,500)
p1 = turtle.Turtle()
p2 = turtle.Turtle()
p1.shape("turtle")
p2.shape("turtle")

# 방향함수
def up():
    p1.setheading(90)
def left():
    p1.setheading(180)
def right():
    p1.setheading(0)
def down():
    p1.setheading(270)

def up2():
    p2.setheading(90)
def left2():
    p2.setheading(180)
def right2():
    p2.setheading(0)
def down2():
    p2.setheading(270)

# 1,2,R,Q
def one():
    onestart()
def two():
    twostart()
def R():
    mainscreen()
def Q():
    wn.bye()

#메인 화면
def mainscreen() :
    # p1.reset() 필요없어 보여서 뺐어
    p1.color("white")
    p2.color("white")
    wn.bgpic("main.png")
    # turtle.hideturtle() 필요없어 보여서 뺐어
    # turtle.clear() 필요없어 보여서 뺐어
    # turtle.pu() #penup
    wn.onkeypress(one, "1")
    wn.onkeypress(two, "2")
    wn.onkeypress(Q, "q")
    wn.listen()
    turtle.mainloop()

food = [] # 음식 생성을 위한 리스트 구현
def delicious(): # 음식 터틀 생성
    global food
    makefood=turtle.Turtle()
    makefood.shape("circle")
    makefood.color("white")
    makefood.penup() # (적->음식) 움직인 경로 숨기기
    makefood.speed(1)
    food.append(makefood) # (적->음식)을 리스트에 넣어줌

#제곱 + 제곱에 루트씌우는거 20 보다작으면 충돌
def kill(t1,t2):
    # 거리 구하는 함수
    d = math.sqrt(math.pow (t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2) )
    if d < 20:
        return True
    else:
        return False

enemyls = []#적의 생성 리스트를 만들어줌
count = 0 # 적수
#적 만들기
def enemy():
    global enemyls #적의 위치를 다른 함수에서도 알기 위해 글로벌변수로 해줌
    enemy=turtle.Turtle()
    enemy.shape("triangle")
    enemy.penup() #적 움직인 경로 숨기기
    enemy.speed(random.randint(1,5))#1~5 랜덤 스피드
    enemyls.append(enemy)#적을 리스트에 넣어용
    global count
    count += 1

# 부딪혔을 떄 현재 좌표 기준으로 거리 구하기
# 제곱 + 제곱에 루트씌우는거 20 보다작으면 충돌
def die(t1,t2):
    d = math.sqrt(math.pow (t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2) )
    if d < 20:
        return True
    else:
        return False

for i in range(7):
    enemy()
for i in range(5):
    delicious()

# 1인용
def onestart():
    eat=0
    wn.bgpic("background.png")
    p1.showturtle()
    p2.hideturtle()
    turtle.clear()

    p1.penup()  # 선이 그려지지 않게
    p1.speed(0)
    p1.goto(210, 210) # 오른쪽 위
    p1.color("yellowgreen")

    #적 등장
    for i in range(count):
        enemyls[i].reset()
        enemyls[i].color("white")
    for i in range(5):
        food[i].reset()
        food[i].color("hotpink")

    enemyxy = []
    for i in range(count):
        enemyxy.append(random.randint(1, 6))
        enemyxy.append(random.randint(1, 6))
    foodxy = []
    for i in range(5):
        foodxy.append(random.randint(1, 6))
        foodxy.append(random.randint(1, 6))

    #방향키 조절
    wn.onkeypress(up, "Up")
    wn.onkeypress(left, "Left")
    wn.onkeypress(right, "Right")
    wn.onkeypress(down, "Down")

    wn.listen()
    wn.tracer(5)

    #출발
    while True:
        # box안에서만 움직이게
        p1.clear()
        if p1.xcor() < 250 and p1.xcor() > -250 and p1.ycor() < 250 and p1.ycor() > -250 :
            p1.fd(3)

        # 벽에 부딪히면 돌아오게ㅔ
        if p1.xcor() > 240 or p1.xcor() < -240 :
            p1.left(180)
        if p1.ycor() > 240 or p1.ycor() < -240 :
            p1.left(180)

        for i in range(len(enemyls)):
            enemyls[i].clear()
            # 적들 박스 못나가게 랜덤좌표 계산해서 튕겨주기
            if enemyls[i].xcor() > 240 or enemyls[i].xcor() < -240: # 적들의 현재 x좌표
                enemyxy[2 *(i-1)] = -enemyxy[2 *(i-1)]
            if enemyls[i].ycor() > 240 or enemyls[i].ycor() < -240: # 적들의 현재 y좌표
                enemyxy[2 *i-1] = -enemyxy[2 *i-1]
            enemyls[i].goto(enemyls[i].xcor() - enemyxy[2 *(i-1)], enemyls[i].ycor() - enemyxy[2 *i-1])
            if die(p1, enemyls[i]):
                for i in range(count):
                    enemyls[i].ht()
                for i in range(5):
                    food[i].ht()
                wn.tracer(1)
                gameover()

        for i in range(len(food)):
            food[i].clear()
            # 음식들 박스 못나가게
            if food[i].xcor() > 240 or food[i].xcor() < -240:
                foodxy[2 * (i - 1)] = -foodxy[2 * (i - 1)]
            if food[i].ycor() > 240 or food[i].ycor() < -240:
                foodxy[2 * i - 1] = -foodxy[2 * i - 1]
            food[i].setpos(food[i].xcor() - foodxy[2 * (i - 1)], food[i].ycor() - foodxy[2 * i - 1])
            if kill(p1, food[i]):
                food[i].pu()
                food[i].ht()
                food[i].goto(random.randint(-240,240),random.randint(-240,240)) # 죽으면 나오는 위치 설정
                food[i].st()
                eat+= 1

        #점수
        turtle.undo()
        turtle.penup()
        turtle.color("white")
        turtle.hideturtle()
        turtle.setpos(-220, 220)
        score = "Score : %d" % eat
        turtle.write(score, move=False, align="left", font=("Arial", 15, "normal"))
        wn.update()

# 2인용
def twostart():
    eat1=0;eat2=0
    wn.bgpic("background.png")
    p1.showturtle()
    p2.showturtle()
    turtle.clear()

    p1.penup()
    p1.speed(0)
    p1.goto(210, 210) #오른쪽위

    p2.penup()
    p2.speed(0)
    p2.goto(-210, 210) #왼쪽위

    p1.color("yellowgreen")
    p2.color("yellow")

    # 적이랑 음식 등장
    for i in range(count):
        enemyls[i].reset()
        enemyls[i].color("white")
    for i in range(5):
        food[i].reset()
        food[i].color("hotpink")

    enemyxy = []
    for i in range(count):
        enemyxy.append(random.randint(1, 6))
        enemyxy.append(random.randint(1, 6))
    foodxy = []
    for i in range(5):
        foodxy.append(random.randint(1, 6))
        foodxy.append(random.randint(1, 6))

    # 방향키 조절
    wn.onkeypress(up, "Up")
    wn.onkeypress(left, "Left")
    wn.onkeypress(right, "Right")
    wn.onkeypress(down, "Down")

    wn.onkeypress(up2, "w")
    wn.onkeypress(left2, "a")
    wn.onkeypress(right2, "d")
    wn.onkeypress(down2, "s")
    wn.listen()
    wn.tracer(5)

    #출발!
    while True:
        # box 안에서만 움직이게
        p1.clear()
        if p1.xcor() < 250 and p1.xcor() > -250 and p1.ycor() < 250 and p1.ycor() > -250 :
            p1.fd(3)
        p2.clear()
        if p2.xcor() < 250 and p2.xcor() > -250 and p2.ycor() < 250 and p2.ycor() > -250:
            p2.fd(3)

        # 벽에 부딪히면 돌아오게
        if p1.xcor() > 240 or p1.xcor() < -240 :
            p1.left(180)
        if p2.xcor() > 240 or p2.xcor() < -240 :
            p2.left(180)
        if p1.ycor() > 240 or p1.ycor() < -240 :
            p1.left(180)
        if p2.ycor() > 240 or p2.ycor() < -240 :
            p2.left(180)

        for i in range(len(enemyls)):
            enemyls[i].clear()
            # 적들 박스 못나가게 랜덤좌표 계산해서 튕겨주기
            if enemyls[i].xcor() > 240 or enemyls[i].xcor() < -240:#적들의 현재 x좌표
                enemyxy[2 * (i - 1)] = -enemyxy[2 * (i - 1)]
            if enemyls[i].ycor() > 240 or enemyls[i].ycor() < -240:#적들의 현재 y좌표
                enemyxy[2 * i - 1] = -enemyxy[2 * i - 1]
            enemyls[i].goto(enemyls[i].xcor() - enemyxy[2 * (i - 1)], enemyls[i].ycor() - enemyxy[2 * i - 1])

            if die(p1, enemyls[i]):
                for i in range(count):
                    enemyls[i].ht()
                for i in range(5):
                    food[i].ht()
                wn.tracer(1)
                gameover()

            if die(p2, enemyls[i]):
                for i in range(count):
                    enemyls[i].ht()
                for i in range(5):
                    food[i].ht()
                wn.tracer(1)
                gameover()

        for i in range(len(food)):
            food[i].clear()
            # 음식들 박스 못나가게
            if food[i].xcor() > 240 or food[i].xcor() < -240:
                foodxy[2 *(i-1)] = -foodxy[2 *(i-1)]
            if food[i].ycor() > 240 or food[i].ycor() < -240:
                foodxy[2 *i-1] = -foodxy[2 *i-1]
            food[i].setpos(food[i].xcor() - foodxy[2 *(i-1)], food[i].ycor() - foodxy[2 *i-1])
            if kill(p1, food[i]):
                food[i].pu()
                food[i].ht()
                food[i].goto(random.randint(-210, 210), random.randint(-210, 210)) # 죽으면 나오는 위치 설정
                food[i].st()
                eat1+= 1
            if kill(p2, food[i]):
                food[i].pu()
                food[i].ht()
                food[i].goto(random.randint(-210, 210), random.randint(-210, 210))  # 죽으면 나오는 위치 설정
                food[i].st()
                eat2 += 1
        #점수
        scored = 0
        scored += (eat1 + eat2)
        turtle.undo()
        turtle.penup()
        turtle.color("white")
        turtle.hideturtle()
        turtle.setpos(-220, 220)
        score = "Score : %d" % scored
        turtle.write(score, move=False, align="left", font=("Arial", 15, "normal"))
        wn.update()

def gameover():
    wn.bgpic("gameover.png")
    p1.hideturtle() # 거북이 숨김
    p2.hideturtle()

    wn.onkeypress(Q, "q")
    wn.onkeypress(R,"r")
    wn.listen()
    wn.mainloop()

mainscreen()
turtle.mainloop()