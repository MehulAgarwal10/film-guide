
def score(imdb, meta, rotten_meter, audience_score):
    imdb_w = 5
    meta_w = 4
    rotten_w = 3
    audience_w = 3
    if meta > 0:
        total = imdb_w + meta_w + rotten_w + audience_w
    else:
        total = imdb_w + rotten_w + audience_w
        meta = 0
    temp1 = imdb_w * imdb
    temp2 = meta_w * meta
    temp3 = rotten_w * rotten_meter
    temp4 = audience_w * audience_score

    sc = (temp1 + temp2 + temp3 + temp4) / total
    # print('Score : ' + str((temp1 + temp2 + temp3 + temp4)/10))
    return sc

