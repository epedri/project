import jenkspy
import pandas as pd

def user_importance(data, tups=[]):
    data_c = data.copy()
    top = sum([tup[1] for tup in tups])
    data_c["result"] = data.drop("geometry", axis=1).T.apply(lambda x: sum([x[tup[0]]*tup[1]/top for tup in tups]))
    data_c.sort_values(by="result", inplace=True)
    
    breaks = jenkspy.jenks_breaks(data_c['result'], n_classes=6)
    breaks[0] = breaks[0] - 1
    data_c['result'] = pd.cut(data_c['result'],
                              bins=breaks,
                              labels=[0, 1, 2, 3, 4, 5],
                              include_lowest=True)

    data_c = data_c.dissolve(by="result").reset_index()

    return data_c