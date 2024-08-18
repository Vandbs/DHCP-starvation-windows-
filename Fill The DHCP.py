import os
import time
import random

def generate_random_mac():
    mac = [0x00, 0x16, 0x3e, random.randint(0x00, 0x7f), random.randint(0x00, 0xff), random.randint(0x00, 0xff)]
    return ''.join(map(lambda x: format(x, '02x'), mac))

def set_laa(reg_path, laa, adapter):
    """通过修改注册表设置本地管理地址（LAA）"""
    print(f"正在设置 LAA 为 {laa}")

    # 执行 reg add 命令修改注册表
    os.system(f"reg add {reg_path} /v NetworkAddress /d {laa} /f")
    # 重新启动网络适配器以应用更改
    os.system(f"netsh interface set interface \"{adapter}\" admin = DISABLE")
    time.sleep(2)
    os.system(f"netsh interface set interface \"{adapter}\" admin = ENABLE")
    time.sleep(2)

def main():
    reg_path = r"HKLM\SYSTEM\CurrentControlSet\Control\Class\{4D36E972-E325-11CE-BFC1-08002BE10318}\0001"  # 修改为你的实际注册表路径
    adapter = "以太网" # 修改为当前适配器名称，注意不是网卡设备名称
    while True:
        laa = generate_random_mac()
        set_laa(reg_path,laa, adapter)
        time.sleep(1)
        os.system("ipconfig")
if __name__ == "__main__":
    main()
