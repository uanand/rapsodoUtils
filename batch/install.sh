apt install -y ffmpeg

cd ..
mkdir log

cd external
python3 get-pip.py

cd ../app
pip3 install imageio
pip3 install imutils
pip3 install imageio_ffmpeg

cd ../external

chmod 755 splitSpinCamRaw

unzip ingame_bf_api.zip
cd ingame_bf_api/bin
chmod 755 test_bulk

cd ../../../batch