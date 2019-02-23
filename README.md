# gokulang

日本語文章をアニメ版ドラゴンボールの孫悟空風に変換すっぞ。

To translate Japanese sentences into Son Goku accent.

## Reuirements

- Janome 0.3.7
- pykakasi 0.94
- semidbm 0.5.1
- six 1.12.0

## Install

(venv) $ pip install gokulang

## Usage

```
from gokulang.gokulang import GokuLang

g = GokuLang()
t = g.translate('FF外から失礼します')
print(t)
```

```
FFげぇからしつれぇすっぞ
```

## Detail

[悟空語ジェネレーターをぺぇそんでも作ってみたぞ！えーぴーえぇ化もしたぞ！ - Qiita](https://qiita.com/shonansurvivors/items/ce6c1c6f5b43fc16719b)

## Web API

[https://gokulang.herokuapp.com/](https://gokulang.herokuapp.com/)

## Reference

このモジュールはきんみさん([@_kinmi](https://twitter.com/_kinmi))の作成された悟空語ジェネレーターを参考に作成しました。

[フロント明るくないおじさんがWebアプリ作った話【悟空語ジェネレーター】 - Qiita](https://qiita.com/kinmi/items/c66aa98718acad84621b)