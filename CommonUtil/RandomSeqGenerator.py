from datetime import date
import pymongo
from pymongo import MongoClient


# Python 3 program to find lexicographically
# next string


class Sequencer:
    # Mongodb details
    key = 'mongodb+srv://User_mdb:mw1@cluster0.qfazv.mongodb.net/Tender_scrape?retryWrites=true&w=majority'
    db_name = 'Tender_scrape'
    urlcode = 'urlcode'

    # Intialization

    __letter = 'empty'  # 65=A
    __number = 1
    __today = date.today()

    def __init__(self, sim=0):
        if sim > 0:
            self.__number = sim

    def id_gen(self, urlc):
        cluster = MongoClient(self.key)
        db = cluster[self.db_name]
        url0 = db[self.urlcode]
        # url0.delete_many({})
        index = url0.count_documents({})
        urll = url0.find()
        mx = ''
        for row in urll:
            if urlc in row['urlcode']:
                # self.number=max(self.number,row[''])
                self.__letter = row['letter']
                # row['count']
                url0.update_one({'letter': row['letter']}, {'$set': {'count': row['count'] + 1}})
                self.__number = row['count'] + 1
                break
            else:
                mx = max(mx, row['letter'])

        if self.__letter == 'empty':
            if index == 0:
                self.__letter = self.nextWord(' ')
            else:
                self.__letter = self.nextWord(mx)
            url0.insert_one({'urlcode': urlc, 'letter': self.__letter, '_id': index + 1, 'count': self.__number})

    def id(self, urlc):
        self.id_gen(urlc)
        num = self.__number
        # self.__number += 1
        letr = self.__letter
        self.__letter = 'empty'
        return "SMT" + self.__today.strftime("%d%m%Y") + letr + f'{num}'

    def nextWord(self, s):
        # If string is empty.
        s = s.lower()
        if (s == " " or s == ""):
            return "A"

        # Find first character from right
        # which is not z.
        i = len(s) - 1
        while (s[i] == 'z' and i >= 0):
            i -= 1

        # If all characters are 'z', append
        # an 'a' at the end.
        if (i == -1):
            s = 'a' + s
            # print(s)
            si = len(s)
            s = ""
            for x in range(0, si):
                s = s + 'a'
        # If there are some non-z characters
        else:
            s = s.replace(s[i], chr(ord(s[i]) + 1), 1)
        s = s.upper()
        return s


obj = Sequencer()
# obj.id()
# obj.id()
# obj.id()
# for i in range(0,100):
# 	print(s)

# 	s=nextWord(s)

# print(obj.id('isro'))
# print(obj.id('eproc'))
print(obj.id('D'))
# for i in range(26):
# 	print(obj.id(chr(i+65)))
