#
#      Copyright (C) 2012 Tommy Winther
#      http://tommy.winther.nu
#
#      Modified for FTV Guide (09/2014 - 04/2016)
#      by Thomas Geppert [bluezed] - bluezed.apps@gmail.com
#
#      Modified for cCloud TV Guide (04/2016 onwards)
#      by podgod - podgod@gmail.com
#
#  This Program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2, or (at your option)
#  any later version.
#
#  This Program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this Program; see the file LICENSE.txt.  If not, write to
#  the Free Software Foundation, 675 Mass Ave, Cambridge, MA 02139, USA.
#  http://www.gnu.org/copyleft/gpl.html
#
import urllib, urllib2, sys, re, os, random, unicodedata, cookielib, shutil
import xbmc, xbmcgui, xbmcplugin, xbmcaddon, requests, base64, gui


cCloudMeta = xbmc.translatePath('special://home/userdata/addon_data/script.ccloudmeta/players')
GuideDB = xbmc.translatePath('special://home/userdata/addon_data/script.ccloudtv/source.db')

addon       = xbmcaddon.Addon()
addonname   = addon.getAddonInfo('name')


if os.path.exists(GuideDB):
	os.remove(GuideDB)
	
if not os.path.exists(cCloudMeta):
	xbmc.executebuiltin('XBMC.RunPlugin(plugin://script.ccloudmeta/setup/)')

	
line1 = 'Welcome to the [B][COLOR yellow]cCloud TV Guide.[/COLOR][/B] This beta version is'
line2 = 'a work in progress, so not all channels are working.'
line3 = 'Check the announcements section for future update info'

 
xbmcgui.Dialog().ok(addonname, line1, line2, line3)

try:
    w = gui.TVGuide()
    w.doModal()
    del w

except:
    import sys
    import traceback as tb
    (etype, value, traceback) = sys.exc_info()
    tb.print_exception(etype, value, traceback)