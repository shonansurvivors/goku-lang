# gokulang

日本語文章をアニメ版ドラゴンボールの孫悟空風に変換します。

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
