from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

tag = 'TnP_Data2017D_HLT_Ele27_MVA94Xwp90_v2'

config.General.requestName = tag
config.General.workArea   = "TnP2017"
config.General.transferOutputs = True
config.General.transferLogs = False


config.JobType.pluginName   = 'Analysis'
config.JobType.psetName    = 'python/TnPTreeProducer_cfg.py'

config.Data.inputDataset   = '/SingleElectron/Run2017D-31Mar2018-v1/MINIAOD'
config.Data.inputDBS = 'global'
config.Data.splitting       = 'LumiBased'

#config.JobType.outputFiles  = ['ElectronNtuple.root']#, 'DQMIO.root']
config.Data.unitsPerJob     = 350#5000
#config.Data.totalUnits      = 1000000


config.Data.lumiMask = 'https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions17/13TeV/ReReco/Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON.txt'
config.Data.runRange = '302030-302663'

config.Data.useParent       = False #!!!!

#config.JobType.numCores     = 1
#config.JobType.maxMemoryMB  = 2500
#config.JobType.pyCfgParams  = ['isMC=False','doEleID=True','maxEvents=-1','doTrigger=True','isAOD=False']

config.Data.outLFNDirBase = '/store/user/%s/TnP2017' % (getUsernameFromSiteDB())
config.Data.outputDatasetTag   = 'TnP2017'
config.Site.storageSite     = 'T2_IN_TIFR'
config.Data.publication = False



