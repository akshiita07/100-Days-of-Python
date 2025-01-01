import pandas
data=pandas.read_csv("Day25_csv_pandas/Squirrel_data_analysis/2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20250101.csv")
# create squirrel_count.csv that has fur_color,n total number of squirrels of that specific fur color
only_colors=data["Primary Fur Color"]

# gray_colors=len(data[data["Primary Fur Color"]=="Gray"])
# cinnamon_colors=len(data[data["Primary Fur Color"]=="Cinnamon"])
# black_colors=len(data[data["Primary Fur Color"]=="Black"])
# print(f"Gray: {gray_colors}, Cinnamon: {cinnamon_colors}, Black: {black_colors}")
# data_dict={
#     "Fur_colors":["Gray","Cinnamon","Black"],
#     "Counts: ":[gray_colors,cinnamon_colors,black_colors]
# }
# new_data=pandas.DataFrame(data_dict)

# or shortcut:
new_data=only_colors.value_counts()
new_data.to_csv("squirrel_count.csv")