import turtle as t
k=30
t.tracer(0)
t.lt(90)
t.pencolor("green")
for i in range(15):
    t.pendown()
    t.fd(15*k)
    t.penup()
    t.goto(i*k,-1)
    
    for j in range(15):
        t.pendown()
        t.fd(15*k)
        t.penup()
        t.goto(0,i*k)
t.pencolor("black")
t.pendown()
t.goto(0,0); t.lt(90)
for i in range(4):
    for j in range(12):
        t.fd(k)#;t.dot(4)
    t.rt(90)

for i in range(5):
    for g in range(4):
        t.fd(k); t.dot(4)
    t.rt(45)
t.hideturtle(); t.goto(0,0)
t.penup()

        
    
    
