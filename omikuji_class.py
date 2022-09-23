"""
Created on Fri Sep 23 2022
おみくじプログラム（ちょっと格好良く関数を使って書いてみます。）
@author: Ryotaro Naka
"""

import random

class Omikuji:
  def __init__(self):
    self.charange_number = 1 #default
  
  """
  #おみくじの回数を確認する関数(数字が入力されれば、Trueが返る)
  """
  def check_charange(self):

    print('おみくじを引きたい回数（整数）を入力してください。')
    self.charange_number = input('>> ')

    #入力された文字が数字を表す文字かどうかチェック
    if self.charange_number.isnumeric() == True:
      #入力された文字が整数かどうかチェック
      if isinstance(int(self.charange_number), int) == True:
        return True
      else:
        return False
    else:
      return False

  """
  #おみくじ関数
  """
  def omikuji(self):

    for i in range(int(self.charange_number)):
      print('おみくじを引きますか？引くなら「y」を入力してください。引かない場合は「文字なし」か「n」を入力してください。')
      do_or_dont = input('>> ') 

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

  def start(self):

    #おみくじの回数を確認する(result == True or False)
    result = self.check_charange()

    #おみくじ関数
    if result == True:
      self.omikuji()
    else:
      print('数字（整数）が入力されていないので終わります。')