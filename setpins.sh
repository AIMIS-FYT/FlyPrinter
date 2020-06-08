#!/bin/bash

echo "Nun werden Pins erstellt"
halcmd net  :achse-x      halui.axis.x.pos-feedback           fytexp.achse-x
halcmd net  :achse-y      halui.axis.y.pos-feedback           fytexp.achse-b
halcmd net  :achse-z      halui.axis.z.pos-feedback           fytexp.achse-z
