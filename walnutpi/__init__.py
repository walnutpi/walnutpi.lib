__model = open("/proc/device-tree/model").read()
if "walnutpi-2b" in __model:
    from walnutpi_npu import NPU
    from walnutpi_npu import YOLO11
    import walnutpi_isp as isp
    
if "CyberCAM" in __model:
    from walnutpi_kpu import YOLO11
    import walnutpi_kpu as kpu
    import k230_sensor as Sensor
    import walnutpi_imgxfer as Imgxfer
    import k230_display as Display
