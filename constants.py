NAN_STRING_TO_REPLACE = 'zz'
NAN_VALUE_FLOAT = 8888.0
NAN_VALUE_INT = 8888
NAN_VALUE_STRING = '8888'

BATCH_SIZE = 1000
EPOCHS = 5
N_NEURONS = 10

SEED = 8888
SPLITS = 20

SMOOTHING = 0.2
OTHER_NAN = 0

IMPUTING_STRATEGY = 'median'

PARAMS_CATBOOST = dict()
PARAMS_CATBOOST['logging_level'] = 'Silent'
PARAMS_CATBOOST['eval_metric'] = 'Logloss'
PARAMS_CATBOOST['custom_metric'] = 'Logloss'
PARAMS_CATBOOST['loss_function'] = 'Logloss'
PARAMS_CATBOOST['iterations'] = 125 # best 125
PARAMS_CATBOOST['od_type'] = 'Iter' # IncToDec, Iter
PARAMS_CATBOOST['random_seed'] = SEED
PARAMS_CATBOOST['learning_rate'] = 0.003 # alpha, default 0.03 if no l2_leaf_reg
PARAMS_CATBOOST['task_type'] = 'CPU'
PARAMS_CATBOOST['use_best_model']: True
PARAMS_CATBOOST['l2_leaf_reg'] = 3.0 # lambda, default 3, S: 300

PARAMS_CATBOOST_REGRESSOR = dict()
PARAMS_CATBOOST_REGRESSOR['logging_level'] = 'Silent'
PARAMS_CATBOOST_REGRESSOR['eval_metric'] = 'RMSE'
PARAMS_CATBOOST_REGRESSOR['custom_metric'] = 'RMSE'
PARAMS_CATBOOST_REGRESSOR['loss_function'] = 'RMSE'
PARAMS_CATBOOST_REGRESSOR['iterations'] = 5
PARAMS_CATBOOST_REGRESSOR['od_type'] = 'Iter' # IncToDec, Iter
PARAMS_CATBOOST_REGRESSOR['random_seed'] = SEED
PARAMS_CATBOOST_REGRESSOR['learning_rate'] = 0.003 # alpha, default 0.03 if no l2_leaf_reg
PARAMS_CATBOOST_REGRESSOR['task_type'] = 'CPU'
PARAMS_CATBOOST_REGRESSOR['use_best_model']: True
PARAMS_CATBOOST_REGRESSOR['l2_leaf_reg'] = 3.0 # lambda, default 3, S: 300

PARAMS_XGB = dict()
PARAMS_XGB['objective']='binary:logistic'
PARAMS_XGB['eval_metric'] = 'mae'
PARAMS_XGB['booster'] = 'gbtree'
PARAMS_XGB['eta'] = 0.02
PARAMS_XGB['subsample'] = 0.35
PARAMS_XGB['colsample_bytree'] = 0.7
PARAMS_XGB['num_parallel_tree'] = 10
PARAMS_XGB['min_child_weight'] = 40
PARAMS_XGB['gamma'] = 10
PARAMS_XGB['max_depth'] = 3


W_FEATURES = [
    'WTeamID', 
    'WFGM', 
    'WFGA', 
    'WFGM3', 
    'WFGA3', 
    'WFTM', 
    'WFTA', 
    'WOR', 
    'WDR', 
    'WAst', 
    'WTO', 
    'WStl', 
    'WBlk', 
    'WPF', 
    'WScore', 
    'Final_WTeam', 
    #'Semi_Final_WTeam', 
    'WTeam_W_count', 
    'WScore_mean',
    'WScore_median', 
    'WScore_sum',
    'WTeam_Seed',
    'WTeam_PerCent',
    'Diff_WTeam',
    'WFGA_min', 
    #'WFGA_max', 
    'WFGA_mean',
    'WFGA_median'
    #'WAst_mean',
    #'WBlk_mean'
]

L_FEATURES = [
    'LTeamID', 
    'LFGM', 
    'LFGA', 
    'LFGM3', 
    'LFGA3', 
    'LFTM', 
    'LFTA', 
    'LOR', 
    'LDR', 
    'LAst', 
    'LTO', 
    'LStl', 
    'LBlk', 
    'LPF', 
    'LScore',
    'Final_LTeam', 
    #'Semi_Final_LTeam', 
    'LTeam_L_count', 
    'LScore_mean',  
    'LScore_median', 
    'LScore_sum',
    'LTeam_Seed',
    'LTeam_PerCent',
    'Diff_LTeam',
    'LFGA_min', 
    #'LFGA_max', 
    'LFGA_mean', 
    'LFGA_median'
    #'LAst_mean',
    #'LBlk_mean'
]
