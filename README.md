# EIGRP-configuration-using-Netmiko
EIGRP configuration using Netmiko


![alt tag](https://github.com/OthmaneBlial/EIGRP-configuration-using-Netmiko/blob/master/Tutorial/1.PNG)


We create three files, one for data, one for configuration and another one for showing results. These files need to be excutable.


![alt tag](https://github.com/OthmaneBlial/EIGRP-configuration-using-Netmiko/blob/master/Tutorial/2.PNG)

Now, let's add Routers information to data.py:

![alt tag](https://github.com/OthmaneBlial/EIGRP-configuration-using-Netmiko/blob/master/Tutorial/3.PNG)

Then, Routers connections with each other:

![alt tag](https://github.com/OthmaneBlial/EIGRP-configuration-using-Netmiko/blob/master/Tutorial/4.PNG)


![alt tag](https://github.com/OthmaneBlial/EIGRP-configuration-using-Netmiko/blob/master/Tutorial/5.PNG)

We import Netmiko, then our data.py:

![alt tag](https://github.com/OthmaneBlial/EIGRP-configuration-using-Netmiko/blob/master/Tutorial/6.PNG)

These config functions will create an interface, then configure eigrp and eigrp summarization: 

![alt tag](https://github.com/OthmaneBlial/EIGRP-configuration-using-Netmiko/blob/master/Tutorial/7.PNG)

While these config functions, will add authentication to eigrp:

![alt tag](https://github.com/OthmaneBlial/EIGRP-configuration-using-Netmiko/blob/master/Tutorial/8.PNG)

Now, we loop around the routers and configure them automatically:

![alt tag](https://github.com/OthmaneBlial/EIGRP-configuration-using-Netmiko/blob/master/Tutorial/9.PNG)

After that, we add showing results functions to the show.py file:

![alt tag](https://github.com/OthmaneBlial/EIGRP-configuration-using-Netmiko/blob/master/Tutorial/10.PNG)

Here we go the results:

![alt tag](https://github.com/OthmaneBlial/EIGRP-configuration-using-Netmiko/blob/master/Tutorial/11.PNG)


![alt tag](https://github.com/OthmaneBlial/EIGRP-configuration-using-Netmiko/blob/master/Tutorial/12.PNG)

