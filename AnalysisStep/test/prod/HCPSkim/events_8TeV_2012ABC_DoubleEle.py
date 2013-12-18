LEPTON_SETUP = 2012

IsMC = False
PD = "DoubleEle"
MCFILTER = ""
ELECORRTYPE = "2012Jul13ReReco"
APPLYELEREGRESSION = True
APPLYELECALIB = True
APPLYMUCORR = True

import os
PyFilePath = os.environ['CMSSW_BASE'] + "/src/ZZAnalysis/AnalysisStep/test/"
execfile(PyFilePath + "analyzer.py")        
execfile(PyFilePath + "prod/json_2012.py")      



process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 1000



process.source.fileNames = cms.untracked.vstring(
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_10_0/cmgTuple_260.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_10_0/cmgTuple_305.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_10_0/cmgTuple_437.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_10_0/cmgTuple_450.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_10_0/cmgTuple_61.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_10_0/cmgTuple_638.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_10_0/cmgTuple_192.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_10_0/cmgTuple_227.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_10_0/cmgTuple_243.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012A-13Jul2012-v1/AOD/V5/PAT_CMG_V5_10_0/cmgTuple_259.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012A-recover-06Aug2012-v1/AOD/V5_B/PAT_CMG_V5_10_0/cmgTuple_4.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012B-13Jul2012-v1/AOD/V5/PAT_CMG_V5_10_0/cmgTuple_1175.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012B-13Jul2012-v1/AOD/V5/PAT_CMG_V5_10_0/cmgTuple_1203.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012B-13Jul2012-v1/AOD/V5/PAT_CMG_V5_10_0/cmgTuple_128.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012B-13Jul2012-v1/AOD/V5/PAT_CMG_V5_10_0/cmgTuple_1282.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012B-13Jul2012-v1/AOD/V5/PAT_CMG_V5_10_0/cmgTuple_1313.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012B-13Jul2012-v1/AOD/V5/PAT_CMG_V5_10_0/cmgTuple_1029.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012B-13Jul2012-v1/AOD/V5/PAT_CMG_V5_10_0/cmgTuple_137.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012B-13Jul2012-v1/AOD/V5/PAT_CMG_V5_10_0/cmgTuple_1391.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012B-13Jul2012-v1/AOD/V5/PAT_CMG_V5_10_0/cmgTuple_1396.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012B-13Jul2012-v1/AOD/V5/PAT_CMG_V5_10_0/cmgTuple_1409.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012B-13Jul2012-v1/AOD/V5/PAT_CMG_V5_10_0/cmgTuple_1411.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012B-13Jul2012-v1/AOD/V5/PAT_CMG_V5_10_0/cmgTuple_144.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012B-13Jul2012-v1/AOD/V5/PAT_CMG_V5_10_0/cmgTuple_1463.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012B-13Jul2012-v1/AOD/V5/PAT_CMG_V5_10_0/cmgTuple_1481.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012B-13Jul2012-v1/AOD/V5/PAT_CMG_V5_10_0/cmgTuple_1041.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012B-13Jul2012-v1/AOD/V5/PAT_CMG_V5_10_0/cmgTuple_1497.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012B-13Jul2012-v1/AOD/V5/PAT_CMG_V5_10_0/cmgTuple_1505.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012B-13Jul2012-v1/AOD/V5/PAT_CMG_V5_10_0/cmgTuple_169.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012B-13Jul2012-v1/AOD/V5/PAT_CMG_V5_10_0/cmgTuple_171.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012B-13Jul2012-v1/AOD/V5/PAT_CMG_V5_10_0/cmgTuple_210.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012B-13Jul2012-v1/AOD/V5/PAT_CMG_V5_10_0/cmgTuple_1049.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012B-13Jul2012-v1/AOD/V5/PAT_CMG_V5_10_0/cmgTuple_1056.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012B-13Jul2012-v1/AOD/V5/PAT_CMG_V5_10_0/cmgTuple_238.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012B-13Jul2012-v1/AOD/V5/PAT_CMG_V5_10_0/cmgTuple_271.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012B-13Jul2012-v1/AOD/V5/PAT_CMG_V5_10_0/cmgTuple_286.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012B-13Jul2012-v1/AOD/V5/PAT_CMG_V5_10_0/cmgTuple_304.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012B-13Jul2012-v1/AOD/V5/PAT_CMG_V5_10_0/cmgTuple_36.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012B-13Jul2012-v1/AOD/V5/PAT_CMG_V5_10_0/cmgTuple_363.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012B-13Jul2012-v1/AOD/V5/PAT_CMG_V5_10_0/cmgTuple_398.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012B-13Jul2012-v1/AOD/V5/PAT_CMG_V5_10_0/cmgTuple_401.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012B-13Jul2012-v1/AOD/V5/PAT_CMG_V5_10_0/cmgTuple_447.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012B-13Jul2012-v1/AOD/V5/PAT_CMG_V5_10_0/cmgTuple_473.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012B-13Jul2012-v1/AOD/V5/PAT_CMG_V5_10_0/cmgTuple_51.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012B-13Jul2012-v1/AOD/V5/PAT_CMG_V5_10_0/cmgTuple_109.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012B-13Jul2012-v1/AOD/V5/PAT_CMG_V5_10_0/cmgTuple_556.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012B-13Jul2012-v1/AOD/V5/PAT_CMG_V5_10_0/cmgTuple_639.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012B-13Jul2012-v1/AOD/V5/PAT_CMG_V5_10_0/cmgTuple_643.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012B-13Jul2012-v1/AOD/V5/PAT_CMG_V5_10_0/cmgTuple_652.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012B-13Jul2012-v1/AOD/V5/PAT_CMG_V5_10_0/cmgTuple_69.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012B-13Jul2012-v1/AOD/V5/PAT_CMG_V5_10_0/cmgTuple_701.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012B-13Jul2012-v1/AOD/V5/PAT_CMG_V5_10_0/cmgTuple_1105.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012B-13Jul2012-v1/AOD/V5/PAT_CMG_V5_10_0/cmgTuple_1106.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012B-13Jul2012-v1/AOD/V5/PAT_CMG_V5_10_0/cmgTuple_703.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012B-13Jul2012-v1/AOD/V5/PAT_CMG_V5_10_0/cmgTuple_775.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012B-13Jul2012-v1/AOD/V5/PAT_CMG_V5_10_0/cmgTuple_792.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012B-13Jul2012-v1/AOD/V5/PAT_CMG_V5_10_0/cmgTuple_917.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012B-13Jul2012-v1/AOD/V5/PAT_CMG_V5_10_0/cmgTuple_951.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012B-13Jul2012-v1/AOD/V5/PAT_CMG_V5_10_0/cmgTuple_986.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012B-13Jul2012-v1/AOD/V5/PAT_CMG_V5_10_0/cmgTuple_989.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012B-13Jul2012-v1/AOD/V5/PAT_CMG_V5_10_0/cmgTuple_1152.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012C-24Aug2012-v1/AOD/V5_B/PAT_CMG_V5_10_0/cmgTuple_1.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012C-24Aug2012-v1/AOD/V5_B/PAT_CMG_V5_10_0/cmgTuple_113.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012C-24Aug2012-v1/AOD/V5_B/PAT_CMG_V5_10_0/cmgTuple_66.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012C-24Aug2012-v1/AOD/V5_B/PAT_CMG_V5_10_0/cmgTuple_73.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012C-24Aug2012-v1/AOD/V5_B/PAT_CMG_V5_10_0/cmgTuple_159.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012C-24Aug2012-v1/AOD/V5_B/PAT_CMG_V5_10_0/cmgTuple_171.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012C-24Aug2012-v1/AOD/V5_B/PAT_CMG_V5_10_0/cmgTuple_198.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012C-24Aug2012-v1/AOD/V5_B/PAT_CMG_V5_10_0/cmgTuple_34.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012C-PromptReco-v2/AOD/PAT_CMG_V5_10_0_runrange_start-203002/cmgTuple_2371.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012C-PromptReco-v2/AOD/PAT_CMG_V5_10_0_runrange_start-203002/cmgTuple_2403.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012C-PromptReco-v2/AOD/PAT_CMG_V5_10_0_runrange_start-203002/cmgTuple_2407.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012C-PromptReco-v2/AOD/PAT_CMG_V5_10_0_runrange_start-203002/cmgTuple_243.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012C-PromptReco-v2/AOD/PAT_CMG_V5_10_0_runrange_start-203002/cmgTuple_2500.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012C-PromptReco-v2/AOD/PAT_CMG_V5_10_0_runrange_start-203002/cmgTuple_252.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012C-PromptReco-v2/AOD/PAT_CMG_V5_10_0_runrange_start-203002/cmgTuple_2534.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012C-PromptReco-v2/AOD/PAT_CMG_V5_10_0_runrange_start-203002/cmgTuple_1147.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012C-PromptReco-v2/AOD/PAT_CMG_V5_10_0_runrange_start-203002/cmgTuple_2667.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012C-PromptReco-v2/AOD/PAT_CMG_V5_10_0_runrange_start-203002/cmgTuple_27.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012C-PromptReco-v2/AOD/PAT_CMG_V5_10_0_runrange_start-203002/cmgTuple_2772.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012C-PromptReco-v2/AOD/PAT_CMG_V5_10_0_runrange_start-203002/cmgTuple_279.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012C-PromptReco-v2/AOD/PAT_CMG_V5_10_0_runrange_start-203002/cmgTuple_2853.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012C-PromptReco-v2/AOD/PAT_CMG_V5_10_0_runrange_start-203002/cmgTuple_1173.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012C-PromptReco-v2/AOD/PAT_CMG_V5_10_0_runrange_start-203002/cmgTuple_1176.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012C-PromptReco-v2/AOD/PAT_CMG_V5_10_0_runrange_start-203002/cmgTuple_348.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012C-PromptReco-v2/AOD/PAT_CMG_V5_10_0_runrange_start-203002/cmgTuple_357.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012C-PromptReco-v2/AOD/PAT_CMG_V5_10_0_runrange_start-203002/cmgTuple_371.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012C-PromptReco-v2/AOD/PAT_CMG_V5_10_0_runrange_start-203002/cmgTuple_380.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012C-PromptReco-v2/AOD/PAT_CMG_V5_10_0_runrange_start-203002/cmgTuple_385.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012C-PromptReco-v2/AOD/PAT_CMG_V5_10_0_runrange_start-203002/cmgTuple_423.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012C-PromptReco-v2/AOD/PAT_CMG_V5_10_0_runrange_start-203002/cmgTuple_446.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012C-PromptReco-v2/AOD/PAT_CMG_V5_10_0_runrange_start-203002/cmgTuple_1198.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012C-PromptReco-v2/AOD/PAT_CMG_V5_10_0_runrange_start-203002/cmgTuple_451.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012C-PromptReco-v2/AOD/PAT_CMG_V5_10_0_runrange_start-203002/cmgTuple_484.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012C-PromptReco-v2/AOD/PAT_CMG_V5_10_0_runrange_start-203002/cmgTuple_496.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012C-PromptReco-v2/AOD/PAT_CMG_V5_10_0_runrange_start-203002/cmgTuple_527.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012C-PromptReco-v2/AOD/PAT_CMG_V5_10_0_runrange_start-203002/cmgTuple_536.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012C-PromptReco-v2/AOD/PAT_CMG_V5_10_0_runrange_start-203002/cmgTuple_621.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012C-PromptReco-v2/AOD/PAT_CMG_V5_10_0_runrange_start-203002/cmgTuple_648.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012C-PromptReco-v2/AOD/PAT_CMG_V5_10_0_runrange_start-203002/cmgTuple_669.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012C-PromptReco-v2/AOD/PAT_CMG_V5_10_0_runrange_start-203002/cmgTuple_1221.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012C-PromptReco-v2/AOD/PAT_CMG_V5_10_0_runrange_start-203002/cmgTuple_726.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012C-PromptReco-v2/AOD/PAT_CMG_V5_10_0_runrange_start-203002/cmgTuple_732.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012C-PromptReco-v2/AOD/PAT_CMG_V5_10_0_runrange_start-203002/cmgTuple_747.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012C-PromptReco-v2/AOD/PAT_CMG_V5_10_0_runrange_start-203002/cmgTuple_777.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012C-PromptReco-v2/AOD/PAT_CMG_V5_10_0_runrange_start-203002/cmgTuple_78.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012C-PromptReco-v2/AOD/PAT_CMG_V5_10_0_runrange_start-203002/cmgTuple_794.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012C-PromptReco-v2/AOD/PAT_CMG_V5_10_0_runrange_start-203002/cmgTuple_826.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012C-PromptReco-v2/AOD/PAT_CMG_V5_10_0_runrange_start-203002/cmgTuple_848.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012C-PromptReco-v2/AOD/PAT_CMG_V5_10_0_runrange_start-203002/cmgTuple_1231.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012C-PromptReco-v2/AOD/PAT_CMG_V5_10_0_runrange_start-203002/cmgTuple_1232.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012C-PromptReco-v2/AOD/PAT_CMG_V5_10_0_runrange_start-203002/cmgTuple_1234.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012C-PromptReco-v2/AOD/PAT_CMG_V5_10_0_runrange_start-203002/cmgTuple_1235.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012C-PromptReco-v2/AOD/PAT_CMG_V5_10_0_runrange_start-203002/cmgTuple_876.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012C-PromptReco-v2/AOD/PAT_CMG_V5_10_0_runrange_start-203002/cmgTuple_898.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012C-PromptReco-v2/AOD/PAT_CMG_V5_10_0_runrange_start-203002/cmgTuple_919.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012C-PromptReco-v2/AOD/PAT_CMG_V5_10_0_runrange_start-203002/cmgTuple_1299.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012C-PromptReco-v2/AOD/PAT_CMG_V5_10_0_runrange_start-203002/cmgTuple_1383.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012C-PromptReco-v2/AOD/PAT_CMG_V5_10_0_runrange_start-203002/cmgTuple_1031.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012C-PromptReco-v2/AOD/PAT_CMG_V5_10_0_runrange_start-203002/cmgTuple_1435.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012C-PromptReco-v2/AOD/PAT_CMG_V5_10_0_runrange_start-203002/cmgTuple_1438.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012C-PromptReco-v2/AOD/PAT_CMG_V5_10_0_runrange_start-203002/cmgTuple_1449.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012C-PromptReco-v2/AOD/PAT_CMG_V5_10_0_runrange_start-203002/cmgTuple_145.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012C-PromptReco-v2/AOD/PAT_CMG_V5_10_0_runrange_start-203002/cmgTuple_1660.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012C-PromptReco-v2/AOD/PAT_CMG_V5_10_0_runrange_start-203002/cmgTuple_1666.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012C-PromptReco-v2/AOD/PAT_CMG_V5_10_0_runrange_start-203002/cmgTuple_1054.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012C-PromptReco-v2/AOD/PAT_CMG_V5_10_0_runrange_start-203002/cmgTuple_168.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012C-PromptReco-v2/AOD/PAT_CMG_V5_10_0_runrange_start-203002/cmgTuple_1699.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012C-PromptReco-v2/AOD/PAT_CMG_V5_10_0_runrange_start-203002/cmgTuple_1756.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012C-PromptReco-v2/AOD/PAT_CMG_V5_10_0_runrange_start-203002/cmgTuple_1077.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012C-PromptReco-v2/AOD/PAT_CMG_V5_10_0_runrange_start-203002/cmgTuple_1809.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012C-PromptReco-v2/AOD/PAT_CMG_V5_10_0_runrange_start-203002/cmgTuple_1816.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012C-PromptReco-v2/AOD/PAT_CMG_V5_10_0_runrange_start-203002/cmgTuple_1859.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012C-PromptReco-v2/AOD/PAT_CMG_V5_10_0_runrange_start-203002/cmgTuple_1914.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012C-PromptReco-v2/AOD/PAT_CMG_V5_10_0_runrange_start-203002/cmgTuple_195.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012C-PromptReco-v2/AOD/PAT_CMG_V5_10_0_runrange_start-203002/cmgTuple_2023.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012C-PromptReco-v2/AOD/PAT_CMG_V5_10_0_runrange_start-203002/cmgTuple_2038.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012C-PromptReco-v2/AOD/PAT_CMG_V5_10_0_runrange_start-203002/cmgTuple_2046.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012C-PromptReco-v2/AOD/PAT_CMG_V5_10_0_runrange_start-203002/cmgTuple_2124.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012C-PromptReco-v2/AOD/PAT_CMG_V5_10_0_runrange_start-203002/cmgTuple_213.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012C-PromptReco-v2/AOD/PAT_CMG_V5_10_0_runrange_start-203002/cmgTuple_214.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012C-PromptReco-v2/AOD/PAT_CMG_V5_10_0_runrange_start-203002/cmgTuple_2142.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012C-PromptReco-v2/AOD/PAT_CMG_V5_10_0_runrange_start-203002/cmgTuple_2146.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012C-PromptReco-v2/AOD/PAT_CMG_V5_10_0_runrange_start-203002/cmgTuple_2223.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012C-PromptReco-v2/AOD/PAT_CMG_V5_10_0_runrange_start-203002/cmgTuple_2241.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012C-PromptReco-v2/AOD/PAT_CMG_V5_10_0_runrange_start-203002/cmgTuple_2244.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012C-PromptReco-v2/AOD/PAT_CMG_V5_10_0_runrange_start-203002/cmgTuple_225.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012C-PromptReco-v2/AOD/PAT_CMG_V5_10_0_runrange_start-203002/cmgTuple_2259.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012C-PromptReco-v2/AOD/PAT_CMG_V5_10_0_runrange_start-203002/cmgTuple_2270.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012C-PromptReco-v2/AOD/PAT_CMG_V5_10_0_runrange_start-203002/cmgTuple_2327.root',
    '/store/cmst3/user/cmgtools/CMG/DoubleElectron/Run2012C-EcalRecover_11Dec2012-v1/AOD/PAT_CMG_V5_10_0/cmgTuple_10.root',
                                )

process.source.eventsToProcess = cms.untracked.VEventRange( *(
    '190736:38:37061827',
    '190736:79:80889207',
    '190895:446:481791479',
    '190895:559:593623897',
    '190895:839:836690441',
    '191046:84:111444776',
    '191062:303:330091192',
    '191226:712:979037526',
    '191226:1420:1730707882',
    '191226:1520:1820521419',
    '191271:352:385661498',
    '191277:704:617265349',
    '191720:141:131384043',
    '191856:64:53791282',
    '193334:123:93268337',
    '193541:208:115301904',
    '193541:480:306664497',
    '193575:318:246768035',
    '193575:523:400912970',
    '194050:90:59331872',
    '194050:414:401484983',
    '194050:542:519488427',
    '194051:7:6362525',
    '194075:98:76117998',
    '194076:323:340846024',
    '194108:404:394007716',
    '194108:859:818802354',
    '194119:190:168130224',
    '194153:100:93572313',
    '194210:74:74688978',
    '194224:261:400957190',
    '194314:180:243501633',
    '194480:122:109881951',
    '194480:972:863682922',
    '194533:496:677674570',
    '194533:681:873825341',
    '194644:72:78891305',
    '194644:185:196674650',
    '194704:415:372667387',
    '194789:118:164079659',
    '194789:353:454236538',
    '194790:40:38426260',
    '194897:81:146471772',
    '194912:503:829690349',
    '194912:899:1347277781',
    '195099:115:137440354',
    '195113:532:622426000',
    '195115:21:18955331',
    '195147:351:399538705',
    '195147:419:502821363',
    '195147:465:567117841',
    '195147:493:607057396',
    '195165:235:306811048',
    '195251:80:147388276',
    '195304:90:128008670',
    '195304:300:393582426',
    '195304:382:487153301',
    '195304:962:1069824602',
    '195378:148:155753218',
    '195378:296:372893489',
    '195378:757:906545322',
    '195397:249:388415395',
    '195397:826:1053831791',
    '195398:66:53211301',
    '195530:137:215099909',
    '195540:68:18145014',
    '195552:139:236444816',
    '195552:553:793110394',
    '195552:1310:1487349718',
    '195552:1445:1621079578',
    '195649:223:323790844',
    '195655:140:167570931',
    '195655:432:477289466',
    '195656:85:78300349',
    '195658:71:59123305',
    '195658:364:338722570',
    '195757:148:244623214',
    '195774:78:152805866',
    '195774:90:174957822',
    '195774:312:549661559',
    '195774:387:660605607',
    '195915:251:426559109',
    '195915:690:990388348',
    '195937:240:194955393',
    '195948:56:116169718',
    '195950:240:254206496',
    '195950:667:630954116',
    '195950:680:640913928',
    '195950:781:719208626',
    '196027:79:123030498',
    '196197:238:352383455',
    '196218:150:198713417',
    '196218:166:227768389',
    '196218:296:446438292',
    '196218:539:794370838',
    '196218:590:858760563',
    '196239:393:384138657',
    '196239:766:687711552',
    '196250:281:469467267',
    '196334:177:252537006',
    '196349:105:112990898',
    '196349:169:234207734',
    '196364:606:574417012',
    '196364:696:646351604',
    '196452:1016:1315227994',
    '196453:399:363484809',
    '196453:1337:1181788896',
    '196453:1427:1259337833',
    '196531:226:305747400',
    '196531:350:497827501',
    '198063:241:167209826',
    '198212:27:15479119',
    '198212:337:221918655',
    '198269:109:177095997',
    '198271:27:36542571',
    '198271:181:232701194',
    '198271:540:631637861',
    '198272:28:26252215',
    '198272:148:141178966',
    '198272:382:345644314',
    '198272:498:440202539',
    '198487:580:664920764',
    '198487:1522:1511453808',
    '198941:106:84544694',
    '198941:217:262583111',
    '198954:115:105011803',
    '198955:493:575302642',
    '198955:1146:1211003130',
    '198969:659:797334672',
    '198969:672:809605982',
    '198969:808:964868227',
    '198969:937:1103535297',
    '199008:118:115388710',
    '199008:447:562986689',
    '199021:107:99969333',
    '199021:198:232250171',
    '199021:292:358003591',
    '199021:782:919744647',
    '199021:1083:1238510739',
    '199021:1327:1464344864',
    '199319:580:770334833',
    '199319:970:1203594102',
    '199409:143:195577806',
    '199409:303:402443918',
    '199409:878:1023292406',
    '199428:357:448557875',
    '199428:391:483168057',
    '199428:548:654887173',
    '199569:68:84956243',
    '199569:90:111437792',
    '199569:298:346269360',
    '199574:233:176859852',
    '199608:101:83178029',
    '199608:697:813802208',
    '199608:803:930210675',
    '199699:346:415865014',
    '199703:244:217542176',
    '199752:104:133641846',
    '199752:185:232018566',
    '199754:106:121019123',
    '199754:484:504370493',
    '199754:933:873005082',
    '199833:197:243627204',
    '199833:525:608612940',
    '199833:833:933684749',
    '199833:893:991082101',
    '199864:296:396825385',
    '199876:75:92622577',
    '199876:289:331257910',
    '199876:290:331969560',
    '199877:27:30975991',
    '199877:224:244791672',
    '199877:642:636036234',
    '200042:300:250036559',
    '200075:377:451096187',
    '200091:1391:1530537922',
    '200091:1481:1605749984',
    '200091:1655:1745216870',
    '200188:139:187920671',
    '200188:235:309219190',
    '200190:240:301478208',
    '200229:44:37968037',
    '200243:69:26763019',
    '200244:59:95922345',
    '200369:42:48304581',
    '200466:226:153791279',
    '200473:163:124745478',
    '200491:195:230077151',
    '200525:410:547514345',
    '200525:866:1066576272',
    '200600:692:892658058',
    '200600:1019:1248257881',
    '200991:63:98100215',
    '200991:152:226487761',
    '200991:435:573405437',
    '200991:787:970724930',
    '200992:324:279759749',
    '200992:572:468873972',
    '201097:292:385556884',
    '201174:284:185135060',
    '201174:335:216745941',
    '201196:44:38288110',
    '201196:102:88225327',
    '201196:157:134355928',
    '201196:419:340900299',
    '201202:316:290344628',
    '201278:487:670652225',
    '201278:801:1021783875',
    '201278:844:1072952721',
    '201278:989:1233293430',
    '201278:1033:1278946974',
    '201278:1517:1723198502',
    '201278:2000:2073195431',
    '201602:558:760006400',
    '201613:6:9620116',
    '201624:102:76732703',
    '201625:369:546665360',
    '201625:628:845122892',
    '201668:121:114003150',
    '201692:124:107217493',
    '201707:426:552697757',
    '201707:438:565245444',
    '201707:503:635670564',
    '201707:656:805047482',
    '201727:83:43697222',
    '201802:80:41527702',
    '201817:112:114538016',
    '201824:229:201387532',
    '201824:411:346074761',
    '202016:143:160415664',
    '202016:173:191382222',
    '202016:362:407076966',
    '202016:505:559670208',
    '202044:388:530312812',
    '202054:394:319813054',
    '202060:791:954338141',
    '202074:73:38166085',
    '202093:75:53125147',
    '202178:92:58141565',
    '202178:176:193770334',
    '202178:288:357059583',
    '202178:328:412076062',
    '202178:386:487671954',
    '202178:448:563981267',
    '202178:604:739864564',
    '202178:1286:1430970868',
    '202237:90:112735227',
    '202237:674:970333313',
    '202237:777:1087639087',
    '202237:973:1294338754',
    '202237:1073:1409704558',
    '202272:86:35886066',
    '202272:667:769186804',
    '202299:251:340486709',
    '202299:304:421267699',
    '202299:419:586836364',
    '202299:449:627007942',
    '202328:493:726409783',
    '202333:212:235647099',
    '202469:201:247836553',
    '202469:252:340674577',
    '202478:657:708573825',
    '202478:901:933835054',
    '202478:1008:1025978128',
    '202478:1022:1037471026',
    '202504:158:177815904',
    '202504:395:535251232',
    '202504:780:974397273',
    '202504:926:1134909166',
    '202504:1191:1394353502',
    '202972:105:155730849',
    '202973:713:681363400',
    '202973:839:779714361',
    '203002:469:630169854',
    '203002:1360:1582982397',
    # 2012C ECAL recovery, https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions12/8TeV/Reprocessing/Cert_201191-201191_8TeV_11Dec2012ReReco-recover_Collisions12_JSON.txt
    '201191:75-201191:98',
    '201191:100-201191:216',
    '201191:218-201191:389',
    '201191:392-201191:492',
    '201191:494-201191:506',
    '201191:509-201191:585',
    '201191:587-201191:594',
    '201191:597-201191:607',
    '201191:609-201191:794',
    '201191:796-201191:838',
    '201191:841-201191:974',
    '201191:977-201191:1105',
    '201191:1108-201191:1117',
    '201191:1120-201191:1382',
    '201191:1384-201191:1386',

))