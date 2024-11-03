# Ableton Hello World Control Surface

This is a skeleton for your Ableton Control Surface Python script

The code is tested in Ableton 12.1

## Open Ableton Log

Here is the command to check Ableton log

```
tail -f -n 500 "$HOME/Library/Preferences/Ableton/`ls $HOME/Library/Preferences/Ableton | sort -V | tail -n 1`/Log.txt"
```

## Install This Control Surface

```
git clone https://github.com/laimison/AbletonHelloWorldControlSurface.git

cp -r AbletonHelloWorldControlSurface "$HOME/Music/Ableton/User Library/Remote Scripts/AbletonHelloWorldControlSurface"
# or
ln -sf $HOME/Documents/git/AbletonHelloWorldControlSurface "$HOME/Music/Ableton/User Library/Remote Scripts/AbletonHelloWorldControlSurface"
```

## Find Log Line

You should see line in Ableton log once you select AbletonHelloWorldControlSurface in Ableton settings

```
2024-11-03T16:40:31.423584: info: Python: INFO:_Framework.ControlSurface:423 - LOG: (AbletonHelloWorldControlSurface) This is a message from AbletonHelloWorldControlSurface in Log.txt
```

You can try to restart Ableton to produce this line as well
