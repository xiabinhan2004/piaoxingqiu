# 输入自己的token
token = 'eyJ0eXAiOiJKV1QiLCJjdHkiOiJKV1QiLCJ6aXAiOiJERUYiLCJhbGciOiJSUzUxMiJ9.eNqEkM1uwjAQhN9lzznY8S85UoFAAiGhcuBUOclGREps5DiIFvHudWRS9dQedzTf7sw-wJkxXLa2cVDYsesyGAf0aX5A2X69uRqhgPVm97GHDIaxXP6IMpfKaIJY51QLnistG8oXPPoieXTdZFqezqtjVPpQnabV9QRKutBE50KXDWeEENooyRVL4H82Ac8M8H5tPb63Pc7BI3m4ojfB_UlP6SqPJrxgqiijhHAmtOSx4OcQsE8F094efXUxNvx-Urw-k0oykcEN_dA6C4VMH7RmDvb8BgAA__8.ViWtyLkWWv9iqbV9MERMn1pXLLr3CY_nk9crKMqTDkRkrk-XIRhmWtW7fiYQSC8mwfgtRB_cEbjAnUP-bUhpyGHeVBOtPHwqhN4dOlzAVZmS3_tVeotCgTRFKlo2x93ltCkcSbMC2VVUYwO2EQmzLx89B8f63RXCa8XOIOp1TPY'
# 项目id，必填
show_id = '65a915252c56f6000186e7d0'
# 日期场次 按序号 指定抢某场次 设置了就不会抢其他场次了
data_id = 0
# 指定场次id，不指定则默认从第一场开始遍历
session_id = ''  # 644fcb7dca916100017dda3d
# 是否要自定义票档 或者随机刷票 是则填true，否则填false
functional=False
# 票档
price_id=0
# 购票数量，一定要看购票须知，不要超过上限
buy_count = 2
# 指定观演人，观演人序号从0开始，人数需与票数保持一致
audience_idx = [0, 1]
# 门票类型，不确定则可以不填，让系统自行判断。快递送票:EXPRESS,电子票:E_TICKET,现场取票:VENUE,电子票或现场取票:VENUE_E,目前只发现这四种，如有新发现可补充
deliver_method = ''
