"""
Departamentos:
Finanzas:           'fz'
Recursos humanas:   'rh'
Administrativo:     'ad'
Oficios varios:     'of'
"""


class Departamento:
    def __init__(self):
        self.cod = None
        self.nombre = None
        self.apellido = None
        self.dept = None

    def get_values(self):
        val = '(\'' + str(self.cod) + '\', \'' + self.nombre + '\', \'' + self.apellido + '\', \'' + self.dept + '\'' + ')'
        return val


class E_finanzas(Departamento):
    def __init__(self, cd, nm, ap, dp):
        self.cod = cd
        self.nombre = nm
        self.apellido = ap
        self.dept = dp


class E_recursos(Departamento):
    def __init__(self, cd, nm, ap, dp):
        self.cod = cd
        self.nombre = nm
        self.apellido = ap
        self.dept = dp


class E_admon(Departamento):
    def __init__(self, cd, nm, ap, dp):
        self.cod = cd
        self.nombre = nm
        self.apellido = ap
        self.dept = dp


class E_otros(Departamento):
    def __init__(self, cd, nm, ap, dp):
        self.cod = cd
        self.nombre = nm
        self.apellido = ap
        self.dept = dp


class Factory:
    def get_emp(self, idd, nm, ap, dpt):
        if dpt == 'fz':
            return E_finanzas(idd, nm, ap, dpt)
        elif dpt == 'rh':
            return E_recursos(idd, nm, ap, dpt)
        elif dpt == 'ad':
            return E_admon(idd, nm, ap, dpt)
        elif dpt == 'ov':
            return E_otros(idd, nm, ap, dpt)
