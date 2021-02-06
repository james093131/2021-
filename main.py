#coding=utf-8  

import requests
import html
import math
import re

url  = "https://www.taiwanlottery.com.tw/news/IN1100128news_detail_650.asp#4439"
url2 = "https://www.taiwanlottery.com.tw/news/IN1100115news_detail_646.asp#4434"
url3 = "https://www.taiwanlottery.com.tw/news/IN1091231news_detail_643.asp#4428"
List = [] 
Name = [] 
Lotto_id = []
ALL_QUAN = []
Cost = []
Expective_Value =[]
P =[]
E_P =[]

def Get_Url_String(url,T):
    r1=requests.get(url)
    r1.encoding="UTF-8"
    T.append(r1.text)
def Find_ID(T):
    index = -1
    indexS = -1
    indexE = -1
    for i in range(len(T)):
        while(1):#catch the store name index
            if '遊戲期數' in T[i]:
                index = T[i].find('遊戲期數',index+1)
                indexS = T[i].find('：',index+1)
                indexE = T[i].find('<',index+1)
            
            # print(T[indexS+1:indexE])
                if index==-1:
                    break
                elif index !=-1:
                    Lotto_id.append(T[i][indexS+1:indexE])
def Find_Name(T):
    index = -1
    indexS = -1
    indexE = -1
    for i in range(len(T)):
        while(1):#catch the store name index
            if '遊戲主題' in T[i]:
                index = T[i].find('遊戲主題',index+1)
                indexS = T[i].find('：',index+1)
                indexE = T[i].find('<',index+1)
            # print(T[i][indexS+1:indexE])
            if index==-1:
               break
            elif index !=-1:
                Name.append(T[i][indexS+1:indexE])
def Find_Value(T):
    index = -1
    indexS = -1
    indexE = -1
    indexQS = -1
    indexQE = -1
    for i in range(len(T)):
        E_VALUE =0
        while(1):#catch the store name index
            if 'NT' in T[i]:
                index = T[i].find('NT',index+1)
                indexS = T[i].find('$',index+1)
                indexE = T[i].find('<',index+1)
                indexQS = T[i].find('right">',indexE+1)
                indexQE = T[i].find('<',indexQS+1)
            S =T[i][indexS+1:indexE]
            S = S.replace(',', '')
            S = S.replace('與', '')
            Quan = T[i][indexQS+7:indexQE]
            Quan = Quan.replace(',', '')
            # print(Quan)
            # print(S)
            if(index > A_index[i][0]):
                Expective_Value.append(E_VALUE)
                E_VALUE = 0
                A_index[i].pop(0) 
            elif index == -1:
                Expective_Value.append(E_VALUE)
                A_index[i].pop(0)
                break        
            elif index != -1 :
                E_VALUE = E_VALUE + int(S)*int(Quan)
def Find_All_Quantity_index(T):
    index = -1
    for i in range(len(T)):
         temp = []
         while(1):#catch the store name index
            if '發行張數' in T[i]:
                index = T[i].find('發行張數',index+1)
            # print(index)
            if index==-1:
                A_index.append(temp)
                break
            elif index !=-1:
                temp.append(index)

def Find_Cost(T):
    index = -1
    indexE = -1
    for i in range(len(T)):
        while(1):#catch the store name index
            if '每張新臺幣' in T[i]:
                index = T[i].find('每張新臺幣',index+1)
                indexE = T[i].find('元',index+1)
            if index== -1:
               break
            elif index != -1:
                S =T[i][index+5:indexE]
                S = S.replace(',', '')
                Cost.append(int(S))

def hint_Delete(T):
    index = -1
    indexE = -1
    for i in range(len(T)):
        while(1):#catch the store name index
            if '<!--tr>' in T[i]:
                index = T[i].find('<!--tr>',index+1)
                indexE = T[i].find('</tr-->',index+1)
            if index== -1:
               break
            elif index != -1:
                T[i] = T[i][0: index:] + T[i][indexE + 1::]
                index = indexE +1
def Find_All_Quantity(T):
    index = -1
    indexS = -1
    indexE = -1
    for i in range(len(T)):
         while(1):
            if '發行張數' in T[i]:
                index = T[i].find('發行張數',index+1)
                indexS = T[i].find('<strong>',index+1)
                indexE = T[i].find('<',indexS+1)
            # print(index)
            if index==-1:
                break
            elif index !=-1:
                S =T[i][indexS+8:indexE]
                S = S.replace(',', '')
                ALL_QUAN.append(int(S))
def Find_P(T):
    index = -1
    indexS = -1
    indexE = -1
    for i in range(len(T)):
         while(1):
            if '本期整體中獎率' in T[i]:
                index = T[i].find('本期整體中獎率',index+1)
                indexS = T[i].find('<strong>',index+1)
                indexE = T[i].find('<',indexS+1)
            # print(index)
            if index==-1:
                break
            elif index !=-1:
                S =T[i][indexS+8:indexE]
                P.append(S)                              
def CALCULATE_EXPECTIVE_VALUE():
    for i in range(len(Expective_Value)):
        Expective_Value[i] = int(Expective_Value[i]/ALL_QUAN[i])
        E_P.append(Expective_Value[i]/Cost[i])
def OUTPUT():
    for i in range(len(Name)):
        IND = SORT_INDEX[i]
        print ("期數 : "+Lotto_id[IND])
        print("名稱 :"+Name[IND])
        print("發行量 : "+str(ALL_QUAN[IND]))
        print("價錢 : "+str(Cost[IND]))
        print("中獎機率 : "+str(P[IND]))
        print("期望值 : "+str(Expective_Value[IND]))
        print("期望值/價錢 : "+str(E_P[IND]))
        print("-------------------------------")

def SORT(L):
    list1 = [None]*(len(Expective_Value))
    for i in range(len(list1)):
        list1[i] = i
    L, list1 = zip(*sorted(zip(L, list1), reverse=True))
    return list1

check = []
A_index = []
Get_Url_String(url,check)
Get_Url_String(url2,check)
Get_Url_String(url3,check)
# print(check[0])
hint_Delete(check)
Find_ID(check)
Find_Name(check)
Find_All_Quantity_index(check)
# print(A_index)

Find_Value(check)
Find_Cost(check)
Find_P(check)
Find_All_Quantity(check)
CALCULATE_EXPECTIVE_VALUE()
# print(Lotto_id)
# print(Name)
# print(ALL_QUAN)
# print(Cost)
# print(P)
SORT_INDEX = SORT(E_P)
OUTPUT()

