#!/usr/bin/python -OO
import sys, commands, re, csv
if sys.version_info < (2, 5):
    print "Sorry, requires Python 2.5, 2.6 or 2.7."
    sys.exit(1)

# -- Changable Variables
# -- The below 'drive' variables will help us build your device string such as: /dev/ad4
drive_device = "ata"
drive_prefix = "ad"
drive_first_num = 14	# first drive number in your sequence
drive_last_num = 14	# last drive number in your sequence
drive_skip = 2		# if your drives skip x numbers between, Ex. 4, 6, 8 - would require a 2 here

# -- Should not need to change anything below here. --

while drive_first_num < drive_last_num + drive_skip:
    status, output = commands.getstatusoutput('smartctl -d ' + drive_device + ' -A /dev/' + drive_prefix + str(drive_first_num))

    if status == 0:
        print '----- Here is the SMART Data for \"' + drive_prefix + str(drive_first_num) + '\" -----'
#	re.sub('[ \t+]', ',', output)
#	output = output.replace("  ", ",")
        print output
    else:
        print "An error occured with a code of %r." % status
        print output
        quit()

    drive_first_num = drive_first_num + drive_skip
