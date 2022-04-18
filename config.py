# -*- coding: utf-8 -*-

# How many seconds to wait for the proxy to make a connection.
# The higher this number, the longer the check will take
# and the more proxies you will receive.
TIMEOUT = 5

# Maximum concurrent connections.
# Don't set higher than 900, please.
MAX_CONNECTIONS = 1000

# Set to False to sort proxies alphabetically.
SORT_BY_SPEED = True

# Path to the folder where the proxy folders will be saved.
# Leave the quotes empty to save the proxies to the current directory.
SAVE_PATH = ""

# Enable which proxy folders to create.
# Set to False to disable.

# Proxies with any anonymity level.
PROXIES = True
# Anonymous proxies.
PROXIES_ANONYMOUS = False
# Same as PROXIES, but including exit-node's geolocation.
# Geolocation format is ip:port|Country|Region|City
PROXIES_GEOLOCATION = True
# Same as PROXIES_GEOLOCATION, but including exit-node's geolocation.
PROXIES_GEOLOCATION_ANONYMOUS = False


# PROTOCOL - whether to enable checking certain protocol proxies (True or False).
# PROTOCOL_SOURCES - proxy lists URLs.
HTTP = True
HTTP_SOURCES = (
	"https://api.proxyscrape.com/v2/?request=getproxies&protocol=http",
	"https://openproxy.space/list/http",
	"https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http%2Bhttps.txt",
	"https://raw.githubusercontent.com/mmpx12/proxy-list/master/http.txt",
	"https://raw.githubusercontent.com/mmpx12/proxy-list/master/https.txt",
	"https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt",
	"https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",
	"https://www.proxy-list.download/api/v1/get?type=http",
	"https://www.proxy-list.download/api/v1/get?type=https",
	"https://github.com/ShiftyTR/Proxy-List/blob/master/http.txt",
	"https://github.com/ShiftyTR/Proxy-List/blob/master/https.txt",
	"https://www.proxyscan.io/download?type=http",
	"https://api.openproxylist.xyz/http.txt",
	"https://api.proxyscrape.com/?request=getproxies&proxytype=http",
	"https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt",
	"https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt",
	"http://proxytime.ru/http",
	"http://www.proxylists.net/http_highanon.txt",
	"https://raw.githubusercontent.com/human1ty/proxy/main/http.txt",
	"https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt",
	"https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all",
	"https://api.best-proxies.ru/proxylist.txt?key=developer&type=http",
	"https://api.best-proxies.ru/proxylist.txt?key=developer&type=https",
	"https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt",
	"https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/https.txt",
	"https://raw.githubusercontent.com/Volodichev/proxy-list/main/http.txt",
	"http://spys.me/proxy.txt",
	"https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt",
	"https://www.sslproxies.org",
	"https://free-proxy-list.net",
	"https://free-proxy-list.net/anonymous-proxy.html",
	"https://free-proxy-list.net/uk-proxy.html",
	"https://www.us-proxy.org/",
	"https://raw.githubusercontent.com/porthole-ascend-cinnamon/proxy_scraper/main/proxies.txt",
	"https://raw.githubusercontent.com/ryanhaticus/superiorproxy.com/main/proxies.txt",
	"https://raw.githubusercontent.com/almroot/proxylist/master/list.txt",
	"https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt",
	"https://raw.githubusercontent.com/hendrikbgr/Free-Proxy-Repo/master/proxy_list.txt",
	"https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/proxies.txt",
	"http://spys.me/proxy.txt",
	"https://www.sslproxies.org/",
	"http://ipaddress.com/proxy-list/",
	"https://freshfreeproxylist.wordpress.com/",
	"https://free-proxy-list.net/",
	"http://www.httptunnel.ge/ProxyListForFree.aspx",
	"https://multiproxy.org/txt_all/proxy.txt",
	"https://raw.githubusercontent.com/KarboDuck/mhddos_bash/main/all_proxy.txt",
	"https://pastebin.com/raw/vQzZ8CwG",
	"https://pastebin.com/raw/vLN81LDa",
	"https://raw.githubusercontent.com/mmpx12/proxy-list/master/proxies.txt",
	"https://raw.githubusercontent.com/UserR3X/proxy-list/main/online/all.txt",
	"https://raw.githubusercontent.com/User-R3X/proxy-list/main/online/all.txt",
	"https://www.freeproxychecker.com/result/mixed_proxies.txt",
	"https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies.txt",
	"https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/proxy.txt",
	"https://www.sslproxies.org/#raw",
	"https://t.me/s/proxiesfine",
	"https://free-proxy-list.net/anonymous-proxy.html",
	"https://free-proxy-list.net/uk-proxy.html",
	"https://www.us-proxy.org/",
)

SOCKS4 = True
SOCKS4_SOURCES = (
	"https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks4",
	"https://openproxy.space/list/socks4",
	"https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt",
	"https://raw.githubusercontent.com/mmpx12/proxy-list/master/socks4.txt",
	"https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt",
	"https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt",
	"https://www.proxy-list.download/api/v1/get?type=socks4",
	"https://www.proxyscan.io/download?type=socks4",
	"https://www.freeproxychecker.com/result/socks4_proxies.txt",
	"https://github.com/ShiftyTR/Proxy-List/blob/master/socks4.txt",
	"https://api.openproxylist.xyz/socks4.txt",
	"https://api.proxyscrape.com/?request=getproxies&proxytype=socks4",
	"https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks4.txt",
	"https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks4.txt",
	"https://raw.githubusercontent.com/human1ty/proxy/main/socks4.txt",
	"https://api.best-proxies.ru/proxylist.txt?key=developer&type=socks4",
	"https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt",
	"https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks4&timeout=10000&country=all",
	"https://spys.me/socks.txt",
	"https://www.socks-proxy.net/",
	"https://socks-proxy.net/",
	"https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt",
	"https://www.sslproxies.org",
	"https://free-proxy-list.net",
	"https://free-proxy-list.net/anonymous-proxy.html",
	"https://free-proxy-list.net/uk-proxy.html",
	"https://www.us-proxy.org/",
	"https://raw.githubusercontent.com/porthole-ascend-cinnamon/proxy_scraper/main/proxies.txt",
	"https://raw.githubusercontent.com/ryanhaticus/superiorproxy.com/main/proxies.txt",
	"https://raw.githubusercontent.com/almroot/proxylist/master/list.txt",
	"https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt",
	"https://raw.githubusercontent.com/hendrikbgr/Free-Proxy-Repo/master/proxy_list.txt",
	"https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/proxies.txt",
	"http://spys.me/proxy.txt",
	"https://www.sslproxies.org/",
	"http://ipaddress.com/proxy-list/",
	"https://freshfreeproxylist.wordpress.com/",
	"https://free-proxy-list.net/",
	"http://www.httptunnel.ge/ProxyListForFree.aspx",
	"https://multiproxy.org/txt_all/proxy.txt",
	"https://raw.githubusercontent.com/KarboDuck/mhddos_bash/main/all_proxy.txt",
	"https://pastebin.com/raw/vQzZ8CwG",
	"https://pastebin.com/raw/vLN81LDa",
	"https://raw.githubusercontent.com/mmpx12/proxy-list/master/proxies.txt",
	"https://raw.githubusercontent.com/UserR3X/proxy-list/main/online/all.txt",
	"https://raw.githubusercontent.com/User-R3X/proxy-list/main/online/all.txt",
	"https://www.freeproxychecker.com/result/mixed_proxies.txt",
	"https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies.txt",
	"https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/proxy.txt",
	"https://www.sslproxies.org/#raw",
	"https://t.me/s/proxiesfine",
	"https://free-proxy-list.net/anonymous-proxy.html",
	"https://free-proxy-list.net/uk-proxy.html",
	"https://www.us-proxy.org/",
	"https://raw.githubusercontent.com/KUTlime/ProxyList/main/ProxyList.txt",
)
SOCKS5 = True
SOCKS5_SOURCES = (
	"https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5",
	"https://openproxy.space/list/socks5",
	"https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt",
	"https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt",
	"https://raw.githubusercontent.com/manuGMG/proxy-365/main/SOCKS5.txt",
	"https://raw.githubusercontent.com/mmpx12/proxy-list/master/socks5.txt",
	"https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt",
	"https://www.proxyscan.io/download?type=socks5",
	"https://github.com/ShiftyTR/Proxy-List/blob/master/socks5.txt",
	"https://www.proxy-list.download/api/v1/get?type=socks5",
	"https://api.openproxylist.xyz/socks5.txt",
	"https://api.proxyscrape.com/?request=getproxies&proxytype=socks5",
	"https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks5.txt",
	"https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks5.txt",
	"https://raw.githubusercontent.com/human1ty/proxy/main/socks5.txt",
	"https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt",
	"https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt",
	"https://api.best-proxies.ru/proxylist.txt?key=developer&type=socks5",
	"https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=10000&country=all",
	"https://spys.me/socks.txt",
	"https://www.socks-proxy.net/",
	"https://socks-proxy.net/",
	"https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt",
	"https://www.sslproxies.org",
	"https://free-proxy-list.net",
	"https://free-proxy-list.net/anonymous-proxy.html",
	"https://free-proxy-list.net/uk-proxy.html",
	"https://www.us-proxy.org/",
	"https://raw.githubusercontent.com/porthole-ascend-cinnamon/proxy_scraper/main/proxies.txt",
	"https://raw.githubusercontent.com/ryanhaticus/superiorproxy.com/main/proxies.txt",
	"https://raw.githubusercontent.com/almroot/proxylist/master/list.txt",
	"https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt",
	"https://raw.githubusercontent.com/hendrikbgr/Free-Proxy-Repo/master/proxy_list.txt",
	"https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/proxies.txt",
	"http://spys.me/proxy.txt",
	"https://www.sslproxies.org/",
	"http://ipaddress.com/proxy-list/",
	"https://freshfreeproxylist.wordpress.com/",
	"https://free-proxy-list.net/",
	"http://www.httptunnel.ge/ProxyListForFree.aspx",
	"https://multiproxy.org/txt_all/proxy.txt",
	"https://raw.githubusercontent.com/KarboDuck/mhddos_bash/main/all_proxy.txt",
	"https://pastebin.com/raw/vQzZ8CwG",
	"https://pastebin.com/raw/vLN81LDa",
	"https://raw.githubusercontent.com/mmpx12/proxy-list/master/proxies.txt",
	"https://raw.githubusercontent.com/UserR3X/proxy-list/main/online/all.txt",
	"https://raw.githubusercontent.com/User-R3X/proxy-list/main/online/all.txt",
	"https://www.freeproxychecker.com/result/mixed_proxies.txt",
	"https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies.txt",
	"https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/proxy.txt",
	"https://www.sslproxies.org/#raw",
	"https://t.me/s/proxiesfine",
	"https://free-proxy-list.net/anonymous-proxy.html",
	"https://free-proxy-list.net/uk-proxy.html",
	"https://raw.githubusercontent.com/KUTlime/ProxyList/main/ProxyList.txt",
)