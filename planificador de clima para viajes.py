distance_mi= 8     # millas para recorrer
is_raining= True      # esta lloviendo
has_bike= False       # si hay bicicleta
has_car= False        # si hay auto
has_ride_share_app= False # si hay aplicacion de viajes


if distance_mi <= 1 and not is_raining and has_bike == False:
    print(True)
elif 1 < distance_mi <= 6 and is_raining==True and has_bike == False:
    print(False)
elif 1 < distance_mi <= 6 and not is_raining and has_bike == False:
    print(False)
elif 1 < distance_mi <= 6 and not is_raining and has_bike == True:
    print(True)
elif distance_mi > 6 and has_ride_share_app == True:
    print (True)
elif distance_mi > 6 and has_car ==True:
    print(True)
elif distance_mi > 6 and not has_car and not has_ride_share_app:
    print(False)
else:
    print(False)
    









