import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from textwrap import wrap

r_data_df = pd.read_csv('./Shootout Data/Shootout_Mac2017.csv')
aishah_data_df = pd.read_csv('./Shootout Data/Shootout_Aishah_Mac2011.csv')
em_data_df = pd.read_csv('./Shootout Data/Shootout_Emily.csv')
agni_data_df = pd.read_csv('./Shootout Data/Shootout_Agni.csv')


r_data_mt = r_data_df['Mersenne Twister']
r_data_xoro = r_data_df['Xoroshiro 128+']
r_data_xorsh = r_data_df['Xorshift 128+']
r_data_spcg = r_data_df['SPCG64']

aishah_data_mt = aishah_data_df['Mersenne Twister']
aishah_data_xoro = aishah_data_df['Xoroshiro 128+']
aishah_data_xorsh = aishah_data_df['Xorshift 128+']
aishah_data_spcg = aishah_data_df['SPCG64']

em_data_mt = em_data_df['Mersenne Twister']
em_data_xoro = em_data_df['Xoroshiro 128+']
em_data_xorsh = em_data_df['Xorshift 128+']
em_data_spcg = em_data_df['SPCG64']

agni_data_mt = r_data_df['Mersenne Twister']
agni_data_xoro = r_data_df['Xoroshiro 128+']
agni_data_xorsh = r_data_df['Xorshift 128+']
agni_data_spcg = r_data_df['SPCG64']


mt_data_a = [r_data_mt.values]
mt_data_b = [em_data_mt.values]
mt_data_c = [aishah_data_mt.values]
mt_data_d = [agni_data_mt.values]

xoro_data_a = [r_data_xoro.values]
xoro_data_b = [em_data_xoro.values]
xoro_data_c = [aishah_data_xoro.values]
xoro_data_d = [agni_data_xoro.values]

xors_data_a = [r_data_xorsh.values]
xors_data_b = [em_data_xorsh.values]
xors_data_c = [aishah_data_xorsh.values]
xors_data_d = [agni_data_xorsh.values]

spcg_data_a = [r_data_spcg.values]
spcg_data_b = [em_data_spcg.values]
spcg_data_c = [aishah_data_spcg.values]
spcg_data_d = [agni_data_spcg.values]

all_data_a = [r_data_mt.values,r_data_xorsh.values,r_data_spcg.values,r_data_xoro.values ]
all_data_b = [em_data_mt.values,em_data_xorsh.values,em_data_spcg.values,em_data_xoro.values]
all_data_c = [aishah_data_mt.values,aishah_data_xorsh.values,aishah_data_spcg.values, aishah_data_xoro.values]
all_data_d = [agni_data_mt.values,agni_data_xorsh.values,agni_data_spcg.values ,agni_data_xoro.values]

#################### MT64

ticks = ["Mersenne Twister Algorithm"]

def set_box_color(bp, color):
    plt.setp(bp['boxes'], color=color)
    plt.setp(bp['whiskers'], color=color)
    plt.setp(bp['caps'], color=color)
    plt.setp(bp['medians'], color=color)

fig = plt.figure()

bpl = plt.boxplot(mt_data_c, positions=np.array(range(len(mt_data_c)))*2.0-1.2, sym='', widths=0.6)
bpr = plt.boxplot(mt_data_b, positions=np.array(range(len(mt_data_b)))*2.0-0.4, sym='', widths=0.6)
bps = plt.boxplot(mt_data_a, positions=np.array(range(len(mt_data_a)))*2.0+0.4, sym='', widths=0.6)
bpt = plt.boxplot(mt_data_d, positions=np.array(range(len(mt_data_d)))*2.0+1.2, sym='', widths=0.6)

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

plt.xticks(range(0, 0,1), ticks)
plt.xlim(-2, len(ticks)*2)
plt.ylim(1000, 2500)
plt.ylabel("MB/s",fontweight='bold')
plt.xlabel("Mersenne Twister Algorithm",fontweight='bold')
fig.suptitle("\n".join(wrap('Random Numbers Generated in One Second for the Mersenne Twister Algorithm Across Different Architectures', 60)), fontsize=10, fontweight='bold')
plt.savefig('./Shootout_Graphs/shootout_boxcompare_mt.png')

################### Xoroshiro

ticks = ['Xoroshiro']

fig = plt.figure()

bpl = plt.boxplot(xoro_data_a, positions=np.array(range(len(xoro_data_a)))*2.0-1.2, sym='', widths=0.6)
bpr = plt.boxplot(xoro_data_b, positions=np.array(range(len(xoro_data_b)))*2.0-0.4, sym='', widths=0.6)
bps = plt.boxplot(xoro_data_c, positions=np.array(range(len(xoro_data_c)))*2.0+0.4, sym='', widths=0.6)
bpt = plt.boxplot(xoro_data_d, positions=np.array(range(len(xoro_data_d)))*2.0+1.2, sym='', widths=0.6)

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

plt.xticks(range(0, 0,1), ticks)
plt.xlim(-2, len(ticks)*2)
plt.ylim(4000, 8000)
plt.ylabel("MB/s",fontweight='bold')
plt.xlabel("Xoroshiro 128+ Algorithm",fontweight='bold')
fig.suptitle("\n".join(wrap('Random Numbers Generated in One Second for the Xoroshiro 128+ Algorithm Across Different Architectures', 60)), fontsize=10, fontweight='bold')
plt.savefig('./Shootout_Graphs/shootout_boxcompare_xoroshiro.png')


################### Xorshift

ticks = ['Xorshift']

fig = plt.figure()

bpl = plt.boxplot(xors_data_c, positions=np.array(range(len(xors_data_c)))*2.0-1.2, sym='', widths=0.6)
bpr = plt.boxplot(xors_data_b, positions=np.array(range(len(xors_data_b)))*2.0-0.4, sym='', widths=0.6)
bps = plt.boxplot(xors_data_a, positions=np.array(range(len(xors_data_a)))*2.0+0.4, sym='', widths=0.6)
bpt = plt.boxplot(xors_data_d, positions=np.array(range(len(xors_data_d)))*2.0+1.2, sym='', widths=0.6)

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

plt.xticks(range(0, 0,1), ticks)
plt.xlim(-2, len(ticks)*2)
plt.ylim(4000, 8000)
plt.ylabel("MB/s",fontweight='bold')
plt.xlabel("Xorshift 128+ Algorithm",fontweight='bold')
fig.suptitle("\n".join(wrap('Random Numbers Generated in One Second for the Xorshift 128+ Algorithm Across Different Architectures', 60)), fontsize=10, fontweight='bold')
plt.savefig('./Shootout_Graphs/shootout_boxcompare_xorshift.png')

################### SPCG64

ticks = ['SPCG64']

fig = plt.figure()

bpl = plt.boxplot(spcg_data_c, positions=np.array(range(len(spcg_data_c)))*2.0-1.2, sym='', widths=0.6)
bpr = plt.boxplot(spcg_data_b, positions=np.array(range(len(spcg_data_b)))*2.0-0.4, sym='', widths=0.6)
bps = plt.boxplot(spcg_data_a, positions=np.array(range(len( spcg_data_a)))*2.0+0.4, sym='', widths=0.6)
bpt = plt.boxplot(spcg_data_d, positions=np.array(range(len(spcg_data_d)))*2.0+1.2, sym='', widths=0.6)

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

plt.xticks(range(0, 0,1), ticks)
plt.xlim(-2, len(ticks)*2)
plt.ylim(2000, 6000)
plt.ylabel("MB/s",fontweight='bold')
plt.xlabel("SPCG64 Algorithm",fontweight='bold')
fig.suptitle("\n".join(wrap('Random Numbers Generated in One Second for the SPCG 64 Algorithm Across Different Architectures', 60)), fontsize=10, fontweight='bold')
plt.savefig('./Shootout_Graphs/shootout_boxcompare_spcg64.png')


##################### All Together

ticks = ['MT','Xorshift', 'SPCG64', 'Xoroshiro']

def set_box_color(bp, color):
    plt.setp(bp['boxes'], color=color)
    plt.setp(bp['whiskers'], color=color)
    plt.setp(bp['caps'], color=color)
    plt.setp(bp['medians'], color=color)

fig = plt.figure(figsize=(10,5))

bpl = plt.boxplot(all_data_c, positions=np.array(range(0, len(ticks) * 7,7)), sym='', widths=0.6)
bpr = plt.boxplot(all_data_b, positions=np.array(range(0, len(ticks) * 7,7))+1, sym='', widths=0.6)
bps = plt.boxplot( all_data_a, positions=np.array(range(0, len(ticks) * 7,7))+2, sym='', widths=0.6)
bpt = plt.boxplot(all_data_d, positions=np.array(range(0, len(ticks) * 7,7))+3, sym='', widths=0.6)

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

plt.xticks(range(2, len(ticks) * 7,7), ticks)
plt.xlim(-2, len(ticks)*6+2)
plt.ylim(0, 9000)
plt.ylabel("MB/s",fontweight='bold')
plt.xlabel("Random Number Generators",fontweight='bold')
fig.suptitle("\n".join(wrap('Random Numbers Generated in One Second Across Different Architectures', 60)), fontsize=10, fontweight='bold')
#plt.tight_layout()
plt.savefig('./Shootout_Graphs/shootout_boxcompare_all.png')

