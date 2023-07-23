""" This module is for calculating the yearly installment """


#loan = input('Por favor introduce el valor de tu prestamo: ')
#loan = float(loan)

#interest = input('Por favor introduce el interés anual: ')
#interest = float(interest)

#periodos = input('Por favor introduce el número de periodos: ')
#periodos = int(periodos)


def is_numeric(value):
    """ Returns if value is a number"""
    try:
        float(value)
        return True
    except ValueError:
        return False
