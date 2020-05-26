def getMixedTypeDict(N, list_B, StartDate):
# see https://github.com/pandas-dev/pandas/blob/4407d9f43e93923422833d95793b09a967047205/pandas/_testing.py
#    index = pd.Index(["a", "b", "c", "d", "e", 'f'])
    l = [i for i in range(N)]
#    index = pd.Index([1, 2, 3, 4, 5, 6])
    index = pd.Index(l)

    import random
    #sampling with replacement
    #list_B = [0.0, 1.0]
    sampling = random.choices(list_B, k=N)
    
    M = ["foo" + str(i) for i in range(N)]
    
    data = {
        "Integer": l,
        "Sampling": sampling,
        "String": M,
        "Date": pd.bdate_range(StartDate, periods=N),
    }

    return index, data


def makeMixedDataFrame(P = 5, list_B=[0.0, 1.0], StartDate = "1/1/2009"):
    """
    Ex: makeMixedDataFrame(7, [0, 3, 4], '3/12/2009')
    """
    return pd.DataFrame(getMixedTypeDict(P, list_B, StartDate)[1])
