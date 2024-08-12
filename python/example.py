import turtle

def draw_grid(t, rows, cols, cell_size=50):
    t.speed(0)  # Speed up the drawing
    t.penup()
    
    # Starting position
    start_x = -cols * cell_size // 2
    start_y = rows * cell_size // 2
    
    for row in range(rows):
        for col in range(cols):
            t.goto(start_x + col * cell_size, start_y - row * cell_size)
            t.pendown()
            for _ in range(4):
                t.forward(cell_size)
                t.right(90)
            t.penup()

# Initialize the turtle screen
wn = turtle.Screen()
wn.setup(400, 400)  # Adjusted the window size to better fit the grid

# Create a turtle
t = turtle.Turtle()

# Draw a 5x5 grid
draw_grid(t, 5, 5)

# Keep the window open
wn.mainloop()
