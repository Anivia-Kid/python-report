import cgi
import cgitb
import csv
import sys,io

sys.stdut=io.TextIOWrapper(sys.stdout.buffer, encoding='shift-jis')

cgitb.enable()
form=cgi.FieldStorage()




template="""
<html>
    <head>
        <meta charset="shift-jis">
        <title>カロリー計算</title>
    </head>
    <body>
        <form method="POST" action="/cgi-bin/L16/calorie_result.py">
        <p>スポーツ:<select name="sports"></p>
            <option value="水泳平泳ぎ">水泳平泳ぎ</option>
            <option value="水泳クロール">水泳クロール</option>
            <option value="ランニング">ランニング</option>
            <option value="ジョギング">ジョギング</option>
            <option value="野球">野球</option>
            <option value="サッカー">サッカー</option>
            <option value="テニス">テニス</option>
            <option value="バドミントン">バドミントン</option>
            <option value="バスケットボール">バスケットボール</option>
            <option value="バレーボール">バレーボール</option>
            <option value="ラグビー">ラグビー</option>
            <option value="ウォーキング">ウォーキング</option>
            </select>
        <p>性別:<select name="sexes"></p>
            <option value="男性">男性</option>
            <option value="女性">女性</option>
            </select>
        <p><input type="text" name="hour">時間,<input type="text" name="minute">分</p>
        <input type="submit">
    </body>
</html>
"""
result=template.format()
print("Content-type:text/html\n")
print(result)
