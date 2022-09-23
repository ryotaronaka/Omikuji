# Omikuji
Omikuji Scripts for Python

## Explain for Scripts
#### 基本要素の動作確認(Jupyter Lab)
- omikuji_1.ipynb : リスト（配列）の作り方、乱数の使い方
- omikuji_2.ipynb : シンプルな、おみくじスクリプト（おみくじを1回引いて終わり）
#### 独立したコードとして完成させていくScripts
WindowsならコマンドプロンプトやPowershellからコマンドで起動させます。<br>
例）
```
PS C:\Users\XXX> py omikuji_3.py
```

- omikuji_3.py : omikuji_2.ipynb をベースにして".py"ファイルに変更。コマンドラインからのパラメータ入力と条件分岐（if文）が加わっています。
- omikuji_4.py : 大吉が出るまで何度も引きたいので、とりあえず10回引けるようにする。繰り返しの構文、forが登場。
- omikuji_5.py : 大吉が出たら終わりにする。
- omikuji_6.py : おみくじを引く回数も指定出来るようにする。入力される文字のエラーチェックが追加。本質的な動作を表していないが、スクリプトが正しく動くために必要な部分。
#### より洗練されたプログラミングの形
- omikuji_7.py : 関数を使って、入力文字エラーチェック機能とおみくじ機能を分離して記載。リーダブル・コードの考え方へ近づきつつあります。
- omikuji.py + omikuji_class.py : クラスを使っておみくじスクリプトをオブジェクト化して関数を呼び出しやすくしつつ、コードの再利用性を上げています。クラスを呼び出しているomikuji.pyのシンプルな書き方にも着目ください。

```
#おみくじクラスの呼び出し
import omikuji_class

def main():
  #インスタンスの生成
  omkj = omikuji_class.Omikuji()
  omkj.start()
  
if __name__ == "__main__":
  main()
```
