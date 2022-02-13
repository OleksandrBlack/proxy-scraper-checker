# proxy-scraper-checker [simple-output]

![Screenshot](screenshot.png)

HTTP, SOCKS4, SOCKS5 proxies scraper and checker.

- Asynchronous.
- Uses regex to search for proxies (ip:port format) on a web page, which allows you to pull out proxies even from json without making any changes to the code.
- Supports determining the geolocation of the proxy exit node.
- Can determine if a proxy is anonymous.

For a version with fancy output powered by [rich](https://github.com/willmcgugan/rich), see the [main](https://github.com/monosans/proxy-scraper-checker) branch.

You can get proxies obtained using this script in [monosans/proxy-list](https://github.com/monosans/proxy-list).

## Usage

- Install [Python](https://python.org/downloads) (Windows 7 requires Python 3.8.X). During installation, be sure to check the box `Add Python to PATH`.
- Download and unpack [the archive with the program](https://github.com/monosans/proxy-scraper-checker/archive/refs/heads/simple-output.zip).
- Install dependencies from `requirements.txt` (`cd` into the unpacked folder and run `python -m pip install -U -r requirements.txt` on the command line).
  - If you want to improve the performance, you can also install extra dependencies. See [aiohttp documentation](https://docs.aiohttp.org/en/stable/index.html#library-installation).
- Edit `config.py` according to your preference.
- Run `main.py` (`python main.py` on the command line).

## Folders description

When the script finishes running, the following folders will be created (this behavior can be changed in the config):

- `proxies` - proxies with any anonymity level.
- `proxies_anonymous` - anonymous proxies.
- `proxies_geolocation` - same as `proxies`, but includes exit-node's geolocation.
- `proxies_geolocation_anonymous` - same as `proxies_anonymous`, but includes exit-node's geolocation.

Geolocation format is `ip:port|Country|Region|City`.

## Buy me a coffee

Ask for details in [Telegram](https://t.me/monosans) or [VK](https://vk.com/id607137534).

## License

[MIT](LICENSE)
