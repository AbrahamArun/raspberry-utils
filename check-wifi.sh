pingip='google.com'
wlan='wlan0'
LOG_PATH='/home/pi/Desktop/log/network.log'
now=$(date +"%m-%d %r")

/bin/ping -c 2 -I $wlan $pingip > /dev/null 2> /dev/null
if [ $? -ge 1 ] ; then
  echo "No network connection, restarting wlan0"
  echo "$now Network is DOWN. Perform a reset" >> $LOG_PATH
  /sbin/ifdown $wlan
  sleep 5
  /sbin/ifup --force $wlan
else
  echo "$now Network is UP." >> $LOG_PATH
fi
