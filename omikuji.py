"""
Created on Fri Sep 23 2022
おみくじプログラム（ちょっと格好良く関数を使って書いてみます。）
@author: Ryotaro Naka
"""

#おみくじクラスの呼び出し
import omikuji_class

def main():
  #インスタンスの生成
  omkj = omikuji_class.Omikuji()
  omkj.start()
  
if __name__ == "__main__":
  main()