#DANNY QUINTANA ESPEJO
#EJ:3
horas = int(input("escriba las horas: "))
minutos = int(input("escriba las minutos: "))
segundos = int(input("escriba las segundos: "))

segundos += horas * 60 * 60
segundos += minutos * 60

print ("la cantidad de segundos es igual: {}",format(segundos))