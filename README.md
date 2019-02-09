# EgammaAnalysis-TnPTreeProducer
TnP package for EGM

For regular users
1. install

```bash
cmsrel CMSSW_10_2_5
cd CMSSW_10_2_5/src
cmsenv

git cms-merge-topic guitargeek:PhotonMVA_10_2_X
git cms-merge-topic swagata87:PhoIDv2cutbased

git cms-addpkg PhysicsTools/TagAndProbe
git cms-init
scram b -j8

cd $CMSSW_BASE/src

git clone -b Nm1 https://github.com/pkalbhor/EGammaTriggerProducer EgammaAnalysis/TnPTreeProducer
    
```


For developpers
1. On github fork the package https://github.com/cms-analysis/EgammaAnalysis-TnPTreeProducer 
2. Add the remote 

git remote add username-push git@github.com:username/EgammaAnalysis-TnPTreeProducer.git

3. push commits to fork and then standard pull request process
git push username-push branchname

4. submit jobs
