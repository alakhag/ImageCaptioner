# ImageCaptioner
### What is this repository for? ###

An Image Captioning chatbot on Telegram chat application.

### How do I get set up? ###

For setting up, you need Torch, Telegram's python libraries along with their dependencies installed. Steps are as follows.
(You would require Anaconda2 installed on your PC.)

```bash
$ curl -s https://raw.githubusercontent.com/torch/ezinstall/master/install-deps | bash
$ git clone https://github.com/torch/distro.git ~/torch --recursive
$ cd ~/torch; 
$ ./install.sh      # and enter "yes" at the end to modify your bashrc
$ source ~/.bashrc* Database configuration
$ luarocks install nn
$ luarocks install nngraph 
$ luarocks install image 
$ luarocks install cutorch
$ luarocks install cunn
```

```bash
$ pip install python-telegram-bot --upgrade
$ sudo apt-get install fswebcam
```

* How to run tests 

Create "model" and "screenshot" directories in "img_caption_bot" directory

Install Telegram app on your mobile. Create your account and search for user : @BotFather

To create your Image Captioner chat app, message as follows:

> /start
>
> /newbot
>
> Image Captioner
>
> <a unique username ending with `bot`> # Remember it, also note the API Token

* Deployment instructions

Clone this repository on your system. Download the [pretrained model checkpoint](http://cs.stanford.edu/people/karpathy/neuraltalk2/checkpoint_v1_cpu.zip) and extract it in "model" folder, which is currently empty.

Create key.py and type `TOKEN = <your bot token>`

Run `python main.py`

Open Telegram and search for the username of your chat app.

start with giving it command `/start`

Now send photo to app and wait for output caption.
