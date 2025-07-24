# -*- coding: utf-8 -*-
# @Author  : HeLei
# @Time    : 2024/3/29 11:01
# @File    : json_beauty.py
import json
import sys
# data = '{"bank_info": {}, "gps": "120.5056131059588,36.19044359015751", "face_info": {"face_result": {"face_type": 1, "face_check_score": 85.05043, "face_channel": "\u65f7\u89c6"}}, "idcard_info": {"ocr_result": {"birthday": "1974\u5e7408\u670816\u65e5", "issued_by": "\u8087\u4e1c\u5e02\u516c\u5b89\u5c40", "valid_date": "2007.01.11-2027.01.11", "address": "\u9ed1\u9f99\u6c5f\u7701\u8087\u4e1c\u5e02\u8dc3\u8fdb\u4e61\u5b8f\u4f1f\u6751\u516d\u64ae\u623f\u5c6f68\u53f7", "gender": "\u7537", "race": "\u6c49"}}, "contract_info": [{"type_no": "001", "pdf_url": "https://xcfs-public.xystatic.com/100041/contract_YED86_2024031612335763140\u4fe1\u5408\u5143\u4e2a\u4eba\u4fe1\u606f\u5904\u7406\u6388\u6743\u4e66.pdf", "title": "\u4fe1\u5408\u5143\u4e2a\u4eba\u4fe1\u606f\u5904\u7406\u6388\u6743\u4e66"}], "app_list": [], "coop_partnerid": 0, "extention": {"partner_name": "86"}, "approve_rateclass": "0", "apply_random": "5455305332539292759324907477586889309826888200087846626627197295", "xy_uid": 223815509202976878, "extend_loan_type": 1, "loan_info": {"has_loan_cnt": 0, "has_loan_amt": 0.0, "on_loan_cnt": 0, "on_loan_amt": 0.0, "lately_amt_repayed_periods": 0, "lately_amt_remain_periods": 0, "history_max_dpd": 0, "current_max_dpd": 0}, "credit_info": "{\"data\":\"{\\\"model_result\\\": [{\\\"score_time\\\": \\\"2024-03-16 12:34:41\\\", \\\"model_name\\\": \\\"x_scr_pboc_v5\\\", \\\"risk_lvl\\\": 43}, {\\\"score_time\\\": \\\"2024-03-16 12:34:41\\\", \\\"model_name\\\": \\\"kyd_non_new_pboc_v4\\\", \\\"risk_lvl\\\": 39}, {\\\"score_time\\\": \\\"2024-03-16 12:34:41\\\", \\\"model_name\\\": \\\"x_scr_pboc_v8\\\", \\\"risk_lvl\\\": 38}, {\\\"score_time\\\": \\\"2024-03-16 12:34:41\\\", \\\"model_name\\\": \\\"x_scr_pboc_v9\\\", \\\"risk_lvl\\\": 86}, {\\\"score_time\\\": \\\"2024-03-16 12:34:41\\\", \\\"model_name\\\": \\\"x_p3_pboc_v1\\\", \\\"risk_lvl\\\": 43}], \\\"rule_result\\\": {\\\"final_result\\\": 0, \\\"score_rule_result\\\": 0, \\\"version\\\": \\\"0.0.1\\\", \\\"rule_time\\\": \\\"2024-03-16 12:34:41\\\", \\\"special_rule_result2\\\": 0, \\\"special_rule_result\\\": 0, \\\"is_no_record\\\": 0}}\",\"version\":\"9.2023.03.01\",\"err_msg\":\"ok\",\"err_code\":0}", "approved_rateclass": "24+"}'

arg_data = sys.argv[1]
data = arg_data
t = json.dumps(json.loads(data), indent=4, ensure_ascii=False)
# print("\n\n\n\n")
print()
print(t)

