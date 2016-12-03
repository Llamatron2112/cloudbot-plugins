import re
import math
from cloudbot import hook

@hook.command("ohm","o")
def ohm(text, notice):
    """Ohm's law calculator, takes two values and calculates the two others."""
    
    rawreq = text.replace(u'Ω', 'o').lower()
 
    request = re.match('^ *([0-9]*\.?[0-9]+) *([avwo]) +([0-9]*\.?[0-9]+) *([avwo]) *$', rawreq, re.I)
    
    if not request:
        return notice("Error: Syntax error. Usage example: .ohm 4.2v 1.8o")

    if request.group(2) == request.group(4):
        return notice("Error: same unit used twice")
    
    units = [ request.group(2), request.group(4) ]
    value = 1
    for unit in units :
        if unit == 'a' : a = float(request.group(value))
        elif unit == 'v' : v = float(request.group(value))
        elif unit == 'w' : w = float(request.group(value))
        elif unit == 'o' : o = float(request.group(value))
        else : return notice("Error: Unit error")
        value = 3

    known = '%s%s' % (request.group(2), request.group(4))
    
    if known == 'ao' or known == 'oa' :
        v = o * a
        w = pow(a, 2) * o
        a = numtostr(a)
        o = numtostr(o)
        v = numtostr(v)
        w = numtostr(w)
        return "%sA & %sΩ ==> %sV & %sW" % (a, o, v, w)
        
    if known == 'av' or known == 'va' :
        w = v * a
        o = v / a
        a = numtostr(a)
        o = numtostr(o)
        v = numtostr(v)
        w = numtostr(w)
        return "%sA & %sV ==> %sW & %sΩ" % (a, v, w, o)
        
    if known == 'aw' or known == 'wa' :
        v = w / a
        o = w / pow(a, 2)
        a = numtostr(a)
        o = numtostr(o)
        v = numtostr(v)
        w = numtostr(w)
        return "%sA & %sW ==> %sV %sΩ" % (a, w, v, o)
        
    if known == 'vo' or known == 'ov' :
        a = v / o
        w = pow(v, 2) / o
        a = numtostr(a)
        o = numtostr(o)
        v = numtostr(v)
        w = numtostr(w)
        return "%sV & %sΩ ==> %sW & %sA" % (v, o, w, a)
        
    if known == 'vw' or known == 'wv' :
        a = w / v
        o = pow(v, 2) / w
        a = numtostr(a)
        o = numtostr(o)
        v = numtostr(v)
        w = numtostr(w)
        return "%sV & %sW ==> %sΩ & %sA" % (v, w, o, a)
        
    if known == 'wo' or known == 'ow' :
        a = math.sqrt(w / o)
        v = math.sqrt(w * o)
        a = numtostr(a)
        o = numtostr(o)
        v = numtostr(v)
        w = numtostr(w)
        return "%sW & %sΩ ==> %sA & %sV" % (w, o, a, v)
        
def numtostr( n ):
    n = round(n, 2)
    if n.is_integer() : n = int(n)
    n = str(n)
    return n