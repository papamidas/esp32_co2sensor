from machine import Pin, I2C
import utime

VZ89TE_Address = 0x70
VZ89TE_CMD_GETSTATUS = bytes([0xC,0,0,0,0,0xF3])
VZ89TE_CMD_GETREVISION = bytes([0xD,0,0,0,0,0xF2])
VZ89TE_CMD_GETR0 = bytes([0x10,0,0,0,0,0xEF])
VZ_89TE_DATE_CODE = 0x0D

class VZ89TE:
    
    def __init__(self, i2c_bus=None, addr=VZ89TE_Address):
        self._i2c = i2c_bus
        self._i2c_addr = addr
        self._d = bytes([0,0,0,0,0,0,0])
        self._crc = 0
        if i2c_bus is None:
          raise ValueError('An I2C object is required.')
    
    def calcCrc(self, _d):
        _sum = 0
        self._crc = 0
        for _b in _d[:-1]:
            _sum += _b
        self._crc = _sum % 256
        self._crc += _sum // 0x100
        self._crc = 0xff-self._crc
        return self._crc
    
    def getAddr(self):
        return self._i2c_addr
    
    def cmdGetStatus(self):
        self._acks = self._i2c.writeto(self._i2c_addr,VZ89TE_CMD_GETSTATUS)
        #print("Acks: ", self._acks)
        utime.sleep_ms(100)
        self._d = self._i2c.readfrom(self._i2c_addr, 7)
        self.calcCrc(self._d)
        #print("CRC empfangen: ", self._rd[-1], " CRC berechnet: ", self._crc)
        #for b in self._rd:
        #    print(" ", hex(b))
        if(self._d[-1] != self._crc):
            raise ValueError('crc error.')
        return self._d
    
    def getData(self):
        self.cmdGetStatus()
        self.tVOC = (self._d[0]-13)*1000/229
        self.CO2 = (self._d[1]-13) * 1600/229 + 400
        self.Res = 10 *(self._d[4]+256*self._d[3])+65536*self._d[2]
        self.ErrStatus = self._d[5]
        return { "tVOC": self.tVOC,
                 "CO2": self.CO2,
                 "Res": self.Res,
                 "ErrStatus": self.ErrStatus }

    def cmdGetRevision(self):
        self._i2c.writeto(self._i2c_addr,VZ89TE_CMD_GETREVISION)
        utime.sleep_ms(100)
        self._r = self._i2c.readfrom(self._i2c_addr, 7)
        self.calcCrc(self._r)
        if(self._r[-1] != self._crc):
            raise ValueError('crc error.')
        return self._r
    
    def getRevision(self):
        self.cmdGetRevision()
        self.year = self._r[0]
        self.month = self._r[1]
        self.day = self._r[2]
        self.charter = self._r[3]
        return { "Year": self.year,
                 "Month": self.month,
                 "Day": self.day,
                 "Charter": self.charter }

    def cmdGetR0(self):
        self._i2c.writeto(self._i2c_addr,VZ89TE_CMD_GETR0)
        utime.sleep_ms(100)
        self._r0 = self._i2c.readfrom(self._i2c_addr, 7)
        self.calcCrc(self._r0)
        if(self._r0[-1] != self._crc):
            raise ValueError('crc error.')
        return self._r0
    
    def getR0(self):
        self.cmdGetR0()
        return self._r0[0] + 256 * self._r0[1]

    
