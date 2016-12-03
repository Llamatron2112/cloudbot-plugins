from cloudbot import hook
import re

@hook.command()
def awg(text, notice, reply):
    """ Converts an American Wire Gauge value into Millimetres. Give a gauge value between 0000 and 40, eg. .awg 28"""
    
    contable = [ ('0000', 11.7),
                 ('4/0', 11.7),
                 ('000', 10.4),
                 ('3/0', 10.4),
                 ('00', 9.27),
                 ('2/0', 9.27),
                 ('0', 8.25),
                 ('1/0', 8.25),
                 ('1', 7.35),
                 ('2', 6.54),
                 ('3', 5.83),
                 ('4', 5.19),
                 ('5', 4.62),
                 ('6', 4.12),
                 ('7', 3.66),
                 ('8', 3.26),
                 ('9', 2.91),
                 ('10', 2.59),
                 ('11', 2.30),
                 ('12', 2.05),
                 ('13', 1.83),
                 ('14', 1.63),
                 ('15', 1.45),
                 ('16', 1.29),
                 ('17', 1.15),
                 ('18', 1.02),
                 ('19', 0.912),
                 ('20', 0.812),
                 ('21', 0.723),
                 ('22', 0.644),
                 ('23', 0.573),
                 ('24', 0.511),
                 ('25', 0.455),
                 ('26', 0.405),
                 ('27', 0.361),
                 ('28', 0.321),
                 ('29', 0.286),
                 ('30', 0.255),
                 ('31', 0.227),
                 ('32', 0.202),
                 ('33', 0.180),
                 ('34', 0.160),
                 ('35', 0.143),
                 ('36', 0.127),
                 ('37', 0.113),
                 ('38', 0.101),
                 ('39', 0.0897),
                 ('40', 0.0799) ]

    rawreq = text.lower()
    request = re.match('^(\d*\.?\d+) ?(mm|g|gauge|awg)?$',  rawreq)
    if request :
        if request.group(2) == 'mm' :

            inputmm = float(request.group(1))
            prevawg = '0000'
            prevmm = 11.7
            
            for awg, mm in contable :
                if inputmm == mm :
                    return reply(str(inputmm) + 'mm is ' + awg + 'g')
                if ( prevmm > inputmm ) and ( inputmm > mm ) : 
                    return reply(str(inputmm) + 'mm is between ' + prevawg + 'g (' + str(prevmm) + 'mm) and ' + awg + 'g (' + str(mm) + 'mm)')
                prevmm = mm
                prevawg = awg
                
        if request.group(2) == ('g' or 'awg' or 'gauge') :
            inputg = request.group(1)
            for awg, mm in contable :
                if awg == inputg : return reply(inputg + 'awg is equal to ' + str(mm) + 'mm')
            return reply('No corresponding awg value found')
            
    else : notice('Wrong input ! Usage example: .awg 28g, or .awg 0.23mm')