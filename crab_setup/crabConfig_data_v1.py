from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

tag = 'TnP_Data_SingleEle_17F_MVA94Xwp90iso'

config.General.requestName = tag
config.General.workArea   = "TnP2018"
config.General.transferOutputs = True
config.General.transferLogs = False


config.JobType.pluginName   = 'Analysis'
config.JobType.psetName    = '../python/TnPTreeProducer_cfg.py'

config.Data.inputDataset   = '/SingleElectron/Run2017F-31Mar2018-v1/MINIAOD'  #'/SingleElectron/Run2016D-03Feb2017-v1/MINIAOD'
config.Data.inputDBS = 'global'
config.Data.splitting       = 'LumiBased'

#config.JobType.outputFiles  = ['ElectronNtuple.root']#, 'DQMIO.root']
config.Data.unitsPerJob     = 500#5000
#config.Data.totalUnits      = 1000000

config.Data.lumiMask = 'https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions17/13TeV/ReReco/Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON.txt' 
#'https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions16/13TeV/ReReco/Final/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt'
config.Data.runRange = '305040-306460' 

config.Data.useParent       = False #!!!!

#config.JobType.numCores     = 1
#config.JobType.maxMemoryMB  = 2500
#config.JobType.pyCfgParams  = ['isMC=False','doEleID=True','maxEvents=-1','doTrigger=True','isAOD=False']

config.Data.outLFNDirBase = '/store/user/%s/TnP2018' % (getUsernameFromSiteDB())
config.Data.outputDatasetTag   = 'TnP2018'
config.Site.storageSite     = 'T2_IN_TIFR'
config.Data.publication = False

#from CRABAPI.RawCommand import crabCommand
#from CRABClient.ClientExceptions import ClientException
#from httplib import HTTPException


    # We want to put all the CRAB project directories from the tasks we submit here into one common directory.
    # That's why we need to set this parameter (here or above in the configuration file, it does not matter, we will not overwrite it).

