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

<p align="justify">This section includes the scripts related to the fetching of data from different sensors and publishing it to OLI Systems's MQTT Broker</p>
