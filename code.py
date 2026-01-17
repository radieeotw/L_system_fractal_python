import tkinter as tk
import turtle

root=tk.Tk()
root.title("L-System Fractal Architect")
root.geometry("1000x600")

canvas=tk.Canvas(root,width=700,height=600,bg="white")
canvas.pack(side=tk.LEFT)

screen=turtle.TurtleScreen(canvas)
screen.bgcolor("white")
t=turtle.RawTurtle(screen)
t.speed(0)
t.hideturtle() 

#control panel
ctrl_frame=tk.Frame(root,padx=10,pady=10)
ctrl_frame.pack(side=tk.RIGHT,fill=tk.Y)

tk.Label(ctrl_frame, text="L-System Fractal Architect",font=("Arial", 14, "bold")).pack(pady=10)

#axiom
tk.Label(ctrl_frame,text="Axiom").pack(anchor="w")
axentry=tk.Entry(ctrl_frame,width=30)
axentry.pack(pady=5)


tk.Label(ctrl_frame,text="Rules (eg: F: F+F--F+F)").pack(anchor="w")
rules=tk.Entry(ctrl_frame,width=30)
rules.pack(pady=5)

tk.Label(ctrl_frame,text="Angle").pack(anchor="w")
angle_entry=tk.Entry(ctrl_frame,width=30)
angle_entry.pack(pady=5)

tk.Label(ctrl_frame,text="Iterations").pack(anchor="w")
iter_entry=tk.Entry(ctrl_frame,width=30)
iter_entry.pack(pady=5)


#l system expansion
def lsystem(axiom,rules,iterations):
    curr_str=axiom
    for i in range(iterations):
        new_str=""
        for j in curr_str:
            new_str=new_str+rules.get(j,j)
        curr_str=new_str
    return curr_str


def draw(instructions, angle, step):
    t.clear()
    t.penup()
    t.goto(0, -250)
    t.setheading(90)
    t.pendown()

    stack = []

    screen.tracer(0, 0)

    n=len(instructions)
    for i, cmd in enumerate(instructions):
        green=i/n
        t.pencolor(0,green,0)
        if cmd == "F":
            t.forward(step)

        elif cmd == "+":
            t.right(angle)

        elif cmd == "-":
            t.left(angle)

        elif cmd == "[":
            stack.append((t.position(), t.heading()))

        elif cmd == "]" and stack:
            pos, heading = stack.pop()
            t.penup()
            t.goto(pos)
            t.setheading(heading)
            t.pendown()

    screen.update()

def generate():
    axiom = axentry.get().strip()
    rule_text = rules.get().strip()
    angle = float(angle_entry.get())
    iterations = int(iter_entry.get())

    rule_dict = {}
    if ":" in rule_text:
        key, value = rule_text.split(":")
        rule_dict[key.strip()] = value.strip()

    result = lsystem(axiom, rule_dict, iterations)
    step=max(2,12-iterations)
    draw(result, angle,step)

button=tk.Button(ctrl_frame,text="Generate Pattern ",command=generate)
button.pack(pady=20)

root.mainloop()