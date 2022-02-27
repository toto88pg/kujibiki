import random
import time

i = 1 #くじを引いた回数
while True:
    print("1000以下の好きな数を入力してください。\n")
    try:
        love_number = int(input()) #好きな数字の入力処理
        if love_number > 1000: #1000以上の数字を入れたらやり直し
            continue
        else: #1000以下の数字を入力した場合は繰り返し終了。次の処理へ
            break
    except ValueError: #文字列、未入力でenterキーを押したら繰り返し
        print("数字を入力してください")
        continue

print(str(love_number) + "ですね。それではくじを開始します・・・")
time.sleep(3)

while True:
    number = random.randint(0,1001) #ランダムで数字を決定
    print(str(number) + " が出ました!")
    if number == love_number:
        print("あなたの選んだ番号が出ました。")
        print("この数字を引くまでに" + str(i) + "回くじを引きました!\n") #くじを引いた回数を出力
        break
    else:
        print("この番号はあなたの選んだ数字ではありません")
        print("くじを引き直します。\n")
        i += 1

print("くじを終了します。お疲れ様でした。")

time.sleep(3)