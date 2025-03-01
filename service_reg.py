


class ServiceRegistry:
    def __init__(self):
        self.services = {}
    def register(self, service_name, service_instance):
        if service_name not in self.services:
            self.services[service_name] = []
        self.services[service_name].append(service_instance)
    def get_service(self, service_name):
        if service_name in self.services:
            return self.services[service_name]

