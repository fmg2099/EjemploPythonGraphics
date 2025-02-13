from cmu_graphics import *
import time 

# Set the window size
app.width = 1024
app.height = 768
app.background = 'black'

app.stepsPerSecond = 60
#en cmu-graphics los labels son objetos, no se deben llamar en onStep
label = Label('cmu-graphics', app.width/2, app.height/2, font='monospace', size=24, bold=True, fill='white')

label_fps = Label(f'FPS: 999', 60,30, size=16, fill='green')
velX = 200
velY = 100
prev_time = time.time()

#colores del logo
label_colors=['lightSalmon','lightYellow','paleGreen','lightCyan','lavender','pink','cornSilk']
lbl_color_idx=0
def getnewcolor():
    global lbl_color_idx
    lbl_color_idx += 1
    lbl_color_idx = lbl_color_idx % len(label_colors)
    return label_colors[lbl_color_idx]

#para que se vea "suave" el movimiento de numeros, hacemos un promedio de 10 valores 
fps_values = [0 for i in range(10)]
for i in range(len(fps_values)):
    fps_values[i]=i
print(fps_values)

print(fps_values)
def calcFPS(delta):
    global fps_values
    max=len(fps_values)-1
    for i in range(max):
        fps_values[i]=fps_values[i+1]
    fps_values[max]=delta

    return len(fps_values)/sum(fps_values)

def onStep():
    global prev_time, velX, velY
    delta_time = time.time() - prev_time
    label.centerX = label.centerX + velX * delta_time
    label.centerY = label.centerY + velY * delta_time
    if(label.centerX + label.width/2 > app.width or label.centerX - label.width/2 <=0 ):
        velX = -velX
        label.fill=getnewcolor()
    if(label.centerY + label.height/2 > app.height or label.centerY - label.height/2 <= 0):
        velY = -velY
        label.fill=getnewcolor()

    #dibujar los FPS
    label_fps.value=f'FPS: {calcFPS(delta_time):.1f}'
    prev_time = time.time()

cmu_graphics.run()