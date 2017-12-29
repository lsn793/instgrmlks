class more_than_two(object):
    def __init__(self, *locator):
        self.locator = locator
    def __call__(self, driver):
        elements = driver.find_elements((*self.locator))
        if len(elements) > 2:
            return elements
        return False