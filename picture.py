"""
picture.py
Author: <Suhan Gui>
Credit: <http://www.color-hex.com/>

Assignment: Picture

Use the ggame library to "paint" a graphical picture of something (e.g. a house, a face or landscape).

Use at least:
1. Three different Color objects.
2. Ten different Sprite objects.
3. One (or more) RectangleAsset objects.
4. One (or more) CircleAsset objects.
5. One (or more) EllipseAsset objects.
6. One (or more) PolygonAsset objects.

See:
https://github.com/HHS-IntroProgramming/Standards-and-Syllabus/wiki/TUTORIAL:-Displaying-Graphics
for general information on how to use ggame.

See:
http://brythonserver.github.io/ggame/
for detailed information on ggame.

"""
from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset

# add your code here \/  \/  \/
red = Color(0xff0000, 1.0)
green = Color(0x0ff000, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)
white= Color(0xfffffff, 1.0)
gold= Color(0xffd700, 1.0)
skin= Color(0xffeead, 1.0)
blue= Color(0x63ace5, 1.0)
pale= Color(0xa2a2a2, 1.0)

thinline = LineStyle(2, black)

face= CircleAsset(200, thinline, skin)
Pupil= EllipseAsset(5,75,thinline,black)
Mouth= EllipseAsset(75,20,thinline,red)
ring1= CircleAsset(30, thinline, white)
ring2= CircleAsset(40, thinline, gold)
face2= CircleAsset(100, thinline, pale)
Geyes= CircleAsset(35, thinline, blue)
Gmouth= EllipseAsset(100,30,thinline, red)
Nose= PolygonAsset([(0,0),(50,50), (100,50)], thinline, pale)
Ground= RectangleAsset(1000,5,thinline, green)

""" Frodo"""
Sprite(face, (300,250))
Sprite(Pupil, (450,200))
Sprite(Pupil, (350,200))
Sprite(Mouth, (350,400))

"""ring"""
Sprite(ring2, (650,100))
Sprite(ring1, (650,100))

"""gollum"""
Sprite(face2, (850,850))
Sprite(Geyes, (750, 700))
Sprite(Geyes, (850, 700))
Sprite(Gmouth, (800, 900))
Sprite(Nose, (750, 600))

Sprite(Ground,(0,1000))
# add your code here /\  /\  /\


myapp = App()
myapp.run()

