import unittest
from banking import Banking

class Test_Banking(unittest.TestCase):
    def test_deposit(self):
        bankAccount = Banking(200)
        self.assertEqual(bankAccount.deposit(300), 500)

    def test_withdraw(self):
        bankAccount = Banking(300)
        self.assertEqual(bankAccount.withdraw(200), 100)
        self.assertEqual(bankAccount.withdraw(500), 0)  # Assuming you can't have a negative balance
    
    def test_verifySufficientFund(self):
        bankAccount = Banking(300)
        self.assertFalse(bankAccount.verify_sufficient_fund(500))
        self.assertTrue(bankAccount.verify_sufficient_fund(100))

    def test_verifyDepositAmount(self):
        bankAccount = Banking(300)
        self.assertFalse(bankAccount.verify_deposit_amount(-10))
        self.assertTrue(bankAccount.verify_deposit_amount(10))

if __name__ == '__main__':
    unittest.main()
