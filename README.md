# IoT-Testboard
IoT-Testboard for Raspberry pi and ESP8266

In order to get the IoT-Evaluation board running you need a recent image of Raspian-Linux.
https://www.raspberrypi.org/downloads/raspbian/

Furthermore you need to install a few more libraries.

## Wiring Pi
git clone https://github.com/WiringPi/WiringPi

./build

## Adafruit_Python GPIO Library
git clone https://github.com/adafruit/Adafruit_Python_GPIO

## Adafruit ILI9341 Display Library
git clone https://github.com/adafruit/Adafruit_Python_ILI9341

## RC-Switch (Radio outlets)
git clone https://github.com/r10r/rcswitch-pi

make

## DHT 11/22 Temp/Humidity sensor
git clone https://github.com/adafruit/Adafruit_Python_DHT

## NeoPixel WS2812:
sudo apt-get install icons

sudo apt-get install swig

sudo apt-get install build-essential python-dev unzip wget 

wget https://github.com/jgarff/rpi_ws281x/archive/master.zip && unzip master.zip && cd rpi_ws281x-master && sudo scons && cd python && 
sudo python setup.py install

## optional Div. Python libs:
sudo pip install pytz (for timezone calculation)

## Optional: Node.JS latest version
sudo wget -O - https://raw.githubusercontent.com/audstanley/NodeJs-Raspberry-Pi/master/Install-Node.sh | sudo bash;
node -v;
