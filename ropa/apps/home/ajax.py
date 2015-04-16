from dajax.core import dajax
from dajaxice.decorators import dajaxice_register

@dajaxice_register
def updatecombo(request, option):
    dajax=Dajax()
    options=[['Madri','Barcelona','Victoria','Burgos'],
    ['Paris','Evreux','Le Havre','Reims'],
    ['London','Birmingham','Bristol','Cardiff']]
out=[]
for option in options[int(option)]:
    out.append("<option value='#'>%s</option>" % option)

    dajax.assing('#combo2', 'innerHTML', ''.join(out))
    return dajax.json()





    @dajaxice_register
def updatecombo(request, option):
    dajax=Dajax()
    options=[['Madri','Barcelona','Victoria','Burgos'],
    ['Paris','Evreux','Le Havre','Reims'],
    ['London','Birmingham','Bristol','Cardiff']]
out=[]
for option in options[int(option)]:
    out.append("<option value='#'>%s</option>" % option)

    dajax.assing('#combo3', 'innerHTML', ''.join(out))
    return dajax.json()