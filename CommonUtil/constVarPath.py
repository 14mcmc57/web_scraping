
NOT_MENTIONED = "Not Mentioned"

csvPath = '../DATAFILE/'
chromeDriverPath = '../Drivers/chromedriver'
firefoxDriverPath = '../Drivers/geckodriver'



urlBRIT = 'https://britatom.gov.in/tender'
urlISRO = 'https://eprocure.isro.gov.in/viewpages/viewtenderlist.asp'
urlDPSDAE = 'https://etenders.dpsdae.gov.in/'
urlNPCIL = 'https://npcil.etenders.in/'
urlIndnRlyMain = 'https://indianrailways.gov.in/railwayboard/Tender_cpp.jsp?lang=0&id=0,3'
urlRlyOther = '.indianrailways.gov.in/Tender_cpp.jsp?lang=0&id=0,'
urlEprocureCPPP = 'https://eprocure.gov.in/cppp/latestactivetendersnew/cpppdata?page='
urlMoil = 'https://www.moil.nic.in/tender-all'
urlMSED = 'https://www.mahadiscom.in/supplier/tenders/'
urlEprocBihar = "https://www.eproc.bihar.gov.in/"
urlVECC = "https://www.vecc.gov.in/notifications/details/1"
railwaysZones = ['rwf','mtp','eastcoastrail','nr','ner','nwr','nfr','ncr','sr','ser','swr','scr','er','ecr','wr','wcr','icf','rcf','clw','rwf','dmw','rwp','core','rdso','mrvc']
urlUprvunl = [
    'http://online.uprvunl.org/uprvunltender/HeadOffice.aspx',
    'http://online.uprvunl.org/uprvunltender/Anpara.aspx',
    'http://online.uprvunl.org/uprvunltender/Obra.aspx',
    'http://online.uprvunl.org/uprvunltender/panki.aspx',
    'http://online.uprvunl.org/uprvunltender/parichha.aspx',
    'http://online.uprvunl.org/uprvunltender/harduaganj.aspx'
]

urlAPProc = 'https://tender.apeprocurement.gov.in'

urlDcsem = "http://dcsem.gov.in/english/tenders"

urlHwb = "https://www.hwb.gov.in/tenders"

urlHc = "https://hindustancopper.com/Page/TenderList"

urlIgcar = "http://www.igcar.gov.in/tenders/"

urlBarc = "http://www.barc.gov.in/tenders/"

urlSail = "https://sailtenders.co.in/"

urlNalco = "http://livetenders.nalcoindia.com/Website/webSearch.aspx?Glnk=search"

urlMoil = "https://www.moil.nic.in/tender-all"

#Xpaths
NPCIL_XPATH = '//*[@id="container"]/div[5]/div[1]/div[2]/table/tbody/tr'
XPATH_DCSEM = "//table//tbody//tr["
XPATH_ISRO='/html/body/form/table/tbody/tr/td[3]/table/tbody/tr/td/table[2]/tbody/tr['
XPATH_BEM_INDIA = "//table[contains(@class,'table-one')]/tbody/tr["



XPATH_RAILWAYS_TEXTBOX = '//*[@id="TenderSearch"]/table/tbody/tr/td/table/tbody/tr/td[2]/input'
XPATH_RAILWAYS = '//*[@id="table17"]/tbody/tr[2]/td/div[2]/table[1]/tbody/tr['
XPATH_GAIL = '/html/body/table/tbody/tr/td/table[2]/tbody/tr/td/table/tbody/tr'



#urlNalco='http://livetenders.nalcoindia.com/Website/webSearch.aspx?Glnk=search'
urlAmdGovIn = "https://www.amd.gov.in/app16/tenders.aspx?link=23&reg=23"

urlDdpmod = "https://www.ddpmod.gov.in/tenders-of-ddp"

urlDesw = "http://www.desw.gov.in/tenders"

urlGail = "https://gailtenders.in/Gailtenders/Home.asp"

urlUcilNit = "http://www.ucil.gov.in/nit57.html"

urlUcilOte = "http://www.ucil.gov.in/ltenq181.html"

urlInfUpGov = "http://information.up.gov.in/en/tender?field_district_target_id=All&field_department_name_value=&field_document_date_value=&field_document_date_value_1=&page="

UrlIrepsGov = "https://www.ireps.gov.in/epsn/anonymSearch.do?advancedSearch=showPageClosed&searchParam=showPageLive" \
        "&searchOption=1&searchOptorOption=0&railwayZone=-1&dateFrom=2/04/2021&dateTo=22/04/2021&linkVal=department" \
        "&selectDate=TENDER_OPENING_DATE&count=9565&pageNo="

urlBem = "https://www.bemlindia.in/viewtender.aspx"