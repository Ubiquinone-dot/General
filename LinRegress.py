from scipy import stats
# import numpy as np

y = [
    0.0274,
    0.0283,
    0.0303,
    0.0308,
    0.0316,
    0.0336,
    0.0338,
    0.0345,
    0.0356,
    0.0361,
    0.0367,
    0.0376,
    0.0393,
    0.0409,
    0.0403,
    0.0409,
    0.0421,
    0.0425,
    0.0434,
    0.0444,
    0.0455,
    0.0461,
    0.047,
    0.0478,
    0.0488,
    0.0499,
    0.0506,
    0.0513,
    0.0524
]
x = [
    40,
    60,
    80,
    100,
    120,
    140,
    160,
    180,
    200,
    220,
    240,
    260,
    280,
    300,
    320,
    340,
    360,
    380,
    400,
    420,
    440,
    460,
    480,
    500,
    520,
    540,
    560,
    580,
    600

]

assert(len(x) == len(y))
data = Fslope, Fintercept, Fr_value, Fp_value, Fstd_err = stats.linregress(x,y)
Data_computed = []  # tuples as (sum of r^2 values, # points on first line)


print('\n\nline:  y = '+str(Fslope)+'x '+ str(Fintercept))
print(data)
print('±')
print(f'n: {len(x)}')