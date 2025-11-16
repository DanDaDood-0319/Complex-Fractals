import pygame as pg
import math as m
import colorsys as csys
zoom,zoom_r=1,14
pg.display.set_caption("DanDaDood-0319's Mandelbrot Set Explorer")
s_w,s_h = 480,360
s = pg.display.set_mode((s_w,s_h))
run = True

c_x, c_y = -0.8, 0
m_vx, m_vy = 0, 0
res = 5
sqrt2, log10_2 = m.sqrt(2), m.log10(2)

def dist(x,y):
  return((x*x+y*y)**0.5)

def mandelbrot(z_r,z_i,p_r,p_i,c_r,c_i,r):
  z_rn, z_in = z_r, z_i
  for i in range(r):
    z_rn,z_in=(z_rn*z_rn)-(z_in*z_in)+c_r,(2*z_rn*z_in)+c_i
    if dist(z_rn,z_in)>=3:
      return(((i+1)-(m.log10(m.log10(dist(z_rn,z_in)))/log10_2)))
  return(-1)

def ifthenelse(c,t,f):
  if(c):
    return(t)
  else:
    return(f)
  

while run:
  x,y = 0,0
  res_2 = res/2
  s_wr = m.ceil(s_w/res)
  s_w2, s_h2 = s_w/2, s_h/2
  for i in range(m.ceil(s_h/res)):
    scroll=0
    for i_2 in range(s_wr):
      c_o = mandelbrot(0,0,2,0,(((x + res_2) - s_w2)/zoom) + c_x,(((y + res_2) - s_h2) / zoom) + c_y,500)
      if c_o == -1:
        c = (0,0,0)
      else:
        c = tuple(x*255%256 for x in csys.hsv_to_rgb(c_o*0.015625,1,1))
      pg.Surface.fill(s,c,(x,y,res,res))
      for event in pg.event.get():
        if event.type == pg.QUIT:
          run = False
          pg.quit()
        elif event.type == pg.MOUSEWHEEL:
          if event.y == 1:
            scroll=1
          else:
            scroll=-1
      x+=res
    pg.draw.circle(s,(0,0,0),(s_w2,s_h2),4)
    pg.draw.circle(s,(255,255,255),(s_w2,s_h2),3)
    pg.display.update()
    if (pg.mouse.get_pressed())[0]:
      if m_sx == "a":
        pg.mouse.get_rel()
      m_sx,m_sy = pg.mouse.get_rel()
      c_x-=(m_sx/zoom)
      c_y-=(m_sy/zoom)
      m_vx,m_vy=m_sx,m_sy
    else:
      m_sx="a"
      c_x-=(m_vx/zoom)
      c_y-=(m_vy/zoom)
      m_vx,m_vy=m_vx*0.9,m_vy*0.9
    if pg.key.get_mods() == 4067:
      scroll+=scroll
    zoom_r+=scroll
    zoom+=((sqrt2**zoom_r)-zoom)*0.01
    x=0
    y+=res
pg.quit()
