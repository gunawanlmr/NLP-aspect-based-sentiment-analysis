aspects_map = {'makanan':'FOOD', 'pelayanan':'SERVICE', 'harga':'PRICE', 'suasana':'AMBIANCE'}
polarities_map = {'positif':'POSITIVE', 'negatif': 'NEGATIVE'}

def most_polar(term_list):
    res = {'FOOD':{'POSITIVE':(0, 0), 'NEGATIVE':(0, 0)}, 'SERVICE':{'POSITIVE':(0, 0), 'NEGATIVE':(0, 0)}, 'PRICE':{'POSITIVE':(0, 0), 'NEGATIVE':(0, 0)}, 'AMBIANCE':{'POSITIVE':(0, 0), 'NEGATIVE':(0, 0)}}
    for term in term_list:
        _, aspect = sim.most_similar_aspect(term[0])
        score, polarity = sim.most_similar_polarities(term[1])
        aspect = aspects_map[aspect]
        polarity = polarities_map[polarity]
        score = score + res[aspect][polarity][0]
        count = res[aspect][polarity][1] + 1
        res[aspect][polarity] = (score, count)
    return res

def determine_polarity(polar_list):
    for aspect in polar_list:
        for polarity in polar_list[aspect]:
            if polar_list[aspect][polarity][0] != 0:
                mean = polar_list[aspect][polarity][0] / polar_list[aspect][polarity][1]
            else:
                mean = 0
            polar_list[aspect][polarity] = mean
        if polar_list[aspect]['POSITIVE'] > polar_list[aspect]['NEGATIVE']:
            polar_list[aspect] = 'POSITIVE'
        elif polar_list[aspect]['POSITIVE'] < polar_list[aspect]['NEGATIVE']:
            polar_list[aspect] = 'NEGATIVE'
        else:
            polar_list[aspect] = None
    return polar_list
    