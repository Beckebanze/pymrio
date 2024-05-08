import numpy as np

import pymrio

mrio = pymrio.load_test()

mrio.calc_all()
mrio.As


sxr = ("reg2", "transport")
idx_sxr = mrio.x.index.get_loc(sxr)
r = [0] * mrio.x.shape[0]
r[idx_sxr] = mrio.x.iloc[idx_sxr][0]

r = np.array(r)

stressor = "emission_type1"


scope1 = mrio.emissions.S.loc[stressor]
upstream = mrio.emissions.M.loc[stressor] - mrio.emissions.S.loc[stressor]
downstream = mrio.emissions.M_down.loc[stressor]

# todo: comment text
# todo: change test_mrio data, to make the values more realistic. Currently, final demand is on average 84 times larger
#  than the output to all sectors combined.
print(
    f"Upstream scope 3 is {upstream.dot(r).values/scope1.dot(r).values*100}% of scope 1 for {sxr}"
)
print(
    f"Upstream scope 3 is {downstream.dot(r).values/scope1.dot(r).values*100}% of scope 1 for {sxr}"
)

upstream = mrio.L.dot(r).sum()
