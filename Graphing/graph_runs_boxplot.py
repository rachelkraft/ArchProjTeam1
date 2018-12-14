import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from textwrap import wrap

rachel_spcg_data_df = pd.read_csv('./10_runs_data/Rachel_SPCG_Mac_2017.csv')
rachel_xorshift_data_df = pd.read_csv('./10_runs_data/Rachel_Xorshift_Mac_2017.csv')
rachel_xoroshiro_data_df = pd.read_csv('./10_runs_data/Rachel_Xoro_Mac_2017.csv')
rachel_mt64_data_df = pd.read_csv('./10_runs_data/Rachel_MT_Mac_2017.csv')

emily_spcg_data_df = pd.read_csv('./10_runs_data/emily_macbook_spcg_time.csv')
emily_xorshift_data_df = pd.read_csv('./10_runs_data/emily_macbook_xorshift_time.csv')
emily_xoroshiro_data_df = pd.read_csv('./10_runs_data/emily_macbook_xoroshiro128plus_time.csv')
emily_mt64_data_df = pd.read_csv('./10_runs_data/emily_macbook_mt64_time.csv')

agni_spcg_data_df = pd.read_csv('./10_runs_data/Agni_SPCG64_Ubuntu_1804.csv')
agni_xorshift_data_df = pd.read_csv('./10_runs_data/Agni_XorShift128P_Ubuntu_1804.csv')
agni_xoroshiro_data_df = pd.read_csv('./10_runs_data/Agni_XoroShiro128P_Ubuntu_1804.csv')
agni_mt64_data_df = pd.read_csv('./10_runs_data/Agni_MT64_Ubuntu_1804.csv')

aishah_spcg_data_df = pd.read_csv('./10_runs_data/Aishah_spcg_Mac_2011.csv')
aishah_xorshift_data_df = pd.read_csv('./10_runs_data/Aishah_XorShift_Mac_2011.csv')
aishah_xoroshiro_data_df = pd.read_csv('./10_runs_data/Aishah_Xoroshiro_Mac_2011.csv')
aishah_mt64_data_df = pd.read_csv('./10_runs_data/Aishah_MT_Mac_2011.csv')


################################## SPCG ################################

spcg_r_data =[rachel_spcg_data_df['1M'],rachel_spcg_data_df['5M'],rachel_spcg_data_df['10M']]
spcg_em_data =[emily_spcg_data_df['1M'],emily_spcg_data_df['5M'],emily_spcg_data_df['10M']]
spcg_aishah_data =[aishah_spcg_data_df['1M'],aishah_spcg_data_df['5M'],aishah_spcg_data_df['10M']]
spcg_agni_data =[agni_spcg_data_df['1M'],agni_spcg_data_df['5M'],agni_spcg_data_df['10M']]

ticks = ['1 million','5 million','10 million']

def set_box_color(bp, color):
    plt.setp(bp['boxes'], color=color)
    plt.setp(bp['whiskers'], color=color)
    plt.setp(bp['caps'], color=color)
    plt.setp(bp['medians'], color=color)

fig = plt.figure(figsize=(9,5))

bpl = plt.boxplot(spcg_aishah_data, positions=np.array(range(0, len(ticks) * 7,7)), sym='', widths=0.6)
bpr = plt.boxplot(spcg_em_data, positions=np.array(range(0, len(ticks) * 7,7))+1, sym='', widths=0.6)
bps = plt.boxplot(spcg_r_data, positions=np.array(range(0, len(ticks) * 7,7))+2, sym='', widths=0.6)
bpt = plt.boxplot(spcg_agni_data, positions=np.array(range(0, len(ticks) * 7,7))+3, sym='', widths=0.6)

set_box_color(bpl, '#D7191C') # colors are from http://colorbrewer2.org/
set_box_color(bpr, '#2C7BB6')
set_box_color(bps, '#2CA25F')
set_box_color(bpt, '#756BB1')

# draw temporary red and blue lines and use them to create a legend
plt.plot([], c='#D7191C', label='MacBook 2011')
plt.plot([], c='#2C7BB6', label='MacBook 2015')
plt.plot([], c='#2CA25F', label='MacBook 2017')
plt.plot([], c='#756BB1', label='Ubuntu 18.04')
plt.legend()

plt.xticks(range(2, len(ticks) * 7, 7), ticks)
plt.xlim(-2, len(ticks)*7)
plt.ylim(0, 3200000)
plt.ylabel("Time in Microseconds (µs)",fontweight='bold')
plt.xlabel("Amount of Random Numbers Generated",fontweight='bold')
fig.suptitle("\n".join(wrap('Time to Generate Random Numbers with SPCG64 Across Different Architectures', 60)), fontsize=10, fontweight='bold')
plt.savefig('./10_Runs_Graphs/spcg_boxcompare.png')


################################# Mersenne Twister ######################################

mt64_r_data =[rachel_mt64_data_df['1M'],rachel_mt64_data_df['5M'],rachel_mt64_data_df['10M']]
mt64_em_data =[emily_mt64_data_df['1M'],emily_mt64_data_df['5M'],emily_mt64_data_df['10M']]
mt64_aishah_data =[aishah_mt64_data_df['1M'],aishah_mt64_data_df['5M'],aishah_mt64_data_df['10M']]
mt64_agni_data =[agni_mt64_data_df['1M'],agni_mt64_data_df['5M'],agni_mt64_data_df['10M']]

ticks = ['1 million','5 million','10 million']

def set_box_color(bp, color):
    plt.setp(bp['boxes'], color=color)
    plt.setp(bp['whiskers'], color=color)
    plt.setp(bp['caps'], color=color)
    plt.setp(bp['medians'], color=color)

fig = plt.figure(figsize=(9,5))

bpl = plt.boxplot(mt64_aishah_data, positions=np.array(range(0, len(ticks) * 7,7)), sym='', widths=0.6)
bpr = plt.boxplot(mt64_em_data, positions=np.array(range(0, len(ticks) * 7,7))+1, sym='', widths=0.6)
bps = plt.boxplot(mt64_r_data, positions=np.array(range(0, len(ticks) * 7,7))+2, sym='', widths=0.6)
bpt = plt.boxplot(mt64_agni_data, positions=np.array(range(0, len(ticks) * 7,7))+3, sym='', widths=0.6)

set_box_color(bpl, '#D7191C') # colors are from http://colorbrewer2.org/
set_box_color(bpr, '#2C7BB6')
set_box_color(bps, '#2CA25F')
set_box_color(bpt, '#756BB1')

# draw temporary red and blue lines and use them to create a legend
plt.plot([], c='#D7191C', label='MacBook 2011')
plt.plot([], c='#2C7BB6', label='MacBook 2015')
plt.plot([], c='#2CA25F', label='MacBook 2017')
plt.plot([], c='#756BB1', label='Ubuntu 18.04')
plt.legend()

plt.xticks(range(2, len(ticks) * 7, 7), ticks)
plt.xlim(-2, len(ticks)*7)
plt.ylim(0, 3200000)
plt.ylabel("Time in Microseconds (µs)",fontweight='bold')
plt.xlabel("Amount of Random Numbers Generated",fontweight='bold')
fig.suptitle("\n".join(wrap('Time to Generate Random Numbers with Mersenne Twister Across Different Architectures', 60)), fontsize=10, fontweight='bold')
plt.savefig('./10_Runs_Graphs/mt64_boxcompare.png')


################################# Xoroshiro 128+ ######################################

xoroshiro_r_data =[rachel_xoroshiro_data_df['1M'],rachel_xoroshiro_data_df['5M'],rachel_xoroshiro_data_df['10M']]
xoroshiro_em_data =[emily_xoroshiro_data_df['1M'],emily_xoroshiro_data_df['5M'],emily_xoroshiro_data_df['10M']]
xoroshiro_aishah_data =[aishah_xoroshiro_data_df['1M'],aishah_xoroshiro_data_df['5M'],aishah_xoroshiro_data_df['10M']]
xoroshiro_agni_data =[agni_xoroshiro_data_df['1M'],agni_xoroshiro_data_df['5M'],agni_xoroshiro_data_df['10M']]

ticks = ['1 million','5 million','10 million']

def set_box_color(bp, color):
    plt.setp(bp['boxes'], color=color)
    plt.setp(bp['whiskers'], color=color)
    plt.setp(bp['caps'], color=color)
    plt.setp(bp['medians'], color=color)

fig = plt.figure(figsize=(9,5))

bpl = plt.boxplot(xoroshiro_aishah_data, positions=np.array(range(0, len(ticks) * 7,7)), sym='', widths=0.6)
bpr = plt.boxplot(xoroshiro_em_data, positions=np.array(range(0, len(ticks) * 7,7))+1, sym='', widths=0.6)
bps = plt.boxplot(xoroshiro_r_data, positions=np.array(range(0, len(ticks) * 7,7))+2, sym='', widths=0.6)
bpt = plt.boxplot(xoroshiro_agni_data, positions=np.array(range(0, len(ticks) * 7,7))+3, sym='', widths=0.6)

set_box_color(bpl, '#D7191C') # colors are from http://colorbrewer2.org/
set_box_color(bpr, '#2C7BB6')
set_box_color(bps, '#2CA25F')
set_box_color(bpt, '#756BB1')

# draw temporary red and blue lines and use them to create a legend
plt.plot([], c='#D7191C', label='MacBook 2011')
plt.plot([], c='#2C7BB6', label='MacBook 2015')
plt.plot([], c='#2CA25F', label='MacBook 2017')
plt.plot([], c='#756BB1', label='Ubuntu 18.04')
plt.legend()

plt.xticks(range(2, len(ticks) * 7, 7), ticks)
plt.xlim(-2, len(ticks)*7)
plt.ylim(0, 3200000)
plt.ylabel("Time in Microseconds (µs)",fontweight='bold')
plt.xlabel("Amount of Random Numbers Generated",fontweight='bold')
fig.suptitle("\n".join(wrap('Time to Generate Random Numbers with Xoroshiro 128+ Across Different Architectures', 60)), fontsize=10, fontweight='bold')
plt.savefig('./10_Runs_Graphs/xoroshiro_boxcompare.png')


################################# Xoroshiro 128+ ######################################

xorshift_r_data =[rachel_xorshift_data_df['1M'],rachel_xorshift_data_df['5M'],rachel_xorshift_data_df['10M']]
xorshift_em_data =[emily_xorshift_data_df['1M'],emily_xorshift_data_df['5M'],emily_xorshift_data_df['10M']]
xorshift_aishah_data =[aishah_xorshift_data_df['1M'],aishah_xorshift_data_df['5M'],aishah_xorshift_data_df['10M']]
xorshift_agni_data =[agni_xorshift_data_df['1M'],agni_xorshift_data_df['5M'],agni_xorshift_data_df['10M']]

ticks = ['1 million','5 million','10 million']

def set_box_color(bp, color):
    plt.setp(bp['boxes'], color=color)
    plt.setp(bp['whiskers'], color=color)
    plt.setp(bp['caps'], color=color)
    plt.setp(bp['medians'], color=color)

fig = plt.figure(figsize=(9,5))

bpl = plt.boxplot(xorshift_aishah_data, positions=np.array(range(0, len(ticks) * 7,7)), sym='', widths=0.6)
bpr = plt.boxplot(xorshift_em_data, positions=np.array(range(0, len(ticks) * 7,7))+1, sym='', widths=0.6)
bps = plt.boxplot(xorshift_r_data, positions=np.array(range(0, len(ticks) * 7,7))+2, sym='', widths=0.6)
bpt = plt.boxplot(xorshift_agni_data, positions=np.array(range(0, len(ticks) * 7,7))+3, sym='', widths=0.6)

set_box_color(bpl, '#D7191C') # colors are from http://colorbrewer2.org/
set_box_color(bpr, '#2C7BB6')
set_box_color(bps, '#2CA25F')
set_box_color(bpt, '#756BB1')

# draw temporary red and blue lines and use them to create a legend
plt.plot([], c='#D7191C', label='MacBook 2011')
plt.plot([], c='#2C7BB6', label='MacBook 2015')
plt.plot([], c='#2CA25F', label='MacBook 2017')
plt.plot([], c='#756BB1', label='Ubuntu 18.04')
plt.legend()

plt.xticks(range(2, len(ticks) * 7, 7), ticks)
plt.xlim(-2, len(ticks)*7)
plt.ylim(0, 3200000)
plt.ylabel("Time in Microseconds (µs)",fontweight='bold')
plt.xlabel("Amount of Random Numbers Generated",fontweight='bold')
fig.suptitle("\n".join(wrap('Time to Generate Random Numbers with Xorshift 128+ Across Different Architectures', 60)), fontsize=10, fontweight='bold')
plt.savefig('./10_Runs_Graphs/xorshift_boxcompare.png')



######################## ARCHITECTURES #################################


############################################## MAC 2017 ##############################################

mt64_r_data =[rachel_mt64_data_df['1M'],rachel_mt64_data_df['5M'],rachel_mt64_data_df['10M']]
xorshift_r_data =[rachel_xorshift_data_df['1M'],rachel_xorshift_data_df['5M'],rachel_xorshift_data_df['10M']]
spcg_r_data =[rachel_spcg_data_df['1M'],rachel_spcg_data_df['5M'],rachel_spcg_data_df['10M']]
xoroshiro_r_data =[rachel_xoroshiro_data_df['1M'],rachel_xoroshiro_data_df['5M'],rachel_xoroshiro_data_df['10M']]

ticks = ['1 million','5 million','10 million']

def set_box_color(bp, color):
    plt.setp(bp['boxes'], color=color)
    plt.setp(bp['whiskers'], color=color)
    plt.setp(bp['caps'], color=color)
    plt.setp(bp['medians'], color=color)

fig = plt.figure(figsize=(9,5))

bpl = plt.boxplot(mt64_r_data, positions=np.array(range(0, len(ticks) * 7,7)), sym='', widths=0.6)
bpr = plt.boxplot(xorshift_r_data, positions=np.array(range(0, len(ticks) * 7,7))+1, sym='', widths=0.6)
bps = plt.boxplot(spcg_r_data, positions=np.array(range(0, len(ticks) * 7,7))+2, sym='', widths=0.6)
bpt = plt.boxplot(xoroshiro_r_data, positions=np.array(range(0, len(ticks) * 7,7))+3, sym='', widths=0.6)

set_box_color(bpl, '#FFC300') # colors are from http://colorbrewer2.org/
set_box_color(bpr, '#FF5733')
set_box_color(bps, '#8A33FF')
set_box_color(bpt, '#339CFF')

# draw temporary red and blue lines and use them to create a legend
plt.plot([], c='#FFC300', label='Mersenne Twister')
plt.plot([], c='#FF5733', label='Xorshift 128+')
plt.plot([], c='#8A33FF', label='SPCG 64')
plt.plot([], c='#339CFF', label='Xoroshiro 128+')
plt.legend()

plt.xticks(range(2, len(ticks) * 7, 7), ticks)
plt.xlim(-2, len(ticks)*7)
plt.ylim(0, 3200000)
plt.ylabel("Time in Microseconds (µs)",fontweight='bold')
plt.xlabel("Amount of Random Numbers Generated",fontweight='bold')
fig.suptitle("\n".join(wrap('Time to Generate Random Numbers For Different PRNGs on a MacBook 2017', 60)), fontsize=10, fontweight='bold')
plt.savefig('./10_Runs_Graphs/mac2017_boxcompare.png')

############################################## Ubuntu 18.04 ##############################################

mt64_agni_data =[agni_mt64_data_df['1M'],agni_mt64_data_df['5M'],agni_mt64_data_df['10M']]
xorshift_agni_data =[agni_xorshift_data_df['1M'],agni_xorshift_data_df['5M'],agni_xorshift_data_df['10M']]
spcg_agni_data =[agni_spcg_data_df['1M'],agni_spcg_data_df['5M'],agni_spcg_data_df['10M']]
xoroshiro_agni_data =[agni_xoroshiro_data_df['1M'],agni_xoroshiro_data_df['5M'],agni_xoroshiro_data_df['10M']]

ticks = ['1 million','5 million','10 million']

def set_box_color(bp, color):
    plt.setp(bp['boxes'], color=color)
    plt.setp(bp['whiskers'], color=color)
    plt.setp(bp['caps'], color=color)
    plt.setp(bp['medians'], color=color)

fig = plt.figure(figsize=(9,5))

bpl = plt.boxplot(mt64_agni_data, positions=np.array(range(0, len(ticks) * 7,7)), sym='', widths=0.6)
bpr = plt.boxplot(xorshift_agni_data, positions=np.array(range(0, len(ticks) * 7,7))+1, sym='', widths=0.6)
bps = plt.boxplot(spcg_agni_data, positions=np.array(range(0, len(ticks) * 7,7))+2, sym='', widths=0.6)
bpt = plt.boxplot(xoroshiro_agni_data, positions=np.array(range(0, len(ticks) * 7,7))+3, sym='', widths=0.6)

set_box_color(bpl, '#FFC300') # colors are from http://colorbrewer2.org/
set_box_color(bpr, '#FF5733')
set_box_color(bps, '#8A33FF')
set_box_color(bpt, '#339CFF')

# draw temporary red and blue lines and use them to create a legend
plt.plot([], c='#FFC300', label='Mersenne Twister')
plt.plot([], c='#FF5733', label='Xorshift 128+')
plt.plot([], c='#8A33FF', label='SPCG 64')
plt.plot([], c='#339CFF', label='Xoroshiro 128+')
plt.legend()

plt.xticks(range(2, len(ticks) * 7, 7), ticks)
plt.xlim(-2, len(ticks)*7)
plt.ylim(0, 3200000)
plt.ylabel("Time in Microseconds (µs)",fontweight='bold')
plt.xlabel("Amount of Random Numbers Generated",fontweight='bold')
fig.suptitle("\n".join(wrap('Time to Generate Random Numbers For Different PRNGs on Ubuntu 18.04', 60)), fontsize=10, fontweight='bold')
plt.savefig('./10_Runs_Graphs/ubuntu1804_boxcompare.png')

############################################## Mac 2011 ##############################################

mt64_aishah_data =[aishah_mt64_data_df['1M'],aishah_mt64_data_df['5M'],aishah_mt64_data_df['10M']]
xorshift_aishah_data =[aishah_xorshift_data_df['1M'],aishah_xorshift_data_df['5M'],aishah_xorshift_data_df['10M']]
spcg_aishah_data =[aishah_spcg_data_df['1M'],aishah_spcg_data_df['5M'],aishah_spcg_data_df['10M']]
xoroshiro_aishah_data =[aishah_xoroshiro_data_df['1M'],aishah_xoroshiro_data_df['5M'],aishah_xoroshiro_data_df['10M']]

ticks = ['1 million','5 million','10 million']

def set_box_color(bp, color):
    plt.setp(bp['boxes'], color=color)
    plt.setp(bp['whiskers'], color=color)
    plt.setp(bp['caps'], color=color)
    plt.setp(bp['medians'], color=color)

fig = plt.figure(figsize=(9,5))

bpl = plt.boxplot(mt64_aishah_data, positions=np.array(range(0, len(ticks) * 7,7)), sym='', widths=0.6)
bpr = plt.boxplot(xorshift_aishah_data, positions=np.array(range(0, len(ticks) * 7,7))+1, sym='', widths=0.6)
bps = plt.boxplot(spcg_aishah_data, positions=np.array(range(0, len(ticks) * 7,7))+2, sym='', widths=0.6)
bpt = plt.boxplot(xoroshiro_aishah_data, positions=np.array(range(0, len(ticks) * 7,7))+3, sym='', widths=0.6)

set_box_color(bpl, '#FFC300') # colors are from http://colorbrewer2.org/
set_box_color(bpr, '#FF5733')
set_box_color(bps, '#8A33FF')
set_box_color(bpt, '#339CFF')

# draw temporary red and blue lines and use them to create a legend
plt.plot([], c='#FFC300', label='Mersenne Twister')
plt.plot([], c='#FF5733', label='Xorshift 128+')
plt.plot([], c='#8A33FF', label='SPCG 64')
plt.plot([], c='#339CFF', label='Xoroshiro 128+')
plt.legend()

plt.xticks(range(2, len(ticks) * 7, 7), ticks)
plt.xlim(-2, len(ticks)*7)
plt.ylim(0, 3200000)
plt.ylabel("Time in Microseconds (µs)",fontweight='bold')
plt.xlabel("Amount of Random Numbers Generated",fontweight='bold')
fig.suptitle("\n".join(wrap('Time to Generate Random Numbers For Different PRNGs on a MacBook 2011', 60)), fontsize=10, fontweight='bold')
plt.savefig('./10_Runs_Graphs/mac2011_boxcompare.png')

############################################## Mac 2015 ##############################################

mt64_em_data =[emily_mt64_data_df['1M'],emily_mt64_data_df['5M'],emily_mt64_data_df['10M']]
xorshift_em_data =[emily_xorshift_data_df['1M'],emily_xorshift_data_df['5M'],emily_xorshift_data_df['10M']]
spcg_em_data =[emily_spcg_data_df['1M'],emily_spcg_data_df['5M'],emily_spcg_data_df['10M']]
xoroshiro_em_data =[emily_xoroshiro_data_df['1M'],emily_xoroshiro_data_df['5M'],emily_xoroshiro_data_df['10M']]

ticks = ['1 million','5 million','10 million']

def set_box_color(bp, color):
    plt.setp(bp['boxes'], color=color)
    plt.setp(bp['whiskers'], color=color)
    plt.setp(bp['caps'], color=color)
    plt.setp(bp['medians'], color=color)

fig = plt.figure(figsize=(9,5))

bpl = plt.boxplot(mt64_em_data, positions=np.array(range(0, len(ticks) * 7,7)), sym='', widths=0.6)
bpr = plt.boxplot(xorshift_em_data, positions=np.array(range(0, len(ticks) * 7,7))+1, sym='', widths=0.6)
bps = plt.boxplot(spcg_em_data, positions=np.array(range(0, len(ticks) * 7,7))+2, sym='', widths=0.6)
bpt = plt.boxplot(xoroshiro_em_data, positions=np.array(range(0, len(ticks) * 7,7))+3, sym='', widths=0.6)

set_box_color(bpl, '#FFC300') # colors are from http://colorbrewer2.org/
set_box_color(bpr, '#FF5733')
set_box_color(bps, '#8A33FF')
set_box_color(bpt, '#339CFF')

# draw temporary red and blue lines and use them to create a legend
plt.plot([], c='#FFC300', label='Mersenne Twister')
plt.plot([], c='#FF5733', label='Xorshift 128+')
plt.plot([], c='#8A33FF', label='SPCG 64')
plt.plot([], c='#339CFF', label='Xoroshiro 128+')
plt.legend()

plt.xticks(range(2, len(ticks) * 7, 7), ticks)
plt.xlim(-2, len(ticks)*7)
plt.ylim(0, 3200000)
plt.ylabel("Time in Microseconds (µs)",fontweight='bold')
plt.xlabel("Amount of Random Numbers Generated",fontweight='bold')
fig.suptitle("\n".join(wrap('Time to Generate Random Numbers For Different PRNGs on a MacBook 2015', 60)), fontsize=10, fontweight='bold')
plt.savefig('./10_Runs_Graphs/mac2015_boxcompare.png')

