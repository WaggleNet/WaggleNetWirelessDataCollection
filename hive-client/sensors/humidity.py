#"module" is not the final name for this interface
#every data generating device (camera, microphone, thermometer) 
#should have its own module class which implements setup and
#poll functions

import time
import busio
import board

#try:
#    print(i2c)
#except:
#    i2c = None
    
#if (i2c is None):
# i2c = busio.I2C(sda=board.GP12, scl=board.GP13)




#dummy class representing a generic sensor, not required
# class TMG():
#     def read_data(self):
#         time.sleep(0.001)
#         data = i2c.readfrom_mem(TMG_ADDR, 0x94, 9) #addr, memaddr, nbytes
#         time.sleep(0.004)
#         #FIX THIS HERE - see note on discord about checking for initialization. All zeros could be a valid measurement.
#         if data[8] == 0: #if the data is all zeros, the TMG hasn't been initialized. Checking the proximity bc that value is never zero, and sometimes the luminance is zero.
#             TMG_data.init_TMG(TMG_data)
#             data = i2c.readfrom_mem(TMG_ADDR, 0x94, 9) #try again after init
#             time.sleep(0.1)
#         #format into useful numbers
#         ir_lum = data[1] * 256.0 + data[0]
#         r_lum = data[3] * 256.0 + data[2]
#         g_lum = data[5] * 256.0 + data[4]
#         b_lum = data[7] * 256.0 + data[6]
#         proximity = data[8] #unused
#         return ir_lum, r_lum, g_lum, b_lum
    
class TMG_data():
    module_name = "TMG_sensor" #put the name of your sensor/project here
    # sensor = TMG()
    polling_interval = .5 #time between polls in seconds
    last_poll = time.monotonic()
    i2c = None

    def init_TMG(self):
        print(f"instance of {self.name} created")

    def setup(self):
        
        try:
            self.i2c = busio.I2C(sda=board.GP12, scl=board.GP13)
        except Exception as e:
            print(e)
        TMG_ADDR = 0x39
        time.sleep(0.004)
        
        if self.i2c is not None:
            while not self.i2c.try_lock():
                pass
        #i2c.writeto_mem(TMG_ADDR,0x80,bytearray([0x0F]))#addr, memaddr, buf
        #time.sleep(0.004)
        #i2c.writeto_mem(TMG_ADDR,0x81,bytearray([0x00]))
        #time.sleep(0.004)
        #i2c.writeto_mem(TMG_ADDR,0x83,bytearray([0xFF]))
        #time.sleep(0.004)
        #i2c.writeto_mem(TMG_ADDR,0x8F,bytearray([0x00]))
        #time.sleep(0.004)
        self.i2c.writeto(TMG_ADDR,bytearray([0x0F]),start = 0x80)#addr, memaddr, buf
        time.sleep(0.004)
        self.i2c.writeto(TMG_ADDR,bytearray([0x00]),start = 0x81)
        time.sleep(0.004)
        self.i2c.writeto(TMG_ADDR,bytearray([0xFF]),start = 0x83)
        time.sleep(0.004)
        self.i2c.writeto(TMG_ADDR,bytearray([0x00]),start = 0x8F)
        time.sleep(0.004)
        self.i2c.unlock()
       

#don't need to modify this
    def wrap_poll(self):
        if ((time.monotonic() - self.last_poll) > self.polling_interval):
            self.last_poll = time.monotonic()
            return self.poll()
        return None


    def poll(self):
        TMG_ADDR = 0x39
        time.sleep(0.001)
        data = self.i2c.readfrom(TMG_ADDR, 0x94, 9) #addr, memaddr, nbytes
        time.sleep(0.004)
        #FIX THIS HERE - see note on discord about checking for initialization. All zeros could be a valid measurement.
        if data[8] == 0: #if the data is all zeros, the TMG hasn't been initialized. Checking the proximity bc that value is never zero, and sometimes the luminance is zero.
            TMG_data.init_TMG(TMG_data)
            data = i2c.readfrom(TMG_ADDR, 0x94, 9) #try again after init
            time.sleep(0.1)
        #format into useful numbers
        ir_lum = data[1] * 256.0 + data[0]
        r_lum = data[3] * 256.0 + data[2]
        g_lum = data[5] * 256.0 + data[4]
        b_lum = data[7] * 256.0 + data[6]
        proximity = data[8] #unused
        return ir_lum, r_lum, g_lum, b_lum