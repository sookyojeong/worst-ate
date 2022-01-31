import pandas as pd
import numpy as np

df = pd.read_stata('../data/2013/personsx.dta')

df['region_south'] = (df.region=='3 South')
df['region_west'] = (df.region=='4 West')
df['region_midwest'] = (df.region=='2 Midwest')
df['region_northeast'] = (df.region=='1 Northeast')

df['sex_female'] = df.sex == '2 Female'
df['sex_male'] = df.sex == '1 Male'

df['hispanic'] = df.origin_i == '1 Yes'
df['race_white'] = df.racreci3 == '1 White'
df['race_black'] = df.racreci3 == '2 Black'
df['race_asian'] = df.racreci3 == '3 Asian'

df['armed_forces'] = df.nowaf == '1 Armed Forces'

#df['dob_y'] = df['dob_y_p'].apply(lambda x: np.nan if x in ['9997','9998','9999'] else int(x))
# get age
df['age'] = df['age_p'].str[0:2].astype('float')

df['married'] = (df['r_maritl']=='1 Married - spouse in household')|(df['r_maritl']=='2 Married - spouse not in household')
df['divorced'] = df['r_maritl'] == '5 Divorced'
df['widowed'] = df['r_maritl'] == '4 Widowed'

df['bio_mother'] = df['mom_degp'] == '1 Biological or adoptive'
df['bio_father'] = df['dad_degp'] == '1 Biological or adoptive'

df['mom_colplus'] = df['mom_ed'].isin(["07 Bachelor's degree",'05 AA degree, technical or vocational',
                                       "08 Master's, professional, or doctoral degree",
                                       "06 AA degree, academic program"])
df['mom_noged'] = df['mom_ed'].isin(['02 9-12th grade, no high school diploma',
                                     '01 Less than/equal to 8th grade'])

df['dad_colplus'] = df['dad_ed'].isin(["07 Bachelor's degree",'05 AA degree, technical or vocational',
                                       "08 Master's, professional, or doctoral degree",
                                       "06 AA degree, academic program"])
df['dad_noged'] = df['dad_ed'].isin(['02 9-12th grade, no high school diploma',
                                     '01 Less than/equal to 8th grade'])

df['special_ed'] = df['pspedeis'] == '1 Yes'
df['need_help_personal_care'] = df['plaadl'] == '1 Yes'

df['need_help_bath_all'] = df['labath'] == '1 Yes'
df['need_help_dress_all'] = df['ladress'] == '1 Yes'
df['need_help_eat_all'] = df['laeat'] == '1 Yes'
df['need_help_bed_all'] = df['labed'] == '1 Yes'
df['need_help_toilt_all'] = df['latoilt'] == '1 Yes'
df['need_help_home_all'] = df['lahome'] == '1 Yes'

df['need_help_routine_needs_gt18'] = df['plaiadl'] == '1 Yes'
df['unable_to_work_gt18'] = df['plawknow'] == '1 Yes'
df['limited_to_work_gt18'] = df['plawklim'] == '1 Limited in work'
df['limited_walking_all'] = df['plawalk'] == '1 Yes'
df['limited_remember_all'] = df['plaremem'] == '1 Yes'
df['limited_other_all'] = df['plimany'] == '1 Yes, limited in some other way'
df['limited_any_lt5'] = df['la1ar'] == '1 Limited in any way'

df['vision_lt18'] = df['lahcc1'] == '1 Mentioned'
df['hearing_lt18'] = df['lahcc2'] == '1 Mentioned'
df['speech_lt18'] = df['lahcc3'] == '1 Mentioned'
df['asthma_lt18'] = df['lahcc4'] == '1 Mentioned'
df['birth_defect_lt18'] = df['lahcc5'] == '1 Mentioned'
df['injury_lt18'] = df['lahcc6'] == '1 Mentioned'
df['retard_lt18'] = df['lahcc7a'] == '1 Mentioned'
df['develop_lt18'] = df['lahcc8'] == '1 Mentioned'
df['mental_lt18'] = df['lahcc9'] == '1 Mentioned'
df['muscle_lt18'] = df['lahcc10'] == '1 Mentioned'
df['epilepsy_lt18'] = df['lahcc11'] == '1 Mentioned'
df['learning_lt18'] = df['lahcc12'] == '1 Mentioned'
df['adhd_lt18'] = df['lahcc13'] == '1 Mentioned'
df['other1_lt18'] = df['lahcc90'] == '1 Mentioned'
df['other2_lt18'] = df['lahcc91'] == '1 Mentioned'

df['vision_1yrp_lt18'] = df['lcdurb1'] == '4 More than 1 year'
df['hearing_1yrp_lt18'] = df['lcdurb2'] == '4 More than 1 year'
df['speech_1yrp_lt18'] = df['lcdurb3'] == '4 More than 1 year'
df['asthma_1yrp_lt18'] = df['lcdurb4'] == '4 More than 1 year'
df['birth_defect_1yrp_lt18'] = df['lcdurb5'] == '4 More than 1 year'
df['injury_1yrp_lt18'] = df['lcdurb6'] == '4 More than 1 year'
df['retard_1yrp_lt18'] = df['lcdurb7a'] == '4 More than 1 year'
df['develop_1yrp_lt18'] = df['lcdurb8'] == '4 More than 1 year'
df['mental_1yrp_lt18'] = df['lcdurb9'] == '4 More than 1 year'
df['muscle_1yrp_lt18'] = df['lcdurb10'] == '4 More than 1 year'
df['epilepsy_1yrp_lt18'] = df['lcdurb11'] == '4 More than 1 year'
df['learning_1yrp_lt18'] = df['lcdurb12'] == '4 More than 1 year'
df['adhd_1yrp_lt18'] = df['lcdurb13'] == '4 More than 1 year'
df['other1_1yrp_lt18'] = df['lcdurb90'] == '4 More than 1 year'
df['other2_1yrp_lt18'] = df['lcdurb91'] == '4 More than 1 year'

df['vision_chrc_lt18'] = df['lcchrc1'] == '1 Chronic'
df['hearing_chrc_lt18'] = df['lcchrc2'] == '1 Chronic'
df['speech_chrc_lt18'] = df['lcchrc3'] == '1 Chronic'
df['asthma_chrc_lt18'] = df['lcchrc4'] == '1 Chronic'
df['birth_defect_chrc_lt18'] = df['lcchrc5'] == '1 Chronic'
df['injury_chrc_lt18'] = df['lcchrc6'] == '1 Chronic'
df['retard_chrc_lt18'] = df['lcchrc7a'] == '1 Chronic'
df['develop_chrc_lt18'] = df['lcchrc8'] == '1 Chronic'
df['mental_chrc_lt18'] = df['lcchrc9'] == '1 Chronic'
df['muscle_chrc_lt18'] = df['lcchrc10'] == '1 Chronic'
df['epilepsy_chrc_lt18'] = df['lcchrc11'] == '1 Chronic'
df['learning_chrc_lt18'] = df['lcchrc12'] == '1 Chronic'
df['adhd_chrc_lt18'] = df['lcchrc13'] == '1 Chronic'
df['other1_chrc_lt18'] = df['lcchrc90'] == '1 Chronic'
df['other2_chrc_lt18'] = df['lcchrc91'] == '1 Chronic'

df['vision_gt18'] = df['lahca1'] == '1 Mentioned'
df['hearing_gt18'] = df['lahca2'] == '1 Mentioned'
df['arthritis_gt18'] = df['lahca3'] == '1 Mentioned'
df['back_gt18'] = df['lahca4'] == '1 Mentioned'
df['bone_injury_gt18'] = df['lahca5'] == '1 Mentioned'
df['other_injury_gt18'] = df['lahca6'] == '1 Mentioned'
df['heart_gt18'] = df['lahca7'] == '1 Mentioned'
df['stroke_gt18'] = df['lahca8'] == '1 Mentioned'
df['hypertension_gt18'] = df['lahca9'] == '1 Mentioned'
df['diabetes_gt18'] = df['lahca10'] == '1 Mentioned'
df['lung_gt18'] = df['lahca11'] == '1 Mentioned'
df['cancer_gt18'] = df['lahca12'] == '1 Mentioned'
df['birth_defect_gt18'] = df['lahca13'] == '1 Mentioned'
df['retard_gt18'] = df['lahca14a'] == '1 Mentioned'
df['other_develop_gt18'] = df['lahca15'] == '1 Mentioned'
df['senility_gt18'] = df['lahca16'] == '1 Mentioned'
df['emotional_gt18'] = df['lahca17'] == '1 Mentioned'
df['weight_gt18'] = df['lahca18'] == '1 Mentioned'
df['amputated_gt18'] = df['lahca19_'] == '1 Mentioned'
df['musculoskeletal_gt18'] = df['lahca20_'] == '1 Mentioned'
df['circulation_gt18'] = df['lahca21_'] == '1 Mentioned'
df['metabolic_gt18'] = df['lahca22_'] == '1 Mentioned'
df['sensory_gt18'] = df['lahca23_'] == '1 Mentioned'
df['digestive_gt18'] = df['lahca24_'] == '1 Mentioned'
df['genitourinary_gt18'] = df['lahca25_'] == '1 Mentioned'
df['skin_gt18'] = df['lahca26_'] == '1 Mentioned'
df['blood_gt18'] = df['lahca27_'] == '1 Mentioned'
df['benign_tumor_gt18'] = df['lahca28_'] == '1 Mentioned'
df['alcohol_gt18'] = df['lahca29_'] == '1 Mentioned'
df['mental_gt18'] = df['lahca30_'] == '1 Mentioned'
df['surgical_gt18'] = df['lahca31_'] == '1 Mentioned'
df['aging_gt18'] = df['lahca32_'] == '1 Mentioned'
df['fatigue_gt18'] = df['lahca33_'] == '1 Mentioned'
df['pregnancy_gt18'] = df['lahca34_'] == '1 Mentioned'
df['other1_gt18'] = df['lahca90'] == '1 Mentioned'
df['other2_gt18'] = df['lahca91'] == '1 Mentioned'

df['vision_1yrp_gt18'] = df['ladurb1'] == '4 More than 1 year'
df['hearing_1yrp_gt18'] = df['ladurb2'] == '4 More than 1 year'
df['arthritis_1yrp_gt18'] = df['ladurb3'] == '4 More than 1 year'
df['back_1yrp_gt18'] = df['ladurb4'] == '4 More than 1 year'
df['bone_injury_1yrp_gt18'] = df['ladurb5'] == '4 More than 1 year'
df['other_injury_1yrp_gt18'] = df['ladurb6'] == '4 More than 1 year'
df['heart_1yrp_gt18'] = df['ladurb7'] == '4 More than 1 year'
df['stroke_1yrp_gt18'] = df['ladurb8'] == '4 More than 1 year'
df['hypertension_1yrp_gt18'] = df['ladurb9'] == '4 More than 1 year'
df['diabetes_1yrp_gt18'] = df['ladurb10'] == '4 More than 1 year'
df['lung_1yrp_gt18'] = df['ladurb11'] == '4 More than 1 year'
df['cancer_1yrp_gt18'] = df['ladurb12'] == '4 More than 1 year'
df['birth_defect_1yrp_gt18'] = df['ladurb13'] == '4 More than 1 year'
df['retard_1yrp_gt18'] = df['ldurb14a'] == '4 More than 1 year'
df['other_develop_1yrp_gt18'] = df['ladurb15'] == '4 More than 1 year'
df['senility_1yrp_gt18'] = df['ladurb16'] == '4 More than 1 year'
df['emotional_1yrp_gt18'] = df['ladurb17'] == '4 More than 1 year'
df['weight_1yrp_gt18'] = df['ladurb18'] == '4 More than 1 year'
df['amputated_1yrp_gt18'] = df['ladurb19'] == '4 More than 1 year'
df['musculoskeletal_1yrp_gt18'] = df['ladurb20'] == '4 More than 1 year'
df['circulation_1yrp_gt18'] = df['ladurb21'] == '4 More than 1 year'
df['metabolic_1yrp_gt18'] = df['ladurb22'] == '4 More than 1 year'
df['sensory_1yrp_gt18'] = df['ladurb23'] == '4 More than 1 year'
df['digestive_1yrp_gt18'] = df['ladurb24'] == '4 More than 1 year'
df['genitourinary_1yrp_gt18'] = df['ladurb25'] == '4 More than 1 year'
df['skin_1yrp_gt18'] = df['ladurb26'] == '4 More than 1 year'
df['blood_1yrp_gt18'] = df['ladurb27'] == '4 More than 1 year'
df['benign_tumor_1yrp_gt18'] = df['ladurb28'] == '4 More than 1 year'
df['alcohol_1yrp_gt18'] = df['ladurb29'] == '4 More than 1 year'
df['mental_1yrp_gt18'] = df['ladurb30'] == '4 More than 1 year'
df['surgical_1yrp_gt18'] = df['ladurb31'] == '4 More than 1 year'
df['aging_1yrp_gt18'] = df['ladurb32'] == '4 More than 1 year'
df['fatigue_1yrp_gt18'] = df['ladurb33'] == '4 More than 1 year'
df['pregnancy_1yrp_gt18'] = df['ladurb34'] == '4 More than 1 year'
df['other1_1yrp_gt18'] = df['ladurb90'] == '4 More than 1 year'
df['other2_1yrp_gt18'] = df['ladurb91'] == '4 More than 1 year'

df['vision_chrc_gt18'] = df['lachrc1'] == '1 Chronic'
df['hearing_chrc_gt18'] = df['lachrc2'] == '1 Chronic'
df['arthritis_chrc_gt18'] = df['lachrc3'] == '1 Chronic'
df['back_chrc_gt18'] = df['lachrc4'] == '1 Chronic'
df['bone_injury_chrc_gt18'] = df['lachrc5'] == '1 Chronic'
df['other_injury_chrc_gt18'] = df['lachrc6'] == '1 Chronic'
df['heart_chrc_gt18'] = df['lachrc7'] == '1 Chronic'
df['stroke_chrc_gt18'] = df['lachrc8'] == '1 Chronic'
df['hypertension_chrc_gt18'] = df['lachrc9'] == '1 Chronic'
df['diabetes_chrc_gt18'] = df['lachrc10'] == '1 Chronic'
df['lung_chrc_gt18'] = df['lachrc11'] == '1 Chronic'
df['cancer_chrc_gt18'] = df['lachrc12'] == '1 Chronic'
df['birth_defect_chrc_gt18'] = df['lachrc13'] == '1 Chronic'
df['retard_chrc_gt18'] = df['lchrc14a'] == '1 Chronic'
df['other_develop_chrc_gt18'] = df['lachrc15'] == '1 Chronic'
df['senility_chrc_gt18'] = df['lachrc16'] == '1 Chronic'
df['emotional_chrc_gt18'] = df['lachrc17'] == '1 Chronic'
df['weight_chrc_gt18'] = df['lachrc18'] == '1 Chronic'
df['amputated_chrc_gt18'] = df['lachrc19'] == '1 Chronic'
df['musculoskeletal_chrc_gt18'] = df['lachrc20'] == '1 Chronic'
df['circulation_chrc_gt18'] = df['lachrc21'] == '1 Chronic'
df['metabolic_chrc_gt18'] = df['lachrc22'] == '1 Chronic'
df['sensory_chrc_gt18'] = df['lachrc23'] == '1 Chronic'
df['digestive_chrc_gt18'] = df['lachrc24'] == '1 Chronic'
df['genitourinary_chrc_gt18'] = df['lachrc25'] == '1 Chronic'
df['skin_chrc_gt18'] = df['lachrc26'] == '1 Chronic'
df['blood_chrc_gt18'] = df['lachrc27'] == '1 Chronic'
df['benign_tumor_chrc_gt18'] = df['lachrc28'] == '1 Chronic'
df['alcohol_chrc_gt18'] = df['lachrc29'] == '1 Chronic'
df['mental_chrc_gt18'] = df['lachrc30'] == '1 Chronic'
df['surgical_chrc_gt18'] = df['lachrc31'] == '1 Chronic'
df['aging_chrc_gt18'] = df['lachrc32'] == '1 Chronic'
df['fatigue_chrc_gt18'] = df['lachrc33'] == '1 Chronic'
df['pregnancy_chrc_gt18'] = df['lachrc34'] == '1 Chronic'
df['other1_chrc_gt18'] = df['lachrc90'] == '1 Chronic'
df['other2_chrc_gt18'] = df['lachrc91'] == '1 Chronic'

df['chronic_all'] = df['lcondrt'] == '1 At least one condition causing limitation of activity is chronic'
df['health_status_excellent'] = df['phstat'] == '1 Excellent'
df['health_status_verygood'] = df['phstat'] == '2 Very good'
df['health_status_good'] = df['phstat'] == '3 Good'
df['health_status_fair'] = df['phstat'] == '4 Fair'
df['health_status_poor'] = df['phstat'] == '5 Poor'

df['care_delayed_cost'] = df['pdmed12m'] == '1 Yes'
df['care_notget_cost'] = df['pnmed12m'] == '1 Yes'
df['overnight_hospital'] = df['phospyr2'] == '1 Yes'
df['overnight_hospital_times'] = df['hospno'].apply(lambda x: 0 if x in ['997 Refused','998',"999 Don't know"] else int(x))
df['overnight_hospital_nights'] = df['hpnite'].apply(lambda x: 0 if x in ['997 Refused','998',"999 Don't know"] else int(x))
df['care_athome_2wks'] = df['phchm2w'] == '1 Yes'
df['care_athome_2wks_times'] = df['phchmn2w'].apply(lambda x: 0 if x in ['97 Refused','98',"99 Don't know"] else int(x))
df['care_phone_2wks'] = df['phcph2wr'] == '1 Yes'
df['care_phone_2wks_times'] = df['phcphn2w'].apply(lambda x: 0 if x in ['97 Refused','98',"99 Don't know"] else int(x))
df['care_office_2wks'] = df['phcdv2w'] == '1 Yes'
df['care_office_2wks_times'] = df['phcdvn2w'].apply(lambda x: 0 if x in ['97 Refused','98',"99 Don't know"] else int(x))

df['care_10more_12mo'] = df['p10dvyr'] == '1 Yes'
df['notcov_'] = df['notcov']=='1 Not covered'
df['medicare_'] = df['medicare'].isin(['1 Yes, information', '2 Yes, but no information'])
df['medicare_partA_only'] = df['mcpart'] == '1 Part A - Hospital only'
df['medicare_partB_only']= df['mcpart'] == '2 Part B - Medical only'
df['medicare_bothparts'] = df['mcpart'] == '3 Both Part A and Part B'
df['medicare_advantage'] = df['mcchoice'] == '1 Yes'
df['medicare_hmo'] = df['mchmo'] == '1 Yes'
df['medicare_need_referral'] = df['mcref'] == '1 Yes'
df['medicare_pay_premium'] = df['mcprem'] == '1 Yes'
df['medicare_partD'] = df['mcpartd'] == '1 Yes'

df['medicaid_'] = df['medicaid'].isin(['1 Yes, information', '2 Yes, but no information'])
df['medicaid_md'] = df['machmd'].isin(['1 Any doctor', '2 Select from book/list', '3 Doctor is assigned'])
df.loc[df['machmd'].isna()==True,'medicaid_md'] = False
#df['medicaid_primary_routine'] = df['mapcmd'] == '1 Yes'
#df['medicaid_special_referral'] = df['maref'] == '1 Yes'

df['single_'] = df['single'].isin( ['1 Yes, with information', '2 Yes, but no information'] )
df['single_accidents'] = df['sstypea'] == '1 Mentioned'
df['single_aids'] = df['sstypeb'] == '1 Mentioned'
df['single_cancer'] = df['sstypec'] == '1 Mentioned'
df['single_catastrophic'] = df['sstyped'] == '1 Mentioned'
df['single_dental'] = df['sstypee'] == '1 Mentioned'
df['single_disability'] = df['sstypef'] == '1 Mentioned'
df['single_hospice'] = df['sstypeg'] == '1 Mentioned'
df['single_hospitalization'] = df['sstypeh'] == '1 Mentioned'
df['single_longterm_care'] = df['sstypei'] == '1 Mentioned'
df['single_prescription'] = df['sstypej'] == '1 Mentioned'
df['single_vision'] = df['sstypek'] == '1 Mentioned'
df['single_other'] = df['sstypel'] == '1 Mentioned'

df['private_'] = df['private'].isin(['1 Yes, information', '2 Yes, but no information'])
df['private1_primary'] = df['whonam1'] == '1 In own name'
df['private1_thru_wrk_employer'] = df['plnwrkr1'] == '01 Through employer'
df['private1_thru_wrk_union'] = df['plnwrkr1'] == '02 Through union'
df['private1_thru_wrk_other'] = df['plnwrkr1'].isin(["03 Through workplace, but don't know if employer or union",
                                                     '04 Through workplace, self-employed or professional association'])
df['private1_thru_direct'] = df['plnwrkr1'] == '05 Purchased directly'
df['private1_thru_state'] = df['plnwrkr1'] == '06 Through a state/local government or community program'
df['private1_thru_school'] = df['plnwrkr1'] == '08 Through school'
df['private1_paid_self'] = df['plnpay11'] == '1 Mentioned'
df['private1_paid_employer'] = df['plnpay21'] == '1 Mentioned'
df['private1_paid_other'] = df['plnpay31'] == '1 Mentioned'
df['private1_paid_medicare'] = df['plnpay41'] == '1 Mentioned'
df['private1_paid_medicaid'] = df['plnpay51'] == '1 Mentioned'
df['private1_paid_schip'] = df['plnpay61'] == '1 Mentioned'
df['private1_paid_government'] = df['plnpay71'] == '1 Mentioned'

df['private1_oop_20k'] = df['hicostr1'].apply(lambda x: 0 if x in ['99997 Refused','99998',"99999 Don't know"]  else x)
df['private1_oop_20k'] = df['private1_oop_20k'].apply(lambda x: 20000 if x=="20000 $20,000 or more"  else float(x))
df['private1_type_hmo'] = df['plnmgd1'] == '1 HMO/IPA'
df['private1_type_ppo'] = df['plnmgd1'] == '2 PPO'
df['private1_type_pos'] = df['plnmgd1'] == '3 POS'
df['private1_type_ffs'] = df['plnmgd1'] == '4 Fee-for-service/indemnity'
df['private1_hdhp'] = df['hdhp1'] == '1 Less than [$1,250/$2,500]'
df['private1_hsa'] = df['hsahra1'] == '1 Yes'
df['private1_choose_md'] = df['mgchmd1'] == '1 Any doctor'
df['private1_network_md'] = df['mgprmd1'] == '1 Yes'
df['private1_oon_md'] = df['mgpymd1'] == '1 Yes'
#df['private1_need_referral'] = df['mgpref1'] == '1 Yes'
df['private1_rx'] = df['prrxcov1'] == '1 Yes'
df['private1_dental'] = df['prdncov1'] == '1 Yes'

df['private2_primary'] = df['whonam2'] == '1 In own name'
df['private2_thru_wrk_employer'] = df['plnwrkr2'] == '01 Through employer'
df['private2_thru_wrk_union'] = df['plnwrkr2'] == '02 Through union'
df['private2_thru_wrk_other'] = df['plnwrkr2'].isin(["03 Through workplace, but don't know if employer or union",
                                                     '04 Through workplace, self-employed or professional association'])
df['private2_thru_direct'] = df['plnwrkr2'] == '05 Purchased directly'
df['private2_thru_state'] = df['plnwrkr2'] == '06 Through a state/local government or community program'
df['private2_thru_school'] = df['plnwrkr2'] == '08 Through school'
df['private2_paid_self'] = df['plnpay12'] == '1 Mentioned'
df['private2_paid_employer'] = df['plnpay22'] == '1 Mentioned'
df['private2_paid_other'] = df['plnpay32'] == '1 Mentioned'
df['private2_paid_medicare'] = df['plnpay42'] == '1 Mentioned'
df['private2_paid_medicaid'] = df['plnpay52'] == '1 Mentioned'
df['private2_paid_schip'] = df['plnpay62'] == '1 Mentioned'
df['private2_paid_government'] = df['plnpay72'] == '1 Mentioned'
df['private2_oop_20k'] = df['hicostr2'].apply(lambda x: 0 if x in ['99997 Refused','99998',"99999 Don't know"]  else x)
df['private2_oop_20k'] = df['private2_oop_20k'].apply(lambda x: 20000 if x=="20000 $20,000 or more"  else float(x))

df['private2_type_hmo'] = df['plnmgd2'] == '1 HMO/IPA'
df['private2_type_ppo'] = df['plnmgd2'] == '2 PPO'
df['private2_type_pos'] = df['plnmgd2'] == '3 POS'
df['private2_type_ffs'] = df['plnmgd2'] == '4 Fee-for-service/indemnity'
df['private2_hdhp'] = df['hdhp2'] == '1 Less than [$1,200/$2,400]'
df['private2_hsa'] = df['hsahra2'] == '1 Yes'
df['private2_choose_md'] = df['mgchmd2'] == '1 Any doctor'
df['private2_network_md'] = df['mgprmd2'] == '1 Yes'
df['private2_oon_md'] = df['mgpymd2'] == '1 Yes'
#df['private2_need_referral'] = df['mgpref2'] == '1 Yes'
df['private2_rx'] = df['prrxcov2'] == '1 Yes'
df['private2_dental'] = df['prdncov2'] == '1 Yes'
df['private_2plus'] = df['prplplus'] == '1 Yes'

df['schip_'] = df['schip'].isin(['1 Yes, information', '2 Yes, but no information'])
df['schip_md'] = df['stdoc1'].isin(['1 Any doctor', '2 Select from book/list', '3 Doctor is assigned'])
#df['schip_primary_routine'] = df['stpcmd1'] == '1 Yes'
#df['schip_special_referral'] = df['stref1'] == '1 Yes'

df['othpub_'] = df['othpub'].isin(['1 Yes, information', '2 Yes, but no information'])
df['othpub_md'] = df['stdoc2'].isin(['1 Any doctor', '2 Select from book/list', '3 Doctor is assigned'])
#df['othpub_primary_routine'] = df['stpcmd2'] == '1 Yes'
#df['othpub_special_referral'] = df['stref2'] == '1 Yes'

df['othgov_'] = df['othgov'].isin(['1 Yes, information', '2 Yes, but no information'])
df['othgov_md'] = df['stdoc3'].isin(['1 Any doctor', '2 Select from book/list', '3 Doctor is assigned'])
#df['othgov_primary_routine'] = df['stpcmd3'] == '1 Yes'
#df['othgov_special_referral'] = df['stref3'] == '1 Yes'

df['milcare_'] = df['milcare'].isin( ['1 Yes, information', '2 Yes, but no information'])
df['milcare_tricare'] = df['milspc1'] == '1 Mentioned'
df['milcare_va'] = df['milspc2'] == '1 Mentioned'
df['milcare_champ-va'] = df['milspc3'] == '1 Mentioned'
df['milcare_other'] = df['milspc4'] == '1 Mentioned'
df['milcare_tricare_prime'] = df['milman'] == '1 TRICARE Prime'
df['milcare_tricare_standard_extra'] = df['milman'].isin(['2 TRICARE Extra', '3 TRICARE Standard'])

df['milcare_tricare_forlife'] = df['milman'] == '4 TRICARE for life'

df['ihs_'] = df['ihs']=='1 Yes'

df['hilast_6mo'] = df['hilast'] == '1 6 months or less'
df['hilast_1yr'] = df['hilast'] == '2 More than 6 months, but not more than 1 year ago'
df['hilast_3yr'] = df['hilast'] == '3 More than 1 year, but not more than 3 years ago'
df['hilast_3yrplus'] = df['hilast'] == '4 More than 3 years'

df['histop_losejob'] = df['histop1'] == '1 Mentioned'
df['histop_divorce'] = df['histop2'] == '1 Mentioned'
df['histop_age'] = df['histop3'] == '1 Mentioned'
df['histop_eligible'] = df['histop4'] == '1 Mentioned'
df['histop_highcost'] = df['histop5'] == '1 Mentioned'
df['histop_refused'] = df['histop6'] == '1 Mentioned'
df['histop_medicaid_pregnancy'] = df['histop7'] == '1 Mentioned'
df['histop_medicaid_newjob'] = df['histop8'] == '1 Mentioned'
df['histop_medicaid_other'] = df['histop9'] == '1 Mentioned'
df['histop_other'] = df['histop10'] == '1 Mentioned'
df['histop_never'] = df['histop11'] == '1 Mentioned'
df['histop_moved'] = df['histop12'] == '1 Mentioned'
df['histop_selfemployed'] = df['histop13'] == '1 Mentioned'
df['histop_noneed'] = df['histop14'] == '1 Mentioned'
df['histop_gotmarried'] = df['histop15'] == '1 Mentioned'

df['hino_12mo'] = df['hinotyr'] == '1 Yes'
df['hino_months'] = df['hinotmyr'].apply(lambda x: 0 if x in ['97 Refused','98',"99 Don't know"] else float(x))

df['care_spent_zero'] = df['hcspfyr'] == '0 Zero'
df['care_spent_lt500'] = df['hcspfyr'] == '1 Less than $500'
df['care_spent_lt2k'] = df['hcspfyr'] == '2 $500 - $1,999'
df['care_spent_lt3k'] = df['hcspfyr'] == '3 $2,000 - $2,999'
df['care_spent_lt5k'] = df['hcspfyr'] == '4 $3,000 - $4,999'
df['care_spent_gt5k'] = df['hcspfyr'] == '5 $5,000 or more'

df['fsa_'] = df['fsa']=='1 Yes'

df['hikind_private'] = df['hikindna'] == '1 Mentioned'
df['hikind_medicare'] = df['hikindnb'] == '1 Mentioned'
df['hikind_medigap'] = df['hikindnc'] == '1 Mentioned'
df['hikind_medicaid'] = df['hikindnd'] == '1 Mentioned'
df['hikind_schip'] = df['hikindne'] == '1 Mentioned'
df['hikind_military'] = df['hikindnf'] == '1 Mentioned'
df['hikind_ihs'] = df['hikindng'] == '1 Mentioned'
df['hikind_state'] = df['hikindnh'] == '1 Mentioned'
df['hikind_othgov'] = df['hikindni'] == '1 Mentioned'
df['hikind_ssp'] = df['hikindnj'] == '1 Mentioned'
df['hikind_nocov'] = df['hikindnk'] == '1 Mentioned'

df['medicare_probe'] = df['mcareprb'] == '1 Yes'
df['medicaid_probe'] = df['mcaidprb'] == '1 Yes'
df['ssp_probe'] = df['sincov'] == '1 Yes'

df['born_us'] = df['plborn'] == '1 Yes'
df['born_mexico'] = df['regionbr'] == '02 Mexico, Central America, Caribbean Islands'
df['born_southamerica'] = df['regionbr'] == '03 South America'
df['born_europe'] = df['regionbr'] == '04 Europe'
df['born_russia'] = df['regionbr'] == '05 Russia (and former USSR areas)'
df['born_africa'] = df['regionbr'] == '06 Africa'
df['born_middle_east'] = df['regionbr'] == '07 Middle East'
df['born_indian'] = df['regionbr'] == '08 Indian Subcontinent'
df['born_asia'] = df['regionbr'] == '09 Asia'
df['born_se_asia'] = df['regionbr'] == '10 SE Asia'

df['yrs_us_lt1'] = df['yrsinus'] == '1 Less than 1 year'
df['yrs_us_lt5'] = df['yrsinus'] == '2 1 yr., less than 5 yrs.'
df['yrs_us_lt10'] = df['yrsinus'] == '3 5 yrs., less than 10 yrs.'
df['yrs_us_lt15'] = df['yrsinus'] == '4 10 yrs., less than 15 yrs.'
df['yrs_us_gt15'] = df['yrsinus'] == '5 15 years or more'

df['us_citizen'] = df['citizenp'] == '1 Yes, citizen of the United States'

df['headstart'] = df['headst'] == '1 Yes'
df['headstart_ever'] = df['headstv1'] == '1 Yes'

df['educ_yrs'] = df['educ1'].str[0:2].astype('int')
df['educ_highschl'] = df['educ1'].isin(['13 GED or equivalent', '14 High School Graduate'])
df['educ_somecol'] = df['educ1'].isin(['15 Some college, no degree', '16 Associate degree: occupational, technical, or vocational program',
                                     '17 Associate degree: academic program'])
df['educ_colplus'] = df['educ1'].isin(["18 Bachelor's degree (Example: BA, AB, BS, BBA)",
                                                               "19 Master's degree (Example: MA, MS, MEng, MEd, MBA)",
                                                               "20 Professional School degree (Example: MD, DDS, DVM, JD)",
                                                               "21 Doctoral degree (Example: PhD, EdD)"])
#df['military_honorable_discharge'] = df['pmiltry'] == '1 Yes'

df['employed']  = df['doinglwp'].isin( ['1 Working for pay at a job or business',
                                                               '2 With a job or business but not at work'])
df['looking_for_work'] = df['doinglwp'] == '3 Looking for work'
df['volunteer'] = df['doinglwp'] == '4 Working, but not for pay, at a family-owned job or business'
df['not_in_labor_force'] = df['doinglwp'] == '5 Not working at a job or business and not looking for work'

df['not_work_family'] = df['whynowkp'] == '01 Taking care of house or family'
df['not_work_school'] = df['whynowkp'] == '02 Going to school'
df['not_work_retired'] = df['whynowkp'] == '03 Retired'
df['not_work_vacation'] = df['whynowkp'] == '04 On a planned vacation from work'
df['not_work_leave'] = df['whynowkp'] == '05 On family or maternity leave'
df['not_work_health'] = df['whynowkp'] == '06 Temporarily unable to work for health reasons'
df['not_work_off_season'] = df['whynowkp'] == '07 Have job/contract and off-season'
df['not_work_layoff'] = df['whynowkp'] == '08 On layoff'
df['not_work_disabled'] = df['whynowkp'] == '09 Disabled'

df['wrkhrs'] = df['wrkhrs2'].apply(lambda x: 0 if x in ['97 Refused','98 Not ascertained',"99 Don't know"] else x)
df['wrkhrs'] = df['wrkhrs'].apply(lambda x: 95 if x == '95 95+ hours' else x)


df['wrkhrs_lt35'] = (0 < df['wrkhrs'].astype('float')) & (df['wrkhrs'].astype('float') <= 35)
df['wrkhrs_lt45'] = (35 < df['wrkhrs'].astype('float')) & (df['wrkhrs'].astype('float') <= 45)
df['wrkhrs_gt20'] = (45 < df['wrkhrs'].astype('float')) & (df['wrkhrs'].astype('float') <= 95)

df['wrk_fulltime'] = df['wrkftall'] == '1 Yes'
df['wrk_lastyr'] = df['wrklyr1'] == '1 Yes'
df['wrk_mo_lastyr'] = df['wrkmyr'].apply(lambda x: 0 if x in ['97 Refused','98 Not ascertained',"99 Don't know"] else x)
df['wrk_mo_lastyr'] = df['wrk_mo_lastyr'].apply(lambda x: 1 if x=='01 1 month or less' else x)

df['earnings_lt5k'] = df['ernyr_p'] == '01 $01-$4,999'
df['earnings_lt10k'] = df['ernyr_p'] == '02 $5,000-$9,999'
df['earnings_lt15k']= df['ernyr_p'] == '03 $10,000-$14,999'
df['earnings_lt20k']= df['ernyr_p'] == '04 $15,000-$19,999'
df['earnings_lt25k']= df['ernyr_p'] == '05 $20,000-$24,999'
df['earnings_lt34k']= df['ernyr_p'] == '06 $25,000-$34,999'
df['earnings_lt45k']= df['ernyr_p'] == '07 $35,000-$44,999'
df['earnings_lt55k']= df['ernyr_p'] == '08 $45,000-$54,999'
df['earnings_lt65k']= df['ernyr_p'] == '09 $55,000-$64,999'
df['earnings_lt75k']= df['ernyr_p'] == '10 $65,000-$74,999'
df['earnings_gt75k']= df['ernyr_p'] == '11 $75,000 and over'

df['hi_offered_atwork'] = df['hiempof'] == '1 Yes'

df['family_income_answered'] = df['fincint'] == '1 Enter 1 to continue'
df['income_wage'] = df['psal'] == '1 Yes'
df['income_self'] = df['pseinc'] == '1 Yes'
df['income_ss'] = df['pssrr'] == '1 Yes'
df['disability_ss'] = df['pssrrdb'] == '1 Yes'
df['disability_benefit'] = df['pssrrd'] == '1 Yes'
df['income_pension'] = df['ppens'] == '1 Yes'

df['income_other_pension'] = df['popens'] == '1 Yes'
df['income_ssi'] = df['pssi'] == '1 Yes'
df['income_ssi_disability'] = df['pssid'] == '1 Yes'
df['income_tanf'] = df['ptanf'] == '1 Yes'
df['income_other_gov'] = df['powben'] == '1 Yes'
df['income_interest'] = df['pintrstr'] == '1 Yes'
df['income_dividend'] = df['pdivd'] == '1 Yes'
df['income_child_support'] = df['pchldsp'] == '1 Yes'
df['income_other'] = df['pincot'] == '1 Yes'
df['applied_ssi'] = df['pssapl'] == '1 Yes'
df['applied_ssdi'] = df['psdapl'] == '1 Yes'
df['months_tanf'] = df['tanfmyr'].apply(lambda x: 0 if x in ['97 Refused','98 Not ascertained',"99 Don't know"] else int(x))
#df['eligible_snap'] = df['pfstp'] == '1 Yes'
#df['months_snap'] = df['fstpmyr'].apply(lambda x: np.nan if x in ['97 Refused','98 Not ascertained',"99 Don't know"] else int(x))
df['eligible_wic'] = df['eligpwic'] == '1 At least 1 WIC age-eligible family member'
df['wic_benefits'] = df['pwic'] == '1 Yes'
df['eligible_wic_recode'] = df['wic_flag'] == '1 Person age-eligible'

df['year'] = 2013
df.to_csv('../data/clean/data2013.csv')
