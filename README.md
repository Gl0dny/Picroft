# Learning [Mycroft](https://mycroft.ai/) on Raspberry Pi 4

The repository contains simple skills code for my [robot](https://github.com/Gl0dny/2-Wheeled-Autonomous-Robot).

The objective is to send POST requests via Flask server running on the main robot platform that are going to run specific scripts.

## Picroft - using Mycroft for Raspberry Pi 4 

- [ ] Get started with [Mycroft](https://mycroft.ai/get-started/)
- [ ] Get started with [Picroft](https://mycroft-ai.gitbook.io/docs/using-mycroft-ai/get-mycroft/picroft#getting-started-with-picroft)

## Installing Picroft ( Specifically packaged to run on Raspberry Pi 4, built on top of Raspbian Buster Lite ):

- [ ] Burn the disk image to the Micro SD card ( min. 8 GB space )
- [ ] Set up your Raspberry Pi ( Wi-Fi, ssh etc. ) with a Picroft img.
- [ ] Boot up Picroft and let the software guide you trough set up/ update phase.
- [ ] Set the HARDWARE SETUP according to your hardware.
- [ ] Update && upgrade your system.
- [ ] Reboot

## Installing and testing [ReSpeaker Pi v1.1 ( 2 mics )](https://wiki.seeedstudio.com/ReSpeaker_2_Mics_Pi_HAT/)

- [ ] Mount your Hat on top of a Raspberry Pi and connect a speaker via JST connector.
      You should connect the power via micro-usb connector on the HAT in case you want to use a speaker.
- [ ] Set the HARDWARE SETUP for:
3) USB audio
- [ ] Install audio drivers for the Hat:

```
git clone https://github.com/respeaker/seeed-voicecard
cd seeed-voicecard
sudo ./install.sh
```
- [ ] Reboot



- [ ] List devices for audio output:

```
aplay -l
```
    
You should get the output:

```
card 1: seeed2micvoicec [seeed-2mic-voicecard], device 0: bcm2835-i2s-wm8960-hifi wm8960-hifi-0 [bcm2835-i2s-wm8960-hifi wm8960-hifi-0]
```

- [ ] List device for audio input:

```
arecord -l
```

You should get the output:

```
card 1: seeed2micvoicec [seeed-2mic-voicecard], device 0: bcm2835-i2s-wm8960-hifi wm8960-hifi-0 [bcm2835-i2s-wm8960-hifi wm8960-hifi-0]
```

- [ ] Test the hardware using ALSA:

``` 
aplay -D playback /usr/share/sounds/alsa/<file>
```

## Connect Mycroft with a sound card

- [ ] Edit Mycroft config:

```
sudo nano /etc/mycroft/mycroft.conf
```

In the file substitute ( headphones output ):

```
"play_wav_cmdline": "aplay -Dhw:0,0 %1".
"play_mp3_cmdline": "mpg123 -a hw:0,0 %1",
```

with a:

```
"play_wav_cmdline": "aplay -Dplayback %1".
"play_mp3_cmdline": "mpg123 -a playback %1",
```

- [ ] Reboot

## Pairing up device

- [ ] [Register]("https://sso.mycroft.ai/login?redirect=https:%2F%2Fhome.mycroft.ai%2F) and pair the device 

Once you have paired your Mycroft Device, pairing information is stored in:

```
~/.config/mycroft/identity/identity2.json 
```

You should move the old config file to a proper directory:
```
mv /home/pi/.mycroft/mycroft.conf /home/pi/.config/mycroft/
```

## Testing if Mycroft is working

- [ ] Test the hardware by following Mycroft guide.

Restarting Mycroft's services:
```
~/mycroft-core/start-mycroft.sh restart all
```

Using the CLI:
```
mycroft-cli-client
```
or
```
mycroft-start debug
```

Using the microphone outside of Mycroft:
```
arecord -f cd -Dhw:1 test.wav
aplay -Dhw:1 test.wav
```

Audio test:
```
mycroft-start audiotest
```

Specyfing input device:
```
mycroft-start audiotest -l
```

A specific device can be added to your user level configuration file using the Configuration Manager by running:
```
mycroft-config set listener.device_name "DEVICE_NAME"
```
Where "DEVICE_NAME" is taken from the audio device output. Note the "(hw:1,0)" is not required.