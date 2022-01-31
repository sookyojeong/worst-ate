import multiprocessing as mp

############################################
# script of params for nhis data
############################################

args_nhis = {}

# for gbdt model
args_nhis['gbdt'] = {}
args_nhis['gbdt']['eta'] = 0.5
args_nhis['gbdt']['max_depth'] = 80
args_nhis['gbdt']['subsample'] = 0.9
args_nhis['gbdt']['min_child_weight'] = 3
args_nhis['gbdt']['colsample_bytree'] = 0.9
args_nhis['gbdt']['tree_method'] = 'hist'
args_nhis['gbdt']['n_jobs'] = mp.cpu_count() - 1
args_nhis['gbdt']['max_bin'] = 300
args_nhis['gbdt']['seed'] = 1
args_nhis['gbdt']['objective']='reg:squarederror'

# for rf model
args_nhis['rf'] = {}
args_nhis['rf']['bagging_fraction'] =.2
args_nhis['rf']['num_threads'] = 90
args_nhis['rf']['bagging_freq'] = 1
args_nhis['rf']['boosting'] = 'rf'
args_nhis['rf']['objective'] = 'cross_entropy'
args_nhis['rf']['learning_rate'] = 0.05
args_nhis['rf']['reg_lambda'] =  1
args_nhis['rf']['feature_fraction'] = 0.05
args_nhis['rf']['reg_alpha'] = 2
args_nhis['rf']['num_leaves'] =  5
args_nhis['rf']['feature_fraction_seed'] =  201
args_nhis['rf']['bagging_seed'] =  427
                                
# features
args_nhis['x'] = ['sex_female', 'sex_male', 'hispanic', 'race_white', 'race_black',
    'race_asian','armed_forces',#'age',
    'married','divorced','widowed',
    'bio_mother','bio_father','mom_colplus','mom_noged','dad_colplus',
    'dad_noged','special_ed','need_help_personal_care',
    'need_help_bath_all','need_help_dress_all',
    'need_help_eat_all', 'need_help_bed_all','need_help_toilt_all',
    'need_help_home_all', 'need_help_routine_needs_gt18',
    'unable_to_work_gt18','limited_to_work_gt18',
    'limited_walking_all','limited_remember_all',
    'limited_other_all','limited_any_lt5',
    'vision_lt18','hearing_lt18','speech_lt18','asthma_lt18',
    'birth_defect_lt18','injury_lt18','retard_lt18','develop_lt18',
    'mental_lt18','muscle_lt18','epilepsy_lt18','learning_lt18',
    'adhd_lt18','other1_lt18','other2_lt18',
    'vision_1yrp_lt18','hearing_1yrp_lt18','speech_1yrp_lt18',
    'asthma_1yrp_lt18','birth_defect_1yrp_lt18','injury_1yrp_lt18',
    'retard_1yrp_lt18','develop_1yrp_lt18','mental_1yrp_lt18',
    'muscle_1yrp_lt18','epilepsy_1yrp_lt18','learning_1yrp_lt18',
    'adhd_1yrp_lt18','other1_1yrp_lt18', 'other2_1yrp_lt18',
    'vision_chrc_lt18', 'hearing_chrc_lt18', 'speech_chrc_lt18',
    'asthma_chrc_lt18','birth_defect_chrc_lt18','injury_chrc_lt18',
    'retard_chrc_lt18','develop_chrc_lt18','mental_chrc_lt18',
    'muscle_chrc_lt18','epilepsy_chrc_lt18','learning_chrc_lt18',
    'adhd_chrc_lt18','other1_chrc_lt18','other2_chrc_lt18',
    'vision_gt18','hearing_gt18','arthritis_gt18','back_gt18',
    'bone_injury_gt18','other_injury_gt18','heart_gt18','stroke_gt18',
    'hypertension_gt18','diabetes_gt18','lung_gt18','cancer_gt18',
    'birth_defect_gt18','retard_gt18','other_develop_gt18',
    'senility_gt18','emotional_gt18','weight_gt18','amputated_gt18',
    'musculoskeletal_gt18','circulation_gt18','metabolic_gt18',
    'sensory_gt18','digestive_gt18','genitourinary_gt18',
    'skin_gt18','blood_gt18','benign_tumor_gt18','alcohol_gt18',
    'mental_gt18','surgical_gt18','aging_gt18','fatigue_gt18',
    #'pregnancy_gt18',
    'other1_gt18','other2_gt18',
    'vision_1yrp_gt18','hearing_1yrp_gt18','arthritis_1yrp_gt18',
    'back_1yrp_gt18',
    'bone_injury_1yrp_gt18','other_injury_1yrp_gt18','heart_1yrp_gt18',
    'stroke_1yrp_gt18',
    'hypertension_1yrp_gt18','diabetes_1yrp_gt18','lung_1yrp_gt18',
    'cancer_1yrp_gt18',
    'birth_defect_1yrp_gt18','retard_1yrp_gt18','other_develop_1yrp_gt18',
    'senility_1yrp_gt18','emotional_1yrp_gt18','weight_1yrp_gt18',
    'amputated_1yrp_gt18',
    'musculoskeletal_1yrp_gt18','circulation_1yrp_gt18',
    'metabolic_1yrp_gt18',
    'sensory_1yrp_gt18','digestive_1yrp_gt18','genitourinary_1yrp_gt18',
    'skin_1yrp_gt18','blood_1yrp_gt18','benign_tumor_1yrp_gt18',
    'alcohol_1yrp_gt18',
    'mental_1yrp_gt18','surgical_1yrp_gt18','aging_1yrp_gt18',
    'fatigue_1yrp_gt18',
    'pregnancy_1yrp_gt18','other1_1yrp_gt18','other2_1yrp_gt18',
    'vision_chrc_gt18','hearing_chrc_gt18','arthritis_chrc_gt18',
    'back_chrc_gt18',
    'bone_injury_chrc_gt18','other_injury_chrc_gt18','heart_chrc_gt18',
    'stroke_chrc_gt18',
    'hypertension_chrc_gt18','diabetes_chrc_gt18','lung_chrc_gt18',
    'cancer_chrc_gt18',
    'birth_defect_chrc_gt18','retard_chrc_gt18',
    'other_develop_chrc_gt18',
    'senility_chrc_gt18','emotional_chrc_gt18','weight_chrc_gt18',
    'amputated_chrc_gt18',
    'musculoskeletal_chrc_gt18','circulation_chrc_gt18',
    'metabolic_chrc_gt18',
    'sensory_chrc_gt18','digestive_chrc_gt18','genitourinary_chrc_gt18',
    'skin_chrc_gt18','blood_chrc_gt18','benign_tumor_chrc_gt18',
    'alcohol_chrc_gt18',
    'mental_chrc_gt18','surgical_chrc_gt18','aging_chrc_gt18',
    'fatigue_chrc_gt18',
    'pregnancy_chrc_gt18','other1_chrc_gt18','other2_chrc_gt18',
    'chronic_all','health_status_excellent','health_status_verygood',
    'health_status_good','health_status_fair','health_status_poor',
    'care_delayed_cost','care_notget_cost','overnight_hospital',
    'overnight_hospital_times','overnight_hospital_nights',
    'care_athome_2wks','care_athome_2wks_times',
    'care_phone_2wks',
    'care_phone_2wks_times',
    'care_10more_12mo','notcov_','medicare_','medicare_partA_only',
    'medicare_partB_only','medicare_bothparts','medicare_advantage',
    'medicare_hmo','medicare_need_referral','medicare_partD',
    'single_','single_accidents','single_aids',
    'single_cancer','single_catastrophic', 'single_dental','single_disability',
    'single_hospice','single_hospitalization','single_longterm_care',
    'single_prescription','single_vision','single_other',
    'private_',#'private1_hmo',
    'private1_primary',
    'private1_thru_wrk_employer','private1_thru_wrk_union',
    #'private1_thru_wrk_other',
    'private1_thru_direct',
    'private1_thru_state','private1_thru_school',
    'private1_paid_self','private1_paid_employer',
    'private1_paid_other','private1_paid_medicare',
    'private1_paid_medicaid','private1_paid_schip',
    'private1_paid_government', #'private1_oop_20k',
    'private1_type_hmo', 'private1_type_ppo',
    'private1_type_pos', 'private1_type_ffs',
    'private1_hdhp','private1_hsa','private1_choose_md',
    'private1_network_md','private1_oon_md','private1_rx',
    'private1_dental',#'private2_hmo',
    'private2_primary',
    'private2_thru_wrk_employer','private2_thru_wrk_union',
    #'private2_thru_wrk_other',
    'private2_thru_direct',
    'private2_thru_state','private2_thru_school',
    'private2_paid_self','private2_paid_employer',
    'private2_paid_other','private2_paid_medicare',
    'private2_paid_medicaid','private2_paid_schip',
    'private2_paid_government', #'private2_oop_20k',
    'private2_type_hmo', 'private2_type_ppo',
    'private2_type_pos', 'private2_type_ffs',
    'private2_hdhp','private2_hsa','private2_choose_md',
    'private2_network_md','private2_oon_md','private2_rx',
    'private2_dental', 'private_2plus',
    'schip_', #'schip_md', 
    'othpub_', #'othpub_md',
    'othgov_',#'othgov_md',
    'milcare_','milcare_tricare',
    'milcare_va','milcare_champ-va',
    'milcare_other','milcare_tricare_prime',
    'milcare_tricare_standard_extra',
    'milcare_tricare_forlife','ihs_',
    'hilast_6mo','hilast_1yr','hilast_3yr',
    'hilast_3yrplus','histop_losejob',
    'histop_divorce','histop_age','histop_eligible',
    'histop_highcost','histop_refused','histop_medicaid_pregnancy',
    'histop_medicaid_newjob','histop_medicaid_other',
    'histop_other','histop_never','histop_moved','histop_selfemployed',
    'histop_noneed','histop_gotmarried','hino_12mo','hino_months',
    'care_spent_zero','care_spent_lt500','care_spent_lt2k',
    'care_spent_lt5k', 'care_spent_lt3k', 'care_spent_gt5k',
    'fsa_','hikind_private','hikind_medicare','hikind_medigap',
    #'hikind_medicaid',
    'hikind_schip','hikind_military','hikind_ihs',
    'hikind_state','hikind_othgov','hikind_ssp','hikind_nocov',
    'medicare_probe','medicaid_probe','ssp_probe','born_us',
    'born_mexico','born_southamerica','born_europe','born_russia',
    'born_africa','born_middle_east','born_indian','born_asia',
    'born_se_asia','yrs_us_lt1','yrs_us_lt5','yrs_us_lt10',
    'yrs_us_lt15','yrs_us_gt15','us_citizen','headstart',
    'headstart_ever','educ_yrs','educ_highschl','educ_somecol',
    'educ_colplus',#'employed',
    'looking_for_work','volunteer',
    'not_in_labor_force', 'not_work_family','not_work_school',
    'not_work_retired','not_work_vacation','not_work_leave','not_work_health',
    'not_work_off_season','not_work_layoff','not_work_disabled',
    'wrkhrs',
    'wrkhrs_lt35','wrkhrs_lt45','wrkhrs_gt20','wrk_fulltime',
    'wrk_lastyr','wrk_mo_lastyr',
    'earnings_lt5k','earnings_lt10k',
    'earnings_lt15k','earnings_lt20k','earnings_lt25k','earnings_lt34k',
    'earnings_lt45k','earnings_lt55k','earnings_lt65k','earnings_lt75k',
    'earnings_gt75k','hi_offered_atwork','family_income_answered',
    'income_wage','income_self','income_ss','disability_ss',
    'disability_benefit','income_pension','income_other_pension',
    'income_ssi','income_ssi_disability','income_tanf','income_other_gov',
    'income_interest','income_dividend','income_child_support','income_other',
    'applied_ssi','applied_ssdi',#'months_tanf','eligible_wic','wic_benefits',
    'eligible_wic_recode']


############################################
# script of params for welfare data
############################################

args_welfare = {}

args_welfare['gb']= {}
args_welfare['gb']['min_samples_leaf'] = 2
args_welfare['gb']['max_depth'] = 30
args_welfare['gb']['min_samples_split'] = 2
args_welfare['gb']['max_features'] = 10
args_welfare['gb']['learning_rate'] = 0.01
args_welfare['gb']['n_estimators'] = 1000
args_welfare['gb']['subsample'] = .7

# for rf model
args_welfare['rf'] = {}
args_welfare['rf']['min_samples_leaf'] = 4
args_welfare['rf']['max_depth'] = 10
args_welfare['rf']['min_samples_split'] = 2
args_welfare['rf']['max_features'] = 22
args_welfare['rf']['n_estimators'] = 1200

# for enet model
args_welfare['enet'] = {}
args_welfare['enet']['alpha'] = .008
args_welfare['enet']['l1_ratio'] = 0.05

# features
args_welfare['x'] = ['attblack', 'polviews', 'partyid', 'educ', 'age', '_cat_year_0', '_cat_year_1', '_cat_year_2', '_cat_year_3', '_cat_year_4', '_cat_year_5', '_cat_year_6', '_cat_year_7', '_cat_year_8', '_cat_year_9', '_cat_year_10', '_cat_year_11', '_cat_year_12', '_cat_year_13', '_cat_year_14', '_cat_year_15', 'cons']