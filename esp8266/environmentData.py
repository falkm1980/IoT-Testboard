
import dht
import machine
import urequests


def MeasureAndSend():
    d = dht.DHT11(machine.Pin(5))
    d.measure()
    temp = d.temperature()
    hum = d.humidity()
    adc = machine.ADC(0)

    voltage = adc.read()

    url = "http://192.168.0.14:3000/data?"
    response = urequests.get(url + "temp=" + str(temp) + "&humidity=" + str(hum) + "&voltage=" + str(voltage))
  