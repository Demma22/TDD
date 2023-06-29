def tax_calc(earnings):
    if earnings < 12000:
        tax = 0
        return tax
    if  12000 <= earnings <= 36000:
        tax = 0.2* earnings
        return tax
    if  earnings > 36000:
        tax = 0.4*earnings
        return tax
    