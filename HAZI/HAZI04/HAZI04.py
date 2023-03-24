# %%
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# %%
'''
FONTOS: Az első feladat által visszaadott DataFrame-et kell használni a további feladatokhoz. 
A függvényeken belül mindig készíts egy másolatot a bemenő df-ről, (new_df = df.copy() és ezzel dolgozz tovább.)
'''

# %%
'''
Készíts egy függvényt, ami egy string útvonalat vár paraméterként, és egy DataFrame ad visszatérési értékként.

Egy példa a bemenetre: 'test_data.csv'
Egy példa a kimenetre: df_data
return type: pandas.core.frame.DataFrame
függvény neve: csv_to_df
'''

# %%
# 1
def csv_to_df(path : str) -> pd.core.frame.DataFrame:
    return pd.read_csv(path)

# %%
'''
Készíts egy függvényt, ami egy DataFrame-et vár paraméterként, 
és átalakítja azoknak az oszlopoknak a nevét nagybetűsre amelyiknek neve nem tartalmaz 'e' betüt.

Egy példa a bemenetre: df_data
Egy példa a kimenetre: df_data_capitalized
return type: pandas.core.frame.DataFrame
függvény neve: capitalize_columns
'''

# %%
# 2     ha most se jó akkor list(map())
def capitalize_columns(input_df : pd.core.frame.DataFrame) -> pd.core.frame.DataFrame:
    new_df = input_df.copy()
    new_df.columns = map(lambda x: x.upper() if 'e' not in x else x, new_df.columns)
    return new_df

# %%
'''
Készíts egy függvényt, ahol egy szám formájában vissza adjuk, hogy hány darab diáknak sikerült teljesíteni a matek vizsgát.
(legyen az átmenő ponthatár 50).

Egy példa a bemenetre: df_data
Egy példa a kimenetre: 5
return type: int
függvény neve: math_passed_count
'''

# %%
# 3
def math_passed_count(input_df : pd.core.frame.DataFrame) -> int:
    new_df = input_df.copy()
    return len(new_df[new_df["math score"] >= 50])

# %%
'''
Készíts egy függvényt, ahol Dataframe ként vissza adjuk azoknak a diákoknak az adatait (sorokat), akik végeztek előzetes gyakorló kurzust.

Egy példa a bemenetre: df_data
Egy példa a kimenetre: df_did_pre_course
return type: pandas.core.frame.DataFrame
függvény neve: did_pre_course
'''

# %%
# 4
def did_pre_course(input_df : pd.core.frame.DataFrame) -> pd.core.frame.DataFrame:
    new_df = input_df.copy()
    return new_df[new_df["test preparation course"] == "completed"]

# %%
'''
Készíts egy függvényt, ahol a bemeneti Dataframet a diákok szülei végzettségi szintjei alapján csoportosításra kerül,
majd aggregációként vegyük, hogy átlagosan milyen pontszámot értek el a diákok a vizsgákon.

Egy példa a bemenetre: df_data
Egy példa a kimenetre: df_average_scores
return type: pandas.core.frame.DataFrame
függvény neve: average_scores
'''

# %%
# 5
def average_scores(input_df : pd.core.frame.DataFrame) -> pd.core.frame.DataFrame:
    new_df = input_df.copy()
    new_df["avg"] = (new_df["math score"] + new_df["reading score"] + new_df["writing score"]) / 3
    return pd.DataFrame(new_df.groupby("parental level of education")["avg"].mean())

# %%
'''
Készíts egy függvényt, ami a bemeneti Dataframet kiegészíti egy 'age' oszloppal, töltsük fel random 18-66 év közötti értékekkel.
A random.randint() függvényt használd, a random sorsolás legyen seedleve, ennek értéke legyen 42.

Egy példa a bemenetre: df_data
Egy példa a kimenetre: df_data_with_age
return type: pandas.core.frame.DataFrame
függvény neve: add_age
'''

# %%
# 6
def add_age(input_df : pd.core.frame.DataFrame) -> pd.core.frame.DataFrame:
    new_df = input_df.copy()
    np.random.seed(42)
    new_df["age"] = np.random.randint(18, 67, new_df.shape[0])
    return new_df

# %%
'''
Készíts egy függvényt, ami vissza adja a legjobb teljesítményt elérő női diák pontszámait.

Egy példa a bemenetre: df_data
Egy példa a kimenetre: (99,99,99) #math score, reading score, writing score
return type: tuple
függvény neve: female_top_score
'''

# %%
# 7
def female_top_score(input_df : pd.core.frame.DataFrame) -> tuple:
    new_df = input_df.copy()
    new_df["avg"] = (new_df["math score"] + new_df["reading score"] + new_df["writing score"]) / 3
    max_girls = new_df.loc[(new_df["gender"] == "female") & (new_df["avg"] == new_df["avg"].max())]
    return tuple([max_girls.iloc[0]["math score"], max_girls.iloc[0]["reading score"], max_girls.iloc[0]["writing score"]])

# %%
'''
Készíts egy függvényt, ami a bementeti Dataframet kiegészíti egy 'grade' oszloppal. 
Számoljuk ki hogy a diákok hány százalékot ((math+reading+writing)/300) értek el a vizsgán, és osztályozzuk őket az alábbi szempontok szerint:

90-100%: A
80-90%: B
70-80%: C
60-70%: D
<60%: F

Egy példa a bemenetre: df_data
Egy példa a kimenetre: df_data_with_grade
return type: pandas.core.frame.DataFrame
függvény neve: add_grade
'''

# %%
# 8      ha nem jó hogy új oszlopot adtam hozzá akkor tömbbel kell megoldani helyette
def add_grade(input_df : pd.core.frame.DataFrame) -> pd.core.frame.DataFrame:
    new_df = input_df.copy()
    new_df["percentage"] = (new_df["math score"] + new_df["reading score"] + new_df["writing score"]) / 3
    new_df["grade"] = list(map(lambda x: 'A' if x >= 90 else ('B' if x >= 80 else ('C' if x >= 70 else ('D' if x >= 60 else 'F'))), new_df["percentage"]))
    return new_df

# %%
'''
Készíts egy függvényt, ami a bemeneti Dataframe adatai alapján elkészít egy olyan oszlop diagrammot,
ami vizualizálja a nemek által elért átlagos matek pontszámot.

Oszlopdiagram címe legyen: 'Average Math Score by Gender'
Az x tengely címe legyen: 'Gender'
Az y tengely címe legyen: 'Math Score'

Egy példa a bemenetre: df_data
Egy példa a kimenetre: fig
return type: matplotlib.figure.Figure
függvény neve: math_bar_plot
'''

# %%
# 9
def math_bar_plot(input_df : pd.core.frame.DataFrame):
    new_df = input_df.copy()
    fig = plt.figure()
    ax = fig.add_axes(new_df.groupby("gender")["math score"].mean().plot(kind='bar'))
    ax.set_title('Average Math Score by Gender')
    ax.set_xlabel('Gender')
    ax.set_ylabel('Math Score')
    return fig

# %%
''' 
Készíts egy függvényt, ami a bemeneti Dataframe adatai alapján elkészít egy olyan histogramot,
ami vizualizálja az elért írásbeli pontszámokat.

A histogram címe legyen: 'Distribution of Writing Scores'
Az x tengely címe legyen: 'Writing Score'
Az y tengely címe legyen: 'Number of Students'

Egy példa a bemenetre: df_data
Egy példa a kimenetre: fig
return type: matplotlib.figure.Figure
függvény neve: writing_hist
'''

# %%
# 10
def writing_hist(input_df : pd.core.frame.DataFrame):
    new_df = input_df.copy()
    fig, ax = plt.subplots()
    plt.hist(new_df["writing score"])
    ax.set_title('Distribution of Writing Scores')
    ax.set_xlabel('Writing Score')
    ax.set_ylabel('Number of Students')
    return fig

# %%
''' 
Készíts egy függvényt, ami a bemeneti Dataframe adatai alapján elkészít egy olyan kördiagramot,
ami vizualizálja a diákok etnikum csoportok szerinti eloszlását százalékosan.

Érdemes megszámolni a diákok számát, etnikum csoportonként,majd a százalékos kirajzolást az autopct='%1.1f%%' paraméterrel megadható.
Mindegyik kör szelethez tartozzon egy címke, ami a csoport nevét tartalmazza.
A diagram címe legyen: 'Proportion of Students by Race/Ethnicity'

Egy példa a bemenetre: df_data
Egy példa a kimenetre: fig
return type: matplotlib.figure.Figure
függvény neve: ethnicity_pie_chart
'''

# %%
# 11
def ethnicity_pie_chart(input_df : pd.core.frame.DataFrame):
    new_df = input_df.copy()
    fig, ax = plt.subplots()
    kek = new_df.groupby("race/ethnicity")["gender"].count()
    print(kek.values)
    ax.pie(kek.values, labels=kek.index, autopct='%1.1f%%')
    ax.set_title('Proportion of Students by Race/Ethnicity')
    return fig


