us5yt = round(fdr.DataReader('US5YT',today).loc[today, 'Adj Close'],2) # 5년 만기 미국국채 수익률
us10yt = round(fdr.DataReader('US10YT',today).loc[today, 'Adj Close'],2) # 1년 만기 미국국채 수익률
us30yt = round(fdr.DataReader('US30YT',today).loc[today, 'Adj Close'],2) # 30년 만기 미국국채 수익률
