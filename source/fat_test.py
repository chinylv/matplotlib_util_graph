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
#ycpu = mySheet.col_values(6)
#ygpu = mySheet.col_values(7)
yfat = mySheet.col_values(8)

xtime.pop(0)
#ycpu.pop(0)
#ygpu.pop(0)
yfat.pop(0)

#ycpu = [y*100 for y in ycpu]
#ygpu = [y*100 for y in ygpu]
yfat = [y*100 for y in yfat]


#declare a figure object to plot
#fig, ax = plt.subplots(num=None, figsize=(8, 6), dpi=80, facecolor='w', edgecolor='k')
fig, ax = plt.subplots()
#lc = ax.plot(xtime, ycpu, '-o', ms=5, lw=2, alpha=0.8, mfc='blue')
#lg = ax.plot(xtime, ygpu, '-o', ms=5, lw=2, alpha=0.8, mfc='green')
lf = ax.plot(xtime, yfat, '-o', ms=5, lw=2, alpha=0.8, mfc='orange')
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
plt.xlabel('Month', fontsize=17, color='#404040')
plt.gca().yaxis.set_label_coords(-0.05, 0.5) # have full control over coordinates
plt.gca().xaxis.set_label_coords(0.5, -0.07) # have full control over coordinates

titl.set_y(1.06)
#plt.subplot_ajust(top=0.86)

#lines = lc, lg, lf
#plt.setp(lines, linestyle='--')   # set all to dashed
#plt.setp(lc, linewidth=2, color='#036cbf')
#plt.setp(lg, linewidth=2, color='#78b400')
#plt.setp(lf, linewidth=2, color='#f05724')
plt.setp(lf, linewidth=2, color='#fd9828')


#legend settings
legend = plt.legend([
            'FAT Nodes'],
           shadow=True,
           fancybox=True)
plt.setp(plt.gca().get_legend().get_texts(), fontsize="13")

#vertical split
plt.axvline(1, hold=None, color='gray', linestyle='--')
ax.text(1,  93, '<--------------------------------------------------------------', color='gray')
ax.text(17, 93,  '--------------------------------------------------------------->', color='gray')
ax.text(11.5, 93, 'Early Access Program', color='gray')
plt.axvline(17.57, hold=None, color='red', linestyle='--')
ax.text(17.8, 55, 'Opening Ceremony', rotation=-90, color='gray')
plt.axvline(27.43, hold=None, color='#fe2ec8', linestyle='--')
ax.text(27.8, 82, 'In Production', rotation=-90, color='gray')
plt.axvline(29.29, hold=None, color='gray', linestyle='--')
ax.text(29.35, 80, '<------------------------------->', color='gray')
ax.text(30.30, 81.8, 'Chinese Spring', color='gray')
ax.text(30.20, 78.2, 'Festival Holidays', color='gray')
plt.axvline(35, hold=None, color='gray', linestyle='--')

#plt.axhline(80, hold=None, color='gray', linestyle='--')

#date of events notation
evtpos = 102
ax.text(-0.3, evtpos, 'Jun 30, 2013', color='gray')
ax.text(16.0, evtpos, 'Oct 23, 2013', color='gray')
ax.text(26.0, evtpos, 'Jan 1, 2014', color='gray')


ax2 = ax.twinx()
#ax2.plot(xtime, y2, '-o', ms=5, lw=0, alpha=0.0, mfc='black')
ax2.plot(xtime, yfat, lw=0, alpha=0.0, mfc='black')
ax2.set_xlim(0.5, len(xtime)+0.5)
ax2.set_ylim(0, 100)

#change week number to date
xtickrange = [1.143,   #Jul
              5.571,   #Aug
              10.0,    #Sep
              14.286,  #Oct
              18.714,  #Nov
              23.0,    #Dec
              27.429,  #Jan
              31.857,  #Feb
              35.857,  #Mar
              40.286]  #Apr
pylab.xticks(xtickrange, ()) #avoid the default number index


#Month notation
monpos = -5;
ax.text(2.3, monpos, 'Jul 2013', color='gray')
ax.text(6.6, monpos, 'Aug 2013', color='gray')
ax.text(11.0, monpos, 'Sep 2013', color='gray')
ax.text(15.5, monpos, 'Oct 2013', color='gray')
ax.text(19.8, monpos, 'Nov 2013', color='gray')
ax.text(24.0, monpos, 'Dec 2013', color='gray')
ax.text(28.5, monpos, 'Jan 2014', color='gray')
ax.text(32.7, monpos, 'Feb 2014', color='gray')
ax.text(36.8, monpos, 'Mar 2014', color='gray')


#hide the deafult x ticks
#plt.gca().xaxis.set_major_locator(plt.NullLocator())


#show the figure
#plt.show()
#pylab.figure()
#fman = pylab.get_current_fig_manager()
#fman.window.move(600, 600)
plt.tight_layout()

plt.gcf().set_size_inches(18.5,10.5)
#plt.gcf().set_size_inches(28,16) # too big
#plt.gcf().set_size_inches(28,16)
plt.savefig('fat_utilization.png',dpi=100)
