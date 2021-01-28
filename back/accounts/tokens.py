# from django.contrib.auth.tokens import PasswordResetTokenGenerator

# class AccountActivationTokenGenerator(PasswordResetTokenGenerator):
#     def _make_hash_value(self, user, timestamp):
#         return (str(user.pk) + str(timestamp)) +  str(user.is_active)
    
# account_activation_token = AccountActivationTokenGenerator()
import random
# length = 6

def make_code():
    string_pool ='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    result = ''
    for i in range(6):
        result += random.choice(string_pool)
    return result