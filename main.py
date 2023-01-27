import time

import numpy as np
import matplotlib.pyplot as plt
import paho.mqtt.client as mqtt

def mqtt_server_connect(server_name):
    client = mqtt.Client(protocol=mqtt.MQTTv5)
    try:
        client.connect(host=server_name)
        client.loop()
        return client
    except:
        return 1
    return 0

def gen_noise(freq, ampl):
    space = np.linspace(0, freq, freq)
    sinwave= ampl * np.sin(np.pi * space)
    return sinwave

def main():
    try:
        freq = 1000
        ampl = 10
        mqtt_client = mqtt_server_connect('127.0.0.1')
        while True:
            start_time = time.time()
            noise = gen_noise(freq=freq, ampl=ampl)
            print(noise)
            mqtt_client.publish(topic='noise/signal', payload=str(noise), qos=1)
            #plt.subplot(1, 1, 1)
            #t = np.linspace(0, freq, freq)
            #plt.plot(t, noise)
            #plt.show()

            stop_time = time.time()

            time.sleep(1-(start_time - stop_time))

            return 1
    except Exception as e:
        print(e)
        return 1
    return 0



if __name__ == '__main__':
    exit_code = main()
    exit(exit_code)