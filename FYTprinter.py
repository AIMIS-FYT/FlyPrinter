#! /usr/bin/python2.7
#Zum Testen der FYT Kinematik
from vismach import *
import hal
import math
import sys

##
for setting in sys.argv[1:]: exec setting
##

c = hal.component("fytexp")
# table-x
c.newpin("achse-x", hal.HAL_FLOAT, hal.HAL_IN)
# head vertical slide
c.newpin("achse-z", hal.HAL_FLOAT, hal.HAL_IN)
# achse-x tilt-b
c.newpin("achse-b", hal.HAL_FLOAT, hal.HAL_IN)
c.ready()


floor = Collection([Box(-500,-500,-3,500,500,0)])
floor = Color([0.5,0.2,0,0.5],[floor]) #[Red,Green,Blue,Opacity]
work = Capture()

#tool goes here.. maybe later
tool = Box(0,0,0,1,1,1)

# "tooltip" for backplot will be the tip of the tool, for now link7
tooltip = Capture()
tool = Collection([tooltip, tool])
tool = Translate([tool],-115,-140,20)

fixpart = AsciiOBJ(filename="~/linuxcnc/configs/Simulator/obj/print_rack.obj")
fixpart = Color([0.5,0.5,0.5,0.5],[fixpart])
fixpart = Translate([fixpart], 150, 0, 375)

printhead = AsciiOBJ(filename="~/linuxcnc/configs/Simulator/obj/print-head2.obj")
printhead = Color([0.6,0.4,0.4,0.5],[printhead])
#Zuerst Translaten, damit Drehpunkt im Ursprung
#printhead = Translate([printhead],187.694,0,-116.549)
printhead = Collection([printhead,tool])
printhead = Translate([printhead],116.549,0,-187.694)
printhead = HalRotate([printhead], c, "achse-b", 1, 0,1,0)
#Nun Printhead an Printer translaten
printhead = Translate([printhead],33.451,0,562.694)

xpart = AsciiOBJ(filename="~/linuxcnc/configs/Simulator/obj/rot-achse.obj")
xpart = Color([0.6,0.5,0,0.5],[xpart])
xpart = Translate([xpart],150,0,375)
xassem = Collection([xpart,printhead])
xassem= HalTranslate([xassem], c, "achse-x", 1,0, 0)

zpart = AsciiOBJ(filename="~/linuxcnc/configs/Simulator/obj/x-achse.obj")
zpart = Color([0.6,0.2,0.9,0.5],[zpart])
zpart = Translate([zpart],150,0,375)
zassem = Collection([zpart,xassem])
zassem = HalTranslate([zassem], c, "achse-z", 0,0, 1)

myhud = Hud()
myhud.show("XZZB")


model = Collection([fixpart, zassem, work,floor])
main(model, tooltip, work, 700)
