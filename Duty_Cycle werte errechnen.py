import math

DC_FW_MAX = 7.0     #Maximaler Duty_Cycle-Wert fuer's Vorwaertsfahren
DC_FW_MIN = 5.1     #Minimaler Duty_Cycle-Wert fuer's Vorwaertsfahren
DC_STOP   = 5.0     #Duty_Cycle-Wert, wo der Buggy sich weder vorwaerts noch rueckwaerts bewegt (still steht)
DC_BW_MIN = 4.9     #Minimaler Duty_Cycle-Wert fuer's Rueckwaertsfahren
DC_BW_MAX = 3.0     #Maximaler Duty_Cycle-Wert fuer's Rueckwaertsfahren


#@desc: rechnet Werte zwischen -1 bis 1 zu den oben deklarierten Duty_Cycle-werten um. 
#@param value: integer zwischen -1 und 1
#@return: berechneter Duty_Cycle-Wert
def getDC(value):
    value = float(value)
    if (value > 0 and value <= 1):
        return remap(value, 0, 1, DC_FW_MIN, DC_FW_MAX)
    elif (value < 0 and value >= -1):
        return remap(math.fabs(value), 1, 0, DC_BW_MAX, DC_BW_MIN)
    elif (value == 0):
        return DC_STOP
    else:
        raise ValueError("value muss zwischen -1 und 1 liegen")

#aequivalent zu der "map"-Funktion aus "Processing"
def remap(value, leftMin, leftMax, rightMin, rightMax):
    return rightMin + ((float(value - leftMin) / float(leftMax - leftMin)) * (rightMax - rightMin))

print(getDC(input("Wert zwischen -1 und 1: ")))
