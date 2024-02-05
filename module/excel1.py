import pandas

df = pandas.DataFrame({'A':['a','b','c','d','e','f','g','h'] , 'B':[10,20,30,40,50,60,70,80]})

excel = pandas.ExcelWriter('demo.xlsx',engine='xlsxwriter')

df.to_excel(excel,"sheet1",index=False,header=False)
excel.close()