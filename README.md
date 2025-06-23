# 🔁 MikroTik CAPsMAN Updater

Скрипт для обновления CAPsMAN-адресов на устройствах MikroTik с помощью Netmiko. Удобный CLI-интерфейс, логирование и два режима ввода: вручную или из файла.

---

## 📦 Возможности

✅ Массовое обновление `/interface wireless cap set caps-man-addresses=...`  
✅ Поддержка ручного и файлового режима  
✅ Удобный CLI-интерфейс через `--mode`, `--file`, `--user`, `--capsman`  
✅ Логирование результатов работы  
✅ Задержка между устройствами для стабильности

---

## 🛠️ Установка

```bash
git clone https://github.com/netscripor/capsman_updater.git
cd capsman_updater
pip install -r requirements.txt
````

---

## 🚀 Примеры запуска

### Ввод IP-адресов вручную

```bash
python3 update_capsman.py \
  --mode manual \
  --user admin \
  --capsman 172.17.1.83,172.17.1.84
```

🟡 После запуска вас попросят ввести IP-адреса устройств и завершить ввод командой `end`.

---

### Загрузка адресов из файла

```bash
python3 update_capsman.py \
  --mode file \
  --file example/hosts.txt \
  --user admin \
  --capsman 172.17.1.83,172.17.1.84
```

Файл должен содержать список IP-адресов по одному в строке, например:

```
192.168.88.1
192.168.88.2
```

---

## ⚙️ Дополнительные параметры

|Параметр|Описание|Обязателен|
|---|---|---|
|`--mode`|`manual` или `file` — способ ввода IP-адресов|✅|
|`--file`|Путь к файлу с адресами (нужен при `--mode file`)|🟡|
|`--user`|Логин для подключения к MikroTik|✅|
|`--capsman`|Новые адреса CAPsMAN через запятую|✅|
|`--log`|Файл для логов (по умолчанию: `capsman_update.log`)|❌|
|`--delay`|Задержка между устройствами в секундах (по умолчанию 10)|❌|

---

## 📝 Пример логов

```log
python3 update_capsman.py --mode manual --user admin --capsman 172.17.1.83,172.17.1.84
Введите пароль:
Введите IP-адреса (по одному в строке). Для завершения введите 'end':
> 10.118.10.2
> end
Найдено устройств: 1
[+] Подключение к 10.118.10.2...
[✓] Обновлено на 10.118.10.2

Результат: успешно — 1, с ошибкой — 0

```

---

## 🔧 Зависимости
```
netmiko==4.2.0
colorama==0.4.3
```
---

📡 Подпишись и поддержи проект:

🔗 GitHub: [github.com/netscripor](https://github.com/netscripor)  
💰 Boosty: [boosty.to/netscripor](https://boosty.to/netscripor)  
✈️ Telegram-канал: [t.me/netscripor](https://t.me/netscripor)

⭐️ Поддержи проект звездой  
🛠 Нашёл баг или есть идея? Создай Issue!
