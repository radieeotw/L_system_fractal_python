import tkinter as tk
import turtle

root=tk.Tk()
root.title("L-System Fractal Architect")
root.geometry("1000x600")
root.configure(bg="black")

canvas=tk.Canvas(root,width=700,height=600,bg="white")
canvas.pack(side=tk.LEFT)

screen=turtle.TurtleScreen(canvas)
screen.bgcolor("white")
t=turtle.RawTurtle(screen)
t.speed(0)
t.hideturtle() 

#control panel
ctrl_frame=tk.Frame(root,padx=15,pady=15,bg="black")
ctrl_frame.pack(side=tk.RIGHT,fill=tk.Y)

tk.Label(ctrl_frame, text="L-System Fractal Architect",font=("Helvetica", 18, "bold"),fg="white",bg="black").pack(pady=15)


def create_label(text):
    tk.Label(
        ctrl_frame,
        text=text,
        font=("Helvetica", 11),
        fg="light cyan",
        bg="black"
    ).pack(anchor="w")

#axiom
create_label("Axiom")
axentry=tk.Entry(ctrl_frame,width=30,font=("Helvetica",10))
axentry.pack(pady=5)


create_label("Rules (eg: F: F+F--F+F)")
rules=tk.Entry(ctrl_frame,width=30,font=("Helvetica",10))
rules.pack(pady=5)

create_label("Angle")
angle_entry=tk.Entry(ctrl_frame,width=30,font=("Helvetica",10))
angle_entry.pack(pady=5)

create_label("Iterations")
iter_entry=tk.Entry(ctrl_frame,width=30,font=("Helvetica",10))
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
       
        t.pencolor("spring green")
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

button=tk.Button(ctrl_frame,text="Generate Pattern ",font=("Helvetica",12,"bold"),bg="light green",fg="black",command=generate)
button.pack(pady=25)

root.mainloop()
