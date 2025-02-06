#----------------------------------------------------------------------------
#
#          INTEGRANTES:
#
#          Carol Dayan Reyes Aguirre - 20211005121
#          Danna Celena Montenegro - 20212005153
#          Juan Esteban Sierra Cristancho - 20211005067
#
#--------------------------------------------------------------------------
import board
import neopixel
import sys
import time
import digitalio
import busio
import board
import pwmio

from adafruit_ov7670 import (  # pylint: disable=unused-import
    OV7670,
    OV7670_SIZE_DIV16,
    OV7670_COLOR_YUV,
    OV7670_TEST_PATTERN_COLOR_BAR_FADE,
)
x=0
y=0
led = pwmio.PWMOut(board.GP10, frequency=5000, duty_cycle=0)#derecha
led1 = pwmio.PWMOut(board.GP18, frequency=5000, duty_cycle=0)#izquierda
led0 = pwmio.PWMOut(board.GP16, frequency=5000, duty_cycle=0)#derecha
led2 = pwmio.PWMOut(board.GP17, frequency=5000, duty_cycle=0)#izquierda
num_pixels = 12  # Número de LEDs en la tira o módulo NeoPixel
pixel_pin = board.GP14  # Cambia esto al pin donde conectaste el NeoPixel

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.15)

# Encender el NeoPixel de color blanco
pixels.fill((255, 255, 255))


cam_bus = busio.I2C(board.GP21, board.GP20)

cam = OV7670(
    cam_bus,
    data_pins=[
        board.GP0,
        board.GP1,
        board.GP2,
        board.GP3,
        board.GP4,
        board.GP5,
        board.GP6,
        board.GP7,
    ],
    clock=board.GP8,
    vsync=board.GP13,
    href=board.GP12,
    mclk=board.GP9,
)
cam.size = OV7670_SIZE_DIV16
cam.colorspace = OV7670_COLOR_YUV
cam.flip_y = True

print(cam.width, cam.height)

buf = bytearray(2 * cam.width * cam.height)
print('##################################')
print(buf)
cam.capture(buf)
print('##################################')
print(len(buf))
print('##################################')
print(len(list(buf)))
t1=0.2
chars = b" 00000111"
velocidad=35
width = cam.width
row = bytearray(2 * width)
while True:

    cam.capture(buf)
    for j in range(cam.height):
        for i in range(cam.width):
            row[i * 2] = row[i * 2 + 1] = chars[
                buf[2 * (width * j + i)] * (len(chars) - 1) // 255
            ]
        print(row)
        for h in range (0,30):
            if (row[h])==49 and j<15:
                x=x+1 #derecha
            if (row[h])==49 and j>15:
                y=y+1 #izquierda
    
    
    if y==0 and x==0:
        led1.duty_cycle = int(65535 *((velocidad*0.85)/100))# Down
        led.duty_cycle = int(65535 *(velocidad/100))
        led0.duty_cycle = int(65535 *0)# Down
        led2.duty_cycle = int(65535 *0)
        time.sleep(t1)
        led1.duty_cycle = int(65535 *0)# Down
        led.duty_cycle = int(65535 *0)
        led0.duty_cycle = int(65535 *0)# Down
        led2.duty_cycle = int(65535 *0)
        umov="rect"
    elif y>x:
        led1.duty_cycle = int(65535 *((velocidad*0.85)/100))# Down
        led.duty_cycle = int(65535*((velocidad*0.60)/100)) #derecha
        led0.duty_cycle = int(65535 *0)# Down
        led2.duty_cycle = int(65535 *0)
        time.sleep(t1)
        led1.duty_cycle = int(65535 *0)# Down
        led.duty_cycle = int(65535 *0)
        led0.duty_cycle = int(65535 *0)# Down
        led2.duty_cycle = int(65535 *0)
        umov="dere"
    elif y<x:
        led1.duty_cycle = int(65535 *((velocidad*0.4)/100))# Down
        led.duty_cycle = int(65535*(velocidad/100)) #derecha
        led0.duty_cycle = int(65535 *0)# Down
        led2.duty_cycle = int(65535 *0)
        time.sleep(t1)
        led1.duty_cycle = int(65535 *0)# Down
        led.duty_cycle = int(65535 *0)
        led0.duty_cycle = int(65535 *0)# Down
        led2.duty_cycle = int(65535 *0)
        umov="izq"
    else:
        if umov=="rect":
            led2.duty_cycle = int(65535 *((velocidad*0.85)/100))# Down
            led0.duty_cycle = int(65535 *(velocidad/100))
            led.duty_cycle = int(65535 *0)# Down
            led1.duty_cycle = int(65535 *0)
            time.sleep(t1)
            led1.duty_cycle = int(65535 *0)# Down
            led.duty_cycle = int(65535 *0)
            led0.duty_cycle = int(65535 *0)# Down
            led2.duty_cycle = int(65535 *0)
        elif umov=="dere":
            led2.duty_cycle = int(65535 *((velocidad*0.85)/100))# Down
            led0.duty_cycle = int(65535*((velocidad*0.60)/100)) #derecha
            led.duty_cycle = int(65535 *0)# Down
            led1.duty_cycle = int(65535 *0)
            time.sleep(t1)
            led1.duty_cycle = int(65535 *0)# Down
            led.duty_cycle = int(65535 *0)
            led0.duty_cycle = int(65535 *0)# Down
            led2.duty_cycle = int(65535 *0)
            time.sleep(t1)
            led1.duty_cycle = int(65535 *((velocidad*0.4)/100))# Down
            led.duty_cycle = int(65535*(velocidad/100)) #derecha
            led0.duty_cycle = int(65535 *0)# Down
            led2.duty_cycle = int(65535 *0)
            time.sleep(t1)
            led1.duty_cycle = int(65535 *0)# Down
            led.duty_cycle = int(65535 *0)
            led0.duty_cycle = int(65535 *0)# Down
            led2.duty_cycle = int(65535 *0)
        elif umov=="izq":
            led2.duty_cycle = int(65535 *((velocidad*0.4)/100))# Down
            led0.duty_cycle = int(65535*(velocidad/100)) #derecha
            led.duty_cycle = int(65535 *0)# Down
            led1.duty_cycle = int(65535 *0)
            time.sleep(t1)
            led1.duty_cycle = int(65535 *0)# Down
            led.duty_cycle = int(65535 *0)
            led0.duty_cycle = int(65535 *0)#
            led2.duty_cycle = int(65535 *0)
            time.sleep(t1)
            led1.duty_cycle = int(65535 *((velocidad*0.85)/100))# Down
            led.duty_cycle = int(65535*((velocidad*0.60)/100)) #derecha
            led0.duty_cycle = int(65535 *0)# Down
            led2.duty_cycle = int(65535 *0)
            time.sleep(t1)
            led1.duty_cycle = int(65535 *0)# Down
            led.duty_cycle = int(65535 *0)
            led0.duty_cycle = int(65535 *0)#
            led2.duty_cycle = int(65535 *0)
        else:
            led1.duty_cycle = int(65535 *0)# Down
            led.duty_cycle = int(65535 *0)
            led0.duty_cycle = int(65535 *0)# Down
            led2.duty_cycle = int(65535 *0)
        
    umov=="no"
    x=0
    y=0
    print()
