import FWCore.ParameterSet.Config as cms

#source = cms.Source("EmptySource")

from Configuration.Generator.PythiaUEZ2Settings_cfi import *

generator = cms.EDFilter(
    "Pythia6GeneratorFilter",
    comEnergy = cms.double(7000.0),
    crossSection = cms.untracked.double(71260000000.),
    filterEfficiency = cms.untracked.double(4e-05),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    maxEventsToPrint = cms.untracked.int32(0),
    pythiaPylistVerbosity = cms.untracked.int32(0),
    ExternalDecays = cms.PSet(
        EvtGen = cms.untracked.PSet(
             operates_on_particles = cms.vint32( 0 ), # 0 (zero) means default list (hardcoded)
                                                      # you can put here the list of particles (PDG IDs)
                                                      # that you want decayed by EvtGen
             use_default_decay = cms.untracked.bool(False),
             decay_table = cms.FileInPath('GeneratorInterface/ExternalDecays/data/DECAY_NOLONGLIFE.DEC'),
             particle_property_file = cms.FileInPath('GeneratorInterface/ExternalDecays/data/evt.pdl'),
             user_decay_file = cms.FileInPath('GeneratorInterface/ExternalDecays/data/Bs_mumu.dec'),
             list_forced_decays = cms.vstring('MyB_s0',
                                              'Myanti-B_s0'),
        ),
        parameterSets = cms.vstring('EvtGen')
    ),

    
    PythiaParameters = cms.PSet(
    pythiaUESettingsBlock,
         bbbarSettings = cms.vstring('MSEL = 1'), 
        # This is a vector of ParameterSet names to be read, in this order
        parameterSets = cms.vstring(
             'pythiaUESettings',
             'bbbarSettings')
       
    )
    )
MuFromBs = cms.EDFilter("PythiaFilter",
    MaxEta = cms.untracked.double(2.5),
    Status = cms.untracked.int32(1),
    MinEta = cms.untracked.double(-2.5),
    MotherID = cms.untracked.int32(531),
    ParticleID = cms.untracked.int32(13)
)
mumugenfilter = cms.EDFilter("MCParticlePairFilter",
    MaxEta = cms.untracked.vdouble(2.5, 2.5),
    Status = cms.untracked.vint32(1, 1),
    MinEta = cms.untracked.vdouble(-2.5, -2.5),
    ParticleID1 = cms.untracked.vint32(-13, 13),
    ParticleID2 = cms.untracked.vint32(-13, 13)
)


configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.1 $'),
    name = cms.untracked.string
    ('$Source: /local/projects/CMSSW/rep/CMSSW/Configuration/GenProduction/python/PYTHIA6_Bs2MuMu_TuneZ2_7TeV_cff.py,v $'),
    annotation = cms.untracked.string('Bs -> mu mu at 7TeV')
    )

ProductionFilterSequence = cms.Sequence(generator*MuFromBs*mumugenfilter)
