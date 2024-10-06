import turtle as t
import random

score = 0
playing = False
enemies = [] 
isCreate = False

enemies.append(t.Turtle())
enemies[0].shape("turtle")
enemies[0].color("red")
enemies[0].speed(0)
enemies[0].up()
enemies[0].goto(random.randint(-230, 230), random.randint(-230, 230))

ts = t.Turtle()
ts.shape("circle")
ts.color("green")
ts.speed(0)
ts.up()
ts.goto(random.randint(-230, 230), random.randint(-230, 230))

def turn_right():
    t.setheading(0)

def turn_up():
    t.setheading(90)

def turn_left():
    t.setheading(180)

def turn_down():
    t.setheading(270)

def start():
    global playing
    if not playing:
        playing = True
        t.clear()
        play()

def play():
    global score
    global playing
    global isCreate
    t.forward(10)

    # 경계 체크 및 반사
    if abs(t.xcor()) > 230 or abs(t.ycor()) > 230:
        if t.xcor() > 230:
            t.setx(230)
        elif t.xcor() < -230:
            t.setx(-230)
        if t.ycor() > 230:
            t.sety(230)
        elif t.ycor() < -230:
            t.sety(-230)

        t.right(180)  # 반대 방향으로 회전
    
    if isCreate and score != 0 and score % 3 == 0:
        tmp = t.Turtle()
        tmp.shape("turtle")
        tmp.color("red")
        tmp.speed(0)
        tmp.up()
        tmp.goto(random.randint(-230, 230), random.randint(-230, 230))
        enemies.append(tmp)
        isCreate = False
        

    if random.randint(1, 5) == 3:
        for e in enemies:
            ang = e.towards(t.pos())
            e.setheading(ang)

    speed = score + 5
    if speed > 15:
        speed = 15
    for e in enemies:
        e.forward(speed)

    for e in enemies:
        if t.distance(e) < 12:
            text = "Score : " + str(score)
            message("Game Over", text)
            playing = False
            score = 0
            while len(enemies) != 1:
                enemy = enemies.pop()
                enemy.hideturtle() 

    if t.distance(ts) < 12:
        score += 1
        if score % 3 == 0:
            isCreate = True
        t.write(score)
        ts.goto(random.randint(-230, 230), random.randint(-230, 230))

    if playing:
        t.ontimer(play, 100)

def message(m1, m2):
    t.clear()
    t.goto(0, 100)
    t.write(m1, False, "center", ("", 20))
    t.goto(0, -100)
    t.write(m2, False, "center", ("", 15))
    t.home()

t.title("Turtle Run")
t.setup(500, 500)
t.bgcolor("orange")
t.shape("turtle")
t.speed(0)
t.up()
t.color("white")
t.onkeypress(turn_right, "Right")
t.onkeypress(turn_up, "Up")
t.onkeypress(turn_left, "Left")
t.onkeypress(turn_down, "Down")
t.onkeypress(start, "space")
t.listen()
message("Turtle Run", "[Space]")
play()
t.mainloop()
