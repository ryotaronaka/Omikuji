#おみくじを何回も引きたい。とりあえず10回引けるようにする

#for文はオブジェクトで回すので、数字を指定しても動きません。（←そのうち意味が分かると思いますが今はそういうもんだと思ってください。）
#for i in 9:

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
    print(omikuji[fuda])


#大吉か永吉引いたら終わりにしたいぞ！