import pandas as pd

df = pd.read_excel("data.xlsx")
df.fillna('#', inplace=True)

df = df.sort_values(by=['name'], ascending=True)

for index, row in df.iterrows():
    temp=f"""- {row["name"].title()}<br> 
[![Linkedin](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)]({row["linkedin"]})
[![Github](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)]({row["github"]})"""
    print(temp)
