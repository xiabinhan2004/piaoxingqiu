# 输入自己的token
token = 'eyJ0eXAiOiJKV1QiLCJjdHkiOiJKV1QiLCJ6aXAiOiJERUYiLCJhbGciOiJSUzUxMiJ9.eNqEkEtPwzAQhP_LnnPw226ORSCQQEhVe-CEnGSjRortynFQH-p_x8EIeoLjrma-3ZkLBDun_ZPvA9R-HscK5gljmS_QDOe70CHU8PD4_P4CFUxzs_5ZKqa0NQSxY9RIwbRRPRUrkXXZuQnjIlrv3u43eeNSu1vQ3WJUdGWIYdI0veCEENprJTQvxv9kEq4V4PEwRNwOLt-gmhpqhGY6a74QrweMNoU_McubbUSbfimcMGY4l4zmpKcpoStJSzMOY7u3Pt22ld-4vV_BB8ZpCB5qWar01n0Drp8AAAD__w.YXnXR9DkwrKOg3P_pE_7eWvOAq76r_4cipoytPzCgutcmrJ90q6-3GmO0u_5BiIEC6-eNp8tp2J9HIfSAQckRzYh50C3LnDqc83_vdNU5JGLMwhUgouSSZAmCF3RUEYYmaMBXaj9qiRyD1te-Gqg1ELlRyqtWBDFPpVcfRJoxe0'
# 项目id，必填
show_id = '65f2625cf3532400015846e9'
# 日期场次 按序号 指定抢某场次
data_id = 0
# 指定场次id，不指定则默认从第一场开始遍历
session_id = '6604ebfab5cdc5000130c105z'  # 644fcb7dca916100017dda3d
# 购票数量，一定要看购票须知，不要超过上限
buy_count = 1
# 指定观演人，观演人序号从0开始，人数需与票数保持一致
audience_idx = [0, 0]
# 门票类型，不确定则可以不填，让系统自行判断。快递送票:EXPRESS,电子票:E_TICKET,现场取票:VENUE,电子票或现场取票:VENUE_E,目前只发现这四种，如有新发现可补充
deliver_method = ''
