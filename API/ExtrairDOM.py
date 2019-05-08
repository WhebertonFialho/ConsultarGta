from bs4 import BeautifulSoup

MEIO_TRANSPORTE = {
    1: 'Rodoviário',
    2: 'A pé',
    3: 'Aéreo',
    4: 'Ferroviário',
    5: 'Marítimo/Fluvial'
}

def extraiDados(DOM):
    dadosExtraidos = {}
    
    htmlDOM = BeautifulSoup(DOM.text, "html.parser")
    secoes = htmlDOM.findAll("fieldset")

    if secoes == []:
        return { 'status': 'Dados Invalido'} 

    # IDENTIFICACAO
    dadosIdentificacao = {}
    linhas = secoes[0].findAll('tr')
    for linha in linhas:
        colunas = linha.findAll('td')
        chave = getTextTag(colunas[0])
        valor = getValueTag(colunas[1])
        dadosIdentificacao[chave] = valor

    dadosExtraidos["Identificacao"] = dadosIdentificacao
    
    # Especie
    dadosEspecie = {}
    linhas = secoes[1].findAll('tr')
    for linha in linhas:
        colunas = linha.findAll('td')
        chave = getTextTag(colunas[0])
        valor = getValueTag(colunas[1])
        if chave != " ":
            dadosEspecie[chave] = valor
    
    dadosExtraidos["Especie"] = dadosEspecie

    # Meio de Transporte
    contMeioTransporte = 0
    dadosMeioTransporte = {}
    linhas = secoes[2].findAll('input')
    for linha in linhas:
        contMeioTransporte+=1
        dicInput = linha.attrs
        if 'checked' in dicInput:
            break

    dadosMeioTransporte["Tipo"] = MEIO_TRANSPORTE[contMeioTransporte]
    dadosExtraidos["MeioTransporte"] = dadosMeioTransporte

    # Local Emissao e Emitente
    dadosEmitente = {}
    linhas = secoes[3].findAll('tr')
    
    for linha in linhas:
        colunas = linha.findAll('td')
        chave = getTextTag(colunas[0])
        valor = getValueTag(colunas[1])
        if chave != " ":
            dadosEmitente[chave] = valor
    
    dadosExtraidos["Emitente"] = dadosEmitente

    #Validacoes e Observacoes
    dadosObservacao = {}
    linhas = secoes[4].findAll('tr')

    for linha in linhas:
        colunas = linha.findAll('td')
        chave = getTextTag(colunas[0])
        valor = getValueTag(colunas[1])
        if chave != " ":
            dadosObservacao[chave] = valor
    
    dadosExtraidos["Observacao"] = dadosObservacao

    #Origem
    dadosOrigem = {}
    linhas = secoes[5].findAll('tr')

    for linha in linhas:
        colunas = linha.findAll('td')
        chave = getTextTag(colunas[0])
        valor = getValueTag(colunas[1])
        if chave != " ":
            dadosOrigem[chave] = valor

    dadosExtraidos["Origem"] = dadosOrigem

    #Destino
    dadosDestino = {}
    linhas = secoes[6].findAll('tr')
    
    for linha in linhas:
        colunas = linha.findAll('td')
        chave = getTextTag(colunas[0])
        valor = getValueTag(colunas[1])
        if chave != " ":
            dadosDestino[chave] = valor

    dadosExtraidos["Destino"] = dadosDestino
    
    #Vacinacao
    dadosVacinacao = {}
    linhas = secoes[7].findAll('tr')

    for linha in linhas:
        colunas = linha.findAll('td')
        for col in colunas:
            inputField = col.find('input')

            if not inputField:
                continue
            
            chave = col.contents[0]['name']
            valor = col.contents[0]['value']
            if chave != " ":
                dadosVacinacao[chave] = valor

    dadosExtraidos["Vacinacao"] = dadosVacinacao

    #Extratificacao
    dadosEstratificacao = {}
    linhas = secoes[8].findAll('tr')
    contador = 0
    for linha in linhas:
        colunas = linha.findAll('td')
        for col in colunas:
            inputField = col.find('input')

            if not inputField:
                continue
            
            chave = col.contents[0]['name']
            valor = col.contents[0]['value']
            if not chave in dadosEstratificacao:
                dadosEstratificacao[chave] = valor
            else:
                dadosEstratificacao[f'{chave}{contador}'] = valor
        contador += 1

    dadosExtraidos["Extratificacao"] = dadosEstratificacao

    return dadosExtraidos

def getTextTag(tag):
    return tag.text.replace(":","")

def getValueTag(tag):
    try:
        return tag.contents[0]['value']
    except:
        return ""