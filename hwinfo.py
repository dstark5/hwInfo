import psutil
import cpuinfo


class gethwinfo():
    def __init__(self):
        self.cpu = cpuinfo.get_cpu_info()
        self.processor_brand = self.cpu['brand_raw']
        self.vendor_id = self.cpu['vendor_id_raw']
        self.arch = self.cpu['arch']
        self.cpuarch = self.cpu['arch_string_raw']
        self.l2cache = str(int((self.cpu['l2_cache_size']) / 1024 / 1024))
        self.l3cache = str(int((self.cpu['l3_cache_size']) / 1024 / 1024))
        self.core = str(psutil.cpu_count(logical=False))
        self.thread = str(psutil.cpu_count())
        self.cpu_maxfrq = str(psutil.cpu_freq().max) + "MHz"
        self.cpu_minfrq = str(psutil.cpu_freq().min) + "MHz"
        self.cpu_currentfrq = str(psutil.cpu_freq().current) + "MHz"
        self.cpu_usage = psutil.cpu_percent()
        self.cpu_coreusagethreads = psutil.cpu_percent(percpu=True, interval=1)
        self.disk_partition = psutil.disk_partitions()
        self.battery = psutil.sensors_battery()
        self.cpu_frqpercent = ((psutil.cpu_freq().current / psutil.cpu_freq().max) * 100)
        self.r_mem = str("%.2f" % (psutil.virtual_memory()[0] / 1024 / 1024 / 1024)) + " GB"
        self.r_usageperc = psutil.virtual_memory()[2]
        self.r_used=str("%.2f" % ((psutil.virtual_memory()[0]-psutil.virtual_memory()[4])/1024/1024/1024))+" GB"
        self.r_free = str("%.2f" % (psutil.virtual_memory()[4] / 1024 / 1024 / 1024)) + " GB"


    def disk_usage(self, path):
        self.disk_usage = psutil.disk_usage(path)
        return self.disk_usage

    def r_perc(self):
        return psutil.virtual_memory()[2]

    def rfree(self):
        return str("%.2f" % (psutil.virtual_memory()[4] / 1024 / 1024 / 1024)) + " GB"

    def rused(self):
        return  str("%.2f" % ((psutil.virtual_memory()[0] - psutil.virtual_memory()[4]) / 1024 / 1024 / 1024)) + " GB"
    def batteryu(self,x):
        if x==1:
            return str(psutil.sensors_battery()[0])
        else:
            return str(psutil.sensors_battery()[2])
    def cpufrq(self,x):
        if x==1:
            return ((psutil.cpu_freq().current / psutil.cpu_freq().max) * 100)
        if x==0:
            return str(psutil.cpu_freq().current) + "MHz"
        else:
            return psutil.cpu_percent(percpu=True, interval=0.5)


