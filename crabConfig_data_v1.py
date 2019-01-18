from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

tag = 'TnP_Data2017D_HLT_Ele27'

config.General.requestName = tag
config.General.workArea   = "TnPLatest"
config.General.transferOutputs = True
config.General.transferLogs = False


config.JobType.pluginName   = 'Analysis'
config.JobType.psetName    = 'python/TnPTreeProducer_cfg.py'

config.Data.inputDataset   = '/SingleElectron/Run2017D-31Mar2018-v1/MINIAOD'
config.Data.inputDBS = 'global'
config.Data.splitting       = 'LumiBased'

#config.JobType.outputFiles  = ['ElectronNtuple.root']#, 'DQMIO.root']
config.Data.unitsPerJob     = 100#5000
#config.Data.totalUnits      = 1000000

config.Data.useParent       = False #!!!!

#config.JobType.numCores     = 1
#config.JobType.maxMemoryMB  = 2500
#config.JobType.pyCfgParams  = ['isMC=False','doEleID=True','maxEvents=-1','doTrigger=True','isAOD=False']

config.Data.outLFNDirBase = '/store/user/%s/TnPLatest' % (getUsernameFromSiteDB())
config.Data.outputDatasetTag   = 'TnPLatest'
config.Site.storageSite     = 'T2_IN_TIFR'


from CRABAPI.RawCommand import crabCommand
from CRABClient.ClientExceptions import ClientException
from httplib import HTTPException


    # We want to put all the CRAB project directories from the tasks we submit here into one common directory.
    # That's why we need to set this parameter (here or above in the configuration file, it does not matter, we will not overwrite it).
#config.Data.outLFNDirBase = '/store/user/pkalbhor/' + tag

