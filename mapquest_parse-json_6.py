import urllib.parse  
import requests  

main_api_benjamincornejo = "https://www.mapquestapi.com/directions/v2/route?" 
key_benjamincornejo  = "NBRA305IVkuxUEwkz8zoXjBN6SeNyqPr" 

while True:
    orig_benjamincornejo  = input ("Indique la ubicacion: ") 
    if orig_benjamincornejo == "quit" or orig_benjamincornejo == "q" or orig_benjamincornejo == "salir" or orig_benjamincornejo == "ok" or orig_benjamincornejo == "OK":
        break
    dest_benjamincornejo  = input("Ingrese eldestino: ")
    if dest_benjamincornejo == "quit" or dest_benjamincornejo == "q" or dest_benjamincornejo == "salir" or dest_benjamincornejo == "ok" or dest_benjamincornejo == "OK":
        break
    url = main_api_benjamincornejo  + urllib.parse.urlencode ({"key" :key_benjamincornejo , "from" :orig_benjamincornejo , "to" :dest_benjamincornejo})  
    json_data = requests.get (url) .json ()  
    print("URL: " + (url)) 
    json_data = requests.get(url).json() 
    json_status = json_data["info"]["statuscode"] 
    if json_status == 0: 
        print("API Status: " + str(json_status) + " = A successful route call.\n")
#seleccion de tipo de auto
        while True:
            print("Seleccione el tipo de auto:")
            print("1) City Car")
            print("2) Sedan")
            print("3) SUV")
            vehiculo = input("Ingrese el número correspondiente al tipo de vehículo: ")
    
            if vehiculo == "1":  
                rendimiento= 20
                break
            elif vehiculo == "2":
                rendimiento = 15
                break   
            elif vehiculo == "3":
                rendimiento = 12
                break
            else:
                print("Opción inválida, seleccione nuevamente.")
#seleccion de tipo de bencina 
        while True:
            print("seleccione el tipo de bencina:")
            print("93")
            print("95")
            print("97")
            bencina = input("ingrese el numero de bencina que utiliza: ")
            if bencina == "93":
                costo = 1208
                break
            elif bencina == "95":
                costo = 1252
                break
            elif bencina == "97":
                costo = 1296
                break
            else :
                print("opcion incorrecta, seleccione nuevamente.")
            
        print("===================================================")
        print("Direccion de " + (orig_benjamincornejo)+ " hasta " + (dest_benjamincornejo))
        print("tiempo de viaje: " + (json_data["route"]["formattedTime"]))
 #conversion de millas a kilometros
        millas = json_data["route"]["distance"]
        kilometros = millas * 1.60934
        print("kilometros:" + str(kilometros) + " Km.")
#consumo combustible
        consumo = kilometros / rendimiento
        print(f"El consumo de combustible es: " + str(round(consumo, 2)) + " litros.")
        costo_bencina = consumo * costo 
        print("El costo total de bencina es: " + str(round(costo_bencina)) + "pesos")
        
        print("===================================================")
        
        for each in json_data["route"]["legs"][0]["maneuvers"]:
            print((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)"))

        print("===================================================")
