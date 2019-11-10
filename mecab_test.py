import MeCab

text = """
ビットコインの取引所
"""
#「マウントゴックス」を運営するMTGOX（東京・渋谷）が、顧客から預かっていたビットコインの流出と経営破綻を発表してから1カ月あまり。日本をはじめ各国で規制の議論も本格化してきたが、目を引くのは、こうした騒動をよそに、ビットコインがなお一定の価値を保って取引されていることだ。低コストで送金できる利便性が、根強く支持されている証しといえる。仮想通貨が持つ可能性を理解するために、ビットコインとはどういうものなのか、改めて仕組みから整理したい。
t = MeCab.Tagger("-Ochasen -d /usr/local/lib/mecab/dic/mecab-ipadic-NEologd")
result = t.parse(text)


words_list = []

for s in text:
    s_parsed = t.parse(s)
    word_s = []

    for line in s_parsed.splitlines()[:-1]:
        word_s.append(line.split("\t")[0])
    words_list.append(word_s)
#Bag of words
#単語ごtの出現回数を測定

word2int = {}

i = 0
#各単語の単語のリストに対して処理を反復
for words in words_list:
#文書内の各単語に対して処理を反復
    for word in words:
        #単語が辞書に含まれてなければ追加して対応する整数を割り当てる
        if word not in word2int:
            word2int[word] = i
            i += 1  
print(word2int)
