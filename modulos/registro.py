def RegTm(gTm1:int,gTm2:int,fechaJuego,tm1,tm2,regFechas:list,equipos:list):
    if (gTm1 > gTm2):
        regFechas.append([fechaJuego,tm1,tm2,gTm1,gTm2,tm1,tm2])
        for item in equipos:
            if (tm1 in item):
                item[1] += 1
                item[2] += 1
                item[5] = item[5] + gTm1
                item[6] = item[6] + gTm2
                item[7] += 3
            elif (tm2 in item):
                item[1] += 1
                item[3] += 1
                item[5] = item[5] + gTm2
                item[6] = item[6] + gTm1
    elif (gTm2 > gTm1):
        regFechas.append([fechaJuego,tm1,tm2,gTm1,gTm2,tm2,tm1])
        for item in equipos:
            if (tm2 in item):
                item[1] += 1
                item[2] += 1
                item[5] = item[5] + gTm2
                item[6] = item[6] + gTm1
                item[7] += 3
            elif (tm1 in item):
                item[1] += 1
                item[3] += 1
                item[5] = item[5] + gTm1
                item[6] = item[6] + gTm2
    else:
        regFechas.append([fechaJuego,tm1,tm2,gTm1,gTm2,"N/A","N/A"])
        for item in equipos:
            if (tm1 in item):
                item[1] += 1
                item[4] +=1
                item[5] = item[5] + gTm1
                item[6] = item[6] + gTm2
                item[7] += 1
            elif (tm2 in item):
                item[1] += 1
                item[4] +=1
                item[5] = item[5] + gTm2
                item[6] = item[6] + gTm1
                item[7] += 1