#Uncomment the pip install code below if you haven't installed these libraries yet
#!pip install pandas
#!pip install zipfile
#!pip install kaggle

# import the pandas library
import pandas as pd

bikes = pd.read_csv(r"C:\Users\cdwiv\Desktop\London Bike Ride Analysis Project\london_merged.csv") 

bikes.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 17414 entries, 0 to 17413
Data columns (total 10 columns):
 #   Column        Non-Null Count  Dtype  
---  ------        --------------  -----  
 0   timestamp     17414 non-null  object 
 1   cnt           17414 non-null  int64  
 2   t1            17414 non-null  float64
 3   t2            17414 non-null  float64
 4   hum           17414 non-null  float64
 5   wind_speed    17414 non-null  float64
 6   weather_code  17414 non-null  int64  
 7   is_holiday    17414 non-null  int64  
 8   is_weekend    17414 non-null  int64  
 9   season        17414 non-null  int64  
dtypes: float64(4), int64(5), object(1)

bikes.shape
(17414, 10)

bikes
	timestamp	      cnt	   t1	 t2	  hum	wind_ speed	weather_code	is_holiday	is_weekend	season
0	2015-01-04     0:00	  182	 3.0	2.0	93.0	6.0	   3	              0	          1	        3
1	2015-01-04     1:00	  138	 3.0	2.5	93.0	5.0	   1	              0	          1	        3
2	2015-01-04     2:00	  134	 2.5	2.5	96.5	0.0	   1	              0	          1	        3
3	2015-01-04     3:00	  72	 2.0	2.0	100.0	0.0	   1	              0	          1	        3
4	2015-01-04     4:00	  47	 2.0	0.0	93.0	6.5	   1	              0	          1	        3
...	...	...	...	...	...	...	...	...	...	...
17409	2017-01-03 19:00	1042 5.0	1.0	81.0	19.0	 3	              0	          0	        3
17410	2017-01-03 20:00	541	 5.0	1.0	81.0	21.0	 4	              0	          0	        3
17411	2017-01-03 21:00	337	 5.5	1.5	78.5	24.0	 4	              0	          0	        3
17412	2017-01-03 22:00	224	 5.5	1.5	76.0	23.0	 4	              0	          0	        3
17413	2017-01-03 23:00	139	 5.0	1.0	76.0	22.0	 2	              0	          0	        3
17414 rows × 10 columns

# count the unique values in the weather_code column
bikes.weather_code.value_counts()
weather_code
1     6150
2     4034
3     3551
7     2141
4     1464
26      60
10      14
Name: count, dtype: int64

# count the unique values in the season column
bikes.season.value_counts()
season
0    4394
1    4387
3    4330
2    4303
Name: count, dtype: int64

# specifying the column names that I want to use
new_cols_dict ={
    'timestamp':'time',
    'cnt':'count', 
    't1':'temp_real_C',
    't2':'temp_feels_like_C',
    'hum':'humidity_percent',
    'wind_speed':'wind_speed_kph',
    'weather_code':'weather',
    'is_holiday':'is_holiday',
    'is_weekend':'is_weekend',
    'season':'season'
}

# Renaming the columns to the specified column names
bikes.rename(new_cols_dict, axis=1, inplace=True)


bikes


              Time           count   temp_real_C  temp_feels_like_C    humidity_percent   wind_speed_kph   weather    is_holiday	is_weekend	season
0	2015-01-04 0:00            182	    3.0	            2.0	             93.0	                   6.0            3	            0	        1	          3
1	2015-01-04 1:00            138	    3.0	            2.5	             93.0	                   5.0	          1	            0	        1	          3
2	2015-01-04 2:00            134	    2.5	            2.5	             96.5	                   0.0	          1	            0	        1           3
3	2015-01-04 3:00            72	      2.0	            2.0	             100.0	                 0.0            1	            0	        1	          3
4	2015-01-04 4:00            47	      2.0	            0.0	             93.0	                   6.5	          1	            0	        1	          3
...	...	...            ...	    ...	...	                  ...	                    ...	                    ...	            ...	...
17409	2017-01-03 19:00      1042	    5.0	            1.0	             81.0	                   19.0	          3	            0	        0	          3
17410	2017-01-03 20:00       541	    5.0	            1.0	             81.0	                   21.0	          4	            0	        0	          3
17411	2017-01-03 21:00       337	    5.5	            1.5    	         78.5        	           24.0	          4	            0	        0	          3
17412	2017-01-03 22:00       224	    5.5	            1.5	             76.0	                   23.0	          4	            0	        0	          3
17413	2017-01-03 23:00       139	    5.0	            1.0	             76.0	                   22.0           2	            0	        0         	3
17414 rows × 10 columns

# creating a season dictionary so that we can map the integers 0-3 to the actual written values
season_dict = {
    0:'spring',
    1:'summer',
    2:'autumn',
    3:'winter'
}
# creating a weather dictionary so that we can map the integers to the actual written values
weather_dict = {
    1:'Clear',
    2:'Scattered clouds',
    3:'Broken clouds',
    4:'Cloudy',
    7:'Rain',
    10:'Rain with thunderstorm',
    26:'Snowfall'
}
# changing the seasons column data type to string
#bikes.season = bikes.season.astype('str')
# mapping the values 0-3 to the actual written seasons
bikes.season = bikes.season.map(season_dict)

# changing the weather column data type to string
#bikes.weather = bikes.weather.astype('str')
# mapping the values to the actual written weathers
bikes.weather = bikes.weather.map(weather_dict)

              Time           count   temp_real_C  temp_feels_like_C    humidity_percent   wind_speed_kph   weather         is_holiday	is_weekend	season
0	2015-01-04 0:00            182	    3.0	            2.0	             93.0	                   6.0       Broken clouds        0	        1	         winter
1	2015-01-04 1:00            138	    3.0	            2.5	             93.0	                   5.0	        Clear	            0	        1	         winter
2	2015-01-04 2:00            134	    2.5	            2.5	             96.5	                   0.0	        Clear	            0	        1          winter 
3	2015-01-04 3:00            72	      2.0	            2.0	             100.0	                 0.0          Clear	            0	        1	         winter 
4	2015-01-04 4:00            47	      2.0	            0.0	             93.0	                   6.5	        Clear 	          0	        1	         winter 
...	...	...            ...	    ...	...	                  ...	                    ...	                    ...	            ...	...
17409	2017-01-03 19:00      1042	    5.0	            1.0	             81.0	                   19.0	      Broken clouds       0	        0	         winter 
17410	2017-01-03 20:00       541	    5.0	            1.0	             81.0	                   21.0	        Cloudy	          0	        0	         winter
17411	2017-01-03 21:00       337	    5.5	            1.5    	         78.5        	           24.0	        Cloudy            0	        0	         winter 
17412	2017-01-03 22:00       224	    5.5	            1.5	             76.0	                   23.0	        Cloudy  	        0	        0	         winter 
17413	2017-01-03 23:00       139	    5.0	            1.0	             76.0	                   22.0      Scattered Clouds     0	        0          winter	
17414 rows × 10 columns

# writing the final dataframe to an excel file that we will use in our Tableau visualisations. The file will be the 'london_bikes_final.xlsx' file and the sheet name is 'Data'
bikes.to_excel('london_bikes_final.xlsx', sheet_name='Data', index=False)
