import random

print('おみくじを引きたい回数を入力してください。')

charange_number = input('>> ')

#入力された文字が数字を表す文字かどうかチェック
if charange_number.isnumeric() == True:
  #入力された文字が整数かどうかチェック
  if isinstance(int(charange_number), int) == True:

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

        if fuda == 6 or fuda == 7:
          break