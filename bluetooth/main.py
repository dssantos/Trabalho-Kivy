from jnius import autoclass
from kivy.lang import Builder
from kivy.app import App

BluetoothAdapter = autoclass('android.bluetooth.BluetoothAdapter')
BluetoothDevice = autoclass('android.bluetooth.BluetoothDevice')
BluetoothSocket = autoclass('android.bluetooth.BluetoothSocket')
UUID = autoclass('java.util.UUID')

bluetooth_device_name = 'BTMODULE' # Dispositivo bluetooth que será conectado. Precisa estar previamente pareado.

def get_socket_stream(name):
    paired_devices = BluetoothAdapter.getDefaultAdapter().getBondedDevices().toArray()
    socket = None
    for device in paired_devices:
        if device.getName() == name:
            socket = device.createRfcommSocketToServiceRecord(
                UUID.fromString("00001101-0000-1000-8000-00805F9B34FB"))
            send_stream = socket.getOutputStream()
            break
    socket.connect()
    return send_stream

class MainApp(App):

    bt_name = bluetooth_device_name

    def conectar(self):
        self.send_stream = get_socket_stream(bluetooth_device_name)

    def send(self, cmd):
        self.send_stream.write('{}\n'.format(cmd))
        self.send_stream.flush()

if __name__ == '__main__':
    MainApp().run()