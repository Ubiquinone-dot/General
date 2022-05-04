
paste = True


strng = '''



'''
import pyperclip
if paste:
    strng = pyperclip.paste()

inp = '' # str(input('Give string: '))
if len(inp)>0:
    strng = inp

code_dict = {
    #H2XY
    'EUH066':'Repeated exposure may cause skin dryness or cracking.',
    'EUH019':'May form explosive peroxides.',
    'EUH014':'Reacts violently with water',
    'H200':'Unstable explosive',
    'H201':'Explosive; mass explosive hazard',
    'H202':'Explosive; severe projection hazard',
    'H203':'Explosive; fire, blast or projection hazard',
    'H204':'Fire or projection hazard',
    'H205':'May mass explode in fire',
    'H220':'Extremely flammable gas',
    'H221':'Flammable gas',
    'H222':'Extremely flammable aerosol',
    'H223':'Flammable aerosol',
    'H224':'Extremely flammable liquid and vapour',
    'H225':'Highly flammable liquid and vapour',
    'H226':'Flammable liquid and vapour',
    'H227':'Combustible liquid',
    'H228':'Flammable solid',
    'H240':'Heating may cause an explosion',
    'H241':'Heating may cause a fire or explosion',
    'H242':'Heating may cause a fire',
    'H250':'Catches fire spontaneously if exposed to air',
    'H251':'Self-heating;; may catch fire',
    'H252':'Self-heating; in large quantities; may catch fire',
    'H260':'In contact with water releases flammable gases which may ignite spontaneously',
    'H261':'In contact with water releases flammable gas',
    'H270':'May cause or intensify fire; oxidizer',
    'H271':'May cause fire or explosion; strong oxidizer',
    'H272':'May intensify fire; oxidizer',
    'H280':'Contains gas under pressure; may explode if heated	Gases under pressure',
    'H281':'Contains refrigerated gas; may cause cryogenic burns or injury',
    'H290':'May be corrosive to metals',
    #H3XY
    'H300':'Fatal if swallowed',
    'H301':'Toxic if swallowed',
    'H302':'Harmful if swallowed',
    'H303':'May be harmful if swallowed',
    'H304':'May be fatal if swallowed and enters airways',
    'H305':'May be harmful if swallowed and enters airways',
    'H310':'Fatal in contact with skin',
    'H311':'Toxic in contact with skin',
    'H312':'Harmful in contact with skin',
    'H313':'May be harmful in contact with skin',
    'H314':'Causes severe skin burns and eye damage',
    'H315':'Causes skin irritation',
    'H316':'Causes mild skin irritation',
    'H317':'May cause an allergic',
    'H318':'Causes serious eye damage',
    'H319':'Causes serious eye irritation',
    'H320':'Causes eye irritation',
    'H330':'Fatal if inhaled',
    'H331':'Toxic if inhaled',
    'H332':'Harmful if inhaled',
    'H333':'May be harmful if inhaled',
    'H334':'May cause allergy or asthma symptoms or breathing difficulties if inhaled',
    'H335':'May cause respiratory irritation',
    'H336':'May cause drowsiness or dizziness',
    'H340':'May cause genetic defects',
    'H341':'Suspected of causing genetic defects',
    'H350':'May cause cancer',
    'H351':'Suspected of causing cancer',
    'H360':'May damage fertility or the unborn child',
    'H361':'Suspected of damaging fertility or the unborn child',
    'H362':'May cause harm to breast-fed children',
    'H370':'Causes damage to organs',
    'H371':'May cause damage to organs',
    'H372':'Causes damage to organs',
    'H373':'May cause damage to organs',
    #H4XY
    'H400': 'Very toxic to aquatic life',
    'H401': 'Toxic to aquatic life',
    'H402': 'Harmful to aquatic life',
    'H410': 'Very toxic to aquatic life with long lasting effects',
    'H411': 'Toxic to aquatic life with long lasting effects',
    'H412': 'Harmful to aquatic life with long lasting effects',
    'H413': 'May cause long lasting harmful effects to aquatic life.'
}

codes = []

hazard_statement = ''
for line in strng.splitlines():
    line = line.strip()
    for code in code_dict.keys():
        f = line.startswith(str(code))
        if f:
            codes.append(code)
            hazard_statement += code + ': {}\n'.format(code_dict[code])

print(hazard_statement)

print('codes:', codes)


# To copy directly to clipboard:
import pyperclip
pyperclip.copy(hazard_statement)
spam = pyperclip.paste()
