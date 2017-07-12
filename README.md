# raspberry-utils

## check-wifi.sh
Periodically check the WiFi connection, if it is down, restart the network to establish the connection again.

### Make it run periodically
Open your crontab config `crontab -e`
And enter the following
`*/5 * * * * /usr/bin/sudo -H /usr/local/bin/checkwifi.sh >> /dev/null 2>&1`

### Run this on boot
You can define things to run on boot in `/etc/rc.local`

DO NOT forget "&" otherwise it will not run in a paralle process and you might be
locked out of yout Pi! e.g. `python3 /home/pi/camera.py &`
