"""This handles listing the networks"""
from wifidroid.wifi import WifiManager


class getNetworks():
    def __init__(self):
        self.wifi = WifiManager()
        self.networks = []

    def scanNetworks(self):
        self.wifi.startScan()
        for i in range(self.wifi.ScanResults.size()):
            ssid = self.wifi.ScanResults.get(i).SSID
            self.networks.append(ssid)

        return self.networks

if __name__ == '__main__':
    networks = getNetworks().scanNetworks()
    print(networks)

