# Testing PRNGS Across Different Architectures
A repository for our architecture group team

## Problem and Motivation
Problem and Motivation text

## Literature Review
Lit Review text

## Our Solution
Solution text

## Experimental Setup
Experimental Setup text and table

## Evaluation
### Dieharder Results
Dieharder results (text and table)

### Shootout Results
In addition to the dieharder suite, we also used a tool "shootout" to test the speed of our chosen PRNGs. It was written by Chris Wellons and can be found here. This tool takes each PRNG and records the amount of random numbers generated in one second, measured in MB. We ran this tool 30 times on each architecture (Mac 2011, Mac 2015, Mac 2017, Ubuntu 18.04) and recorder the value for all four algorithms (Mersenne Twister, Xorshift 128+, SPCG 64, and Xoroshiro 128+). Our expectations are that we will see higher MBs generated per second for 

Graphs looking at all the results
<img src="Graphing/Shootout_Graphs/shootout_boxcompare_all.png" alt="hi" class="inline"/>
<img src="Graphing/barchart_compare.png" alt="hi" class="inline"/>

<img src="Graphing/Shootout_Graphs/shootout_boxcompare_mt.png" alt="hi" width="425"/> <img src="Graphing/Shootout_Graphs/shootout_boxcompare_xorshift.png" alt="hi" width="425"/>
<img src="Graphing/Shootout_Graphs/shootout_boxcompare_spcg64.png" alt="hi" width="425"/><img src="Graphing/Shootout_Graphs/shootout_boxcompare_xoroshiro.png" alt="hi" width="425"/>


### 1,5,10 Million Results

Graphs showing comparison of architecture

<img src="Graphing/10_Runs_Graphs/mt64_boxcompare.png" alt="hi" width="425"/> <img src="Graphing/10_Runs_Graphs/xorshift_boxcompare.png" alt="hi" width="425"/> 
<img src="Graphing/10_Runs_Graphs/spcg_boxcompare.png" alt="hi" width="425"/> <img src="Graphing/10_Runs_Graphs/xoroshiro_boxcompare.png" alt="hi" width="425"/> 

Graphs showing comparison of algorithms

<img src="Graphing/10_Runs_Graphs/mac2011_boxcompare.png" alt="hi" width="425"/> <img src="Graphing/10_Runs_Graphs/mac2015_boxcompare.png" alt="hi" width="425"/> 
<img src="Graphing/10_Runs_Graphs/mac2017_boxcompare.png" alt="hi" width="425"/> <img src="Graphing/10_Runs_Graphs/ubuntu1804_boxcompare.png" alt="hi" width="425"/> 

## Discussion/Results
Our discussion of the graphs and results

## Threats to Validity
I think we should add in this section, since it will be public

## Future Work
Future work

## Challenges
List some of our challenges or challenges that people might run into 

## References
Our references















# Examples
## How to put in Image
<img src="Graphing/barchart_compare.png" alt="hi" class="inline"/>

## Subtitle
Some stuff
### Sub Subtitle
More stuff
#### Sub Sub Sub Title
```
Give an example
```
## This is how you do a list
* Item 1
* Item 2
* Item 3

This is how you do **bold** and this is how you do *italics*
[Web link](https://rachelkraft.github.io/ArchProjTeam1/)
