import csv
phone_book ={

    "mohammed" : 8105,
    "ibrahim" :3931,
    "faiz" :80560
}

phone_book_1 = {
    "rayyan" : 262018,
    "noufal" : 162016,
     "ibrahim" :3931
}
##Append values
phone_book['Faiz'] = 98993

##Append Duplicates
phone_book['Faiz'] = 98993
phone_book["faiz"] = 80560
phone_book["faiz"] = 80562

## merge Two Dict
myDict = {**phone_book,**phone_book_1}

#/*
   #Dict dont accepts Duplicates
   #Dict is mutable ,values can be changed
##*/
stock_prices=[]
with open('D:\FAYAZ\DataScience\GL\Dataset\stock_price.csv','r') as f:
    for i in f:
        token=i.split(',')
        day = token[0]
        price=float(token[1])
        stock_prices.append([day,price])

### Nested Maps
user_info = {
             1: {'name': 'Jason', 'age': '17', 'gender': 'Male'},
             2: {'name': 'Jessica', 'age': '30', 'gender': 'Female'}}

if __name__ == '__main__':
   print(phone_book.get("faiz"))
   print(phone_book , "Not Sorted")
   print(type(phone_book))
   print('\n', stock_prices)
   print('\n' "Only KeyValues", phone_book.keys())
   print ('\n' "Only Values", phone_book.values())
   print('\n'  " items :--" , phone_book.items())
   print('\n' "Length Of Variable ",len(phone_book))
   print('\n',myDict)
   print(user_info[1]['gender'])
   print(sorted(myDict.items()) , " Sorting-1") ## notworked
   for i in sorted(phone_book_1):
       print(i,phone_book_1[i],end= " ") ## Still not sorted

