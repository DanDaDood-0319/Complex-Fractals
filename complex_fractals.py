import pygame as pg
from pygame.locals import *
import math as m
import time as t
import colorsys as csys

pg.init()

#Window
s_w, s_h = 480, 360 
s = pg.display.set_mode((s_w,s_h), pg.RESIZABLE)
pg.display.set_caption("DanDaDood-0319's Mandelbrot Set Explorer") # Title
run = True

# Frame delay re-render
t_g =  0.1 # Goal FPS (will be ignored if frame finishes rendering before then)
t_f  = t.time() + t_g

c_x, c_y = -0.8, 0 # Camera x and y
m_vx, m_vy = 0, 0 # Camera velocity for drag-off
res = 1 # How big each pixel is. Useful for efficient rendering, while not having to put your head close to see.
sqrt2, log10_2 = m.sqrt(2), m.log10(2) # To avoid repeated calculations on a constant
zoom, zoom_r = 1, 14 # starting zoom

# Defining for start tick
s_wr = m.ceil(s_w/res)
scroll = 0
res_2 = res/2

def dist(x,y): #sqrt((x^2)+(y^2))
  return((x*x+y*y)**0.5)

# The most important part of this project
# Add to this to make your own fractals!
def mandelbrot(z_r,z_i,p_r,p_i,c_r,c_i,r):
  z_rn, z_in = z_r, z_i
  for i in range(r):
    z_rn,z_in=(z_rn*z_rn)-(z_in*z_in)+c_r,(2*z_rn*z_in)+c_i
    if dist(z_rn,z_in)>=3:
      return(((i+1)-(m.log10(m.log10(dist(z_rn,z_in)))/log10_2)))
  return(-1)

# A if-then statement condensed into a function
def ifthenelse(c,t,f):
  if(c):
    return(t)
  else:
    return(f)
  
# What happens in each render/tick
# Condensed into a function to avoid repetition
def tick():
  global c_x, c_y, m_vx, m_vy, m_sx, m_sy, scroll, zoom, zoom_r, t_f, t_g, sqrt2, s_w, s_h, s_wr, s_w2, s_h2 # Add extra variables here
  res_2 = res/2
  s_wr = m.ceil(s_w/res)
  s_w2, s_h2 = s_w/2, s_h/2
  s_w, s_h = pg.display.get_surface().get_size()
  t_f = t.time() + t_g
  # Crosshair for zoom
  pg.draw.circle(s,(0,0,0),(s_w2,s_h2),4)
  pg.draw.circle(s,(255,255,255),(s_w2,s_h2),3)

  # Display update
  pg.display.update()
  if pg.key.get_mods() == 4097:
    fast = 2
  elif pg.key.get_mods() == 4160:
    fast = 0.25
  else:
    fast = 1

  # Drag
  if (pg.mouse.get_pressed())[0]:
    if m_sx == "a":
      # Drag reset. pg.mouse.get_rel() gets the velocity since last call, calling it before will output (0,0).
      pg.mouse.get_rel()
    m_sx,m_sy = pg.mouse.get_rel()
    c_x-=(m_sx/zoom) * fast
    c_y-=(m_sy/zoom) * fast
    m_vx,m_vy=m_sx,m_sy
  else:
    # For extra velocity when let go.
    m_sx="a"
    c_x-=(m_vx/zoom)
    c_y-=(m_vy/zoom)
    m_vx,m_vy=m_vx*0.9,m_vy*0.9
  
  zoom_r+=scroll*fast
  zoom+=((sqrt2**zoom_r)-zoom)*0.5
  scroll=0

tick()
# Main loop
while run:
  # reset
  x, y = 0, 0
  for i in range(m.ceil(s_h/res)):
    for i_2 in range(s_wr):
      c_o = mandelbrot(0,0,2,0,(((x + res_2) - s_w2)/(zoom)) + c_x,(((y + res_2) - s_h2) / zoom) + c_y,500)
      if c_o == -1:
        c = (0,0,0)
      else:
        c = tuple(x*255%256 for x in csys.hsv_to_rgb(c_o*0.015625,1,1))
      pg.Surface.fill(s,c,(x,y,res,res))
      for event in pg.event.get():
        if event.type == pg.QUIT: # quit
          run = False
          pg.quit()
        elif event.type == pg.MOUSEWHEEL:
          if event.y == 1:
            scroll = 1
          else:
            scroll = -1
      x+=res
    x=0
    y+=res
    if t.time() >= t_f:
      tick()
  tick()
pg.quit()
