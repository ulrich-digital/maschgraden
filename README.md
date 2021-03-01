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
1.1 Wenn Sensor auslöst: Funktion zum_wohl aufrufen

2. Funktion zum_wohl
2.1. funktion_läuft = true
2.2. if funktion_läuft = true > nichts tun
2.3. else 
2.3.1. funtkion licht_an aufrufen
2.3.2. funktion koerper_aufrichten aufrufen
2.3.3. funktion anschauen aufrufen
2.3.4. funktion zum_fenster_schauen aufrufen
2.3.5. funktion glas_heben aufrufen
2.3.6. funktion glas_senken aufrufen
2.3.7. funktion licht_aus aufrufen
2.3.8. funktion gerade_aus_schauen aufrufen
2.3.9. funktion koerper_senken aufrufen
2.3.9. 5 sekunden warten



