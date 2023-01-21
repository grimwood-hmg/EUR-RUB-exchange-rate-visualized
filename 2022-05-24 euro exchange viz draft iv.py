#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt
import matplotlib.style as style
import matplotlib.dates as mdates

# import euro-exchange rates datasets
# source for exchange_rates: https://www.kaggle.com/datasets/lsind18/euro-exchange-daily-rates-19992020
# secondary source for euro-rub exchange rate: https://www.exchange-rates.org/history/RUB/EUR/T

exchange_rates = pd.read_csv('2022-04-27 DataQuest Euro Exchange Rate Viz/euro_exchange_rates_1999_2022_cleaned.csv')
exchange_rates_contemporary = pd.read_csv('2022-04-27 DataQuest Euro Exchange Rate Viz/euro_rouble_contemporary_cleaned.csv')

# copying euro-rub to separate df
euro_rouble = exchange_rates[['time', 'russian_rouble']].dropna().sort_values(by=['time']).copy()
euro_rouble_contemporary = exchange_rates_contemporary[['time','russian_rouble']].dropna().sort_values(by=['time']).copy()

# convert to datetime
euro_rouble['time'] = pd.to_datetime(euro_rouble['time'])
euro_rouble_contemporary['time'] = pd.to_datetime(exchange_rates_contemporary['time'])

# grapheroo
print(style.available)
style.use('fivethirtyeight')

fig, ax = plt.subplots(figsize=(21,9), constrained_layout=True)

ax.plot(euro_rouble['time'], euro_rouble['russian_rouble'].rolling(30).mean(), color='#4e5cfc')
ax.plot(euro_rouble_contemporary['time'], euro_rouble_contemporary['russian_rouble'].rolling(30).mean(), color='#964efc')

# setting labels
# ax.set_xlabel('Year')
# ax.set_ylabel('Euros', labelpad=-40)

# adding a grid
ax.grid(visible=True,which='both',axis='both',alpha=0.4)

# no more spines
for i in ['top', 'bottom', 'right', 'left']:
	ax.spines[i].set_visible(False)
	
# set title
ax.text(10930, 142, 'Historical Euro-Russian Rouble Exchange Rate', horizontalalignment='left', verticalalignment='center', fontsize=20, fontfamily='monospace', alpha=0.5)
ax.text(10930, 138, '30-day rolling average', horizontalalignment='left', verticalalignment='center', fontsize=16, fontfamily='monospace', alpha=0.5)
# 1999-01-04 through 2022-05-23

# add a signature
ax.text(10410, 16, 'hmg' +' '*283 + 'Source: European Central Bank, EXCHANGE-RATES.org     ', color='#f0f0f0', backgroundcolor='#4d4d4d', size=12)

# adjusting xticks
ax.xaxis.set_major_locator(mdates.YearLocator(2))
ax.xaxis.set_major_formatter(mdates.ConciseDateFormatter('%Y'))
ax.xaxis.tick_top()
ax.tick_params(axis='x', pad=-10, rotation=45)
ax.tick_params(top=True, bottom=False)
ax.set_xbound(lower=dt.datetime(1999, 1, 1), upper=dt.datetime(2023, 1, 1))

# annotations
ax.annotate(
	'Russia invades Ukraine, 2022',
	xy=(dt.datetime(2022, 2, 24), 87.31),
	xytext=(dt.datetime(2001, 2, 1), 117),
	fontstyle='oblique',
	alpha=0.6,
	arrowprops=dict(
		arrowstyle='-',
		connectionstyle='bar,angle=-90,armA=0.0,armB=.0,fraction=-0.984', # bar,angle=-90,armA=0.0,armB=0.0,fraction=-0.7
		alpha=0.7,
		color='#4eb3fc',
		linewidth=2,
	)
)

ax.annotate(
	'Russian military buildup in Ukrainian region, 2021',
	xy=(dt.datetime(2021, 3, 20), 88.92),
	xytext=(dt.datetime(2001, 2, 1), 113),
	fontstyle='oblique',
	alpha=0.6,
	arrowprops=dict(
		arrowstyle='-',
		connectionstyle='angle,angleA=180,angleB=90,rad=0',
		alpha=0.7,
		color='#4eb3fc',
		linewidth=2
	)
)

ax.annotate(
	'Russia invades Ukraine, 2014',
	xy=(dt.datetime(2014, 8, 15), 47.48),
	xytext=(dt.datetime(2001, 2, 1), 109),
	fontstyle='oblique',
	alpha=0.6,
	arrowprops=dict(
		arrowstyle='-',
		connectionstyle='angle,angleA=180,angleB=90,rad=0',
		alpha=0.7,
		color='#4eb3fc',
		linewidth=2
	)
)

ax.annotate(
	'Russia begins Crimea annexation, 2014',
	xy=(dt.datetime(2014, 2, 20), 47.03),
	xytext=(dt.datetime(2001, 2, 1), 105),
	fontstyle='oblique',
	alpha=0.6,
	arrowprops=dict(
		arrowstyle='-',
		connectionstyle='angle,angleA=180,angleB=90,rad=0',
		alpha=0.7,
		color='#4eb3fc',
		linewidth=2
	)
)

# annotations part II
ax.annotate(
	'2022 era sanctions begin',
	xy=(dt.datetime(2022, 2, 24), 87.31),
	xytext=(dt.datetime(2017, 7, 1), 45),
	fontstyle='oblique',
	alpha=0.6,
	arrowprops=dict(
		arrowstyle='-',
		connectionstyle='bar,angle=360,armA=0.0,armB=0.0,fraction=-0.26',
		alpha=0.7,
		color='#4eb3fc',
		linewidth=2
	)
)

ax.annotate(
	'2014 era sanctions begin',
	xy=(dt.datetime(2014, 3, 1), 47.86),
	xytext=(dt.datetime(2017, 7, 1), 41),
	fontstyle='oblique',
	alpha=0.6,
	arrowprops=dict(
		arrowstyle='-',
		connectionstyle='angle,angleA=180,angleB=90,rad=0',
		alpha=0.7,
		color='#4eb3fc',
		linewidth=2
	)
)

plt.savefig('2022-04-27 DataQuest Euro Exchange Rate Viz/euro-rub exchange rate vii.svg', dpi=300, format='svg')
plt.savefig('2022-04-27 DataQuest Euro Exchange Rate Viz/euro-rub exchange rate vii.jpg', dpi=300, format='jpg')
plt.show()
print(fig.canvas.get_supported_filetypes())
print(euro_rouble_contemporary.tail())
print(euro_rouble.head())