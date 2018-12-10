#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'resources', 'lib'))

import xbmc, xbmcvfs

pluginid = "script.ccloudmeta"

def get_url(stream_file):
    if stream_file.endswith(".strm"):
        f = xbmcvfs.File(stream_file)
        try:
            content = f.read()
            if content.startswith("plugin://" + pluginid):
                return content.replace("/library", "/select")
        finally:
            f.close()
            
    return None
    
def main():
    stream_file = xbmc.getInfoLabel('ListItem.FileNameAndPath')    
    url = get_url(stream_file)
    if url is None:
        title = "Meta"
        msg = "Invalid media file. Try using the Meta-Context-Menu addon instead"
        xbmc.executebuiltin('XBMC.Notification("%s", "%s", "%s", "%s")' 
                % (msg, title, 2000, ''))
    else:
        xbmc.executebuiltin("PlayMedia({0})".format(url))
    
if __name__ == '__main__':
    main()