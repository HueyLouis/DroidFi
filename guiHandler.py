"""Kivy for GUI"""
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from getNetworkList import getNetworks
from jnius import autoclass
class WifiSettings(App):
    def build(self):
        #Create grid layout for gui
        layout = GridLayout(cols=2)

        #Add a lablel for all available networks
        layout.add_widget(Label(text='Available Networks:'))

        #List all available networks
        networkList = getNetworks().scanNetworks()
        for network in networkList:
            layout.add_widget(Label(text=network))

        #Add a label for every selected network
        layout.add_widget(Label(text='Selected Network:'))

        #Add a text input for network Passowrd
        passwordInput = TextInput(multiline=False)
        layout.add_widget(passwordInput)

        #Add a button to connect to a selected network
        connectButton = Button(text='Connect')
        connectButton.bind(on_press=lambda x: self.connectToNetwork(networkList, passwordInput.text))
        layout.add_widget(connectButton)

        return layout

    def connectToNetwork(self, networkList, password):
        #Save network name
        selectedNetwork = networkList[0]
        Environment = autoclass('android.os.Environment')
        dcimFolder = Environment.getExternalStoragePublicDirectory(Environment.DIRECTORY_DCIM)
        filePath = dcimFolder.getAbsolutePath() + '/network.txt'
        with open(filePath, 'w') as f:
            f.write(selectedNetwork + ',' + password)

        #Connect to selected Network

        #Create the popup grid
        popupContent = GridLayout(cols=1)
        popupContent.add_widget(Label(text='Connecting to network: ' + selectedNetwork))

        #Create the popup and open it
        popup = Popup(title='Network Connection: ', content=popupContent, size=(400, 200))
        popup.open()