ping -c4 192.168.1.1 > /dev/null

# interface to check
wlan='wlan0'
LOG_PATH='/home/pi/Desktop/log/network.log'
now=$(date +"%m-%d %r")

if [ $? != 0 ]
then
  echo "No network connection, restarting wlan0"
  echo "$now Network is DOWN. Perform a reset" >> $LOG_PATH
  /sbin/ifdown $wlan
  sleep 5
  /sbin/ifup --force $wlan
else
  echo "$now Network is UP." >> $LOG_PATH
fi
