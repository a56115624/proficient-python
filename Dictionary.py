""" acme_customer = {'first':'wile','middle':'E','last':'Coyote'}
print(acme_customer)

acme_customer = dict(first="wile",middle="E",last = "Coyote")
print(acme_customer) """

""" lol = [('a','b'),('c','d'),('e','f')] 
print(dict(lol))
 """

""" pythons = {
     'Chapman':'Graham',
     'Cleese':'John',
     'Idle':'Terry',
     'Palin':'Michael'
 }
print(pythons)

pythons['Gilliam'] = 'Terry'
print(pythons) """

""" singals = {'green':'go','yellow':'go faster','red':'smile for the camera'}
print(singals.keys())
print(singals.values())
print(singals.items())
print(len(singals)) """

""" frist = {'a':'agony','b':'bliss'}
second = {'b':'bagels','c':'candy'}
third = {'c':'donuts'}
print({**frist,**second,**third})  """

""" pythons = {'chapman':'Gragam',
            'cleese':'john',
            'Gilliam':'Terry',
            'Idle':'Eric',
            'Jones':'Terry',
            'palin':'Michael'}
others = {'Marx':'Groucho','Howard':'Moe'}
pythons.update(others)
print(pythons) """

""" frist = {'a':'1','b':'2'}
second = {'b':'platypus'}
frist.update(second)
print(frist) """

""" pythons = {'chapman':'Gragam',
            'cleese':'john',
            'Gilliam':'Terry',
            'Idle':'Eric',
            'Jones':'Terry',
            'palin':'Michael'}
del pythons['palin']
print(pythons) """

""" pythons = {'chapman':'Gragam',
            'cleese':'john',
            'Gilliam':'Terry',
            'Idle':'Eric',
            'Jones':'Terry',
            'palin':'Michael'}
print(len(pythons))
pythons.pop('palin')
print(len(pythons))
pythons.clear()
print(pythons) """

""" pythons = {'Chapmn':'Graham','Cleese':'john','Jones':'Terry','Palin':'Michael','Idle':'Eric'}
print('Chapman' in pythons) """

""" singals = {'green':'go','yellow':'go faster','red':'smile for the camera'}
save_signals = singals
singals['blue'] = 'confuse everyone'
print(save_signals)
 """
""" signals = {'green':'go','yellow':'go faster','red':'smile for the camera'}
original_signals = signals.copy
signals['blue'] = 'confuse everyone'
print(signals)
print(original_signals) """

signals = {'green':'go','yellow':'go faster','red':['stop','smile']}
signals_copy = signals.copy()
print(signals)
print(signals_copy)
signals['red'][1] = 'sweat'
print(signals)