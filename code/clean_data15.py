import pandas as pd
import numpy as np

df = pd.read_csv('../data/2015/personsx15.csv')
df.columns = df.columns.str.lower()
df['region_south'] = (df.region==3)
df['region_west'] = (df.region==4)
df['region_midwest'] = (df.region==2)
df['region_northeast'] = (df.region==1)

df['sex_female'] = df.sex == 1
df['sex_male'] = df.sex == 1

df['hispanic'] = df.origin_i == 1
df['race_white'] = df.racreci3 == 1
df['race_black'] = df.racreci3 == 2
df['race_asian'] = df.racreci3 == 3

df['armed_forces'] = df.nowaf == 1

#df['dob_y'] = df['dob_y_p'].apply(lambda x: np.nan if x in [9997,9998,9999] else int(x))
df['age'] = df['age_p']
df['married'] = (df['r_maritl']==1)|(df['r_maritl']==2)
df['divorced'] = df['r_maritl'] == 5
df['widowed'] = df['r_maritl'] == 4

df['bio_mother'] = df['mom_degp'] == 1
df['bio_father'] = df['dad_degp'] == 1

df['mom_colplus'] = df['mom_ed'].isin([5,6,7,8])
df['mom_noged'] = df['mom_ed'].isin([1,2])

df['dad_colplus'] = df['dad_ed'].isin([5,6,7,8])
df['dad_noged'] = df['dad_ed'].isin([1,2])

df['special_ed'] = df['pspedeis'] == 1
df['need_help_personal_care'] = df['plaadl'] == 1

df['need_help_bath_all'] = df['labath'] == 1
df['need_help_dress_all'] = df['ladress'] == 1
df['need_help_eat_all'] = df['laeat'] == 1
df['need_help_bed_all'] = df['labed'] == 1
df['need_help_toilt_all'] = df['latoilt'] == 1
df['need_help_home_all'] = df['lahome'] == 1

df['need_help_routine_needs_gt18'] = df['plaiadl'] == 1
df['unable_to_work_gt18'] = df['plawknow'] == 1
df['limited_to_work_gt18'] = df['plawklim'] == 1
df['limited_walking_all'] = df['plawalk'] == 1
df['limited_remember_all'] = df['plaremem'] == 1
df['limited_other_all'] = df['plimany'] == 1
df['limited_any_lt5'] = df['la1ar'] ==1

df['vision_lt18'] = df['lahcc1'] == 1
df['hearing_lt18'] = df['lahcc2'] == 1
df['speech_lt18'] = df['lahcc3'] == 1
df['asthma_lt18'] = df['lahcc4'] == 1
df['birth_defect_lt18'] = df['lahcc5'] == 1
df['injury_lt18'] = df['lahcc6'] == 1
df['retard_lt18'] = df['lahcc7a'] == 1
df['develop_lt18'] = df['lahcc8'] == 1
df['mental_lt18'] = df['lahcc9'] == 1
df['muscle_lt18'] = df['lahcc10'] == 1
df['epilepsy_lt18'] = df['lahcc11'] == 1
df['learning_lt18'] = df['lahcc12'] == 1
df['adhd_lt18'] = df['lahcc13'] == 1
df['other1_lt18'] = df['lahcc90'] == 1
df['other2_lt18'] = df['lahcc91'] == 1

df['vision_1yrp_lt18'] = df['lcdurb1'] == 4
df['hearing_1yrp_lt18'] = df['lcdurb2'] == 4
df['speech_1yrp_lt18'] = df['lcdurb3'] == 4
df['asthma_1yrp_lt18'] = df['lcdurb4'] == 4
df['birth_defect_1yrp_lt18'] = df['lcdurb5'] == 4
df['injury_1yrp_lt18'] = df['lcdurb6'] == 4
df['retard_1yrp_lt18'] = df['lcdurb7a'] == 4
df['develop_1yrp_lt18'] = df['lcdurb8'] ==4
df['mental_1yrp_lt18'] = df['lcdurb9'] == 4
df['muscle_1yrp_lt18'] = df['lcdurb10'] == 4
df['epilepsy_1yrp_lt18'] = df['lcdurb11'] == 4
df['learning_1yrp_lt18'] = df['lcdurb12'] == 4
df['adhd_1yrp_lt18'] = df['lcdurb13'] == 4
df['other1_1yrp_lt18'] = df['lcdurb90'] == 4
df['other2_1yrp_lt18'] = df['lcdurb91'] == 4

df['vision_chrc_lt18'] = df['lcchrc1'] == 1
df['hearing_chrc_lt18'] = df['lcchrc2'] == 1
df['speech_chrc_lt18'] = df['lcchrc3'] == 1
df['asthma_chrc_lt18'] = df['lcchrc4'] == 1
df['birth_defect_chrc_lt18'] = df['lcchrc5'] == 1
df['injury_chrc_lt18'] = df['lcchrc6'] == 1
df['retard_chrc_lt18'] = df['lcchrc7a'] == 1
df['develop_chrc_lt18'] = df['lcchrc8'] == 1
df['mental_chrc_lt18'] = df['lcchrc9'] == 1
df['muscle_chrc_lt18'] = df['lcchrc10'] == 1
df['epilepsy_chrc_lt18'] = df['lcchrc11'] == 1
df['learning_chrc_lt18'] = df['lcchrc12'] == 1
df['adhd_chrc_lt18'] = df['lcchrc13'] == 1
df['other1_chrc_lt18'] = df['lcchrc90'] == 1
df['other2_chrc_lt18'] = df['lcchrc91'] == 1

df['vision_gt18'] = df['lahca1'] == 1
df['hearing_gt18'] = df['lahca2'] == 1
df['arthritis_gt18'] = df['lahca3'] == 1
df['back_gt18'] = df['lahca4'] == 1
df['bone_injury_gt18'] = df['lahca5'] == 1
df['other_injury_gt18'] = df['lahca6'] == 1
df['heart_gt18'] = df['lahca7'] == 1
df['stroke_gt18'] = df['lahca8'] == 1
df['hypertension_gt18'] = df['lahca9'] == 1
df['diabetes_gt18'] = df['lahca10'] == 1
df['lung_gt18'] = df['lahca11'] == 1
df['cancer_gt18'] = df['lahca12'] == 1
df['birth_defect_gt18'] = df['lahca13'] == 1
df['retard_gt18'] = df['lahca14a'] == 1
df['other_develop_gt18'] = df['lahca15'] ==  1
df['senility_gt18'] = df['lahca16'] == 1
df['emotional_gt18'] = df['lahca17'] == 1
df['weight_gt18'] = df['lahca18'] == 1
df['amputated_gt18'] = df['lahca19_'] == 1
df['musculoskeletal_gt18'] = df['lahca20_'] == 1
df['circulation_gt18'] = df['lahca21_'] == 1
df['metabolic_gt18'] = df['lahca22_'] == 1
df['sensory_gt18'] = df['lahca23_'] == 1
df['digestive_gt18'] = df['lahca24_'] == 1
df['genitourinary_gt18'] = df['lahca25_'] == 1
df['skin_gt18'] = df['lahca26_'] == 1
df['blood_gt18'] = df['lahca27_'] == 1
df['benign_tumor_gt18'] = df['lahca28_'] == 1
df['alcohol_gt18'] = df['lahca29_'] == 1
df['mental_gt18'] = df['lahca30_'] == 1
df['surgical_gt18'] = df['lahca31_'] == 1
df['aging_gt18'] = df['lahca32_'] == 1
df['fatigue_gt18'] = df['lahca33_'] == 1
df['pregnancy_gt18'] = df['lahca34_'] == 1
df['other1_gt18'] = df['lahca90'] == 1
df['other2_gt18'] = df['lahca91'] == 1

df['vision_1yrp_gt18'] = df['ladurb1'] == 4
df['hearing_1yrp_gt18'] = df['ladurb2'] == 4
df['arthritis_1yrp_gt18'] = df['ladurb3'] == 4
df['back_1yrp_gt18'] = df['ladurb4'] == 4
df['bone_injury_1yrp_gt18'] = df['ladurb5'] == 4
df['other_injury_1yrp_gt18'] = df['ladurb6'] == 4
df['heart_1yrp_gt18'] = df['ladurb7'] == 4
df['stroke_1yrp_gt18'] = df['ladurb8'] == 4
df['hypertension_1yrp_gt18'] = df['ladurb9'] == 4
df['diabetes_1yrp_gt18'] = df['ladurb10'] == 4
df['lung_1yrp_gt18'] = df['ladurb11'] == 4
df['cancer_1yrp_gt18'] = df['ladurb12'] == 4
df['birth_defect_1yrp_gt18'] = df['ladurb13'] == 4
df['retard_1yrp_gt18'] = df['ldurb14a'] == 4
df['other_develop_1yrp_gt18'] = df['ladurb15'] == 4
df['senility_1yrp_gt18'] = df['ladurb16'] == 4
df['emotional_1yrp_gt18'] = df['ladurb17'] == 4
df['weight_1yrp_gt18'] = df['ladurb18'] == 4
df['amputated_1yrp_gt18'] = df['ladurb19'] == 4
df['musculoskeletal_1yrp_gt18'] = df['ladurb20'] == 4
df['circulation_1yrp_gt18'] = df['ladurb21'] == 4
df['metabolic_1yrp_gt18'] = df['ladurb22'] == 4
df['sensory_1yrp_gt18'] = df['ladurb23'] == 4
df['digestive_1yrp_gt18'] = df['ladurb24'] == 4
df['genitourinary_1yrp_gt18'] = df['ladurb25'] == 4
df['skin_1yrp_gt18'] = df['ladurb26'] == 4
df['blood_1yrp_gt18'] = df['ladurb27'] == 4
df['benign_tumor_1yrp_gt18'] = df['ladurb28'] == 4
df['alcohol_1yrp_gt18'] = df['ladurb29'] == 4
df['mental_1yrp_gt18'] = df['ladurb30'] ==4
df['surgical_1yrp_gt18'] = df['ladurb31'] ==4
df['aging_1yrp_gt18'] = df['ladurb32'] == 4
df['fatigue_1yrp_gt18'] = df['ladurb33'] == 4
df['pregnancy_1yrp_gt18'] = df['ladurb34'] == 4
df['other1_1yrp_gt18'] = df['ladurb90'] == 4
df['other2_1yrp_gt18'] = df['ladurb91'] == 4

df['vision_chrc_gt18'] = df['lachrc1'] == 1
df['hearing_chrc_gt18'] = df['lachrc2'] == 1
df['arthritis_chrc_gt18'] = df['lachrc3'] == 1
df['back_chrc_gt18'] = df['lachrc4'] == 1
df['bone_injury_chrc_gt18'] = df['lachrc5'] ==1
df['other_injury_chrc_gt18'] = df['lachrc6'] == 1
df['heart_chrc_gt18'] = df['lachrc7'] == 1
df['stroke_chrc_gt18'] = df['lachrc8'] == 1
df['hypertension_chrc_gt18'] = df['lachrc9'] == 1
df['diabetes_chrc_gt18'] = df['lachrc10'] == 1
df['lung_chrc_gt18'] = df['lachrc11'] ==1
df['cancer_chrc_gt18'] = df['lachrc12'] == 1
df['birth_defect_chrc_gt18'] = df['lachrc13'] == 1
df['retard_chrc_gt18'] = df['lchrc14a'] == 1
df['other_develop_chrc_gt18'] = df['lachrc15'] == 1
df['senility_chrc_gt18'] = df['lachrc16'] == 1
df['emotional_chrc_gt18'] = df['lachrc17'] == 1
df['weight_chrc_gt18'] = df['lachrc18'] == 1
df['amputated_chrc_gt18'] = df['lachrc19'] == 1
df['musculoskeletal_chrc_gt18'] = df['lachrc20'] == 1
df['circulation_chrc_gt18'] = df['lachrc21'] == 1
df['metabolic_chrc_gt18'] = df['lachrc22'] == 1
df['sensory_chrc_gt18'] = df['lachrc23'] == 1
df['digestive_chrc_gt18'] = df['lachrc24'] == 1
df['genitourinary_chrc_gt18'] = df['lachrc25'] == 1
df['skin_chrc_gt18'] = df['lachrc26'] == 1
df['blood_chrc_gt18'] = df['lachrc27'] == 1
df['benign_tumor_chrc_gt18'] = df['lachrc28'] == 1
df['alcohol_chrc_gt18'] = df['lachrc29'] == 1
df['mental_chrc_gt18'] = df['lachrc30'] == 1
df['surgical_chrc_gt18'] = df['lachrc31'] == 1
df['aging_chrc_gt18'] = df['lachrc32'] == 1
df['fatigue_chrc_gt18'] = df['lachrc33'] == 1
df['pregnancy_chrc_gt18'] = df['lachrc34'] == 1
df['other1_chrc_gt18'] = df['lachrc90'] == 1
df['other2_chrc_gt18'] = df['lachrc91'] == 1

df['chronic_all'] = df['lcondrt'] == 1
df['health_status_excellent'] = df['phstat'] ==  1
df['health_status_verygood'] = df['phstat'] == 2
df['health_status_good'] = df['phstat'] == 3
df['health_status_fair'] = df['phstat'] == 4
df['health_status_poor'] = df['phstat'] == 5

df['care_delayed_cost'] = df['pdmed12m'] == 1
df['care_notget_cost'] = df['pnmed12m'] == 1
df['overnight_hospital'] = df['phospyr2'] == 1
df['overnight_hospital_times'] = df['hospno'].apply(lambda x: 0 if x in [997,998,999] else x)
df['overnight_hospital_nights'] = df['hpnite'].apply(lambda x: 0 if x in [997,998,999] else x)
df['care_athome_2wks'] = df['phchm2w'] == 1
df['care_athome_2wks_times'] = df['phcphn2w'].apply(lambda x: 0 if x in [97,98,99] else x)
df['care_phone_2wks'] = df['phcph2wr'] == 1
df['care_phone_2wks_times'] = df['phcphn2w'].apply(lambda x: 0 if x in [97,98,99] else x)
df['care_office_2wks'] = df['phcdv2w'] == 1
df['care_office_2wks_times'] = df['phcdv2w'].apply(lambda x: 0 if x in [97,98,99] else x)

df['care_10more_12mo'] = df['p10dvyr'] == 1
df['notcov_'] = df['notcov']==1
df['medicare_'] = df['medicare'].isin([1,2])
df['medicare_partA_only'] = df['mcpart'] == 1
df['medicare_partB_only']= df['mcpart'] == 2
df['medicare_bothparts'] = df['mcpart'] == 3
df['medicare_advantage'] = df['mcchoice'] == 1
df['medicare_hmo'] = df['mchmo'] == 1
df['medicare_need_referral'] = df['mcref'] == 1
df['medicare_pay_premium'] = df['mcprem'] == 1
df['medicare_partD'] = df['mcpartd'] == 1

df['medicaid_'] = df['medicaid'].isin([1,2])

df['medicaid_md'] = df['machmd'].isin([1,2,3])
df.loc[df['machmd'].isna()==True,'medicaid_md'] = False


#df['medicaid_primary_routine'] = df['mapcmd'] == 1
#df['medicaid_special_referral'] = df['maref'] == 1

df['single_'] = df['single'].isin([1,2])
df['single_accidents'] = df['sstypea'] == 1
df['single_aids'] = df['sstypeb'] == 1
df['single_cancer'] = df['sstypec'] == 1
df['single_catastrophic'] = df['sstyped'] == 1
df['single_dental'] = df['sstypee'] == 1
df['single_disability'] = df['sstypef'] == 1
df['single_hospice'] = df['sstypeg'] == 1
df['single_hospitalization'] = df['sstypeh'] == 1
df['single_longterm_care'] = df['sstypei'] == 1
df['single_prescription'] = df['sstypej'] == 1
df['single_vision'] = df['sstypek'] == 1
df['single_other'] = df['sstypel'] == 1

df['private_'] = df['private'].isin([1,2])
df['private1_hmo'] = df['plnmgd1'] == 1
df['private1_primary'] = df['whonam1'] == 1
df['private1_thru_wrk_employer'] = df['plnwrks1'] == 1
df['private1_thru_wrk_union'] = df['plnwrks1'] == 2
df['private1_thru_wrk_other'] = df['plnwrks1'].isin([3,4])
df['private1_thru_direct'] = df['plnwrks1'] == 5
df['private1_thru_state'] = df['plnwrks1'] == 7
df['private1_thru_school'] = df['plnwrks1'] == 9
df['private1_paid_self'] = df['plnpay11'] == 1
df['private1_paid_employer'] = df['plnpay21'] == 1
df['private1_paid_other'] = df['plnpay31'] == 1
df['private1_paid_medicare'] = df['plnpay41'] == 1
df['private1_paid_medicaid'] = df['plnpay51'] == 1
df['private1_paid_schip'] = df['plnpay61'] == 1
df['private1_paid_government'] = df['plnpay71'] == 1

df['private1_oop_20k'] = df['hicostr1'].apply(lambda x: 0 if x in [99997,99998,99999]  else x)
df['private1_type_hmo'] = df['plnmgd1'] == 1
df['private1_type_ppo'] = df['plnmgd1'] == 2
df['private1_type_pos'] = df['plnmgd1'] == 3
df['private1_type_ffs'] = df['plnmgd1'] == 4
df['private1_hdhp'] = df['hdhp1'] == 1
df['private1_hsa'] = df['hsahra1'] == 1
df['private1_choose_md'] = df['mgchmd1'] == 1
df['private1_network_md'] = df['mgprmd1'] == 1
df['private1_oon_md'] = df['mgpymd1'] == 1
#df['private1_need_referral'] = df['mgpref1'] == 1
df['private1_rx'] = df['prrxcov1'] == 1
df['private1_dental'] = df['prdncov1'] == 1

df['private2_hmo'] = df['plnmgd2'] == 1
df['private2_primary'] = df['whonam2'] == 1
df['private2_thru_wrk_employer'] = df['plnwrks2'] == 1
df['private2_thru_wrk_union'] = df['plnwrks2'] == 2
df['private2_thru_wrk_other'] = df['plnwrks2'].isin([3,4])
df['private2_thru_direct'] = df['plnwrks2'] == 5
df['private2_thru_state'] = df['plnwrks2'] == 7
df['private2_thru_school'] = df['plnwrks2'] == 9
df['private2_paid_self'] = df['plnpay12'] == 1
df['private2_paid_employer'] = df['plnpay22'] == 1
df['private2_paid_other'] = df['plnpay32'] == 1
df['private2_paid_medicare'] = df['plnpay42'] == 1
df['private2_paid_medicaid'] = df['plnpay52'] == 1
df['private2_paid_schip'] = df['plnpay62'] == 1
df['private2_paid_government'] = df['plnpay72'] == 1
df['private2_oop_20k'] = df['hicostr2'].apply(lambda x: 0 if x in [99997,99998,99999]  else x)

df['private2_type_hmo'] = df['plnmgd2'] == 1
df['private2_type_ppo'] = df['plnmgd2'] == 2
df['private2_type_pos'] = df['plnmgd2'] == 3
df['private2_type_ffs'] = df['plnmgd2'] == 4
df['private2_hdhp'] = df['hdhp2'] == 1
df['private2_hsa'] = df['hsahra2'] == 1
df['private2_choose_md'] = df['mgchmd2'] == 1
df['private2_network_md'] = df['mgprmd2'] == 1
df['private2_oon_md'] = df['mgpymd2'] == 1
#df['private2_need_referral'] = df['mgpref2'] == 1
df['private2_rx'] = df['prrxcov2'] == 1
df['private2_dental'] = df['prdncov2'] == 1
df['private_2plus'] = df['prplplus'] == 1

df['schip_'] = df['schip'].isin([1,2])
df['schip_md'] = df['stdoc1'].isin([1,2,3])
#df['schip_primary_routine'] = df['stpcmd1'] == 1
#df['schip_special_referral'] = df['stref1'] == 1

df['othpub_'] = df['othpub'].isin([1,2])
df['othpub_md'] = df['stdoc2'].isin([1,2,3])
#df['othpub_primary_routine'] = df['stpcmd2'] == 1
#df['othpub_special_referral'] = df['stref2'] == 1

df['othgov_'] = df['othgov'].isin([1,2])
df['othgov_md'] = df['stdoc3'].isin([1,2,3])
#df['othgov_primary_routine'] = df['stpcmd3'] == 1
#df['othgov_special_referral'] = df['stref3'] ==1

df['milcare_'] = df['milcare'].isin([1,2])
df['milcare_tricare'] = df['milspc1'] == 1
df['milcare_va'] = df['milspc2'] == 1
df['milcare_champ-va'] = df['milspc3'] == 1
df['milcare_other'] = df['milspc4'] == 1
df['milcare_tricare_prime'] = df['milmanr'] == 1
df['milcare_tricare_standard_extra'] = df['milmanr'] == 2
df['milcare_tricare_forlife'] = df['milmanr'] == 4

df['ihs_'] = df['ihs']==1

df['hilast_6mo'] = df['hilast'] == 1
df['hilast_1yr'] = df['hilast'] == 2
df['hilast_3yr'] = df['hilast'] == 3
df['hilast_3yrplus'] = df['hilast'] == 4

df['histop_losejob'] = df['histop1'] == 1
df['histop_divorce'] = df['histop2'] == 1
df['histop_age'] = df['histop3'] == 1
df['histop_eligible'] = df['histop4'] == 1
df['histop_highcost'] = df['histop5'] == 1
df['histop_refused'] = df['histop6'] == 1
df['histop_medicaid_pregnancy'] = df['histop7'] == 1
df['histop_medicaid_newjob'] = df['histop8'] == 1
df['histop_medicaid_other'] = df['histop9'] == 1
df['histop_other'] = df['histop10'] == 1
df['histop_never'] = df['histop11'] == 1
df['histop_moved'] = df['histop12'] == 1
df['histop_selfemployed'] = df['histop13'] == 1
df['histop_noneed'] = df['histop14'] == 1
df['histop_gotmarried'] = df['histop15'] == 1

df['hino_12mo'] = df['hinotyr'] == 1
df['hino_months'] = df['hinotmyr'].apply(lambda x: 0 if x in [97,98,99] else float(x))

df['care_spent_zero'] = df['hcspfyr'] == 0
df['care_spent_lt500'] = df['hcspfyr'] == 1
df['care_spent_lt2k'] = df['hcspfyr'] == 2
df['care_spent_lt3k'] = df['hcspfyr'] == 3
df['care_spent_lt5k'] = df['hcspfyr'] == 4
df['care_spent_gt5k'] = df['hcspfyr'] == 5

df['fsa_'] = df['fsa']==1

df['hikind_private'] = df['hikindna'] == 1
df['hikind_medicare'] = df['hikindnb'] == 1
df['hikind_medigap'] = df['hikindnc'] == 1
df['hikind_medicaid'] = df['hikindnd'] == 1
df['hikind_schip'] = df['hikindne'] == 1
df['hikind_military'] = df['hikindnf'] == 1
df['hikind_ihs'] = df['hikindng'] == 1
df['hikind_state'] = df['hikindnh'] == 1
df['hikind_othgov'] = df['hikindni'] == 1
df['hikind_ssp'] = df['hikindnj'] == 1
df['hikind_nocov'] = df['hikindnk'] == 1

df['medicare_probe'] = df['mcareprb'] == 1
df['medicaid_probe'] = df['mcaidprb'] == 1
df['ssp_probe'] = df['sincov'] == 1

df['born_us'] = df['plborn'] == 1
df['born_mexico'] = df['regionbr'] == 2
df['born_southamerica'] = df['regionbr'] == 3
df['born_europe'] = df['regionbr'] == 4
df['born_russia'] = df['regionbr'] == 5
df['born_africa'] = df['regionbr'] == 6
df['born_middle_east'] = df['regionbr'] == 7
df['born_indian'] = df['regionbr'] == 8
df['born_asia'] = df['regionbr'] == 9
df['born_se_asia'] = df['regionbr'] == 10

df['yrs_us_lt1'] = df['yrsinus'] == 1
df['yrs_us_lt5'] = df['yrsinus'] == 2
df['yrs_us_lt10'] = df['yrsinus'] == 3
df['yrs_us_lt15'] = df['yrsinus'] == 4
df['yrs_us_gt15'] = df['yrsinus'] == 5

df['us_citizen'] = df['citizenp'] == 1

df['headstart'] = df['headst'] == 1
df['headstart_ever'] = df['headstv1'] == 1

df['educ_yrs'] = df['educ1'].apply(lambda x: 0 if x in [97,98,99] else x)
df['educ_highschl'] = df['educ1'].isin([13,14])
df['educ_somecol'] = df['educ1'].isin([15,16,17])
df['educ_colplus'] = df['educ1'].isin( [18,19,20,21])
#df['military_honorable_discharge'] = df['pmiltry'] == 1

df['employed']  = df['doinglwp'].isin([1,2])
df['looking_for_work'] = df['doinglwp'] == 3
df['volunteer'] = df['doinglwp'] == 4
df['not_in_labor_force'] = df['doinglwp'] == 5

df['not_work_family'] = df['whynowkp'] == 1
df['not_work_school'] = df['whynowkp'] == 2
df['not_work_retired'] = df['whynowkp'] == 3
df['not_work_vacation'] = df['whynowkp'] == 4
df['not_work_leave'] = df['whynowkp'] == 5
df['not_work_health'] = df['whynowkp'] == 6
df['not_work_off_season'] = df['whynowkp'] == 7
df['not_work_layoff'] = df['whynowkp'] == 8
df['not_work_disabled'] = df['whynowkp'] == 9

df['wrkhrs'] = df['wrkhrs2'].apply(lambda x: 0 if x in ['97 Refused','98',"99 Don't know"] else x)
df['wrkhrs'] = df['wrkhrs'].apply(lambda x: 95 if x == '95 95+ hours' else x)

df['wrkhrs_lt35'] = (0 < df['wrkhrs']) & (df['wrkhrs'] <= 35)
df['wrkhrs_lt45'] = (35 < df['wrkhrs']) & (df['wrkhrs'] <= 45)
df['wrkhrs_gt20'] = (45 < df['wrkhrs']) & (df['wrkhrs'] <= 95)

df['wrk_fulltime'] = df['wrkftall'] == 1
df['wrk_lastyr'] = df['wrklyr1'] == 1
df['wrk_mo_lastyr'] = df['wrkmyr'].apply(lambda x: np.nan if x in [97,98,99] else x)

df['earnings_lt5k'] = df['ernyr_p'] == 1
df['earnings_lt10k'] = df['ernyr_p'] == 2
df['earnings_lt15k']= df['ernyr_p'] == 3
df['earnings_lt20k']= df['ernyr_p'] == 4
df['earnings_lt25k']= df['ernyr_p'] == 5
df['earnings_lt34k']= df['ernyr_p'] == 6
df['earnings_lt45k']= df['ernyr_p'] == 7
df['earnings_lt55k']= df['ernyr_p'] == 8
df['earnings_lt65k']= df['ernyr_p'] == 9
df['earnings_lt75k']= df['ernyr_p'] == 10
df['earnings_gt75k']= df['ernyr_p'] == 11

df['hi_offered_atwork'] = df['hiempof'] == 1

df['family_income_answered'] = df['fincint'] == 1
df['income_wage'] = df['psal'] == 1
df['income_self'] = df['pseinc'] == 1
df['income_ss'] = df['pssrr'] == 1
df['disability_ss'] = df['pssrrdb'] == 1
df['disability_benefit'] = df['pssrrd'] == 1
df['income_pension'] = df['ppens'] == 1

df['income_other_pension'] = df['popens'] == 1
df['income_ssi'] = df['pssi'] == 1
df['income_ssi_disability'] = df['pssid'] == 1
df['income_tanf'] = df['ptanf'] == 1
df['income_other_gov'] = df['powben'] == 1
df['income_interest'] = df['pintrstr'] == 1
df['income_dividend'] = df['pdivd'] == 1
df['income_child_support'] = df['pchldsp'] == 1
df['income_other'] = df['pincot'] == 1
df['applied_ssi'] = df['pssapl'] == 1
df['applied_ssdi'] = df['psdapl'] == 1
df['months_tanf'] = df['tanfmyr'].apply(lambda x: 0 if x in [97,98,99] else x)
#df['eligible_snap'] = df['pfstp'] == 1
#df['months_snap'] = df['fstpmyr'].apply(lambda x: np.nan if x in [97,98,99] else x)
df['eligible_wic'] = df['eligpwic'] == 1
df['wic_benefits'] = df['pwic'] == 1
df['eligible_wic_recode'] = df['wic_flag'] == 1

df['year'] = 2015

df.to_csv('../data/clean/data2015.csv')