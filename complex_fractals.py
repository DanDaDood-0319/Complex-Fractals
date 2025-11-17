# This file is part of Complex-Fractals.
# Copyright (C) 2025 DanDaDood-0319
# Licensed under the GNU General Public License v3.0.
# See <https://www.gnu.org/licenses/> for details.

import pygame as pg
from pygame.locals import *
import math as m
import time as t
import colorsys as csys
import mpmath as mp

# Initialize
pg.init()
mp.mp.dps = 5

# Window
s_w, s_h = 480, 360 
s = pg.display.set_mode((s_w,s_h), pg.RESIZABLE)
pg.display.set_caption("DanDaDood-0319's Mandelbrot Set Explorer") # Title
run = True

# Frame delay re-render
t_g =  0.1 # Goal FPS (will be ignored if frame finishes rendering before then)
t_f  = t.time() + t_g

c_x, c_y = mp.mpf(-0.75), mp.mpf(0) # Camera x and y
m_vx, m_vy = mp.mpf(0), mp.mpf(0) # Camera velocity for drag-off
res = 5 # How big each pixel is. Useful for efficient rendering, while not having to put your head close to see.
sqrt2, log10_2 = mp.sqrt(2), m.log10(2) # To avoid repeated calculations on a constant
zoom, zoom_r = mp.mpf(1), mp.mpf(14) # starting zoom
depth = 50

# Defining for start tick
s_wr = m.ceil(s_w/res)
scroll = 0
res_2 = res/2

def dist(x,y): #sqrt((x^2)+(y^2))
  return(mp.power(mp.fadd(mp.fmul(x,x),mp.fmul(y,y)),0.5))

# The most important part of this project
# Add to this to make your own fractals!
def mandelbrot(z_r,z_i,p_r,p_i,c_r,c_i,r):
  z_r, z_i, p_r, p_i, c_r, c_i = map(mp.mpf, (z_r, z_i, p_r, p_i, c_r, c_i))
  z_do = dist(z_r, z_i)
  for i in range(r):
    z_r, z_i = mp.fadd(mp.fsub(mp.fmul(z_r, z_r), mp.fmul(z_i, z_i)), c_r), mp.fadd(mp.fmul(2, mp.fmul(z_r, z_i)), c_i)
    if dist(z_r, z_i) >= mp.mpf(3):
      return(float(mp.fsub(mp.mpf(i + 1), mp.fdiv(mp.log10(mp.log10(dist(z_r, z_i))), log10_2))))
    elif dist(z_r, z_i) <= z_do:
      print("orbit detected!")
      return(-1)
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
    m_sx, m_sy = pg.mouse.get_rel()
    c_x = mp.fsub(c_x, mp.fdiv(mp.mpf(m_sx*fast),zoom))
    c_y = mp.fsub(c_y, mp.fdiv(mp.mpf(m_sy*fast),zoom))
    m_vx, m_vy = m_sx, m_sy
  else:
    # For extra velocity when let go.
    m_sx="a"
    c_x = mp.fsub(c_x, mp.fdiv(mp.mpf(m_vx),zoom))
    c_y = mp.fsub(c_y, mp.fdiv(mp.mpf(m_vy),zoom))
    m_vx, m_vy = m_vx*0.9, m_vy*0.9
  zoom_r += scroll * fast
  zoom = zoom + mp.fmul(mp.fsub((mp.power(sqrt2,zoom_r)),zoom), 0.5)
  scroll  =0

tick()
# Main loop
while run:
  # reset
  x, y = 0, 0
  for i in range(m.ceil(s_h / res)):
    for i_2 in range(s_wr):
      c_o = mandelbrot(0, 0, 2, 0, (((x + res_2) - s_w2) / (zoom)) + c_x, (((y + res_2) - s_h2) / zoom) + c_y, depth)
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
        if event.type == pg.KEYDOWN:
          if event.key == pg.K_h:
            c_x, c_y, zoom_r, scroll = mp.mpf(-0.75), mp.mpf(0), mp.mpf(14), mp.mpf(0)
          elif event.key == pg.K_r:
            i, i_2 = m.ceil(s_h / res)+1, s_wr+1
      x+=res
    x=0
    y+=res
    if t.time() >= t_f:
      tick()
  tick()
pg.quit()
