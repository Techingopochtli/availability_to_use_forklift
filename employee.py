
class Employee:

    def __init__(self, id_emp):    # initialize Employee with id, name  and last names
        self.sbp = 120
        self.dbp = 80
        self.pulse = 70
        self.sp02 = 98
        self.id = id_emp
        self.glasses = False
        self.alcohol = False
        self.meals = 8
        self.equilibrium_t = True
        self.equilibrium_4r = True
        self.equilibrium_4l = True
        self.is_apt = True
        self.is_extern = 0

    def set_sbp(self, bp):  # set systolic blood pressure
        self.sbp = bp

    def set_dbp(self, bp):  # set diastolic blood pressure
        self.sbp = bp

    def set_pulse(self, pulse):  # set pulse
        self.pulse = pulse

    def set_sp02(self, sp):   # set percentage of oxygen in blood
        self.sp02 = sp

    def set_equilibrium_t(self, t):
        self.equilibrium_t = t

    def set_equilibrium_4r(self, r):
        self.equilibrium_4r = r

    def set_equilibrium_4l(self, l):
        self.equilibrium_4l = l

    def set_is_apt(self, apt):
        self.is_apt = apt

    def set_meals(self, meal):
        self.meals = meal

    def set_glasses(self, glass):
        self.glasses = glass

    def set_alcohol(self, alcohol):
        self.alcohol = alcohol

    def set_is_extern(self, extern):
        self.is_extern = extern

