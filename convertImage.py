import binascii
from threading import Thread

class bitValue:
    def __init__(this):
        pass;

    def start(this):
        Thread(target=this.getVal, args=()).start();
        return this;

    def getVal(this):
        this.val = str((file.read(1)[0] & 0b1));
        print(this.val, end="");
        this.complete = True;

file = open("littleschoolbus.bmp", "rb");
string = "";
vals = []

while True:
    try:
        vals.append(bitValue().start());
        
    except EOFError:
        print("End of file");
        break;

print(string);
file.close();
file = open("newlittleschoolbus.bmp", "w");
file.write(string);
file.close();
