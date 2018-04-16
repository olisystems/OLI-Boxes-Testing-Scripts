# OLI-Boxes-Testing-Scripts
<p align="justify">Some of our testing scripts for our OLI Boxes. They show basic functionality to accomplish some simple tasks which inlcudes fetching and sending data to a MQQT Broker.</p>
This Repository is divided into two parts.<br />
1- Fetching Scripts<br />
2- Local Scripts<br />

## Fetching Scripts
<p align="justify">This includes the scripts related to the fetching of data from OLI System's MQTT Broker.
For example, to get "MQTT_Receiver.py" script on a OLI Box, User just need to type in console..</p>

 <p align="justify"> $wget https://raw.githubusercontent.com/olisystems/OLI-Boxes-Testing-Scripts/master/Fetching/MQTT_Receiver.py<br/>
To get the code running user need to have some packages installed, if already not installed i.e "PAHO.MQTT"<br/>
Other necessory things includes the credentials for our MQTT Broker i.e.</p>
1- Broker Address<br/>
2- Broker Port<br/>
3- Username<br/>
4- Password<br/>
5- Topics Name<br/>

## Local Scripts

<p align="justify">This section includes the scripts related to the fetching of data from different sensors and publishing it to OLI Systems's MQTT Broker. These scripts can also be downloaded directly into OLI Box using wget.</p>
These scripts includes fetching of data from different hardwares i.e.</p>
1- Solar.py(Get data from EPSolar MPPT Controller using Modbus protocol)<br/>
2- Smartpi.py(Get real-time power and energy data using REST API)<br/>
3- Rest_auth.py(Get real-time data using discovergy REST Auth API)<br/>
4- Oli_local.py & Oli.main.py(OLI architecture from real-time hardware to blockchain node)<br/>
5- SMA.py(Get real-time data from SMA controller using bluetooth)<br/>
