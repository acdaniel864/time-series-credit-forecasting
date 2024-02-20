# Credit Catastrophe or Consultancy
### Project 5 by Aaran Daniel, Steven Goulden, and Bejamin Wolff for General Assembly's DSI
Due: Tuesday, February 20th, 2024 at 9 AM ET

## Table of Contents

## Problem Statement

In such turbulent times when nothing is sure anymore, one's credit solvency is definitely at the top of the list. A well established credit agency in the USA reached out to our consulting firm (fict.) to explore trends in the market and try to identify factors that contribute to delinquency rates (people not paying their bills timely) and credit growth (annual percentage change in outstanding bank loans). Afterwards, the agency asked to forecast expected rates for at least a year into the future, to get a gauge of what to expect. Finally, any seasonal or other cyclical trends that may be useful to discover or confirm about the financial cycle would be desired to be seen as well.

So, bottom line we hope to answer when are 'good times' for the producer to lend openly with little risk?

Banks and policy makers are the designated audience for this study, putting a heavy emphasis on simplicity with any of the upcoming explorations and forecasting.

## Executive Summary
For the sake of simplicity regading the General Assembly project, it was decided to itemize each participant's work and write their own executive summary.

### Executive Summary - Aaran Daniel
#### Technology: 
pandas, lumpy, matplotlib, seaboard, sys, scikit-learn, pmdarima, statsmodels
#### Data:
From St Louis Fed, fred.stlouisfed.org: Fed Funds rate monthly, nominal GDP,
#### Cleaning:
Cleaned data from Bureau of Labour Statistics, plotting distributions
Cleaned Bureau of Economic Analysis data which contained monthly information on income, tax, benefits and savings for the US economy wide.
Cleaned credit card delinquency, credit card balances and 30 year mortgage data.
Cleaned FRB monthly consumer credit data.
Combined all the above into one master data frame.
#### EDA:
Understanding the economic context: inflation, credit, disposable income:
CPI slightly left skewed, centred around mean of 2.53%, slightly above FED target of 2%.
GDP annual 4.37% average. Range of -6.9 to 17%. Huge fall in GDP growth in the wake of covid then a recovery mid 2020 through to early 2021.
FedFunds rate median 1% - the ‘zerp era’ - max of 5.98% observed in the time period analysed.
Early 2022 fed begins to hike rates to highs not seen since the 2008 crisis.
Median annual disposable income of $41,000 (chained 2017)

### Executive Summary - Steven Goulden
#### Technology:
pandas, lumpy, matplotlib, seaboard, sys, scikit-learn, pmdarima, statsmodels
#### Data Collection:
We primarily used US government economic data from the following sources.
- Bureau of Labour Statistics (bls.gov)
- Bureau of Economic Analysis (bea.gov)
- New York Fed
- St Louis Fed/ Federal Reserve Economic Data
- Fed Reserve Board
The data was reliable and clean, but much of it was only available on a quarterly basis and given the relatively short length of available data (post 2000), we had to use monthly data in order to have a sufficiently large dataset. As such, we had to interpolate (ie create entries from Q1 to Q2 using April = March + ((Q2-Q1)/3) between quarterly data to create monthly comparable entries.
We used the BLS and BEA API and manually downloaded the data from the NY and St Louis Fed manually in csv format.
#### EDA
- We then looked at credit growth against CPI and its key components and it was interesting to see a clear positive correlation. This made broad intuitive sense as credit generally grows during periods of economic expansion, when inflation tends to be higher.
[credit_vs_cpi.png]
- We then looked at some scatter charts of credit growth versus 1) unemployment, which was negatively correlated, as one would expect (people do not tend to borrow more during recessions, or at least credit is not available) and 2) the savings rate, which showed a weak negative relationship. This was largely impacted by the COVID period, during which time personal savings rate spiked (as people were not spending), but other that that the savings rate tended to be fails stable at 2-10%, with clustering around the 4-6% level. Similarly, annual credit growth tended to be clustered in the 4-8% range, slightly ahead of nominal GDP, which broadly makes sense. This was evident in the histograms for both features.
[credit_hist.png]
- We then used domain knowledge to select a relevant feature set and looked at a pair grid and correlation matrix. As expected, inflation was heavily linked to credit growth, and interestingly far more so than employee compensation. Also, medical care generally had a negative correlation with credit growth. We removed energy as it was highly correlated with gasoline.
[correl_chart.png]
#### Modelling
- We then built our first model to predict credit growth and for Lasso and Ridge linear regression and achieved a cross validation score of 0.5, with random forests achieving 0.83 and SVR achieving 0.89
- We can see that as credit card rates have been rising over the last 10 years, this in conjunction with higher balances has driven a significant increase in annual credit card servicing costs. The same can be said for mortgage servicing costs.
[credit_card_servicing.png]
- We then built a model to predict delinquent credit, as defined by 30 and 90 days late. We could predict this from current macro data with a cross val score of 0.86 on current data, using random forests.
- But the aim was to be able to predict 6 or 12 months forward so that the credit card company would know when growth was picking up but also would be able to identify low quality growth, ie periods of worsening credit quality.
- We achieved the best results with SVR, with a cross val score of 0.82 for 12m forward 30 day delinquencies and 0.83 for 12m forward credit growth.
[SVR_yoy_credit.png] [SVR_12m_30day.png]
- Based on July data, which was the last date in our data set, the model predicted a decline in credit growth to 4.3% (from 4.9%) and 30 day delinquencies to 2.34% (from 3.2%) in July 2024.
- We also used PCA for dimensionality reduction given there were relatively limited rows. This made little difference to our delinquency model but resulted in a far worse credit growth model
- Lastly we tried to create a metric for good vs bad credit growth. The point being that a credit card company would ideally like to expand credit into an environment of growth in credit and declining 30/90 day delinquencies.¶
- Overall, we can see that delinquencies tend to grow during times of credit, with something of a lag and so it is very difficult, if not impossible to identify periods of 'good' credit growth.
[good_bad_credit.png]
- With more work we could analyse the profitability of expansion, despite worsening credit, because the company is currently charging rates of over 20% and so an incremental 1% charge off likely makes good business sense. With that analysis, we could decide how to allocate credit most effectively, in terms of deciding what would be profitable lending, on a case by case, or perhaps group by group basis. This would probably be an interetsing use case for k-means clustering or DB-SCAN, if we had customer level data.
- Lastly, we did some SHAP analysis to understand the impact of individual features. What stood out was the importance of credit card payment growth on delinquent credit, along with the negative impact of earnings growth. CPI tended to go hand in hand with worse credit, as we saw earlier as CPI correlates well to credit growth, which generally leads worsening credit standards
[credit_30d_shap]
- For credit growth, the SHAP analysis showed that wage and price inflation were the major drivers.
["images/credit_growth_shap.png”]


### Executive Summary - Benjamin Wolff
#### Technology Requirements
BW ran the following versions of packages:
Maplotlib 3.7.2
Numpy 1.24.3
Pandas 2.0.3
Pmdarima 2.0.4
Scikit-learn 1.3.0
Seaborn 0.12.2
Statsmodels 0.14.0
#### Data
BW used data from the Bureau of Labour Statistics, Bureau of Economic Analysis, New York Fed, St. Louis Fed, and the Federal Reserve Board.
The main 'cleaning' BW was involved in from a data perspecive was trying to ensure that quarterly data remained distinct from monthly data, feeling it disengious and straying from the original data science project to linearly interpoltate between quarterly dates to theoetically get a more robust dataset. However, such changes are local to the relevant notebook.
#### EDA
Of worthiness for an Executive Summary is limited to BW's 'eda_i.ipynb'. Principal findngs include the following:
- Around 30 feature' are highly postively correlated with each other (2 of whom are negative; rest positive), being defined with a correlation of at least .5. This would imply an overwhelming 'dominoe effect' of one thing to fall after another. With out current analysis it is too pre-mature to focus on one 'cause' feature, if there is one at all.
- The major focus of BW was spent on trying to analyize delinquency rates. Astonishngly, aside from the 30 and 90 day rates being incredibly close together (.96; which makes sense, basically suggesting that people that don't pay off their bills within 30 days probably still won't have them paid in 90 days), only one other feature was found to be significant (see above) - the yoy car consumption rate (interestingly negative). Another close second, being below the threshold for significant, was a federal funds rate at .48. Despite attempts to transform the data via root or logistic relationships, trends remained the same. So, it emerged that basically all features have nothing to do with delinquency rates (see below for more on this).
#### Modeling
BW focused on modeling delinquency rates, 30 and 90, with SARIMAX models, with the accompanying work found in his 'modeling_ii.ipynb'. Without even the presence of any exogenous (outside) variabls besides the flow of time and the delinquent rates, models were found to be accurate within .014 and .0218 of the mean absolute percentage error of the actual delinquency rates and later visually confirmed for accuracy.
Attempts were made to try to improve their accuracy by the addition of exogenous features (external features to our target that still effect its performance over time). However, no feature within the current dataset was found to be significant to further understanding of delinquency rate change. The bright side, however, is that this was already hinted at by the EDA stage when essentially no significant correlation the delinquents had with the numerous features.
-Perplexingly, even yoy car consumption rate, despite its high correlation, did not improve accuracy. However, even this is somewhat understood via an earlier modling attempt ('modeling_i.ipynb') where via recursive feature elimination (RFE) this feature was one to be eliminated, implying a weak impact for whatever reason.
It was debated to try a VAR model to graph both simultaneously, however ultimately rejected when defnitionally 90 day delinquents must first be 30 day delinquents.
#### Conclusion
So, it remains clear that delinquent rates are going up, a sign that more people are unable to pay their credit card bills and a prudent thing to do would be to raise interest rates and not be as open to lending money to others given the default greater risk. However, such results should likley be taken with at least a grain of salt when per our current analysis we were unsuccuesful in finding out what does influence delinquent rates.

## Sources
### Data



https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.gettyimages.com%2Fphotos%2Fcrying-baby-office&psig=AOvVaw1m61EX851u1z2lLejR1Xhy&ust=1708467604181000&source=images&cd=vfe&opi=89978449&ved=2ahUKEwio48P2t7iEAxUzuIkEHX1ZD80QjRx6BAgAEBU

### Images



?? add back table of contents?

PS
Economic Context
Analysis and Findings
modelling
forcasting
strategy guidance
conclusion
q and a

POST ON PUBLIC GIT
    and tell the others...