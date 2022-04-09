# -*- coding: utf-8 -*-

# How many seconds to wait for the proxy to make a connection.
# The higher this number, the longer the check will take
# and the more proxies you will receive.
TIMEOUT = 10

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
PROXIES_GEOLOCATION = False
# Same as PROXIES_GEOLOCATION, but including exit-node's geolocation.
PROXIES_GEOLOCATION_ANONYMOUS = False


# PROTOCOL - whether to enable checking certain protocol proxies (True or False).
# PROTOCOL_SOURCES - proxy lists URLs.
HTTP = True
HTTP_SOURCES = (
	"http://pubproxy.com/api/proxy?limit=2&format=txt&country=RU&http=true&type=http",
    "https://openproxy.space/list/http",
    "https://raw.githubusercontent.com/almroot/proxylist/master/list.txt",
    "https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt",
    "https://raw.githubusercontent.com/hendrikbgr/Free-Proxy-Repo/master/proxy_list.txt",
    "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http%2Bhttps.txt",
    "https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt",
    "https://raw.githubusercontent.com/mmpx12/proxy-list/master/http.txt",
    "https://raw.githubusercontent.com/mmpx12/proxy-list/master/https.txt",
    "https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt",
    "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt",
    "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/https.txt",
    "https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/proxies.txt",
    "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",
    "https://raw.githubusercontent.com/User-R3X/proxy-list/main/online/http%2Bs.txt",
    "https://raw.githubusercontent.com/Volodichev/proxy-list/main/http.txt",
    "https://www.proxy-list.download/api/v1/get?type=http",
    "https://www.proxy-list.download/api/v1/get?type=https",
	"http://pubproxy.com/api/proxy?limit=2&format=txt&http=true&type=http",
	"https://premiumproxy.net/full-proxy-list",
	"https://proxypremium.top/full-proxy-list",
	"http://spys.me/proxy.txt",
	"https://www.freeproxychecker.com/result/mixed_proxies.txt",
	"https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all",
	"https://www.proxyscan.io/download?type=http",
	"https://api.openproxylist.xyz/http.txt",
	"http://ipaddress.com/proxy-list/",
	"https://www.sslproxies.org",
	"https://t.me/s/proxiesfine",
	"https://free-proxy-list.net",
	"https://free-proxy-list.net/anonymous-proxy.html",
	"https://free-proxy-list.net/uk-proxy.html",
	"https://www.us-proxy.org/",
	"https://socks-proxy.net/",
	"http://www.httptunnel.ge/ProxyListForFree.aspx",
	"https://proxy-list.org/russian/search.php?search=RU&country=RU&type=any&port=any&ssl=any",
	"https://api.best-proxies.ru/proxylist.txt?key=developer&type=http",
	"https://api.best-proxies.ru/proxylist.txt?key=developer&type=https",
	"https://hidemy.name/en/proxy-list/?country=AFALAOARAMBDBZBOBRBGKHCACLCOCWCYCZEGETFRGEDEGTHKHUINIDIRIEITJPKZKEKRLVLYMYMTMXMDMNNPNLNGPKPEPHPLPRRORURSSGZAESCHTWTHTRUAGBUSVEVNVG&maxtime=2000&anon=234#list",
	"https://hidemy.name/en/proxy-list/?country=AFALAOARAMBDBZBOBRBGKHCACLCOCWCYCZEGETFRGEDEGTHKHUINIDIRIEITJPKZKEKRLVLYMYMTMXMDMNNPNLNGPKPEPHPLPRRORURSSGZAESCHTWTHTRUAGBUSVEVNVG&maxtime=2000&anon=234&start=64#list",
	"https://hidemy.name/en/proxy-list/?country=AFALAOARAMBDBZBOBRBGKHCACLCOCWCYCZEGETFRGEDEGTHKHUINIDIRIEITJPKZKEKRLVLYMYMTMXMDMNNPNLNGPKPEPHPLPRRORURSSGZAESCHTWTHTRUAGBUSVEVNVG&maxtime=2000&anon=234&start=128#list",
	"https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt",
	

)
SOCKS4 = True
SOCKS4_SOURCES = (
	"http://pubproxy.com/api/proxy?limit=2&format=txt&country=RU&type=socks4",
    "https://openproxy.space/list/socks4",
    "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt",
    "https://raw.githubusercontent.com/mmpx12/proxy-list/master/socks4.txt",
    "https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt",
    "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks4.txt",
    "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt",
    "https://raw.githubusercontent.com/User-R3X/proxy-list/main/online/socks4.txt",
    "https://www.proxy-list.download/api/v1/get?type=socks4",
	"http://pubproxy.com/api/proxy?limit=2&format=txt&type=socks4",
	"https://premiumproxy.net/full-proxy-list",
	"https://proxypremium.top/full-proxy-list",
	"https://pastebin.com/raw/vQzZ8CwG",
	"https://pastebin.com/raw/vLN81LDa",
	"https://pastebin.com/raw/1DeAN3xi",
	"https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/proxies.txt",
	"https://raw.githubusercontent.com/hendrikbgr/Free-Proxy-Repo/master/proxy_list.txt",
	"https://raw.githubusercontent.com/almroot/proxylist/master/list.txt",
	"https://www.my-proxy.com/free-socks-4-proxy.html",
	"https://spys.me/socks.txt",
	"https://www.freeproxychecker.com/result/mixed_proxies.txt",
	"https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks4&timeout=10000&country=all",
	"https://www.proxyscan.io/download?type=socks4",
	"https://api.openproxylist.xyz/socks4.txt",
	"https://t.me/s/proxiesfine",
	"https://free-proxy-list.net",
	"https://free-proxy-list.net/anonymous-proxy.html",
	"https://free-proxy-list.net/uk-proxy.html",
	"https://www.us-proxy.org/",
	"https://socks-proxy.net/",
	"https://proxy-list.org/russian/search.php?search=RU&country=RU&type=any&port=any&ssl=any",
	"https://api.best-proxies.ru/proxylist.txt?key=developer&type=socks4",
	"https://hidemy.name/en/proxy-list/?country=AFALAOARAMBDBZBOBRBGKHCACLCOCWCYCZEGETFRGEDEGTHKHUINIDIRIEITJPKZKEKRLVLYMYMTMXMDMNNPNLNGPKPEPHPLPRRORURSSGZAESCHTWTHTRUAGBUSVEVNVG&maxtime=2000&anon=234#list",
	"https://hidemy.name/en/proxy-list/?country=AFALAOARAMBDBZBOBRBGKHCACLCOCWCYCZEGETFRGEDEGTHKHUINIDIRIEITJPKZKEKRLVLYMYMTMXMDMNNPNLNGPKPEPHPLPRRORURSSGZAESCHTWTHTRUAGBUSVEVNVG&maxtime=2000&anon=234&start=64#list",
	"https://hidemy.name/en/proxy-list/?country=AFALAOARAMBDBZBOBRBGKHCACLCOCWCYCZEGETFRGEDEGTHKHUINIDIRIEITJPKZKEKRLVLYMYMTMXMDMNNPNLNGPKPEPHPLPRRORURSSGZAESCHTWTHTRUAGBUSVEVNVG&maxtime=2000&anon=234&start=128#list",
	"https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt",
)
SOCKS5 = True
SOCKS5_SOURCES = (
	"http://pubproxy.com/api/proxy?limit=2&format=txt&country=RU&type=socks5",
	"https://openproxy.space/list/socks5",
    "https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt",
    "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt",
    "https://raw.githubusercontent.com/manuGMG/proxy-365/main/SOCKS5.txt",
    "https://raw.githubusercontent.com/mmpx12/proxy-list/master/socks5.txt",
    "https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt",
    "https://raw.githubusercontent.com/ryanhaticus/superiorproxy.com/main/proxies.txt",
    "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks5.txt",
    "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt",
    "https://raw.githubusercontent.com/User-R3X/proxy-list/main/online/socks5.txt",
    "https://www.proxy-list.download/api/v1/get?type=socks5",
	"http://pubproxy.com/api/proxy?limit=2&format=txt&type=socks5",
	"https://premiumproxy.net/full-proxy-list",
	"https://proxypremium.top/full-proxy-list",
	"https://pastebin.com/raw/vQzZ8CwG",
	"https://pastebin.com/raw/vLN81LDa",
	"https://pastebin.com/raw/1DeAN3xi",
	"https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/proxies.txt",
	"https://raw.githubusercontent.com/hendrikbgr/Free-Proxy-Repo/master/proxy_list.txt",
	"https://raw.githubusercontent.com/almroot/proxylist/master/list.txt",
	"https://www.my-proxy.com/free-socks-5-proxy.html",
	"https://spys.me/socks.txt",
	"https://www.freeproxychecker.com/result/mixed_proxies.txt",
	"https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=10000&country=all",
	"https://www.proxyscan.io/download?type=socks5",
	"https://api.openproxylist.xyz/socks5.txt",
	"https://t.me/s/proxiesfine",
	"https://free-proxy-list.net",
	"https://free-proxy-list.net/anonymous-proxy.html",
	"https://free-proxy-list.net/uk-proxy.html",
	"https://www.us-proxy.org/",
	"https://socks-proxy.net/",
	"https://proxy-list.org/russian/search.php?search=RU&country=RU&type=any&port=any&ssl=any",
	"https://api.best-proxies.ru/proxylist.txt?key=developer&type=socks5",
	"https://hidemy.name/en/proxy-list/?country=AFALAOARAMBDBZBOBRBGKHCACLCOCWCYCZEGETFRGEDEGTHKHUINIDIRIEITJPKZKEKRLVLYMYMTMXMDMNNPNLNGPKPEPHPLPRRORURSSGZAESCHTWTHTRUAGBUSVEVNVG&maxtime=2000&anon=234#list",
	"https://hidemy.name/en/proxy-list/?country=AFALAOARAMBDBZBOBRBGKHCACLCOCWCYCZEGETFRGEDEGTHKHUINIDIRIEITJPKZKEKRLVLYMYMTMXMDMNNPNLNGPKPEPHPLPRRORURSSGZAESCHTWTHTRUAGBUSVEVNVG&maxtime=2000&anon=234&start=64#list",
	"https://hidemy.name/en/proxy-list/?country=AFALAOARAMBDBZBOBRBGKHCACLCOCWCYCZEGETFRGEDEGTHKHUINIDIRIEITJPKZKEKRLVLYMYMTMXMDMNNPNLNGPKPEPHPLPRRORURSSGZAESCHTWTHTRUAGBUSVEVNVG&maxtime=2000&anon=234&start=128#list",
	"https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt",
	
)
