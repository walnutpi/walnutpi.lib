__model = open("/proc/device-tree/model").read()
if "walnutpi-2b" in __model:
    from walnutpi_npu import NPU
    from walnutpi_npu import YOLO11
    import walnutpi_isp as isp
    
if "CyberCAM" in __model:
    from walnutpi_kpu import kpu
    import k230_sensor as Sensor
    import walnutpi_imgxfer as IDE
    import k230_display as Display
