import pandas as pd
import numpy as np

file = '../Files/A204 UV LambdaMax.csv'
csread = pd.read_csv(file, header=0)
print(csread.iloc[0])

lambdas = np.array(csread.iloc[:,-1])
print(lambdas)
spectra = [np.array(csread.iloc[:,i]) for i in range(0,12)]
print(len(spectra))

lmax = -1

# spectrum = spectra[0]
LMXes = []
for spectrum in spectra:
    absmax = np.max(spectrum)
    if absmax > spectrum[0]:
        print(absmax)
        print(lambdas[spectrum == absmax], np.mean(lambdas[spectrum == absmax]), np.median(lambdas[spectrum == absmax]))
    else:
        min_reach = False
        for i in range(len(spectrum)-1):
            if spectrum[i+1] > spectrum[i]:
                min_reach = True
                #print(lambdas[i])

            if min_reach:
                if spectrum[i+1] < spectrum[i]:
                    absmax = spectrum[i]
                    break

    lmaxes = lambdas[spectrum == absmax]
    print(absmax,np.median(lmaxes),lmaxes)
    print('\nLMAX: {}\n'.format(np.median(lmaxes)))
    LMXes.append(np.median(lmaxes))
print(LMXes)