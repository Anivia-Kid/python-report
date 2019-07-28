import cgi
import cgitb
import csv
import sys,io

sys.stdout=io.TextIOWrapper(sys.stdout.buffer, encoding='shift-jis')

cgitb.enable()
form=cgi.FieldStorage()

total=[]
list1=[]
sports=form.getvalue('sports','')
sexes=form.getvalue('sexes','')
hour=form.getvalue('hour','0')
minute=form.getvalue('minute','0')

with open(r"C:\Users\admin\Desktop\python2\18k1117-final-2\cgi-bin\L16\calorie.csv","r",encoding="shift-jis",errors='ignore') as f:
    csvlist = csv.reader(f)
    total=[x for x in csvlist]
    f.close
print(total)

list1=[x for x in total if x[1]==sexes and x[2]==sports]

template="""
<html>
    <head>
        <meta charset="shift-jis">
        <title>カロリー結果</title>
    </head>
    <body>
        <p>{result}</p>
    </body>
</html>

"""
result=template.format(result=list1[0][0])
print("Content-type:text/html\n")
print(result)
