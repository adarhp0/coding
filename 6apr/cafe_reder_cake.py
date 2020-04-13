import unittest

def is_first_come_first_served(take_out_orders, dine_in_orders, served_orders):

    # Check if we're serving orders first-come, first-served
    my_list=take_out_orders
    alices_list=dine_in_orders
    new_list=[]
    n1=len(my_list)
    n2=len(alices_list)
    n3=len(served_orders)
    i=0
    j=0
    k=0
    fl=0
    if n1+n2!=n3:
        return False
    while i<n1 and j<n2 and k<n3:
        if my_list[i]<alices_list[j]:
            if my_list[i]==served_orders[k]:
                i=i+1
                k=k+1
                fl=0
            else:
                return False
        else:
            if alices_list[j]==served_orders[k]:
                j=j+1
                k=k+1
                fl=0
            else:
                return False
    while i<n1 and k<n3:
        if my_list[i]==served_orders[k]:
            i=i+1
            k=k+1
            fl=0
        else:
            return False
    while j<n2 and k<n3:
        if alices_list[j]==served_orders[k]:
            j=j+1
            k=k+1
            fl=0
        else:
            return False
    return True


















# Tests

class Test(unittest.TestCase):

    def test_both_registers_have_same_number_of_orders(self):
        result = is_first_come_first_served([1, 4, 5], [2, 3, 6], [1, 2, 3, 4, 5, 6])
        self.assertTrue(result)

    def test_registers_have_different_lengths(self):
        result = is_first_come_first_served([1, 5], [2, 3, 6], [1, 2, 6, 3, 5])
        self.assertFalse(result)

    def test_one_register_is_empty(self):
        result = is_first_come_first_served([], [2, 3, 6], [2, 3, 6])
        self.assertTrue(result)

    def test_served_orders_is_missing_orders(self):
        result = is_first_come_first_served([1, 5], [2, 3, 6], [1, 6, 3, 5])
        self.assertFalse(result)

    def test_served_orders_has_extra_orders(self):
        result = is_first_come_first_served([1, 5], [2, 3, 6], [1, 2, 3, 5, 6, 8])
        self.assertFalse(result)

    def test_one_register_has_extra_orders(self):
        result = is_first_come_first_served([1, 9], [7, 8], [1, 7, 8])
        self.assertFalse(result)

    def test_one_register_has_unserved_orders(self):
        result = is_first_come_first_served([55, 9], [7, 8], [1, 7, 8, 9])
        self.assertFalse(result)


unittest.main(verbosity=2)