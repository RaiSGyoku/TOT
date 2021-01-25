#will handle the function for computing the deductions

def SalaryDeduction(val1,val2,totalGross):
    tax = 0.12
    taxed = int(totalGross) * tax
    return (int(val1)+int(val2)+taxed)