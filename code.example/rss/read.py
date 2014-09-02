#!/usr/bin/env python
# coding: utf-8
#
#
#
# 2014-05-08
#
# Python で RSS を読み込むサンプルです。
#
#
#
#
#

import sys
import feedparser
import codecs





###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
class out:

	@staticmethod
	def println(*arguments):
		
		out = codecs.getwriter('utf-8')(sys.stdout)
		for x in arguments:
			if x is None:
				continue
			out.write('' + x)
		out.write("\n")






###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
class rssreader:

	@staticmethod
	def get(url):

		out.println(url)

		feed = feedparser.parse(url)

		for entry in feed['entries']:
			published = entry['published']
			title = entry['title']
			link = entry['link']
			out.println(published, ', ', title, ', ', str(link))






###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
class main:

	@staticmethod
	def main():

		rssreader.get('http://rss.dailynews.yahoo.co.jp/fc/world/rss.xml')

main.main()
