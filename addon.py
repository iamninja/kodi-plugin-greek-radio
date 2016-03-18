import sys
import xbmc
import xbmcgui
import xbmcplugin

addon_handle = int(sys.argv[1])
xbmcplugin.setContent(addon_handle, 'music')

url = 'http://localhost/some_video.mkv'
li = xbmcgui.ListItem('My First Music!', iconImage='DefaultVideo.png')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

xbmcplugin.endOfDirectory(addon_handle)
