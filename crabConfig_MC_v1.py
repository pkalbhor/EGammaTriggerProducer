from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

tag = 'TnP_MC_2016_DYJets'

config.General.requestName = tag
config.General.workArea   = "TnP2016"
config.General.transferOutputs = True
config.General.transferLogs = False


config.JobType.pluginName   = 'Analysis'
config.JobType.psetName    = 'python/TnPTreeProducer_cfg.py'

config.Data.inputDataset   = '/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext1-v2/MINIAODSIM'
#'/DY1JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAOD-94X_mc2017_realistic_v10-v1/MINIAODSIM'#'/SingleElectron/Run2017D-31Mar2018-v1/MINIAOD'
config.Data.inputDBS = 'global'
config.Data.splitting       = 'FileBased'

#config.JobType.outputFiles  = ['ElectronNtuple.root']#, 'DQMIO.root']
config.Data.unitsPerJob     = 5#5000
#config.Data.totalUnits      = 1000000

config.Data.useParent       = False #!!!!
config.Data.publication = False

#config.JobType.numCores     = 1
#config.JobType.maxMemoryMB  = 2500
#config.JobType.pyCfgParams  = ['isMC=False','doEleID=True','maxEvents=-1','doTrigger=True','isAOD=False']

config.Data.outLFNDirBase = '/store/user/%s/TnP2016' % (getUsernameFromSiteDB())
config.Data.outputDatasetTag   = 'TnP2016'
config.Site.storageSite     = 'T2_IN_TIFR'


#from CRABAPI.RawCommand import crabCommand
#from CRABClient.ClientExceptions import ClientException
#from httplib import HTTPException


    # We want to put all the CRAB project directories from the tasks we submit here into one common directory.
    # That's why we need to set this parameter (here or above in the configuration file, it does not matter, we will not overwrite it).

