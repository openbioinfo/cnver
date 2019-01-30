import sys
sys.path.insert(0,"../")

from ctCNV.plot.plot import plot

baseline_normalized_region_depth = "data/result/YH2017Lcf07050384.finally_normalized_depth.txt"
outdir = "data/result/"

def test_plot():

    plot(baseline_normalized_region_depth,outdir)

if __name__ == "__main__":
    test_plot()
