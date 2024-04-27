# vpkextractor
**Based on [VPK](https://github.com/ValvePython/vpk) python library.**

Python script for extracring VPK (Valve Package) format files. <br>
Tested on Termux (Android) and Windows. (Python 3.12.1) 

# PIP required!

# Installation
**Termux**
```
pkg upgrade
pkg install git -y 
pkg install python -y 
git clone https://github.com/Dim1xs/vpkextractor.git
cd vpkextractor
pip3 install -r requirements.txt
```

# Using
```
cd vpkextractor
python extractor.py
```
## **Termux**
```
Write path to vpk: 
```
### If you want to get into **main phone storage**, always start your path with: <br>
#### *"/storage/emulated/0/"* <br>
### **Example:** <br>
#### *"/storage/emulated/0/vpks/hl2_misc_dir.vpk"* <br>
### Result:
```
Write path to vpk: /storage/emulated/0/vpks/hl2_misc_dir.vpk
```

[TERMUX VIDEO TUTORIAL | EN](https://youtu.be/yLzBlhhG-z8)

