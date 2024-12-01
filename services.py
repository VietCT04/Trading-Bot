from abc import ABC, abstractmethod

class Service(ABC):    
    @abstractmethod
    def perform(self):
        pass

class AccountDetailsService(Service):
    def perform(self):
        print("You selected Service 1: Check Account Details.")

class FundsTransferService(Service):
    def perform(self):
        print("You selected Service 2: Transfer Funds.")

class DepositService(Service):
    def perform(self):
        print("You selected Service 3: Deposit Money.")

class WithdrawalService(Service):
    def perform(self):
        print("You selected Service 4: Withdraw Money.")

class TransactionHistoryService(Service):
    def perform(self):
        print("You selected Service 5: View Transaction History.")