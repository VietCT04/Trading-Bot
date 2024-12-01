from services import *
class ServiceManager:
    def __init__(self, apikey, secretkey):
        self._apikey = apikey
        self._secretkey = secretkey
        self.services = {
            1: AccountDetailsService(),
            2: FundsTransferService(),
            3: DepositService(),
            4: WithdrawalService(),
            5: TransactionHistoryService()
        }

    def choose_service(self, service_number):
        service = self.services.get(service_number)
        if service:
            service.perform()
        else:
            print("Invalid service choice.")