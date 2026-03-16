__model = open("/proc/device-tree/model").read()
if "walnutpi-2b" in __model:
    from walnutpi_npu import NPU
    from walnutpi_npu import YOLO11
    import walnutpi_isp as isp
    
if "K230" in __model:
    from walnutpi_kpu import nncase_2_10
    from walnutpi_kpu import nncase_2_11
    from walnutpi_kpu import YOLO11
