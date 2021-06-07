py -m venv genshin-impact-venv
CALL genshin-impact-venv\Scripts\activate.bat
curl https://bootstrap.pypa.io/get-pip.py -o genshin-impact-venv\Scripts\get-pip.py
py genshin-impact-venv\Scripts\get-pip.py
pip install selenium