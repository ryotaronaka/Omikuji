# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 2022
おみくじプログラム（ちょっと格好良く関数を使って書いてみます。）
@author: Ryotaro Naka
"""

# import系は先頭に記載しておく
import random

#グローバル変数（関数を越えて共有する変数）
charange_number = ''

"""
#おみくじの回数を確認する関数(数字が入力されれば、Trueが返る)
"""
def check_charange():

  #グローバル変数にアクセスするために宣言
  global charange_number

  print('おみくじを引きたい回数（整数）を入力してください。')
  charange_number = input('>> ')

  #入力された文字が数字を表す文字かどうかチェック
  if charange_number.isnumeric() == True:
    #入力された文字が整数かどうかチェック
    if isinstance(int(charange_number), int) == True:
      return True
    else:
      return False
  else:
    return False


"""
#おみくじ関数
"""
def omikuji():

  #グローバル変数にアクセスするために宣言
  global charange_number

  for i in range(int(charange_number)):
    print('おみくじを引きますか？引くなら「y」を入力してください。引かない場合は「文字なし」か「n」を入力してください。')

    do_or_dont = input('>> ') 

    print(do_or_dont)

    if do_or_dont == 'y':

      #札を準備する
      omikuji=['大凶','凶','末吉','小吉','中吉','吉','大吉','永吉']

      #ランダムに札番号を決める
      fuda = random.randint(1,8) - 1

      #fuda は文字だと怒られるので、整数に置き換える
      fuda = int(fuda)

      #おみくじ結果を表示
      #print(fuda, omikuji[fuda])
      print(omikuji[fuda])

      #大吉か永吉だったら止める！
      if fuda == 6 or fuda == 7:
        break

def main():
  #おみくじの回数を確認する(result == True or False)
  result = check_charange()

  print(charange_number)

  #おみくじ関数
  if result == True:
    omikuji()
  else:
    print('数字（整数）が入力されていないので終わります。')

if __name__ == "__main__":
  main()