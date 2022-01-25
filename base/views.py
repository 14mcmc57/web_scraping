from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
import logging
logger = logging.getLogger(__name__)
from rest_framework import status
from rest_framework.views import APIView

import pytesseract
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from CommonUtil.constVarPath import csvPath,urlISRO, XPATH_ISRO, NOT_MENTIONED
from selenium.webdriver.support.ui import Select
from CommonUtil.sequentialSeqGenerator import obj
import sys
import time
from datetime import datetime
import pandas as pd




# Create your views here.
# class Schedule(viewsets.ModelViewSet):
#     def get_queryset(self):
#         try:
#             print("============")
#             return Response({'massage': 'Created successfully','status': True})
#         except Exception as e:
#             logger.error('Something Went Wrong' + str(e))
#             context = {'status': False, 'error': {'message': ['Something Went Wrong']}}
#             return Response(context, status=status.HTTP_200_OK)





class Schedule(viewsets.ModelViewSet):
        def get_queryset(self):
            try:
                url=urlISRO
                driver = webdriver.Chrome(ChromeDriverManager().install())
                #driver = webdriver.Chrome()
                # for i in range(2, 10):
                #     driver.get("https://eprocure.gov.in/cppp/latestactivetendersnew/cpppdata?page=")
                #     driver.maximize_window()
                #     time.sleep(5)
                #     # captcha
                #     driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[' + str(i) + ']/td[5]/a').click()
                #     # captcha
                #     # s = getCaptchaText(dr iver.find_element_by_xpath('//*[@id="tenderfullview-tenders"]/div/div/div[1]/div/img'))
                #     driver.find_element_by_xpath('//*[@id="tenderDetailDivTd"]/div/a').click()
                #     # captcha
                #     driver.find_element_by_xpath('//*[@id="docDownoad"]').click()
                #     # captcha
                #     driver.find_element_by_xpath('//*[@id="DirectLink_0"]').click()
                #     driver.quit()
                # driver.quit()
                driver.get(url)
                drp1=Select(driver.find_element_by_class_name('biggerComboBox'))
                drp1.select_by_value('All')
                driver.find_element_by_xpath('/html/body/form/table/tbody/tr/td[3]/table/tbody/tr/td/table[1]/tbody/tr/td/table[2]/tbody/tr/td/table[2]/tbody/tr/td[1]/input').click()
                time.sleep(5)
                tempList = []
                i=1
                #modify code with
                while i < 3:
                    #while True:
                    driver.implicitly_wait(10)
                    rows=len(driver.find_elements_by_xpath('/html/body/form/table/tbody/tr/td[3]/table/tbody/tr/td/table[2]/tbody/tr'))
                    for r in range(3,rows+1,2):
                        try:
                            Tender_Ref_NO=driver.find_element_by_xpath(XPATH_ISRO+str(r)+']/td[2]').text
                            print(Tender_Ref_NO)
                            Center_Name=driver.find_element_by_xpath(XPATH_ISRO+str(r)+']/td[3]').text
                            print(Center_Name)
                            Tender_Desc=driver.find_element_by_xpath(XPATH_ISRO+str(r)+']/td[4]').text
                            print(Tender_Desc)
                            BidSubmissionClose=driver.find_element_by_xpath(XPATH_ISRO+str(r)+']/td[5]').text
                            BidAuth=driver.find_element_by_xpath(XPATH_ISRO+str(r)+']/td[6]').text
                            BidOpen=driver.find_element_by_xpath(XPATH_ISRO+str(r)+']/td[7]').text
                            TenderType=driver.find_element_by_xpath(XPATH_ISRO+str(r)+']/td[8]').text
                            url=driver.current_url
                            print(url)
                            allTenderData = {"SMTTNo": obj.id(),
                                                    "agencyTenderID": NOT_MENTIONED,
                                                    "agencyTenderNo": Tender_Ref_NO,
                                                    "agencyName": "ISRO",
                                                    "subsidaryName": Center_Name,
                                                    "tenderTitle": Tender_Desc,
                                                    "tenderDescription": Tender_Desc,
                                                    "tenderInfoPublishDate": NOT_MENTIONED,
                                                    "tenderIssueStartDate": NOT_MENTIONED,
                                                    "tenderIssueCloseDate": NOT_MENTIONED,
                                                    "tenderSubmitCloseDate": BidSubmissionClose,
                                                    "tenderOpeningDate": BidOpen,
                                                    "tenderType": TenderType,
                                                    "tenderEstimatedBudget": NOT_MENTIONED,
                                                    "tenderURL": url,
                                                    "Keyword": NOT_MENTIONED,
                                                    "city": NOT_MENTIONED,
                                                    "state": NOT_MENTIONED,
                                                    "detailTimeStamp" : datetime.now().strftime("%d%m%Y")
                                                    }
                            # x = colName.insert_one(allTenderData)
                            tempList.append(allTenderData)
                            df=pd.DataFrame(tempList)
                            
                        except NoSuchElementException:
                            continue
                    df.to_csv('ISRO.csv')
                    print("after continue df.to_csv")
                    i=i+1
                    try:
                        driver.find_element_by_xpath('/html/body/form/table/tbody/tr/td[3]/table/tbody/tr/td/table[3]/tbody/tr/td/a['+str(i)+']').click()
                    except NoSuchElementException:
                        break
                driver.close()



                print("============")
                return Response({'massage': 'Created successfully','status': True})
            except Exception as e:
                logger.error('Something Went Wrong' + str(e))
                context = {'status': False, 'error': {'message': ['Something Went Wrong']}}
                return Response(context, status=status.HTTP_200_OK)


