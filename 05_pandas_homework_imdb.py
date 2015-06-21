'''
Pandas Homework with IMDB data
'''

'''
BASIC LEVEL
'''

# read in 'imdb_1000.csv' and store it in a DataFrame named movies
import pandas as pd
pd.read_table('imdb_1000.csv')
movies = pd.read_table('imdb_1000.csv', sep=',')

# check the number of rows and columns
movies.shape

# check the data type of each column
movies.dtypes

# calculate the average movie duration
movies.duration.mean()

# sort the DataFrame by duration to find the shortest and longest movies
movies.sort('duration',ascending=False).head(1)
movies.sort('duration',ascending=True).head(1)

# create a histogram of duration, choosing an "appropriate" number of bins
movies.duration.plot(kind='hist', bins=20)

# use a box plot to display that same data
movies.duration.plot(kind='box')

'''
INTERMEDIATE LEVEL
'''

# count how many movies have each of the content ratings
movies.groupby('content_rating').title.count()

# use a visualization to display that same data, including a title and x and y labels
movies.content_rating.value_counts().plot(kind='bar', title='Content Rating per Movie')
movies.xlabel('Content Rating')
movies.ylabel('Frequency')

# convert the following content ratings to "UNRATED": NOT RATED, APPROVED, PASSED, GP
movies.content_rating.replace('NOT RATED', 'UNRATED', inplace=True)
movies.content_rating.replace('APPROVED', 'UNRATED', inplace=True)
movies.content_rating.replace('PASSED', 'UNRATED', inplace=True)
movies.content_rating.replace('GP', 'UNRATED', inplace=True)

# convert the following content ratings to "NC-17": X, TV-MA
movies.content_rating.replace('TV-MA','NC-17', inplace=True)
movies.content_rating.replace('X', 'NC-17', inplace=True)

# count the number of missing values in each column
movies.isnull().sum
# if there are missing values: examine them, then fill them in with "reasonable" values
len(movies.index-movies.count()

# calculate the average star rating for movies 2 hours or longer
# and compare that with the average star rating for movies shorter than 2 hours
movies[movies.duration > 120].star_rating.mean() 
movies[movies.duration < 120].star_rating.mean()  

# use a visualization to detect whether there is a relationship between star rating and duration
pd.scatter_matrix(movies[['star_rating', 'duration']])
movies.plot(kind='scatter', x='duration', y='star_rating')

# calculate the average duration for each genre
movies.groupby('genre').duration.mean()

'''
ADVANCED LEVEL
'''

# visualize the relationship between content rating and duration

# determine the top rated movie (by star rating) for each genre
movies.groupby(['genre','title']).star_rating.max().
movies.groupby(['genre','title']).star_rating.max()
# check if there are multiple movies with the same title, and if so, determine if they are actually duplicates
movies.title.duplicated().sum()
movies.set_index('title').index.get_duplicates()

# calculate the average star rating for each genre, but only include genres with at least 10 movies
movies[movies.genre >'10'].star_rating.mean()
'''
BONUS
'''

# Figure out something "interesting" using the actors data!
