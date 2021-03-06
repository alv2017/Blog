# MAC Spoofing

**MAC spoofing** is a technique for changing a factory-assigned Media Access
Control Address (MAC) of a network interface or a network device. The MAC 
address is hard-coded on a network interface or a network device. It is used to
identify a device and exchange data between network devices. MAC address
of the device shouldn't be changed. However, many drivers allow MAC address 
to be changed. Additionally, there are tools which can make an operating 
system believe that the NIC (Network Interface Card) has the MAC address of a user's choice. 
The process of changing of MAC address is known as MAC spoofing. Essentially, 
MAC spoofing entails changing a computer identity, and it is quite easy 
to implement.

### Changing MAC address on Linux

As was already mentioned, MAC address references a network device or 
a network interface, so the first thing we need to do is to access the network
devices data. This can be done by opening a Linux terminal (with CTRL+ALT+T)
and typing in

    $ ip link show

You will get something like this:

    1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN mode DEFAULT group default qlen 1000
        link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    2: enp3s0: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc fq_codel state DOWN mode DEFAULT group default qlen 1000
        link/ether fc:cf:74:b3:6f:e4 brd ff:ff:ff:ff:ff:ff
    3: wlo1: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP mode DORMANT group default qlen 1000
        link/ether fc:d1:df:d2:a8:02 brd ff:ff:ff:ff:ff:ff


*lo* stands for loopback interface, *enp3s0* is a name of wired network interface, and *wlo1* references
the wireless network interface. The MAC addresses of the network devices are given in a line starting with 
*link/ether*. The MAC address of the wired network card is *fc:cf:74:b3:6f:e4*, and the address of the
wireless card is *fc:d1:df:d2:a8:02*.

I will be showing how to change the MAC address of the wireless device wlo1. This is an active network device
having the access to the Internet. The MAC changing process for the wired network interface is the same, and 
I'm not going to show it.

#### Method 1: Changing MAC address using **macchanger**

**macchanger** is a GNU/Linux utility for viewing/manipulating the MAC address for network interfaces.

You can install **macchanger** using the package installer of your Linux distro.
I'm using Ubuntu, and for me it is as simple as

    $ sudo apt install macchanger

During the installation process you will be asked if you want to change MAC automatically. If you say yes,
then every time when the network interface starts it will be getting a new MAC address. So choose "No"
for starters.

After the *macchanger* is installed, remember to read the manual, it is short and easy to understand:

    $ man macchanger

The basic usage of the utility is as follows:

    $ macchanger [options] device


A good starting point would be to extract a MAC address of the device you are going to modify. 
I will be doing a demo session with my wireless network interface *wlo1*:

    $ macchanger --show wlo1

This is going to return my current MAC address:

    Current MAC:   fc:d1:df:d2:a8:02 (unknown)

Let's try to change the MAC address to a new value: 00:11:22:33:44:55. 
Please note, that you are going to need root or sudo access in order to do this. 

The whole process requires three easy steps:

**STEP 1: Disable the network interface**

    # ip link set wlo1 down

**STEP 2: Change MAC address of the network interface**

    # macchanger --mac 00:11:22:33:44:55 wlo1

**STEP 3: Enable the network interface**

    # ip link set wlo1 up

Ok, let's check if we succeeded:

    # ip link show wlo1

This gives us

    3: wlo1: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP mode DORMANT group default qlen 1000
        link/ether **00:11:22:33:44:55** brd ff:ff:ff:ff:ff:ff

This is exactly what we wanted!

Ok, now let's assume that we want our original IP address back:
    
    # ip link set wlo1 down
    # macchanger -p wlo1
    # ip link set wlo1 up

After this procedure the network is expected to go back to its *original* MAC address.
Altenatively, you can reboot your Linux system and it will return to the original MAC address.

**macchanger** offers a couple of useful options that is worth exploring:

-A: this option allows to set a random MAC address with a random existing vendor of any kind of device. 
(The first 6 symbols of the MAC address identify the vendor of the device.)

-a: this option allows to set a random MAC address with a random vendor of the same kind of device.

-e: this option allows to set a random MAC address preserving the vendor information.

-r: this option generates a completely random MAC address.


#### Method 2: Changing MAC address using iproute2 tools

The **iproute2** is a set of utilities for configuring network and network interfaces.
We will be using *ip-link* which is a part of **iproute2** bundle.
*ip-link* is responsible for network interfaces configuration.

I will be doing the demonstration using my wireless network interface wlo1. Let 
me remind, that in order to get the information about network interface MAC address
one needs to type to the Linux terminal:

    $ ip link show

Let me also remind the result that I received for the interface wlo1:

    3: wlo1: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP mode DORMANT group default qlen 1000
        link/ether fc:d1:df:d2:a8:02 brd ff:ff:ff:ff:ff:ff

The MAC address of the wireless card interface is *fc:d1:df:d2:a8:02*. 
Let's change the MAC address using *ip-link* program. We will be changing the
MAC address to *00:11:22:33:44:55*. Please note, that you are going to need root or 
sudo access in order to do this. The steps needed to change the MAC address 
are as follows:

**STEP 1: Disable the wireless network interface**

    # ip link set wlo1 down

**STEP 2: Change the MAC address**

    # ip link set wlo1 address 00:11:22:33:44:55

**STEP 3: Enable the wireless network interface**

    # ip link set wlo1 up

Verify that the change took place by issuing the command

     # ip link show wl01

In my case I've got
    
    3: wlo1: <BROADCAST,MULTICAST> mtu 1500 qdisc noqueue state DOWN mode DEFAULT group default qlen 1000
        link/ether 00:11:22:33:44:55 brd ff:ff:ff:ff:ff:ff

It means that the MAC address change was successful and that the network interface is up
and running again. 

You can revert to the original address by following the procedure above
and changing MAC address to the original value. There is no need to do this though, 
because the original MAC address will be restored after the system reboots.