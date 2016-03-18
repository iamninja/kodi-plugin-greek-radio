import sys
import xbmc
import xbmcgui
import xbmcplugin

addon_handle = int(sys.argv[1])
xbmcplugin.setContent(addon_handle, 'songs')

radio = {}
radio['pepper9660'] = {
  'url':  'http://netradio.live24.gr/pepper9660',
  'li':   xbmcgui.ListItem('Pepper 96.6', iconImage='DefaultAudio.png')
}
radio['realfm'] = {
  'url':  'http://netradio.live24.gr/realfm',
  'li':   xbmcgui.ListItem('Real FM', iconImage='DefaultAudio.png')
}
for key, value in radio.items():
  xbmcplugin.addDirectoryItem(handle=addon_handle, url=value['url'], listitem=value['li'])

xbmcplugin.endOfDirectory(addon_handle)
