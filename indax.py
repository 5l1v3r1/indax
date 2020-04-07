import xml.dom.minidom as minidom
import os,sys
global pilih

def main():
    os.system('cls')
    doc = minidom.parse("src/jakarta/dki.xml")
    waktu = doc.getElementsByTagName("timestamp")[0].firstChild.data
    tahun = doc.getElementsByTagName("year")[0].firstChild.data
    bulan = doc.getElementsByTagName("month")[0].firstChild.data
    hari = doc.getElementsByTagName("day")[0].firstChild.data
    jam = doc.getElementsByTagName("hour")[0].firstChild.data
    menit = doc.getElementsByTagName("minute")[0].firstChild.data
    detik = doc.getElementsByTagName("second")[0].firstChild.data
    listdaerah = doc.getElementsByTagName("area")
    temperatur = doc.getElementsByTagName("parameter")

    print
    print "-------------------------"
    print """    INFO BMKG UPDATED    """
    print
    print "versi : "+waktu
    print ("Tahun: {}\nBulan: {}\nHari: {}\nJam: {}\nMenit: {}\nDetik: {}\n".format(tahun, bulan, hari, jam, menit, detik))
    print "-------------------------"
    print ("Mendapatkan {} data Daerah:".format(len(listdaerah)))
 
    for daerah in listdaerah:
        print
        print "KOTA ID    : ", daerah.getAttribute("id")
        print "NAMA KOTA  : ", daerah.getAttribute("description")
        print "Kordinator : ", daerah.getAttribute("coordinate")
        print
    pilih()

def pilih():
    while True:
     try:
         x = int(raw_input("Silahkan isi ID daerah: "))
         break
     except KeyboardInterrupt:
         print "\n CTRL+C DETECTED"
         exit()
     except ValueError:
         print "ERROR 2: Isikan Hanya Angka!"
     else:
         print "ID TIDAK DITEMUKAN!!"

	
    if x.lower() not in ('501192', '501195', '501193', '501191', '501196', '501194'):
        print("ERROR 1: ID TIDAK DITEMUKAN!!")
    elif int(x) == 501192:
    	jakbar()
    elif int(x) == 501195:
    	jakpus()
    elif int(x) == 501193:
    	jaksel()
    elif int(x) == 501191:
    	jaktim()
    elif int(x) == 501196:
    	jakut()
    elif int(x) == 501194:
    	kepuser()
    	
if __name__ == "__main__":
    main()
