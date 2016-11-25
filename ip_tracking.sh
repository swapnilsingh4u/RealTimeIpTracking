sudo netstat -antp | grep ESTA | cut -d " " -f 23 | grep . >ip_port.txt
sudo netstat -antp | awk '/ESTA/ {print $7}' >process.txt
cat ip_port.txt | cut -d ":" -f 1 >onlyip.txt
#cat ip_port.txt | cut -d ":" -f 2 >onlyport.txt
#cat ii.txt | grep IP >ipaddress.txt
python ip3.py >ip3.txt
cat ip3.txt | grep Country: | awk '{print $2,$3}' | sed "/\b\(Hostname\)\b/d" >country.txt
cat ip3.txt | grep City | awk '{print $2,$3}' | sed "/\b\(Lat\|Hostname\)\b/d" | cut -d ":" -f 2 >city.txt
python desc.py
rm ip_port.txt onlyip.txt country.txt city.txt process.txt ip3.txt

