OUT_FOLDER=zonefiles

today_date=$(date +%Y_%m_%d)
out_name="$OUT_FOLDER/zonefile_$today_date.txt"

dig -k zonedata.key @zonedata.switch.ch +noall +answer +noidnout +onesoa AXFR ch. > $out_name
