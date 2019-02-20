# goku-lang

日本語文章をアニメ版ドラゴンボールの孫悟空風に変換すっぞ。

## Reuirements

- Janome 0.3.7
- pykakasi 0.94
- semidbm 0.5.1
- six 1.12.0

```
(venv) $ pip install janome pykakasi
```

## Usage

```
(venv) $ python
>>> from gokulang import GokuLang
>>> g = GokuLang()
>>> g.translate('FF外から失礼します')
'FFげぇからしつれぇすっぞ'
```

## Reference

きんみさん([@_kinmi](https://twitter.com/_kinmi))の作成された悟空語ジェネレーターを参考に作成しました。

[フロント明るくないおじさんがWebアプリ作った話【悟空語ジェネレーター】 - Qiita](https://qiita.com/kinmi/items/c66aa98718acad84621b)