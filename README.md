# ****Complex Fractals****
This is ****[DanDaDood-0319](https://github.com/DanDaDood-0319)****'s **complex fractal renderer**.

## Dependencies
This requires [Python](http://python.org/) *(duh)* as well as the following libraries:
* **math** for... well, math! *(comes with a generic installation of* ***[Python](http://python.org/)****)*
* **[pygame](https://www.pygame.org/)** for rendering.
* **[colorsys](https://github.com/python/cpython/blob/3.14/Lib/colorsys.py)** for converting HSV into RGB for the coloring.
* **time** for optimizing fps-to-render by only rendering every `t_g` seconds, or after a frame. *(****also*** *comes with a generic installation of* ***[Python](http://python.org/)****)*

## How to...
### Run
1. Get [Python](http://python.org/) *(this is a Python project)*
2. Get all [dependencies](#dependencies) *(listed in the dependencies section)*
3. Run [`complex_fractals.py`](/complex_fractals.py)
4. Have fun!
### Use
Hold and drag to move, and scroll to zoom. That's it! *(for now...)*
### Mod
Everything is self-contained in the [`complex_fractals.py`](/complex_fractals.py) file. Just enter it with an editor such as [VSC](https://code.visualstudio.com/)/[VSCodium](https://vscodium.com/) *(my current editor)*, and do whatever. *(And if you somehow didn't realize, YOU NEED TO KNOW PYTHON TO MOD THIS.)*

## Photos
![](/photos/mandelbrot-0.png "Whole Mandelbrot")
![](/photos/mandelbrot-1.png "Zoomed into Mandelbrot")
![](/photos/mandelbrot-2.png "Straight Minibrot")
![](/photos/mandelbrot-3.png "Diagonal Minibrot")

## Goals
### Part 1
- [x] Render Mandelbrot
- [ ] Render Julia
- [ ] Handle more than 64-bit precision for float
- [ ] Add more formulas *(such as burning shipwreck)*
- [ ] Add color customization
### Part 2
- [ ] Figure out **TkInter**
  - [ ] Labels
  - [ ] Buttons
  - [ ] Input fields
  - [ ] Tabs
  - [ ] Colors
  - [ ] Set variables
  - [ ] Integrate with PyGame
- [ ] Make UI ***(in TkInter)*** for renderer
  - [ ] Set position and zoom
  - [ ] Change origin
  - [ ] Changeable formulas
  - [ ] User-friendly color customization
### Part 3
- [ ] Be able to reassign values
- [ ] ***Powerbrot Set*** *(secret!)*
- [ ] Finalize
- [ ] **Celebrate** *(I think I deserve it after this many list items.)*

## Personal Notes
* This is my second project with **[PyGame](https://www.pygame.org/)** and **[TkInter](https://docs.python.org/3/library/tkinter.html)**! *(TkInter not* ***just*** *implemented yet)*
  * *(also my first README.md file!)* 
* Expect it to suck, because I'm not that good at programming. This is just a fun personal project I'm working on. Also, as you have noticed, this is *very*, ***very*** informal.
* I don't expect anyone to see this, but if you do, then **hi**!

## License
**[GNU General Public License, Version 3.0](https://www.gnu.org/licenses/#GPL)**

  This is a complex fractal renderer. It renders complex fractals, such as the mandelbrot set.
    **Copyright (C) 2025  [DanDaDood-0319](https://github.com/DanDaDood-0319)**

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
