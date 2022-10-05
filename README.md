# Picroft - using [Mycroft](https://mycroft.ai/) for Raspberry Pi 4 

- [ ] Get started with [Mycroft](https://mycroft.ai/get-started/)
- [ ] Get started with [Picroft](https://mycroft-ai.gitbook.io/docs/using-mycroft-ai/get-mycroft/picroft#getting-started-with-picroft)

## Installing Picroft ( Specifically packaged to run on Raspberry Pi 4, built on top of Raspbian Buster Lite ):

- [ ] Burn the disk image to the Micro SD card ( min. 8 GB )
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
git clone https://github.com/waveshare/WM8960-Audio-HAT.git
cd WM8960-Audio-Hat.git
sudo ./install.sh
```
      Then reboot

- [ ] List devices for audio output:

```
aplay -l
```
    
    You should get the output:

```
card 1: wm8960soundcard [wm8960-soundcard], device 0: bcm2835-i2s-wm8960-hifi wm8960-hifi-0 [bcm2835-i2s-wm8960-hifi wm8960-hifi-0]
```