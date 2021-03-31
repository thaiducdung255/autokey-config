text = clipboard.get_selection()
keyboard.send_key("<delete>")
output = system.exec_command("node -p \"string='%s'.replace(/\s/g,'');encodeURI(string)\"" % text)
keyboard.send_keys("%s" % output)