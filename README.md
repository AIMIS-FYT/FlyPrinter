# AIMIS_SIMULATOR: Simulator for the AIMIS_PRINTER

Simulator.ini:
In dieser Datei ist der 3D-Drucker konfiguriert. 

setpin.sh:
Nach dem start von Linuxcnc muss dieses Skript per Terminal aufgerufen werden.

FYTprinter.py:
Dieses Skript wird für die Simulation ausgeführt. 

Ordner hallib:
Die Hallib ist für Linuxcnc wichtig (Simulator-Mode).

Ordner obj:
Hier sind die CAD Dateien abgespeichert für die Simulation

guitobin.sh
Skript, dass FYTprinter.py nach bin kopiert

startup.sh:
Mit diesem Skript ruft Simulator.ini beim Start von Linuxcnc die FYTprinter.py Datei auf.
