import sys
import argparse
import datetime

defaultNDays = 7

parser = argparse.ArgumentParser(prog = "argparser",
                                 description = "Python script to download logs and RIF files from GCP")
parser.add_argument("-hostlib",               action="store_true", help = "Download hostlib logs")
parser.add_argument("-devicelib",             action="store_true", help = "Download device logs")
parser.add_argument("-rif",                   action="store_true", help = "Download RIF files")
parser.add_argument("-startdate", type = str,                      help = "Start date in YYYYMMDD format")
parser.add_argument("-enddate",   type = str,                      help = "End date in YYYYMMDD format")
parser.add_argument("-ndays",     type = int,                      help = "Previous N days from now")

args = parser.parse_args()

if (args.startdate != None):
    args.startdate = datetime.datetime.strptime(args.startdate, "%Y%m%d").date()
if (args.enddate != None):
    args.enddate = datetime.datetime.strptime(args.enddate, "%Y%m%d").date()
    
if ((args.hostlib == False) and (args.devicelib == False) and (args.rif == False)):
    print ("FATAL: All the download files flags are False. Exit program.")
    sys.exit()
elif ((args.startdate == None) and (args.enddate == None)):
    if (args.ndays == None):
        print ("No start and end dates entered. Data from last %d days will be downloaded." %(defaultNDays))
        args.ndays = defaultNDays
        args.enddate = datetime.date.today()
        args.startdate = args.enddate - datetime.timedelta(days = defaultNDays)
    else:
        print ("Data from last %d days will be downloaded." %(args.ndays))
        args.enddate = datetime.date.today()
        args.startdate = args.enddate - datetime.timedelta(days = args.ndays)
elif ((args.startdate != None) and (args.enddate == None)):
    if (args.ndays == None):
        print ("No enddate and ndays entered. Data for next %d days from the startdate will be downloaded." %(defaultNDays))
        args.ndays = defaultNDays
        args.enddate = args.startdate + datetime.timedelta(days = defaultNDays)
    else:
        print ("No enddate entered. Data for next %d days from the startdate will be downloaded." %(args.ndays))
        args.enddate = args.startdate + datetime.timedelta(days = args.ndays)
elif ((args.startdate == None) and (args.enddate != None)):
    if (args.ndays == None):
        print ("No startdate and ndays entered. Data for previous %d days from the enddate will be downloaded." %(defaultNDays))
        args.ndays = defaultNDays
        args.startdate = args.enddate - datetime.timedelta(days = defaultNDays)
    else:
        print ("No startdate entered. Data for previous %d days from the enddate will be downloaded." %(args.ndays))
        args.startdate = args.enddate - datetime.timedelta(days = args.ndays)
else:
    if (args.startdate > args.enddate):
        print ("FATAL: startdate is bigger than enddate. Exit program.")
        sys.exit()
        
print (args)