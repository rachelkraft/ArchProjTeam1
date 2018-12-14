import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

r_data_df = pd.read_csv('Shootout_Mac2017.csv')
em_data_df = pd.read_csv('Shootout_Emily.csv')
aishah_data_df = pd.read_csv('Shootout_Aishah_Mac2011.csv')
agni_data_df = pd.read_csv('Shootout_Agni.csv')

df = pd.concat([r_data_df.mean(),em_data_df.mean(),aishah_data_df.mean(),agni_data_df.mean()],axis=1).T

print(df)

#raw_data = {'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'],
# 'pre_score': [4, 24, 31, 2, 3],
#    'mid_score': [25, 94, 57, 62, 70],
#   'post_score': [5, 43, 23, 23, 51]}
#df = pd.DataFrame(raw_data, columns = ['first_name', 'pre_score', 'mid_score', 'post_score'])

# Setting the positions and width for the bars
#pos = list(range(len(df['pre_score'])))
pos = list(range(len(df['Mersenne Twister'])))
print(pos)
width = 0.2

# Plotting the bars
fig, ax = plt.subplots(figsize=(10,5))

# Create a bar with pre_score data,
# in position pos,
plt.bar(pos,
        #using df['pre_score'] data,
        df['Mersenne Twister'],
        # of width
        width,
        # with alpha 0.5
        alpha=0.5,
        # with color
        color='#EE3224')
        # with label the first value in first_name
        #label=df['first_name'][0])

# Create a bar with mid_score data,
# in position pos + some width buffer,
plt.bar([p + width for p in pos],
        #using df['mid_score'] data,
        df['SPCG64'],
        # of width
        width,
        # with alpha 0.5
        alpha=0.5,
        # with color
        color='#F78F1E')
        # with label the second value in first_name
        #label=df['first_name'][1])

# Create a bar with post_score data,
# in position pos + some width buffer,
plt.bar([p + width*2 for p in pos],
        #using df['post_score'] data,
        df['Xoroshiro 128+'],
        # of width
        width,
        # with alpha 0.5
        #alpha=0.5,
        # with color
        color='#FFC222')
        # with label the third value in first_name
        #label=df['first_name'][2])
        
# Create a bar with post_score data,
# in position pos + some width buffer,
plt.bar([p + width*3 for p in pos],
        #using df['post_score'] data,
        df['Xorshift 128+'],
        # of width
        width,
        # with alpha 0.5
        #alpha=0.5,
        # with color
        color='#FF3300')
        # with label the third value in first_name
        #label=df['first_name'][2])

# Set the y axis label
ax.set_ylabel('Average MB/s',fontweight='bold')

# Set the chart's title
ax.set_title('Average MBs of Random Numbers Generated in a Second',fontweight='bold')

# Set the position of the x ticks
ax.set_xticks([p + 1.5 * width for p in pos])

# Set the labels for the x ticks
ax.set_xticklabels(['MacBook 2017','MacBook 2015','MacBook 2011','Ubuntu 18.04'])

# Setting the x-axis and y-axis limits
plt.xlim(min(pos)-width, max(pos)+width*4)
plt.ylim([0, max(df['Mersenne Twister'] + df['SPCG64'] + df['Xoroshiro 128+'] + df['Xorshift 128+'])] )

# Adding the legend and showing the plot
plt.legend(['Mersenne Twister', 'SPCG64', 'Xoroshiro 128+','Xorshift 128+'], loc='upper left')
plt.grid()
#plt.show()
plt.savefig('barchart_compare.png')
