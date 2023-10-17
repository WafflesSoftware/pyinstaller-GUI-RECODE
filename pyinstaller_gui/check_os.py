import platform

write_os = open("system", "w")
write_os.write(platform.system())
write_os.close()
