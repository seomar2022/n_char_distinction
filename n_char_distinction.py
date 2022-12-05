def is_unique( poem, poems, n ): #poemのuniqueを確認
  return all( poem[:n] != other_poem[:n]
    for other_poem in poems - set([poem])
  )#該当poemを除いて他のpoem全部と比較し、n以下まで違う場合return

def is_deterministic( poem, poems, n ):
  #  poem[:n] で unique で、かつ poem[:n-1] で not unique
  return is_unique( poem, poems, n ) and not is_unique( poem, poems, n-1 )
    
def get_poems( poemlist, n ):
  # n 字きまりの句をリストで返す
  poems = set(poemlist) #集合に変更
  return [poem for poem in poems if is_deterministic( poem, poems, n )]
    
with open('100poems.csv', encoding='UTF-8') as f:
    poems ={line.strip().split(',')[1] for line in f if line.strip()}

for n in range(1, len(poems)):
  print('■', n, '字きまり')
  for poem in sorted(get_poems( poems, n )):
     print(poem)
