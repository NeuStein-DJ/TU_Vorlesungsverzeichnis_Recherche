# TU_Vorlesungsverzeichnis_Recherche
Spider + GUI filter for the Vorlesungsverzeichnis von TU Darmstadt

使用基于Scrapy架构的Spide爬取TU Darmstadt的VV，并把它写入XX.json的文件中。
之后使用基于TKinter的GUI来读取.json的课表，根据在GUI中用户输入的制定时间范围来查找对应课程。

Das Ziel des Programms ist Herunterladen der Daten aus Vorlesungsverzeichnis der TU Darmstadt in File mit Extenion .json und Bearbeitung der Daten aus JSON in GUI.

Das heißt, Spider und GUI sind individuel.

Dieses Programm basiert auf Python 3.7 mit Beautifulsoup4, re, Scrapy

Für Durchfürung des Spiders gehen Sie einfach in Folder TU_Spider und geben in CMD dieses Befehl:
python entrypoint.py

Für Durführung des GUIS:(in dem Folder TU_Vorlesungsverzeichnis_Recherche)
python GUI_dj.py
