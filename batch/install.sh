apt install -y ffmpeg

cd ../external
python3 get-pip.py

cd ../app
pip3 install imageio
pip3 install imutils
pip3 install imageio_ffmpeg

cd ../external/ingame_bf_api/bin
chmod 777 test_bulk

cd ../../../batch