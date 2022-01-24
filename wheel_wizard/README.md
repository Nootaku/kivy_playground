# Wheel WheelWizard

## Install dependency

```shell
pip install kivy
pip install kivymd
pip install ffpyplayer
pip install buildozer
```

## Create an Android APK

**_Step 1: Edit the `buildozer.spec` file_**

Open `buildozer.spec`.

- on line 15:

```
# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,otf,mp4
```

- on line 37:

```
# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy,ffpyplayer,ffmpeg,kivymd
```

**_Step 2: Run buildozer_**

```shell
cd wheel_wizard
buildozer init
buildozer android debug run
```

## Problems to be tackled

Add videos to the list without putting them on GitHub
