echo "SSR Downloading"
wget -N --no-check-certificate https://softs.fun/Bash/ssrmu.sh && chmod +x ssrmu.sh
echo "Make Directory"
mkdir udp2raw
mkdir udpspeeder
cd udp2raw
echo "Udp2Raw Downloading"
wget https://github.com/wangyu-/udp2raw-tunnel/releases/download/20180225.0/udp2raw_binaries.tar.gz
echo "Extract Udp2Raw"
tar -zxvf udp2raw_binaries.tar.gz
cd ..
cd udpspeeder
echo "UdpSpeeder Downloading"
wget https://github.com/wangyu-/UDPspeeder/releases/download/v2%4020171125.0/speederv2_binaries.tar.gz
echo "Extract UdpSpeeder"
tar -zxvf speederv2_binaries.tar.gz
cd ..
echo "SSR Setting"
bash ssrmu.sh
echo "Udp2Raw Setting"
nohup ./udpspeeder/speederv2_amd64 -s -l0.0.0.0:28900 -r127.0.0.1:2333 -f2:4 -k "splatoon2" --mode 0 -q1 > udpspeeder.log 2>&1 &
echo "UdpSpeeder Setting"
nohup ./udp2raw/udp2raw_amd64 -s -l0.0.0.0:1024 -r127.0.0.1:28900 -a -k "splatoon2" --raw-mode faketcp > udp2raw.log 2>&1 &