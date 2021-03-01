# maschgraden
Setup für Maschgraden-Schaufenster

### Anweisung an Schaufenster-Scheibe
"Klopfe an die Scheibe und wecke die Maschgraden auf"

## Drehbuch
1. Sensor (Erschütterung oder Entfernung) löst aus.
2. Licht geht an
4. Maschgraden richten sich auf.
5. Maschgraden schauen sich an.
6. Maschgraden schauen zum Fenster
7. Maschgraden heben das Glas.
9. Maschgraden senken das Glas
10. Licht aus
11. Maschgraden schauen gerade aus.
13. Maschgraden senken sich.

## Hardware-Topologie
Sensor
Raspberry Pi
IN: Sensor
OUT (Variante 1):
- Licht
- M1 + M2 > Alle Bewegungen bei M1 bzw. M2 werden mechanisch gelöst
OUT (Variante 2):
- Licht
- M1 koerper_aufrichten
- M1 kopf_dreher
- M1 arm_heber
- M2 koerper_aufrichten
- M2 kopf_dreher
- M2 arm_heber



## Programmablauf
1. Auf Sensor warten
2. Wenn Sensor auslöst: Funktion zum_wohl aufrufen
3. Funktion zum_wohl
  1. funktion_läuft = true
    1. if funktion_läuft = true > nichts tun
  2.
    1. funtkion licht_an aufrufen
    2. funktion koerper_aufrichten aufrufen
    3. funktion anschauen aufrufen
    4. funktion zum_fenster_schauen aufrufen
    5. funktion glas_heben aufrufen
    6. funktion glas_senken aufrufen
    7. funktion licht_aus aufrufen
    8. funktion gerade_aus_schauen aufrufen
    9. funktion koerper_senken aufrufen
    10. 5 sekunden warten



