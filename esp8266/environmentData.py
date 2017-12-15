
import dht
import machine
import urequests

def MeasureAndSend():
    d = dht.DHT11(machine.Pin(5))
    d.measure()
    temp = d.temperature()
    hum = d.humidity()

    url = "http://10.31.12.103:3000/data?"
    response = urequests.get(url + "temp=" + str(temp) + "&humidity=" + str(hum))
  