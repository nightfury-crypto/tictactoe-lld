def Players(StartGame):
    ptemp = StartGame[1 : len(StartGame) - 1]
    pArry = []
    isComp = False
    ValidateSymbol = []
    validatePlayerId = []
    k = 0
    while k < len(ptemp):
        print(ptemp[k], k)
        if isComp == True:
            if ptemp[k] == "C":
                return 202
        if ptemp[k] == "C":
            isComp = True
            if k + 1 < (len(ptemp)) and ptemp[k + 1] != "C":
                pArry.append([ptemp[k], "C"])
                if "C" not in ValidateSymbol:
                    ValidateSymbol.append("C")
                k = k + 1
                continue
            elif k + 1 <(len(ptemp)) and ptemp[k + 1] == "C":
                pArry.append([ptemp[k], ptemp[k + 1]])
                k = k + 2
                continue
            elif k + 1 == (len(ptemp)):
                pArry.append([ptemp[k], "C"])
                return pArry
                
        if k + 1 == (len(ptemp)) or ptemp[k + 1] == "C":
            return 201

        pArry.append([ptemp[k], ptemp[k + 1]])
        if ptemp[k + 1] not in ValidateSymbol:
            ValidateSymbol.append(ptemp[k + 1])
        else:
            return 203
        
        # validate player Id
        if ptemp[k] not in validatePlayerId:
            validatePlayerId.append(ptemp[k])
        else:
            return 204
        k = k + 2
    return pArry
