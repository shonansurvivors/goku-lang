import re

from janome.tokenizer import Tokenizer
from pykakasi import kakasi as Kakasi

from .romakana import romaji_to_hiragana


class GokuLang:

    _detail = {
        'surface': '',
        'part_of_speech': '',
        'reading': '',
        'base_form': '',
        'original_romaji': '',
        'translated_romaji': '',
        'translated': ''
    }

    _result = {
        'original': '',
        'translated': '',
        'details': [],
    }

    def __init__(self):

        self._result['original'] = ''
        self._result['translated'] = ''
        self._result['details'] = []

    def __str__(self):

        return self._result['translated']

    def translate(self, text):

        self.__init__()

        self._result['original'] = text

        self._morphological_analysis(text)

        self._goku_translation()

        self._romaji_to_japanese()

        for detail in self._result['details']:
            self._result['translated'] += detail['translated']

        return self._result['translated']

    def _morphological_analysis(self, text):
        T = Tokenizer()
        tokens = T.tokenize(text.replace('\n', ''))
        for i in range(len(tokens)):
            self._detail['surface'] = tokens[i].surface
            self._detail['part_of_speech'] = tokens[i].part_of_speech.split(',')[0]
            self._detail['reading'] = tokens[i].reading
            self._detail['base_form'] = tokens[i].base_form

            if self._detail['reading'] != '*':
                self._detail['original_romaji'] = self._kana_to_romaji(self._detail['reading'])
            else:
                self._detail['original_romaji'] = self._kana_to_romaji(self._detail['surface'])

            self._result['details'].append(self._detail.copy())

    def _goku_translation(self):

        self._changing_verb()

        for detail in self._result['details']:

            if detail['translated_romaji'] == '':
                detail['translated_romaji'] = detail['original_romaji']

            detail['translated_romaji'] = re.sub('(a|e|o)(i|e)', 'ele', detail['translated_romaji'])

    def _changing_verb(self):

        for i in range(len(self._result['details'])):

            # i + 1 を参照するとIndexErrorとなるため、ループを終了させる
            if i == len(self._result['details']) - 1:
                break

            # 助動詞が文末以外だと想定外の変化が発生してしまうため、判定を追加
            # e.g.) し(動詞) + た(助動詞) + ぞ(助詞) => すっ + ぞ + ぞ
            if i != len(self._result['details']) - 2:
                continue

            if self._result['details'][i + 1]['part_of_speech'] != '助動詞':
                continue

            if re.match('^た|だ|ない$', self._result['details'][i + 1]['base_form']):
                continue

            if self._result['details'][i]['part_of_speech'] == '動詞':
                # e.g.) します => する(動詞)+ます(助動詞) => suru + masu => sultu + zo => すっ + ぞ
                t = self._result['details'][i]['base_form']
                t = self._kana_to_romaji(t)
                self._result['details'][i]['translated_romaji'] = t.replace('ru', 'ltu')

                self._result['details'][i + 1]['translated_romaji'] = 'zo'

        '''
        越えるよ => けぇっよ になるのでコメントアウト
        for i in range(len(self._result['details'])):

            if i == len(self._result['details']) - 1:
                break

            if self._result['details'][i + 1]['part_of_speech'] != '助詞':
                continue

            if self._result['details'][i - 1]['part_of_speech'] != '助詞':
                continue

            if self._result['details'][i]['part_of_speech'] == '動詞':
                # e.g.) 〜てみるか => 〜(動詞)+て(助詞)+みる(動詞)+か(助詞) => te + miru + ka => te + miltu + ka => て + みっ + か
                t = self._result['details'][i]['original_romaji']
                self._result['details'][i]['translated_romaji'] = t.replace('ru', 'ltu')
        '''

    def _romaji_to_japanese(self):

        for detail in self._result['details']:
            if detail['translated_romaji'] == detail['original_romaji'] or detail['translated_romaji'] == '':
                detail['translated'] = detail['surface']
            else:
                detail['translated'] = romaji_to_hiragana(detail['translated_romaji'])

    def _kana_to_romaji(self, text):

        kakasi = Kakasi()

        kakasi.setMode("H", "a")  # Hiragana to ascii
        kakasi.setMode("K", "a")  # Katakana to ascii
        kakasi.setMode("J", "a")  # Japanese(kanji) to ascii

        kakasi.setMode("r", "Hepburn")  # Use Hepburn romanization

        conv = kakasi.getConverter()
        result = conv.do(text)

        return result


if __name__ == '__main__':
    text = 'FF外から失礼します'
    g = GokuLang()
    g.translate(text)
    print(g._result['details'])
    print(g._result['original'])
    print(g._result['translated'])
