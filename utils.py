import jenkspy
import pandas as pd
import geopandas as gpd

def user_importance(data, tups=[]):
    data_c = data.copy()
    data_c = gpd.GeoDataFrame(data_c[[t[0] for t in tups] + ["geometry"]])

    for ind in range(len(tups)):
        if tups[ind][0] == "buy_quality":
            m = data_c["buy_quality"].max()
            data_c["buy_quality"] = data_c["buy_quality"].apply(lambda x: 5*(m-abs(x-tups[ind][1]))/m)
            tups[ind] = ("buy_quality", 1)
        elif tups[ind][0] == "rent_quality":
            m = data_c["rent_quality"].max()
            data_c["rent_quality"] = data_c["rent_quality"].apply(lambda x: 5*(m-abs(x-tups[ind][1]))/m)
            tups[ind] = ("rent_quality", 1)
        else:
            pass


    top = sum([tup[1] for tup in tups])
    data_c["result"] = data.drop("geometry", axis=1).T.apply(lambda x: sum([x[tup[0]]*tup[1]/top for tup in tups]))
    data_c.sort_values(by="result", inplace=True)
    
    alpha = data_c['result'].nunique()
    if alpha >= 6:
        breaks = jenkspy.jenks_breaks(data_c['result'], n_classes=6)
        labels = [0, 1, 2, 3, 4, 5]
    else:
        breaks = jenkspy.jenks_breaks(data_c['result'], n_classes=alpha)
        labels = [0, 1, 2, 3, 4, 5][6-alpha:]
    breaks[0] = breaks[0] - 1
    data_c['result'] = pd.cut(data_c['result'],
                              bins=breaks,
                              labels=labels,
                              include_lowest=True)

    data_c = data_c.dissolve(by="result").reset_index()

    return data_c

def splitter(txt):
    lt = txt.split("_")
    if len(lt) == 2:
        return lt[0]
    elif len(lt) == 3:
        return lt[0] + "_" + lt[1]
    else:
        raise ValueError("Oh No! It seems Yehor is really in need of vacation!")