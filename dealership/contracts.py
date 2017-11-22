from vehicles import *
from customers import *
class Contract(object):
    pass


class BuyContract(Contract):
    def __init__(self, vehicle, customer, monthly_payments):
        self.vehicle = vehicle
        self.customer = customer
        self.payment = monthly_payments
        print(self.vehicle)
    def total_value(self):
    	if isinstance(self.vehicle, Car):
    		i = 1.07
    	if isinstance(self.vehicle, Motorcycle):
    		i = 1.03
    	if isinstance(self.vehicle, Truck):
    		i = 1.11
    	if isinstance(self.customer, Employee):
    		d = 0.9
    	if isinstance(self.customer, Customer):
    		d = 1

    	return self.vehicle.sale_price() + (i * self.payment * self.vehicle.sale_price() / 100) * d
    	
    def monthly_value(self):
        return self.total_value() / self.payment
        
class LeaseContract(Contract):
    def __init__(self, vehicle, customer, length_in_months):
        pass

