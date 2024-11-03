# Ableton Hello World Control Surface

This is a skeleton for your Ableton Control Surface Python script

## View Ableton log

Here is the command to check Ableton logs

```
tail -f -n 500 "$HOME/Library/Preferences/Ableton/`ls $HOME/Library/Preferences/Ableton | sort -V | tail -n 1`/Log.txt"
```

## Install This Control Surface

```
git clone github.com/laimison/AbletonHelloWorldControlSurface.git

cp -r AbletonHelloWorldControlSurface "$HOME/Music/Ableton/User Library/Remote Scripts/AbletonHelloWorldControlSurface"
# or
ln -sf $HOME/Documents/git/AbletonHelloWorldControlSurface "$HOME/Music/Ableton/User Library/Remote Scripts/AbletonHelloWorldControlSurface"
```

## Restart Ableton and Check Logs

You should see line in Ableton log once you select this Control Surface in Ableton settings

```
2024-11-03T16:40:31.423584: info: Python: INFO:_Framework.ControlSurface:423 - LOG: (AbletonHelloWorldControlSurface) This is a message from AbletonHelloWorldControlSurface in Log.txt
```