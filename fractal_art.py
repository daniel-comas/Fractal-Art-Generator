from cmu_graphics import *

def onAppStart(app):
    app.color = 'beige'
    app.depth = 1
    app.setMaxShapeCount(10000)

def squares(centerX, centerY, size, color):
    outerBorder = max(1, size*0.025)
    innerSize = size*0.25
    innerBorder = max(1, innerSize*0.025)
    drawRect(centerX, centerY, size, size, fill=color, border='black', borderWidth=outerBorder, align='center')
    drawRect(centerX, centerY, size*0.25, size*0.25, fill='white', border='black', borderWidth=innerBorder, align='center')

def recursiveSquares(centerX, centerY, size, step, color):
    if step == 0:
        return
    squares(centerX, centerY, size, color)
    recursiveSquares(centerX - size/3, centerY - size/3, size/3, step-1, color) #top-left
    recursiveSquares(centerX, centerY - size/3, size/3, step-1, color) #top
    recursiveSquares(centerX + size/3, centerY - size/3, size/3, step-1, color) #top-right
    recursiveSquares(centerX - size/3, centerY, size/3, step-1, color) #left
    recursiveSquares(centerX + size/3, centerY, size/3, step-1, color) #right
    recursiveSquares(centerX - size/3, centerY + size/3, size/3, step-1, color) #bottom-left
    recursiveSquares(centerX, centerY + size/3, size/3, step-1, color) #bottom
    recursiveSquares(centerX + size/3, centerY + size/3, size/3, step-1, color) #bottom-right

def changeColor():
    drawRect(50, 320, 40, 40, fill='crimson')
    drawRect(100, 320, 40, 40, fill='darkOrange')
    drawRect(150, 320, 40, 40, fill='gold')
    drawRect(200, 320, 40, 40, fill='mediumSeaGreen')
    drawRect(250, 320, 40, 40, fill='dodgerBlue')
    drawRect(300, 320, 40, 40, fill='darkOrchid')

def onMousePress(app, mouseX, mouseY): #startingX + 30, startingY + 30
    if 50 <= mouseX <= 80 and 320 <= mouseY <= 350:
        app.color = 'crimson'
    elif 100 <= mouseX <= 130 and 320 <= mouseY <= 350:
        app.color = 'darkOrange'
    elif 150 <= mouseX <= 180 and 320 <= mouseY <= 350:
        app.color = 'gold'
    elif 200 <= mouseX <= 230 and 320 <= mouseY <= 350:
        app.color = 'mediumSeaGreen'
    elif 250 <= mouseX <= 280 and 320 <= mouseY <= 350:
        app.color = 'dodgerBlue'
    elif 300 <= mouseX <= 330 and 320 <= mouseY <= 350:
        app.color = 'darkOrchid'
    else:
        app.depth += 1

def redrawAll(app):
    drawLabel('Make the Sierpinski Carpet!', 200, 40, size=18, font='arial', bold=True, fill='black', border=None, align='center')
    drawLabel('Press the squares below to change its color', 200, 60, size=14, font='arial', bold=True, fill='black', border=None, align='center')
    recursiveSquares(200, 200, 200, app.depth, app.color)
    changeColor()

def main():
    runApp(width=400, height=400)

main()