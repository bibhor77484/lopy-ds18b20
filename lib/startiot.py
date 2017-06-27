from network import LoRa
import socket
import time
import binascii
import pycom
import machine

class Startiot:

    def __init__(self):
        self.dev_eui = binascii.unhexlify("000000000000022d")
        self.app_eui = binascii.unhexlify("00000000000000b3")
        self.app_key = binascii.unhexlify("7a5a6e506f6e54495357705532737364")

        self.lora = LoRa(mode=LoRa.LORAWAN)
    def connect(self, blocking):
        self.lora.join(activation=LoRa.OTAA, auth=(self.dev_eui, self.app_eui, self.app_key), timeout=0)

        while not self.lora.has_joined():
            pass

        self.s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)

        # set the LoRaWAN data rate
        self.s.setsockopt(socket.SOL_LORA, socket.SO_DR, 5)

        # make the socket non-blocking
        self.s.setblocking(blocking)

    def send(self, data):
        self.s.send(data)

    def recv(self, length):
        return self.s.recv(length)
