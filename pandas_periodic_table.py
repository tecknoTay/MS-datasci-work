# This code takes the first 8 elements of the periodic table and reads a manual csv into a df. It then creates a new column
# within the df and reads in additional elements/contents!

import pandas as pd

#initial reading of manually created csv
periodic_df = pd.read_csv('periodic.csv')

#adding in the the 9th and 10th elements of the periodic table and their contents
periodic_df1 = pd.DataFrame({'Name': ['Fluorine', 'Neon'], 
                    'Symbol': ['F', 'Ne'], 
                    'Atomic_number': ['9', '10']})

#merging the contents from the old df into new df
periodic_df = pd.concat([periodic_df, periodic_df1], ignore_index=True)

#adding in a new column and contents name
periodic_df["Atomic_weights"] = [1, 4, 7, 9, 11, 12, 14, 16, 19, 20]

#printing the contents of the new df! :)
print(periodic_df)