from nba_api.stats.static import teams
import pandas as pd


dict_ = {'a': [11, 21, 31], 'b': [12, 22, 32]}

df = pd.DataFrame(dict_)


nba_teams = teams.get_teams()


def one_dict(list_dict):
    keys = list_dict[0].keys
    out_dict = {key: [] for key in keys}
    for dict_in in list_dict:
        for key, value in dict_.items():
            out_dict[key].append(value)
    return out_dict

    dict_nba_team = one_dict(nba_teams)

    df_warriors = dict_nba_team[dict_nba_team['nickname'] == 'Warriors']
    print(df_warriors)
    id_warriors = df_warriors[['id']].values[0][0]
    print(id_warriors)
