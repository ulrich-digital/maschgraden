# Maschgraden-Schaufenster
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

## Hardware
* Raspberry Pi
* Sensor (Distanz, Erschütterung oder Helligkeit)
* 6 Motoren (Servo oder ...)

## Hardware-Topologie
### Variante 1
* IN
  * Sensor
* OUT
  * Licht
  * M1 > Alle Bewegungen bei M1 werden mechanisch gelöst
  * M2 > Alle Bewegungen bei M2 werden mechanisch gelöst

### Variante 2
* IN:
  * Sensor
* OUT:
  * Licht
  * M1 koerper_aufrichten
  * M1 kopf_dreher
  * M1 arm_heber
  * M2 koerper_aufrichten
  * M2 kopf_dreher
  * M2 arm_heber



## Programmablauf
1. Auf Sensor warten
2. Wenn Sensor auslöst: Funktion zum_wohl aufrufen

### Funktion zum_wohl
```
function zum_wohl(){
    funktion_laeuft = true;
    if (funktion_laeuft == true){
        exit();
    }else{
        licht_an();
        koerper_aufrichten(); 
        anschauen(); 
        zum_fenster_schauen(); 
        glas_heben(); 
        glas_senken(); 
        go_to_startposition();
        wait_five_sec(); 
        funktion_laeuft = false;
    }
}

function go_to_startposition(){
    licht_aus(); 
    gerade_aus_schauen(); 
    koerper_senken(); 
}

```

## Figur 1 + Figur 2 unterscheiden
* Wird es Bewegungen geben, die identisch sind?
* Oder sollen möglichst viele Parameter individuell anpassbar sein?
* Wenn viele Parameter individuell anpassbar sind, könnte dies die beiden Figuren besser/unterschiedlicher charakterisieren.


