output = system.exec_command("xxd -u -l 12 -p /dev/urandom | awk '{print tolower($0)}'")
keyboard.send_keys(output)