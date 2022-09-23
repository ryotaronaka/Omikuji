

for i in range(9):
  print('おみくじを引きますか？引くなら「y」を入力してください。引かない場合は「文字なし」か「n」を入力してください。')

  do_or_dont = input('>> ') 

  print(do_or_dont)

  if do_or_dont == 'y':
    import random

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

#おみくじを引く回数を決められるようにしよう！