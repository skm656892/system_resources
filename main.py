import psutil
import time
import datetime

def cpu():
    f = open("cpu_report.txt", "a+")
    datetime_object = datetime.datetime.now()
    f.write("start time : %s \n" % datetime_object)
    f.write("Physical cores: %d \n" % psutil.cpu_count(logical=False))
    f.write("Total cores: %d \n" % psutil.cpu_count(logical=True))
    cpufreq = psutil.cpu_freq()
    f.write("Max Frequency: %d Mhz \n" % cpufreq.max)
    f.write("Min Frequency: %d Mhz \n" % cpufreq.min)
    f.write("Current Frequency: %d Mhz \n" % cpufreq.current)
    f.write("CPU Usage Per Core: ")
    for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
        f.write("Core " + str(i) + ": %d Percent \n" % percentage)
    f.write("Total CPU Usage: %d Percent \n" % psutil.cpu_percent())
    f.write("=======end======= \n\n\n")
    f.close()

def ram():
    memory = psutil.virtual_memory()
    f = open("ram_report.txt", "a+")
    datetime_object = datetime.datetime.now()
    f.write("start time : %s \n" % datetime_object)
    f.write("Total: %d \n" % memory.total)
    f.write("Available: %d \n" % memory.available)
    f.write("Used: %d \n" % memory.used)
    f.write("Percentage: %d Percent \n" % memory.percent)
    # get the swap memory details (if exists)
    swap = psutil.swap_memory()
    f.write("Total: %d \n" % swap.used)
    f.write("Free: %d \n" % swap.used)
    f.write("Used: %d \n" % swap.used)
    f.write("Percentage: %d Percent \n" % swap.percent)
    f.write("=======end======= \n\n\n")
    f.close()

def disk():
    f = open("disk_report.txt", "a+")
    datetime_object = datetime.datetime.now()
    f.write("start time : %s \n" % datetime_object)

    partitions = psutil.disk_partitions()
    for partition in partitions:
        f.write(" === drive name: %s === \n" % partition.device)
        f.write("Mount point: %s \n" % partition.mountpoint)
        f.write("File system type: %s \n" % partition.fstype)
        try:
            partition_usage = psutil.disk_usage(partition.mountpoint)
        except PermissionError:
            continue
        f.write("Total Size: %s \n" % partition_usage.total)
        f.write("Used: %s \n" % partition_usage.used)
        f.write("Free: %s \n" % partition_usage.free)
        f.write("Percentage: %s  Percent\n" % partition_usage.percent)

    # get IO statistics since boot
    disk_io = psutil.disk_io_counters()
    f.write("Total read: %s \n" % disk_io.read_bytes)
    f.write("Total write: %s \n" % disk_io.write_bytes)

    f.write("=======end======= \n\n\n")
    f.close()


if __name__ == '__main__':
    repeat = input("Please Enter repeat (number)? ")
    delay = input("Please Enter delay (number)? ")
    for i in range(int(repeat)):
        cpu()
        ram()
        disk()
        time.sleep(int(delay))

    print("finish")


