header=['No.', '2-theta', 'd', 'FWHM', 'Rel. int.', 'I']
units = ['',   '(deg)', '(ang.)', '(deg)', '(a.u.)','']
sample_data='''
481 22.188(14) 4.003(2) 0.389(12) 11.66
482 31.558(4) 2.8327(4) 0.347(4) 100.00
483 38.899(10) 2.3134(6) 0.340(8) 28.14
484 43.51(10) 2.079(5) 2.3(3) 4.88
485 45.207(11) 2.0042(4) 0.440(10) 43.18
486 50.929(13) 1.7916(4) 0.37(3) 14.74
487 54.35(6) 1.6866(17) 1.10(14) 4.58
488 56.181(9) 1.6359(2) 0.409(10) 48.34
489 65.902(9) 1.41620(17) 0.428(11) 25.69
490 70.43(3) 1.3358(6) 0.52(2) 4.54
491 74.23(9) 1.2765(13) 0.45(18) 1.06
492 74.861(12) 1.26735(17) 0.61(2) 14.51
493 78.48(3) 1.2177(4) 0.20(6) 0.31
494 79.19(3) 1.2085(3) 0.585(18) 6.68
495 82.94(11) 1.1632(13) 0.44(10) 0.86
496 83.50(3) 1.1568(3) 0.53(2) 6.88
497 87.69(2) 1.1120(2) 1.59(12) 13.74
'''

importantdata=[] #2-theta, d, rel.int
print(sample_data.splitlines())
for line in sample_data.splitlines():
    indices = line.split()
    if len(indices) > 3:
        importantdata.append([indices[1][:-3].split('(')[0], indices[2].split('(')[0], indices[4]])

print('2-theta')
[print(data[0]) for data in importantdata]

print('d / ang.')
[print(data[1]) for data in importantdata]

print('rel. int')
[print(data[2]) for data in importantdata]