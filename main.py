import pandas as pd

df = pd.read_csv("2023gamesPlayed.txt", header=None)

df_cleaned = df.iloc[:, [0, 2, 3, 4, 5, 6]]

df_cleaned.columns = ["Week", "Date", "Time", "Team 1", "Home/Away", "Team 2"]

df_cleaned.to_csv("cleaned_output.csv", index=False)

print(df_cleaned.head())

for index in df_cleaned.index:
    if df_cleaned.at[index, "Home/Away"] == "@":
        temp = df_cleaned.at[index, "Team 1"]
        df_cleaned.at[index, "Team 1"] = df_cleaned.at[index, "Team 2"]
        df_cleaned.at[index, "Team 2"] = temp



df_cleaned = df_cleaned.iloc[:, [0, 1, 2, 3, 5]]

df_cleaned.rename(columns={"Team 1": "Home Team", "Team 2": "Away Team"}, inplace=True)

df_cleaned.to_csv("cleaned_output.csv", index=False)

print(df_cleaned.head())