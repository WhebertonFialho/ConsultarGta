import mechanicalsoup
from API import ExtrairDOM as DOM

ERROR = { 'status': 'error'}

#cod_barra = '42103446775020820160600030246000189481001019' # codigoBarras
#num_gta = '344677' # numeroGta
#uf = 'SC' # sgUf
#serie = 'j' # serie

URL_GTA = 'http://pga.agricultura.gov.br/sispga/webclient/consultaPublica.jsp'

def consultarGtaPorNroGta(nro_gta, serie, estado):
    if not nro_gta:
        return ERROR

    if not serie:
        return ERROR

    if not estado:
        return ERROR

    browser = mechanicalsoup.StatefulBrowser()
    browser.open(URL_GTA)
    browser.select_form('form[name="consulta"]')

    browser["numeroGta"] = nro_gta
    browser["serie"] = serie
    browser["sgUf"] = estado

    htmlDom = browser.submit_selected()
    dados = DOM.extraiDados(htmlDom)
    return dados

def consultarGtaPorCodBarra(cod_barra):
    if not cod_barra:
        return ERROR

    browser = mechanicalsoup.StatefulBrowser()
    browser.open(URL_GTA)
    browser.select_form('form[name="consulta"]')

    browser["codigoBarras"] = cod_barra
    
    htmlDOM = browser.submit_selected()
    dados = DOM.extraiDados(htmlDOM)
    return dados