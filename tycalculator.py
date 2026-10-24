import gooeypie as gp

#defining a keyboard input function to add the value of the button pressed to the expression string
def key(value):
    global expr
    expr += str(value)
    display.text = expr

#defining "=" to evaluate the expression string and display the result
def equal():
    global expr
    try:
        result = str(eval(expr))
        expr = result
        display.text = expr
    except:
        display.text = "error"
        expr = ""

#cleaing all values
def clear():
    global expr
    expr = ""
    display.text = expr

#removing the last character
def backspace():
    global expr
    expr = expr[:-1]
    display.text = expr

#dividing by 100 to get a percentage value
def percent():
    global expr
    try:
        result = str(eval(expr) / 100)
        expr = result
        display.text = expr
    except:
        display.text = "error"
        expr = ""

#turning a number into a negative value or back to positive (multiplying it by -1 :\)
def negate():
    global expr
    try:
        result = str(eval(expr) * -1)
        expr = result
        display.text = expr
    except:
        display.text = "error"
        expr = ""

def operator(symbol):
    global expr
    expr += f" {symbol} "
    display.text = expr

expr = " " #Global expression string

#app setup (window size, title, etc.))
app = gp.GooeyPieApp("TyCalc")
app.width = 300
app.height = 400


#position for display screen (for expressions)
display = gp.Label(expr)
display.style.font_size = 32
display.style.corner_radius = 5
display.style.padding_x = 20
display.style.padding_y = 10
display.style.font_name = "Pixeboy"

#display screen color and allignment
display.style.bg_color = "black"
display.style.align = "right"

#display screen location and size
display.row = 1
display.width = 260
display.height = 60

#background color
background = gp.Frame()
background.style.bg_color = "#343333"  # Sky blue color
background.add(display, 1, 1, column_span=4, align_vertical="top")
background.set_row_weights(0)
background.width = 300
background.height = 400

#button layout and actions
rows = [
    [("<", backspace), ("c", clear), ("%", percent), ("÷", lambda: operator("/"))],
    [("7", lambda: key(7)), ("8", lambda: key(8)), ("9", lambda: key(9)), ("×", lambda: operator("*"))],
    [("4", lambda: key(4)), ("5", lambda: key(5)), ("6", lambda: key(6)), ("−", lambda: operator("-"))],
    [("1", lambda: key(1)), ("2", lambda: key(2)), ("3", lambda: key(3)), ("+", lambda: operator("+"))],
    [("±", negate), ("0", lambda: key(0)), (".", lambda: key(".")), ("=", equal)]
]

#calculator grid layout
for row_number, row in enumerate(rows, start=2):
    for column, (label, action) in enumerate(row, start=1):
        if action is None:
            continue

        button = gp.Button(label, lambda event, fn=action: fn())
        button.width = 45
        button.height = 42
        button.style.corner_radius = 5
        button.style.font_size = 25
        button.style.button_color = "#555454"  # Light gray color
        button.style.font_name = "Pixeboy"
        button.style.font_weight = "bold"
        if label in ["÷", "×", "−", "+",]:
            button.style.button_color = "#536878"
        if label in ["<", "c", "%"]:
            button.style.button_color = "#7D7D7D"
        if label == "=":
            button.style.button_color = "#65808D"
        background.add(button, column, row_number)

# Add the button and label to the app
app.add(background, 1, 1, margin=0,
        expand_horizontal=True, expand_vertical=True,
        align_vertical="top")

app.set_column_weights(1)
app.set_row_weights(1)
app.run()