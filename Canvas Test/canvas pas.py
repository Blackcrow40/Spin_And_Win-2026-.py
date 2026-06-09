from graphics import Canvas

def main():
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
    oval = canvas.create_oval(
        150, 
        0, 
        450, 
        100,
        color ='blue'
        
    )
    canvas.create_text(
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
    
    bordered_rectangle(
    canvas,
    10, 350,
    190, 470,
    "black",
    "light gray",
    3
)
    

   
        
    
    
    

    canvas.mainloop()
    
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
    
    
    
     
main()

if __name__ == '__main__':
    main()