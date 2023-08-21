def Players(StartGame):
    ptemp = StartGame[1 : len(StartGame) - 1]
    pArry = []
    isComp = False
    ValidateSymbol = []
    validatePlayerId = []
    symbols = "XO#$%&@+-<=>?^~KASDEFGHIJKLMNOPQRSTUVZYW"
    symbolToAssign = 0
    k = 0
    while k < len(ptemp):
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
                ValidateSymbol.append("C")
                k = k + 2
                continue
            elif k + 1 == (len(ptemp)):
                pArry.append([ptemp[k], "C"])
                ValidateSymbol.append("C")
                return pArry
                
        if len(ptemp[k]) == 1:
            return 205
        

        if (k+1 != len(ptemp) and len(ptemp[k + 1]) == 1 and ptemp[k + 1] != "C"):
            pArry.append([ptemp[k], ptemp[k + 1]])

        else:
            while True:
                if symbols[symbolToAssign] not in ValidateSymbol or symbols[symbolToAssign] not in ptemp:
                    pArry.append([ptemp[k], symbols[symbolToAssign]])
                    print(pArry)
                    symbolToAssign = symbolToAssign + 1
                    break
                symbolToAssign = symbolToAssign + 1
            
                    # validate player Symbol
            if symbols[symbolToAssign] not in ValidateSymbol:
                ValidateSymbol.append(symbols[symbolToAssign])
            else:
                return 203
            
            # validate player Id
            if ptemp[k] not in validatePlayerId:
                validatePlayerId.append(ptemp[k])
            else:
                return 204
            k = k + 1
            continue

        # validate player Symbol
        if ptemp[k + 1] not in ValidateSymbol:
            ValidateSymbol.append(ptemp[k + 1])
        else:
            return 203
        
        ValidatePlayerId(ptemp[k], validatePlayerId)
        k = k + 2
    return pArry


def ValidatePlayerId(pId, validatePlayerId,):
    if pId not in validatePlayerId:
        validatePlayerId.append(pId)
    else:
        return 204