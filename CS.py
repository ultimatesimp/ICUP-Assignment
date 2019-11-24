import pandas as p
import matplotlib.pyplot as plt


#Question 1
#Print the first and last five rows from the dataset

file_name = p.read_csv('C:\\Users\\admin\\Desktop\\CS\\Automobile_data.csv')
print(file_name.head(5))
print(file_name.tail(5))

#Question 2
#Replace all column values which contain ‘?’ and n.a with NaN


file_name = p.read_csv('C:\\Users\\admin\\Desktop\\CS\\Automobile_data.csv', na_values = {
								'price' : ['?','n.a'], 'stroke' : ['?','n.a'], 'horsepower' : ['?','n.a'],
								'peak-rpm' : ['?','n.a'], 'average-mileage' : ['?','n.a'] } )
print(file_name)


#Question 3
#Print most expensive car’s company name and price and show it using line graph

file_name = p.read_csv('C:\\Users\\admin\\Desktop\\CS\\Automobile_data.csv')
file_name = file_name[['company','price']][file_name.price == file_name['price'].max()]
print(file_name)





#Question 4
# Print all  the details of the particular car manufacturer


file_name = p.read_csv('C:\\Users\\admin\\Desktop\\CS\\Automobile_data.csv')
manufacturers = file_name.groupby('company')
mercedes_info = manufacturers.get_group('mercedes-benz')
print(mercedes_info)

left = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
labels = ['Toyota','BMW','Nissan','Mazda','Mercedes-benzr','Volkswagen','Audi','Mitsubishi',
'Honda','Jaguar','Chevorlet'
,'Alfa-romero','Isuzu','Porsche','Volvo','Dodge']
height = [7,6,5,5,4,4,4,4,3,3,3,3,3,3,2,2]
plt.bar(left, height, tick_label=labels,color='red',width = 0.3,edgecolor='black')
plt.ylabel('Number of Models')
plt.xlabel('Companies')
plt.show()


# Question 5
# Find the total number of cars manufactured by each company and show it using line graph


file_name = p.read_csv('C:\\Users\\admin\\Desktop\\CS\\Automobile_data.csv')
print(file_name['company'].value_counts())


#Question 6
# Find the average mileage of each car making company


file_name = p.read_csv('C:\\Users\\admin\\Desktop\\CS\\Automobile_data.csv')
manufacturers = file_name.groupby('company')
mileage_info  = manufacturers['company','average-mileage'].mean()
print(mileage_info)


#Question 7
# Create two data frames using the following two Dicts, Concatenate those two data frames and create a key for each data frame

German_Cars = {'Company': ['Ford', 'Mercedes', 'BMV', 'Audi'], 'Price': [23845, 171995, 135925 , 71400]}
German_Car_Dataframe = p.DataFrame.from_dict(German_Cars)

Japanese_Cars = {'Company': ['Toyota', 'Honda', 'Nissan', 'Mitsubishi '], 'Price': [29995, 23600, 61500 , 58900]}
Japanese_Car_Dataframe = p.DataFrame.from_dict(Japanese_Cars)

Global_Cars_Dataframe = p.concat([German_Car_Dataframe, Japanese_Car_Dataframe], keys = ['German_Cars','Japanese_Cars'])
print(Global_Cars_Dataframe)


#Question 8
#Create two data frames using the following two Dicts, Concatenate those two data frames and create a key for each data frame


Car_Price = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'Price': [23845, 17995, 135925 , 71400]}
Car_Price_Dataframe = p.DataFrame.from_dict(Car_Price)

Car_Horsepower = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'Horsepower': [141, 80, 182 , 160]}
Car_Horsepower_Dataframe = p.DataFrame.from_dict(Car_Horsepower)

Global_Cars_Dataframe_2 = p.merge(Car_Price_Dataframe, Car_Horsepower_Dataframe, on = 'Company')
print(Global_Cars_Dataframe_2)






















