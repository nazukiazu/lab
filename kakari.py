#!/usr/bin/python
# coding:utf-8

import CaboCha
 
def get_word(tree, chunk):
    surface = ''
    for i in range(chunk.token_pos, chunk.token_pos + chunk.token_size):
        token = tree.token(i)
        features = token.feature.split(',')
        if features[0] == '名詞':
            surface += token.surface
        elif features[0] == '形容詞':
            surface += features[6]
            break
        elif features[0] == '動詞':
            surface += features[6]
            break
    return surface
 
def get_2_words(line):
    cp = CaboCha.Parser('-f1')
    tree = cp.parse(line)
    chunk_dic = {}
    chunk_id = 0
    for i in range(0, tree.size()):
        token = tree.token(i)
        if token.chunk:
            chunk_dic[chunk_id] = token.chunk
            chunk_id += 1
 
    tuples = []
    for chunk_id, chunk in chunk_dic.items():
        if chunk.link > 0:
            from_surface =  get_word(tree, chunk)
            to_chunk = chunk_dic[chunk.link]
            to_surface = get_word(tree, to_chunk)
            tuples.append((from_surface, to_surface))
    return tuples
 
if __name__ == '__main__' :
    f = open('text.txt')
    lines = f.readlines()
    f.close()
    i = 0
    uni_text = [0]*len(lines)

    for line in lines:
        uni_text[i] = line
        tuples = get_2_words(uni_text[i])
        for t in tuples:
            print(t[0] + ' => ' + t[1])
        i = i + 1 
    
   
