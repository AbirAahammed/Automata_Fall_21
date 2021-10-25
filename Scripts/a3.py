
reg = '1+0+$+(1+0+$)(1+0)*(1+0+$)'
print(reg[:reg.find('+')], '|',reg[reg.find('+')+1:])

res = []
while reg.find('+') < reg.find('('):
    res += reg[:reg.find('+')]
    reg = reg[reg.find('+')+1:]