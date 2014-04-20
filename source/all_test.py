#!/usr/bin/env python
#-*- coding: utf-8 -*-

from __future__ import print_function
import matplotlib.pyplot as plt
import numpy as np
import pylab
import xlrd

pylab.mpl.rcParams['font.sans-serif'] = ['DejaVu Serif']
pylab.mpl.rcParams['axes.unicode_minus'] = False

#open excel file and get sheet
myBook = xlrd.open_workbook(r'report.xls')
mySheet = myBook.sheet_by_index(0)

#get datas
xtime = mySheet.col(0)
xtime = [x.value for x in xtime]
ycpu = mySheet.col_values(6)
ygpu = mySheet.col_values(7)
yfat = mySheet.col_values(8)

xtime.pop(0)
ycpu.pop(0)
ygpu.pop(0)
yfat.pop(0)

ycpu = [y*100 for y in ycpu]
ygpu = [y*100 for y in ygpu]
yfat = [y*100 for y in yfat]


#declare a figure object to plot
#fig, ax = plt.subplots(num=None, figsize=(8, 6), dpi=80, facecolor='w', edgecolor='k')
fig, ax = plt.subplots()
lc = ax.plot(xtime, ycpu, '-o', ms=5, lw=2, alpha=0.8, mfc='green')
lg = ax.plot(xtime, ygpu, '-o', ms=5, lw=2, alpha=0.8, mfc='orange')
lf = ax.plot(xtime, yfat, '-o', ms=5, lw=2, alpha=0.8, mfc='blue')
ax.set_xlim(0.5, len(xtime)+0.5)
#ax.yticks(np.arange(0, 1.1, 0.1))
ax.set_ylim(0, 100)
#ax.yaxis.set_major_formatter(plt.FormatStrFormatter('%d%%'))
#ax.grid()

#fig.patch.set_alpha(0.5)
#ax.patch.set_alpha(0.5)

#advance settings π
titl = plt.title(u'Resource Utilization for Π, the Supercomputer of SJTU', fontsize=20, color='#404040')
plt.ylabel('Percentage(%)', fontsize=17, color='#404040')
plt.xlabel('Time(week)', fontsize=17, color='#404040')
plt.gca().yaxis.set_label_coords(-0.05, 0.5) # have full control over coordinates
plt.gca().xaxis.set_label_coords(0.5, -0.07) # have full control over coordinates

titl.set_y(1.04)
#plt.subplot_ajust(top=0.86)

lines = lc, lg, lf
#plt.setp(lines, linestyle='--')   # set all to dashed
plt.setp(lc, linewidth=2, color='#0f870f')
plt.setp(lg, linewidth=2, color='#f05724')
plt.setp(lf, linewidth=2, color='#4f7086')


legend = plt.legend(['Intel CPUs',
            'Nvidia GPUs',
            'FAT Nodes'],
           shadow=True,
           fancybox=True)
plt.setp(plt.gca().get_legend().get_texts(), fontsize="13")

#vertical split
plt.axvline(1, hold=None, color='gray', linestyle='--')
ax.text(1.0, 80, '<-------------', color='gray')
ax.text(25, 80,  '------------->', color='gray')
ax.text(12, 80, 'Early Access Program', color='gray')
plt.axvline(17.57, hold=None, color='gray', linestyle='--')
ax.text(15.5, 90, 'Opening Ceremony', color='gray')
plt.axvline(27.43, hold=None, color='gray', linestyle='--')
ax.text(27.5, 70, '<-------------', color='gray')
ax.text(30, 70, 'Formal Running Starts', color='gray')
plt.axvline(29.29, hold=None, color='gray', linestyle='--')
ax.text(29.35, 80, '<---Winter  Vocation--->', color='gray')
plt.axvline(35, hold=None, color='gray', linestyle='--')

#plt.axhline(80, hold=None, color='gray', linestyle='--')

#Month notation
monpos = -5;
ax.text(1.2, monpos, 'Jul 2013', color='gray')
ax.text(5.2, monpos, 'Aug 2013', color='gray')
ax.text(9.7, monpos, 'Sep 2013', color='gray')
ax.text(14.7, monpos, 'Oct 2013', color='gray')
ax.text(18.2, monpos, 'Nov 2013', color='gray')
ax.text(22.7, monpos, 'Dec 2013', color='gray')
ax.text(27.7, monpos, 'Jan 2014', color='gray')
ax.text(31.7, monpos, 'Feb 2014', color='gray')
ax.text(35.7, monpos, 'Mar 2014', color='gray')
ax.text(40.2, monpos, 'Apr 2014', color='gray')

#show the figure
#plt.show()

plt.gcf().set_size_inches(18.5,10.5)
#plt.gcf().set_size_inches(28,16) # too big
#plt.gcf().set_size_inches(28,16)
plt.savefig('weekly_utilization.png',dpi=100)
