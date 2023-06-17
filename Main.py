import sys
import time
import  multiprocessing
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import QRect, Qt, QTimer
import os
from PyQt5.QtWidgets import QApplication, QStackedWidget, QLabel, QPushButton, QFrame, QProgressBar, QScrollArea, \
    QWidget, QScrollBar, QVBoxLayout
import threading
import hwinfo



class window(QWidget):

    def __init__(self):
        super(window, self).__init__()

        self.setGeometry(250, 100, 1080, 750)
        self.setWindowTitle("Hardware Info")
        self.setFixedWidth(1080)
        self.setFixedHeight(750)
        self.setStyleSheet("background:black;")
        os.chdir(sys._MEIPASS)
        self.setWindowIcon(QtGui.QIcon("windowIcon.png"))

        self.stackedWidget = QStackedWidget(self)
        self.stackedWidget.setGeometry(QRect(0, 0, 1081, 751))

        self.widget_1()
        self.widget_2()

        self.stackedWidget.setCurrentIndex(0)



    def widget_1(self):
        widget = QWidget()

        scrollbar = QScrollBar()
        scrollbar.setStyleSheet("*::sub-line:vertical,*::add-line:vertical{border:none;background:none;}" + "*::handle:vertical{background:transparent;background-color:grey;}")

        scrollArea = QScrollArea(widget)
        scrollArea.setGeometry(QRect(0, 0, 1081, 751))
        scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scrollArea.setVerticalScrollBar(scrollbar)

        scrollareacontent = QWidget()
        scrollareacontent.setGeometry(QRect(0, 0, 1000, 1500))

        hw = hwinfo.gethwinfo()

        label = QLabel(scrollareacontent)
        label.setText("# CPU-INFO ")
        label.setGeometry(QRect(0,1,75,100))
        label.setStyleSheet("color:#ec0101;font-weight:bold;font-size:25px;padding:5px;")
        label.adjustSize()

        l1 = QLabel(scrollareacontent)
        l1.setText("CPU : " + hw.processor_brand)
        l1.setGeometry(QRect(0, 50, 75, 100))
        l1.setStyleSheet("color:white;font-size:21px;padding:5px;font-weight:bold;")
        l1.adjustSize()

        l2 = QLabel(scrollareacontent)
        l2.setText("Architecture : " + hw.arch)
        l2.setGeometry(QRect(0,100, 75, 100))
        l2.setStyleSheet("color:white;font-size:21px;padding:5px;font-weight:bold;")
        l2.adjustSize()

        l3 = QLabel(scrollareacontent)
        l3.setText("Vendor_Id : "+hw.vendor_id)
        l3.setGeometry(QRect(0, 150, 75, 100))
        l3.setStyleSheet("color:white;font-size:21px;padding:5px;font-weight:bold;")
        l3.adjustSize()

        l4 = QLabel(scrollareacontent)
        l4.setText("Cores : " + hw.core)
        l4.setGeometry(QRect(0, 200, 75, 100))
        l4.setStyleSheet("color:white;font-size:21px;padding:5px;font-weight:bold;")
        l4.adjustSize()

        l5 = QLabel(scrollareacontent)
        l5.setText("Threads : " + hw.thread)
        l5.setGeometry(QRect(0, 250, 75, 100))
        l5.setStyleSheet("color:white;font-size:21px;padding:5px;font-weight:bold;")
        l5.adjustSize()

        l6 = QLabel(scrollareacontent)
        l6.setText("CPU_Architecture : " + hw.cpuarch)
        l6.setGeometry(QRect(0, 300, 75, 100))
        l6.setStyleSheet("color:white;font-size:21px;padding:5px;font-weight:bold;")
        l6.adjustSize()

        l7 = QLabel(scrollareacontent)
        l7.setText("L2Cache : " + hw.l2cache+"MB")
        l7.setGeometry(QRect(0, 350, 75, 100))
        l7.setStyleSheet("color:white;font-size:21px;padding:5px;font-weight:bold;")
        l7.adjustSize()

        l8 = QLabel(scrollareacontent)
        l8.setText("L3Cache : " + hw.l3cache+"MB")
        l8.setGeometry(QRect(0, 400, 75, 100))
        l8.setStyleSheet("color:white;font-size:21px;padding:5px;font-weight:bold;")
        l8.adjustSize()

        l9= QLabel(scrollareacontent)
        l9.setText("CPU_Maxfrq : " + hw.cpu_maxfrq)
        l9.setGeometry(QRect(0, 450, 75, 100))
        l9.setStyleSheet("color:white;font-size:21px;padding:5px;font-weight:bold;")
        l9.adjustSize()

        l10 = QLabel(scrollareacontent)
        l10.setText("CPU_CurrentFrq  ")
        l10.setGeometry(QRect(0, 500, 75, 100))
        l10.setStyleSheet("color:white;font-size:21px;padding:5px;font-weight:bold;")
        l10.adjustSize()

        l11 = QLabel(scrollareacontent)
        l11.setText(hw.cpu_currentfrq)
        l11.setGeometry(QRect(550, 500, 75, 100))
        l11.setStyleSheet("color:white;font-size:15px;padding:5px;")
        l11.adjustSize()

        probar = QProgressBar(scrollareacontent)
        probar.setGeometry(QRect(195, 505, 350, 25))
        probar.setProperty('value', hw.cpu_frqpercent)
        probar.setStyleSheet("color:black;text-align:center;")


        button=QPushButton(scrollareacontent)
        button.setText("CPU USAGE")
        button.setGeometry(QRect(750,350,75,100))
        button.setStyleSheet("*{background-color:black;color:white;padding:21px;font-weight:bold;font-size:19px;border:3px solid red;border-radius:33px;}"+"*:hover{background-color:red;color:black;border:3px solid #ec0101;}")
        button.adjustSize()
        button.clicked.connect(self.widgetchange)


        hline=QFrame(scrollareacontent)
        hline.setGeometry(QRect(100,590,850,100))
        hline.setFrameShape(QFrame.HLine)
        hline.setFrameShadow(QFrame.Sunken)
        hline.setFixedHeight(3)
        hline.setStyleSheet("background-color:white;")

        label1 = QLabel(scrollareacontent)
        label1.setText("# Battery-INFO ")
        label1.setGeometry(QRect(0, 650, 75, 100))
        label1.setStyleSheet("color:#ec0101;font-weight:bold;font-size:25px;padding:5px;")
        label1.adjustSize()

        l12 = QLabel(scrollareacontent)
        l12.setText("Battery Percent : "+str(hw.battery[0])+"%")
        l12.setGeometry(QRect(0, 700, 75, 100))
        l12.setStyleSheet("color:white;font-size:21px;padding:5px;font-weight:bold;")
        l12.adjustSize()

        l13 = QLabel(scrollareacontent)
        l13.setText("Time left : " + str("%.2f" %(hw.battery[1]/60/60)) + "Hrs")
        l13.setGeometry(QRect(0, 750, 75, 100))
        l13.setStyleSheet("color:white;font-size:21px;padding:5px;font-weight:bold;")
        l13.adjustSize()


        l14 = QLabel(scrollareacontent)
        l14.setText("PowerPlugged : " + str(hw.battery[2]))
        l14.setGeometry(QRect(0, 800, 75, 100))
        l14.setStyleSheet("color:white;font-size:21px;padding:5px;font-weight:bold;")
        l14.adjustSize()

        hline1 = QFrame(scrollareacontent)
        hline1.setGeometry(QRect(100, 890, 850, 100))
        hline1.setFrameShape(QFrame.HLine)
        hline1.setFrameShadow(QFrame.Sunken)
        hline1.setFixedHeight(3)
        hline1.setStyleSheet("background-color:white;")

        label2 = QLabel(scrollareacontent)
        label2.setText("# Disk-INFO ")
        label2.setGeometry(QRect(0, 900, 75, 100))
        label2.setStyleSheet("color:#ec0101;font-weight:bold;font-size:25px;padding:5px;")
        label2.adjustSize()

        disks=hw.disk_partition
        x = 950
        for disk in range(len(disks)):
            x=x+(50*disk)
            disku="disk"+str(disk)
            disku = QLabel(scrollareacontent)
            disku.setText("Disk path : " + str(hw.disk_partition[disk][0]))
            disku.setGeometry(QRect(0, x, 75, 100))
            disku.setStyleSheet("color:white;font-size:21px;padding:5px;font-weight:bold;")
            disku .adjustSize()

            diskz = "disk" + str(disk)+"l"
            diskz = QLabel(scrollareacontent)
            diskz.setText("Disk fstype : " + str(hw.disk_partition[disk][2]))
            diskz.setGeometry(QRect(0, x+50, 75, 100))
            diskz.setStyleSheet("color:white;font-size:21px;padding:5px;font-weight:bold;")
            diskz.adjustSize()

            disk_usage=hw.disk_usage(hw.disk_partition[disk][0])

            diskx = "disk" + str(disk) + "l1"
            diskx = QLabel(scrollareacontent)
            diskx.setText("Total Memory : " + str("%.2f" % (disk_usage[0]/1024/1024/1024))+" GB")
            diskx.setGeometry(QRect(0, x+100, 75, 100))
            diskx.setStyleSheet("color:white;font-size:21px;padding:5px;font-weight:bold;")
            diskx.adjustSize()

            disky = "disk" + str(disk) + "l2"
            disky = QLabel(scrollareacontent)
            disky.setText("Memory Used : " + str("%.2f" % (disk_usage[1]/1024/1024/1024))+" GB")
            disky.setGeometry(QRect(0, x+150, 75, 100))
            disky.setStyleSheet("color:white;font-size:21px;padding:5px;font-weight:bold;")
            disky.adjustSize()

            diskyz = "disk" + str(disk) + "l3"
            diskyz= QLabel(scrollareacontent)
            diskyz.setText("Memory free ")
            diskyz.setGeometry(QRect(0, x+200, 75, 100))
            diskyz.setStyleSheet("color:white;font-size:21px;padding:5px;font-weight:bold;")
            diskyz.adjustSize()

            probar = "disk"+str(disk)+"probar"
            probar = QProgressBar(scrollareacontent)
            probar.setProperty('value', disk_usage[3])
            probar.setGeometry(QRect(159,x+3+200,350,25))
            probar.setStyleSheet("color:black;text-align:center;")

            diskxz = "disk" + str(disk) + "l4"
            diskxz = QLabel(scrollareacontent)
            diskxz.setText(str("%.2f"  %(disk_usage[2]/1024/1024/1024))+" GB")
            diskxz.setGeometry(QRect(530, x+200, 75, 100))
            diskxz.setStyleSheet("color:white;font-size:19px;padding:5px;")
            diskxz.adjustSize()

        hline2 = QFrame(scrollareacontent)
        hline2.setGeometry(QRect(100, x+90+200, 850, 100))
        hline2.setFrameShape(QFrame.HLine)
        hline2.setFrameShadow(QFrame.Sunken)
        hline2.setFixedHeight(3)
        hline2.setStyleSheet("background-color:white;")

        label3 = QLabel(scrollareacontent)
        label3.setText("# RAM-INFO ")
        label3.setGeometry(QRect(0, x+300, 75, 100))
        label3.setStyleSheet("color:#ec0101;font-weight:bold;font-size:25px;padding:5px;")
        label3.adjustSize()

        lz1 = QLabel(scrollareacontent)
        lz1.setText("RAM Memory : " + hw.r_mem)
        lz1.setGeometry(QRect(0, x+350, 75, 100))
        lz1.setStyleSheet("color:white;font-size:21px;padding:5px;font-weight:bold;")
        lz1.adjustSize()

        lz2 = QLabel(scrollareacontent)
        lz2.setText("RAM Used : " + hw.r_used)
        lz2.setGeometry(QRect(0, x + 400, 75, 100))
        lz2.setStyleSheet("color:white;font-size:21px;padding:5px;font-weight:bold;")
        lz2.adjustSize()

        lz3 = QLabel(scrollareacontent)
        lz3.setText("RAM Usage : ")
        lz3.setGeometry(QRect(0, x + 450, 75, 100))
        lz3.setStyleSheet("color:white;font-size:21px;padding:5px;font-weight:bold;")
        lz3.adjustSize()

        lz4 = QLabel(scrollareacontent)
        lz4.setText(hw.r_free)
        lz4.setGeometry(QRect(530, x + 450, 75, 100))
        lz4.setStyleSheet("color:white;font-size:19px;padding:5px;")
        lz4.adjustSize()


        probar_r = QProgressBar(scrollareacontent)
        probar_r.setProperty('value', hw.r_usageperc)
        probar_r.setGeometry(QRect(159, x + 3 + 450, 350, 25))
        probar_r.setStyleSheet("color:black;text-align:center;")

        scrollareacontent.setGeometry(QRect(0, 0, 1000, x+550))

        def getcurrentusage():
            while True:
                lz2.setText("RAM Used : " + hw.rused())
                lz2.adjustSize()
                lz4.setText(hw.rfree())
                lz4.adjustSize()
                probar_r.setProperty('value', hw.r_perc())
                l12.setText("Battery Percent : " + hw.batteryu(1) + "%")
                l14.setText("PowerPlugged : " + hw.batteryu(0))
                l12.adjustSize()
                l14.adjustSize()
                probar.setProperty('value', hw.cpufrq(1))
                l11.setText(hw.cpufrq(0))
                l11.adjustSize()
                time.sleep(5.5)


        thread1 = threading.Thread(target=getcurrentusage)
        thread1.daemon=True
        thread1.start()

        scrollArea.setWidget(scrollareacontent)
        self.stackedWidget.addWidget(widget)

    def widgetchange(self):
        self.stackedWidget.setCurrentIndex(1)

    def widgetchange_1(self):
        self.stackedWidget.setCurrentIndex(0)

    def widget_2(self):
        widget1=QWidget()

        scrollbar=QScrollBar()
        scrollbar.setStyleSheet("*::sub-line:vertical,*::add-line:vertical{border:none;background:none;}"+"*::handle:vertical{background:transparent;background-color:grey;}")

        scrollArea = QScrollArea(widget1)
        scrollArea.setGeometry(QRect(0, 0, 1081, 751))
        scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scrollArea.setVerticalScrollBar(scrollbar)

        scrollareacontent = QWidget()
        scrollareacontent.setGeometry(QRect(0, 0, 1000, 951))


        hw = hwinfo.gethwinfo()

        backbuttonimg=QtGui.QIcon('previous.png')
        backbutton=QPushButton(scrollareacontent)
        backbutton.setIcon(backbuttonimg)
        backbutton.setIconSize(QtCore.QSize(50,50))
        backbutton.setGeometry(0,1,50,50)
        backbutton.setStyleSheet("background-color:white;border:3px solid black;border-radius:25px;")
        backbutton.clicked.connect(self.widgetchange_1)

        label = QLabel(scrollareacontent)
        label.setText("# CPU-USAGE ")
        label.setGeometry(QRect(0, 50, 75, 100))
        label.setStyleSheet("color:#ec0101;font-weight:bold;font-size:25px;padding:5px;")
        label.adjustSize()

        prolabel = QLabel(scrollareacontent)
        prolabel.setText("CPU_Usage ")
        prolabel.setGeometry(QRect(0, 100, 75, 100))
        prolabel.setStyleSheet("color:white;font-weight:bold;font-size:21px;padding:5px;")
        prolabel.adjustSize()

        probar=QProgressBar(scrollareacontent)
        probar.setGeometry(QRect(150,101,350,25))
        probar.setProperty('value',hw.cpu_usage)
        probar.setStyleSheet("color:white;")
        probarls=[]
        for x in range(len(hw.cpu_coreusagethreads)):
            y=150
            lablex='core'+str(x)
            labelx = QLabel(scrollareacontent)
            labelx.setText("Core#"+str(x))

            labelx.setStyleSheet("color:white;font-weight:bold;font-size:21px;padding:5px;")


            probarx='core'+str(x)
            probarx = QProgressBar(scrollareacontent)
            probarls.append(probarx)
            probarx.setProperty('value', hw.cpu_coreusagethreads[x])
            probarx.setStyleSheet("color:white;")
            if x==0:
                labelx.setGeometry(QRect(0, y, 75, 100))
                probarx.setGeometry(QRect(150, y + 1, 350, 25))
                labelx.adjustSize()
            else:
                labelx.setGeometry(QRect(0, y+(50*x), 75, 100))
                probarx.setGeometry(QRect(150, y+1+(50*x), 350, 25))
                labelx.adjustSize()


        def getcurrentusagecore():
            while True:
                core_usage=hw.cpufrq(2)
                for x in range(len(probarls)):
                    probarls[x].setProperty('value', core_usage[x])

                time.sleep(15)

        thread2 = threading.Thread(target=getcurrentusagecore)
        thread2.daemon = True
        thread2.start()

        scrollArea.setWidget(scrollareacontent)
        self.stackedWidget.addWidget(widget1)


class splashScreen(QWidget):
    def __init__(self):
        super(splashScreen, self).__init__()
        self.setWindowTitle("Splash Screen")
        self.setFixedSize(1100,500)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.x=0
        self.widget()
        self.timer=QTimer()
        self.timer.timeout.connect(self.load)
        self.timer.start()

    def widget(self):
        layout=QVBoxLayout()
        self.setLayout(layout)

        self.frame=QFrame()
        self.frame.setStyleSheet("background-color:#393e46;")#6a1287
        layout.addWidget(self.frame)

        lable=QLabel(self.frame)
        lable.setText("Hardware Info")
        lable.setGeometry(QRect(255,100,550,31))
        lable.setStyleSheet("color:#f50ff5;font-weight:bold;font-family:sans-serif;font-size:39px;")
        lable.setAlignment(Qt.AlignCenter)


        self.probar=QProgressBar(self.frame)
        self.probar.setAlignment(Qt.AlignCenter)
        self.probar.setGeometry(QRect(170,215,750,25))
        self.setStyleSheet("*{color:white;border-radius:10px;text-align:center;}"+"*::chunk{border-radius:10px;background-color:qlineargradient(spread:pad x1:0,x2:1,y1:0.515364,y2:0.523,stop:0 #b34bff,stop:1 #01feff);}")#qlineargradient(90deg,#ffd33d,#ea4aaa 17%,#b34bff 34%,#01feff 51%,#ffd33d 68%,#ea4aaa 85%,#b34bff)
        self.probar.setValue(20)

        lable1 = QLabel(self.frame)
        lable1.setText("Loading.....")
        lable1.setGeometry(QRect(255,270, 550, 31))
        lable1.setStyleSheet("color:#ea4aaa;font-weight:bold;font-size:19px;")
        lable1.setAlignment(Qt.AlignCenter)

        lable2 = QLabel(self.frame)
        lable2.setText("# Getting System info")
        lable2.setGeometry(QRect(255, 325, 550, 31))
        lable2.setStyleSheet("color:#01feff;font-weight:bold;font-size:21px;")
        lable2.setAlignment(Qt.AlignCenter)

        def get():
            hw= hwinfo.gethwinfo()
            hw.processor_brand

        thread=threading.Thread(target=get)
        thread.daemon=True
        thread.start()

    def load(self):
        self.probar.setValue(self.x)
        if self.x==100:
            self.timer.stop()
            self.close()
            self.Mainwindow=window()
            self.Mainwindow.show()
        time.sleep(0.05)
        self.x=self.x+1




if __name__=="__main__":

  multiprocessing.freeze_support()

  app = QApplication([])
  win = splashScreen()
  win.show()
  sys.exit(app.exec_())
