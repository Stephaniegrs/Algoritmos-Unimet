# Programa de arepas
# Solicitar al usuario la cantidad de harina (Tazas)
harina_str = input ("Introduce la cantidad de harina que desea que tenga su masa de arepas: ")
harina= float(harina_str)
print("Las tazas de harina para la masa es", harina)
# Solicitar al usuario la cantidad de agua (Tazas)
agua_str= input("Introduce la cantidad de agua que desea que tenga su masa de arepas: ")
agua= float(agua_str)
print("Las tazas de agua para la masa es", agua)
# Solicitar al usuario la cantidad de aceite (cucharadas, 1 cucharada = 1/16 de taza)
aceite_str= input("Introduce la cantidad de aceite que desea que tenga su masa de arepas: ")
# Convertimos de taza a cucharada
aceite= float(aceite_str)/16
print("Las cucharas de aceite para la cocción de las arepas son", aceite)
# Solicitar al usuario la cantidad de sal (cucharadas, 1 cucharadita = 1/16/3 de taza)
sal_str= input("Introduce la cantidad de sal que desea que tenga su masa de arepas: ")
# Convertimos de taza a cucharadita
sal = float(sal_str)/16/3
print("Las cucharaditas de sal para la masa son", sal)
# La masa total es la suma de los ingredientes (bol)
bol = harina + agua + sal
print("la masa preparada es", bol)
# La masa total en el budare con el aceite
budare = bol + aceite
print("La arepa final es", budare)
input("Para salir, presiones Enter")






