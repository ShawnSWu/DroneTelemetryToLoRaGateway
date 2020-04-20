硬體介紹:
-------

><font face="黑體" size=5>機身</font>
>>本實作中使用碳纖維+金屬管狀支撐架組成的四軸無人機，搭載pixhawk4當作飛控版，holybro數據傳輸模組與控制台連接，
並且外接一塊raspberry pi4讀取飛控版資料並且接上LoRa模組設置成，電池為5800mA的鋰電池。(圖為測試時暫時拆掉槳與未固定EK-S76S)
![](https://i.imgur.com/YxgE5Am.jpg)



><font face="黑體" size=6>LoRaGateway</font>
>>LoRaGateway採用Advantech的WISE-6610，頻率為915MHz，從自己網路環境的Router接一條RJ45到WISE-6610，並設置bridge將封包轉送到我自己的MQTT Broker。
![](https://i.imgur.com/9l64RCc.jpg)



><font face="黑體" size=6>LoRa node</font>
>>本實作中採用EK-S76S作為LoRa node，透過EK-S76S官方[command set手冊](https://edit.wpgdadawant.com/uploads/news_file/program/2019/35461/tech_files/S7678S_Commands_Set_Reference_1.6.5.pdf)，透過手冊中指令可以設置LoRa node的Appkey, NwsKey, devaddr等等
，本實作中選用Activation by personalization(ABP)的方式將node加入LoRaWAN。
![](https://i.imgur.com/ydg6oen.jpg)


---------------------------------------------------------------


如何將LoRa node加入LoRaWAN?
--------------------------
>以本文方式為例

下指令設定好node的Appkey，NwsKey，devaddr，並且設定好Gateway支援的頻率，
1. 設Appkey指令: 
mac set_appkey 2b7e151628aed2a6abf7158809cf4f3c
Response: >> Ok

2. 設NwsKey指令: 
mac set_nwkskey 2b7e151628aed2a6abf7158809cf4f3c
Response: >> Ok

3. 設Devaddr指令: 
mac set_devaddr 12345678
Response: >> Ok





LoRaGateway configuration：
--------------------------
WISE-6610必須透過內網方式進入
>根據[官方手冊](https://www.induo.com/wp-content/uploads/2018/09/wise-6610-manual.pdf)先透過IP:192.168.1.1進入，要進入Gateway把自己的ip手動改成同網段的其他沒被使用的IP(ex:192.168.1.100)，然後再訪問『192.168.1.1』即可開始登入
(為了方便自己的開發環境，我這邊已將預設IP改為『192.168.100.123)
![](https://i.imgur.com/xEDWv1N.png)



進入Gateway後在根據手冊引導進入Server Admin
![](https://i.imgur.com/4BQySCq.png)

>點選Devices->Activeed(Nodes)新增一個新的node，按下create後即可輸入跟剛剛node一樣的Appkey，NwsKey，devaddr以及相關設定
>
![](https://i.imgur.com/6XJQXm3.png)

>設定好後基本上就可以運作了，可以在透過下指令嘗試發送封包以便於測試
>> mac tx ucnf 2 546573742064617461

若是成功 可以再Gateway的Server Admin的Received Frames看到剛剛發送的封包
![](https://i.imgur.com/Nx67ycO.png)


若是失敗，比較有可能是Gateway的頻率跟node沒對上，可以看看Gateway裡的LoRaWAN Radio setting查看Gateway的頻率，是否支持node的頻率
![](https://i.imgur.com/kHjxqC5.png)



------------------------------

Raspberry pi與pixhawk4接線:
--------------------------

![](https://i.imgur.com/5QsemDi.png)



EK-S76S與pixhawk4接線:
--------------------------

![](https://i.imgur.com/KOuRS7A.png)
