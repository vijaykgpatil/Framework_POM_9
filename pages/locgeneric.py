class LocGeneric:
    def locator(self,loc_type,locator_val):
        try:
            if loc_type=="name":
                ele = self.driver.find_element_by_name(locator_val)
            elif loc_type=="id":
                ele = self.driver.find_element_by_name(locator_val)
            return ele
        except:
            pass

