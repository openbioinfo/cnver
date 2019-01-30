import sys
sys.path.insert(0,"../")

from ctCNV.baseline_normalize.baseline_normalize import baseline_normalize

baseline = "data/result/baseline.txt"
self_normalized_region_depth = "data/result/YH2017Lcf07050384.self_normalized_region_depth.txt"
outdir = "data/result"
def test_baseline_normalize():

    baseline_normalize(baseline,self_normalized_region_depth,outdir)

if __name__ == "__main__":
    test_baseline_normalize()
