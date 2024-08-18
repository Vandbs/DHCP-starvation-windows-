### A Small Threat to Home Routers: Exhausting the DHCP Address Pool

Translated by GPT-4o,Chinese to English

#### Introduction:

"With the advent of IPv6, every grain of sand on Earth could potentially be addressed with an IP."

This guide is purely for entertainment purposes and should not be taken seriously. It’s a playful idea, reminiscent of children playing house, and shouldn’t be used for anything potentially illegal. If you’re new to networking, don’t try this on your home Wi-Fi.

I’m a university student. One day, while reading *Computer Networking: A Top-Down Approach* (8th Edition) by Kurose and Ross, I came across sections discussing IPv4 address exhaustion, NAT technology, and DHCP servers. This made me think: since IPv4 addresses are running out and private IP addresses (like 192.168.0.100) are a compromise for this exhaustion, what if I could “mess with” my neighbor’s use of IPv4? Maybe this could even promote the adoption of IPv6 (though, to be honest, one person’s efforts are quite limited). This idea revolves around the DHCP server.

Nowadays, most home routers are connected to the LAN port of an optical modem, with local ISPs usually handling fiber-optic installation. The router then uses a DHCP server to assign private IP addresses to devices connected via Wi-Fi, relying on MAC addresses as unique identifiers. Let’s skip the technical details and get to the point: how to annoy your neighbor, who might not know much about router configuration and user authentication, by causing short-term frustration with their router.

#### Step 1

If you’re new to networking, the first thing you need is your neighbor’s Wi-Fi password or a PC that was previously connected and can still auto-connect. This is essential because, without a connected device, the DHCP server won’t assign you an IP address.

If you’re an expert, there are many other ways to achieve this. To avoid legal issues, I won’t go into those here. You could even skip this step altogether and focus on later steps using packet sniffing and creating DHCP spoofing packets to interact with the router. (If you can do this, you probably don’t need this guide and might even scoff at this method). There are also software tools that support DHCP spoofing, but again, I won’t discuss them due to legal concerns—remember to be a law-abiding citizen.

#### Step 2

Set up a virtual machine.

This step is optional, but I recommend using a virtual machine so that the router management interface will show an anonymous host rather than your actual PC name.

For this fun experiment, I used Oracle VM VirtualBox. My virtual machine setup: Windows 11 v23h2, 4GB RAM, 4 vCPUs, and a bridged network adapter.

Virtual machine network adapter settings: Intel PRO/1000 MT Desktop (82540EM).

#### Step 3

In the Network Adapter Properties—Advanced tab, find the “Locally Administered Address” (LAA) option and change the value to "112233445566" or another 12-character combination of numbers and letters you’re familiar with. This step may vary depending on your network adapter; some allow you to change the MAC address directly, in which case the process is similar.

Press Win+R, type “regedit” to open the Registry Editor. You’ll see several large folders on the left sidebar. Randomly pick one and press Ctrl+F to search for the value you just entered. If you don’t find it, try another folder.

If the value you find has “Network Address” in the left sidebar, congratulations—you’re more than halfway there. If not, don’t worry; try a different value and repeat Step 3 until you find it. (If you’re using the same setup as me, you can try following the path I provide below).

Now, click on the address bar at the top, and copy the address, like so: “HKLM\SYSTEM\CurrentControlSet\Control\Class{4D36E972-E325-11CE-BFC1-08002BE10318}\0001”.

#### Step 4

Modify the Python script.

Update the path and adapter name, then open the Windows search bar, type “cmd” or “PowerShell,” and run it as an administrator (modifying the registry requires admin privileges). Navigate to the file path, and run the script.

You can adjust the value of `time.sleep()` in the script to shorten or lengthen the intervals depending on your device. You might wonder how long it takes to fill the pool. Assuming it takes 5 seconds to acquire one IPv4 address, it could take just over 20 minutes to fill the pool! (Not accounting for any missed requests). This is because most home routers use a 255.255.255.0 subnet mask for IPv4, which supports up to 256 addresses, with the first one reserved. You can estimate the required time based on the subnet mask in the network properties.

#### Conclusion

Once again, this project is purely for experimental purposes, tested on your home router. After filling the DHCPv4 address pool, new devices may indeed be unable to obtain an IPv4 address. If your router doesn’t have IPv6 enabled, your new devices won’t be able to connect to the internet. Additionally, if the code runs continuously and DHCP is constantly being occupied, the original device’s IPv4 address might also be taken when its lease expires (assuming there’s no MAC-to-IP binding). The original device might then be treated as a new device, unable to connect to the network. At that point, the owner’s only options are to connect via Ethernet to access the management interface and clear the address pool, or to reset the router. If their router has IPv6 enabled, new devices can still connect and access the internet since DHCPv6 and DHCPv4 are independent—at least your neighbor will benefit from IPv6 adoption.

Feel free to discuss this as a learning experience!