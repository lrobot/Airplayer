import select
from pybonjour import pybonjour
import logging
import appletv

logger = logging.getLogger('airplayer')
str_raop = "_raop._tcp."

def register_service(name, regtype, port):
    record = str(pybonjour.TXTRecord(appletv.DEVICE_INFO))
    record1 = str(pybonjour.TXTRecord(appletv.raop_info))

    def register_callback(sdRef, flags, errorCode, name, regtype, domain):
        print "register_service callback:", sdRef, flags, errorCode, name, regtype, domain
        if errorCode == pybonjour.kDNSServiceErr_NoError:
            print "err reg:", errorCode
            logger.debug('Registered bonjour service %s.%s', name, regtype)
        print pybonjour.DNSServiceUpdateRecord(sdRef, None, rdata=record, ttl=1000)


    def register_callback1(sdRef, flags, errorCode, name, regtype, domain):
        print "register_service callback1:", sdRef, flags, errorCode, name, regtype, domain
        if errorCode == pybonjour.kDNSServiceErr_NoError:
            print "err reg:", errorCode
            logger.debug('Registered bonjour service %s.%s', name, regtype)
        print pybonjour.DNSServiceUpdateRecord(sdRef, None, rdata=record1, ttl=1000)

    service = pybonjour.DNSServiceRegister(name = appletv.Name,
                                         regtype = regtype,
                                         port = port,
                                         txtRecord = None,
                                         callBack = register_callback)
    print pybonjour.DNSServiceUpdateRecord(service, None, rdata=record, ttl=1000)


    service1 = pybonjour.DNSServiceRegister(name = appletv.MAC_ADDR.replace(":","") + "@" + appletv.Name,
                                         regtype = str_raop,
                                         port = port+1,
                                         txtRecord = None,
                                         callBack = register_callback1)
    print pybonjour.DNSServiceUpdateRecord(service1, None, rdata=str(record1), ttl=1000)

    print service, service1
    try:
        try:
            while True:
                ready = select.select([service,service1], [], [])
                print("*0", ready)
                if service in ready[0]:
                    print("*1")
                    pybonjour.DNSServiceProcessResult(service)
                if service1 in ready[0]:
                    print("*2")
                    pybonjour.DNSServiceProcessResult(service1)
        except KeyboardInterrupt:
            pass
    finally:
        service.close()