import unittest
from gokulang import GokuLang


class GokuLangTest(unittest.TestCase):
    def setUp(self):
        self.G = GokuLang()

    def tearDown(self):
        pass

    def test_ai_ae(self):
        q = '最初の試合は緊張するだろうけど、今のお前なら大丈夫だ'
        a = 'せぇしょのしえぇは緊張するだろうけど、今のおめぇならでぇじょうぶだ'
        self.assertEqual(a, self.G.translate(q))

    def test_ei_ae_oi(self):
        q = '冷静に考えろ、奴は強いぞ'
        a = 'れぇせぇにかんげぇろ、奴はつえぇぞ'
        self.assertEqual(a, self.G.translate(q))

    def test_oe(self):
        q = 'ここを越えるよ'
        a = 'ここをけぇるよ'
        self.assertEqual(a, self.G.translate(q))

    def test_kaeru(self):
        q = 'もう帰ります'
        a = 'もうけぇっぞ'
        self.assertEqual(a, self.G.translate(q))

    def test_non_reading_shimasu(self):
        q = 'FF外から失礼します'
        a = 'FFげぇからしつれぇすっぞ'
        self.assertEqual(a, self.G.translate(q))

    def test_ta(self):
        # 見送っぞ にならないことのテスト
        q = '見送った'
        a = '見送った'
        self.assertEqual(a, self.G.translate(q))

    def test_ta2(self):
        # 登録すっぞぞ にならないことのテスト
        q = '登録したぞ'
        a = '登録したぞ'
        self.assertEqual(a, self.G.translate(q))

    def test_nai(self):
        # みえっぞ にならないことのテスト
        q = '見えない'
        a = '見えねぇ'
        self.assertEqual(a, self.G.translate(q))

    def test_da(self):
        # あそっぞ や あそぶぞ にならないことのテスト
        q = '遊んだ'
        a = '遊んだ'
        self.assertEqual(a, self.G.translate(q))

    def test_dekami(self):
        q = 'ぱいぱいでか美'
        a = 'ぺぇぺぇでか美'
        self.assertEqual(a, self.G.translate(q))


if __name__ == '__main__':
    unittest.main()