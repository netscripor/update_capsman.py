#!/usr/bin/env python3
import argparse
import getpass
import time
from netmiko import ConnectHandler
from colorama import Fore, Style, init
from pathlib import Path

init(autoreset=True)

def log(message, log_file=None):
    print(message)
    if log_file:
        with open(log_file, "a") as f:
            f.write(message + "\n")

def get_ip_list(mode, file_path=None):
    if mode == "manual":
        ip_list = []
        print("Введите IP-адреса (по одному в строке). Для завершения введите 'end':")
        while True:
            ip = input("> ").strip()
            if ip.lower() == "end":
                break
            ip_list.append(ip)
        return ip_list

    elif mode == "file":
        if not file_path or not Path(file_path).is_file():
            raise FileNotFoundError(f"Файл не найден: {file_path}")
        with open(file_path) as f:
            return [line.strip() for line in f if line.strip()]
    else:
        raise ValueError("Неверный режим. Используйте 'manual' или 'file'.")

def update_capsman(ip, username, password, capsman_addresses, log_path=None):
    router = {
        'device_type': 'mikrotik_routeros',
        'ip': ip,
        'username': username,
        'password': password
    }
    try:
        log(f"[+] Подключение к {ip}...", log_path)
        ssh = ConnectHandler(**router)
        command = f'/interface wireless cap set caps-man-addresses={capsman_addresses}'
        ssh.send_command_expect(command)
        log(Fore.GREEN + f"[✓] Обновлено на {ip}", log_path)
        return True
    except Exception as e:
        log(Fore.RED + f"[✗] Ошибка на {ip}: {e}", log_path)
        return False

def main():
    parser = argparse.ArgumentParser(description="Обновление CAPsMAN адресов на MikroTik устройствах")
    parser.add_argument("--mode", choices=["manual", "file"], required=True, help="Режим: manual или file")
    parser.add_argument("--file", help="Путь к файлу с IP-адресами (для режима file)")
    parser.add_argument("--user", required=True, help="Имя пользователя для доступа")
    parser.add_argument("--capsman", required=True, help="Адреса CAPsMAN, через запятую")
    parser.add_argument("--log", default="capsman_update.log", help="Файл логов")
    parser.add_argument("--delay", type=int, default=10, help="Задержка между устройствами (сек)")
    args = parser.parse_args()

    password = getpass.getpass("Введите пароль: ")
    log_file = args.log

    try:
        ip_list = get_ip_list(args.mode, args.file)
    except Exception as e:
        log(Fore.RED + f"[!] Ошибка получения IP-адресов: {e}")
        return

    log(f"Найдено устройств: {len(ip_list)}", log_file)

    success = 0
    fail = 0

    for ip in ip_list:
        if update_capsman(ip, args.user, password, args.capsman, log_file):
            success += 1
        else:
            fail += 1
        time.sleep(args.delay)

    log(Fore.CYAN + f"\nРезультат: успешно — {success}, с ошибкой — {fail}", log_file)

if __name__ == "__main__":
    main()
