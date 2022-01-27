import numpy as np
import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt
pd.set_option("display.max_rows", None, "display.max_columns", None)

#Setting up where my data is stored
DATADIR = Path('/Volumes/Macintosh HD/Users/danielradoff/Desktop/Complexin File')
assert DATADIR.exists()

#Reading the animal complexin file and organizing it by length of protein ("Acc. Len") and plotting the data as a histogram
animal_file = DATADIR / "Animal Alignment Descriptions.csv"
assert animal_file.exists()

animal_data = pd.read_csv(animal_file)
print(animal_data["Acc. Len"].to_string())
animal_data.hist(column="Acc. Len", bins=50)
#The complexins tend to fall between 88 and 171 amino acids long in animals.

#Reading the plant complexin analogues and organizing it by length of protein ("Acc. Len") and plotting it as a historgram too
plant_file = DATADIR / "Plant Alignment Descriptions.csv"
assert plant_file.exists()
plant_data = pd.read_csv(plant_file)
plant_sorted_data = plant_data.sort_values(["Acc. Len"], ascending=True)
print(plant_sorted_data)
plant_sorted_data.hist(column="Acc. Len", bins=50)

#Truncating so only look at "complexins" of the right length range and plotting that histogram
truncated_plant_sorted_data = plant_sorted_data[plant_sorted_data["Acc. Len"].between(88,171)]
truncated_plant_sorted_data.hist(column="Acc. Len", bins=50)

#Resorting the truncated list by E value to see what the best matches are
resorted_truncated_plant_sorted_data = truncated_plant_sorted_data.sort_values(["E value"], ascending=True)
print(resorted_truncated_plant_sorted_data.to_string)

#Exporting to an excel file so I can more easily read it
resorted_truncated_plant_sorted_data.to_excel(DATADIR / "Sorted plant complexin data.xlsx")

#Looking at the proteins between 172 and 366 amino acids just in case
longer_truncated_plant_sorted_data = plant_sorted_data[plant_sorted_data["Acc. Len"].between(172,366)]
longer_truncated_plant_sorted_data.hist(column="Acc. Len", bins=50)

#Resorting the new truncated list by E value to see what the best matches are and exporting to excel
resorted_longer_truncated_plant_sorted_data = longer_truncated_plant_sorted_data.sort_values(["E value"], ascending=True)
print(resorted_longer_truncated_plant_sorted_data.to_string)
resorted_longer_truncated_plant_sorted_data.to_excel(DATADIR / "Sorted longer plant complexin data.xlsx")

plt.show()