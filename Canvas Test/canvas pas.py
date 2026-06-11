from graphics import Canvas
import random
import time

money = 10
money_text = None
title_text = None
is_spinning = False
symbols =["circle", "triangle", "square"]
values = {
    "circle": 5,
    "triangle": 3,
    "square": 2
}


#Makes Circle for slots screen
#Value (5)
def draw_circle(canvas, x, y):
    canvas.create_oval(
        x, y,
        x + 80, y + 80,
        color="red"
    )
    
#Makes Square for slots screen
#Value (3)
def draw_square(canvas, x, y):
    canvas.create_rectangle(
        x, y,
        x + 80, y + 80,
        color="blue"
    )
    
#Makes triangle for slots screen
#Value (2)
def draw_triangle(canvas, x, y):
    canvas.create_polygon(
        x + 40, y,        
        x, y + 80,        
        x + 80, y + 80,  
        fill="yellow"
    )
    
#makes Rectangles with Auto borders
def bordered_rectangle(canvas, left, top, right, bottom, border_color, fill_color, border_width):
    canvas.create_rectangle(
        left, top,
        right, bottom,
        color=border_color
    )

    canvas.create_rectangle(
        left + border_width,
        top + border_width,
        right - border_width,
        bottom - border_width,
        color=fill_color
    )
    
#Spin Rules 
def spin():
    slot1 = random.choice(symbols)
    slot2 = random.choice(symbols)
    slot3 = random.choice(symbols)

    return slot1, slot2, slot3

def draw_symbol(canvas, symbol, x, y):
    if symbol == "circle":
        draw_circle(canvas, x, y)
    elif symbol == "triangle":
        draw_triangle(canvas, x, y)
    elif symbol == "square":
        draw_square(canvas, x, y)
        
def render_slots(canvas, s1, s2, s3):
    # Left
    draw_symbol(canvas, s1, 75, 160)

    # Middle
    draw_symbol(canvas, s2, 245, 160)

    # Right
    draw_symbol(canvas, s3, 415, 160)

def render(canvas, s1, s2, s3):
    # redraw slot backgrounds first (THIS FIXES THE UGLY LOOK)

    bordered_rectangle(canvas, 30, 100, 210, 300, "black", "white", 3)
    bordered_rectangle(canvas, 210, 100, 390, 300, "black", "white", 3)
    bordered_rectangle(canvas, 390, 100, 570, 300, "black", "white", 3)

    # draw symbols on top
    draw_symbol(canvas, s1, 75, 160)
    draw_symbol(canvas, s2, 245, 160)
    draw_symbol(canvas, s3, 415, 160)
    
#flicker symbols on spin
def fake_spin(canvas):
    for _ in range(8):  # number of “spin frames”

        s1 = random.choice(symbols)
        s2 = random.choice(symbols)
        s3 = random.choice(symbols)

        render(canvas, s1, s2, s3)
        canvas.update()
        time.sleep(0.1)

#The money box updating
def update_money_display(canvas):
    
    
    
    global money_text

    if money_text is not None:
        canvas.delete(money_text)

    money_text = canvas.create_text(
        500,
        410,
        text=f"${money}",
        font="impact 30",
        anchor="center",
        color="green"
    )
#give you the money
def calculate_payout(canvas, s1, s2, s3):
    global money

    winnings = 0

    if s1 == s2 == s3:
        winnings = values[s1] * 3
        set_title(canvas, "JACKPOT!", "gold")
        flash_screen(canvas)

    elif s1 == s2 or s1 == s3 or s2 == s3:
        winnings = 2

    if winnings > 0:
        money += winnings
        show_floating_text(canvas, 500, 410, winnings)
        
#money pop up when winning 
def show_floating_text(canvas, x, y, amount):

    if amount >= 10:
        color = "gold"
        size = 30
        prefix = "JACKPOT +$"
    else:
        color = "green"
        size = 20
        prefix = "+$"

    text = canvas.create_text(
        x,
        y,
        text=f"{prefix}{amount}",
        font=f"impact {size}",
        color=color,
        anchor="center"
    )

    for i in range(15):
        canvas.move(text, 0, -2)
        canvas.update()
        time.sleep(0.03)

    canvas.delete(text)

    # animate upward
    for i in range(15):
        canvas.move(text, 0, -2)
        canvas.update()
        time.sleep(0.03)

    canvas.delete(text)
    
def set_title(canvas, text, color="gold"):
    global title_text

    canvas.delete(title_text)

    title_text = canvas.create_text(
        300,
        50,
        text=text,
        font="Impact 22",
        color=color,
        anchor="center"
    )

def flash_screen(canvas):
    for _ in range(3):
        canvas.set_canvas_background_color("yellow")
        canvas.update()
        time.sleep(0.1)

        canvas.set_canvas_background_color("white")
        canvas.update()
        time.sleep(0.1)
        
def main():
    global money
    global title_text
    
    canvas = Canvas(600, 500)
    
    #center frame
    bordered_rectangle(
        canvas,
        30, 100,
        570, 300,
        "black",
        "white",
        3
    )
    
      #top frame
    canvas.create_rectangle(
        0, 0,
        600, 100,
        color='red'
    )

    #left frame
    canvas.create_rectangle(
        0, 0,
        30, 500,
        color='gray'
    )
    
    #right frame
    canvas.create_rectangle(
        570, 0,
        600, 500,
        color='gray'
    )
    
    #bottom frame 
    canvas.create_rectangle(
        0, 300,
        600, 500,
        color='silver'
    )
    
    # bottom bar 
    canvas.create_rectangle(
        0, 300,
        600, 300,
        color='gray'
    )
    
    #Sign circle
    oval = canvas.create_oval(
        150, 
        0, 
        450, 
        100,
        color ='blue'
        
    )
    
    #Spin and win text
    title_text = canvas.create_text(
        300,
        50,
        text="SPIN AND WIN!",
        font="Impact 20",
        color="gold",
        anchor="center"
)
    
    # Left slot
    bordered_rectangle(
        canvas,
        30, 100,
        210, 300,
        "black",
        "white",
        3
    )

    # Middle slot
    bordered_rectangle(
        canvas,
        210, 100,
        390, 300,
        "black",
        "white",
        3
    )

    # Right slot
    bordered_rectangle(
        canvas,
        390, 100,
        570, 300,
        "black",
        "white",
        3
    )
    
    

# =========================
# 🔘 SPIN BUTTON 
# =========================

    # butt border
    canvas.create_oval(
        215, 315,
        385, 475,
        color="black"
    )

    # Main button 
    canvas.create_oval(
        225, 325,
        375, 465,
        color="gold"
    )

    #shine highlight
    canvas.create_oval(
        255, 335,
        345, 355,
        color="light yellow"
    )

    # Button text 
    canvas.create_text(
        300,
        395,
        text="SPIN",
        font="impact 45",
        anchor="center"
    )
    
    #money box
    bordered_rectangle(
        canvas,
        420, 350,
        580, 470,
        "black",
        "white",
        3
    )
    
    #upgrades
    bordered_rectangle(
    canvas,
    10, 350,
    190, 470,
    "black",
    "light gray",
    3
    )
    
    

        
    slot1, slot2, slot3 = "circle", "triangle", "square"
    render(canvas, slot1, slot2, slot3)
    
    #updates money box
    update_money_display(canvas)
    
    while True:
        canvas.wait_for_click()

        x = canvas.get_mouse_x()
        y = canvas.get_mouse_y()

        # ignore clicks during spin
        if is_spinning:
            continue

        # trigger spin if clicked on button
        if 215 <= x <= 385 and 315 <= y <= 475:

            if money <= 0:
                set_title(canvas, "NO MONEY!", "red")
                continue

            # lock game
            is_spinning = True

            # cost of spin
            money -= 1
            update_money_display(canvas)

            if money <= 0:
                set_title(canvas, "GAME OVER", "red")
                is_spinning = False
                break

            # animation
            fake_spin(canvas)

            # result
            slot1, slot2, slot3 = spin()
            render(canvas, slot1, slot2, slot3)

            calculate_payout(canvas, slot1, slot2, slot3)

            update_money_display(canvas)
            set_title(canvas, "SPIN AND WIN!", "gold")

            # unlock game
            is_spinning = False

if __name__ == '__main__':
    main()
