# gokulang

日本語文章をアニメ版ドラゴンボールの孫悟空風に変換すっぞ。

To translate Japanese sentences into Son Goku accent.

## Requirements

- Janome 0.4.2
- pykakasi 2.2.1
- semidbm 0.5.1
- six 1.15.0

## Installation

```
pip install gokulang
```

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

## Downloads

[![Downloads](https://pepy.tech/badge/gokulang)](https://pepy.tech/project/gokulang) [![Downloads](https://pepy.tech/badge/gokulang/month)](https://pepy.tech/project/gokulang) [![Downloads](https://pepy.tech/badge/gokulang/week)](https://pepy.tech/project/gokulang)

## Detail

[悟空語ジェネレーターをぺぇそん(Python)でも作ってみたぞ！えーぴーえぇ(API)化もしたぞ！ - Qiita](https://qiita.com/shonansurvivors/items/ce6c1c6f5b43fc16719b)

## Web API

[https://gokulang.herokuapp.com/](https://gokulang.herokuapp.com/)

## Reference

このモジュールはきんみさん([@_kinmi](https://twitter.com/_kinmi))の作成された悟空語ジェネレーターを参考に作成しました。

[フロント明るくないおじさんがWebアプリ作った話【悟空語ジェネレーター】 - Qiita](https://qiita.com/kinmi/items/c66aa98718acad84621b)
