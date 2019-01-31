import math,random
import string

def generateOTP():
    digit = '0123456789'
    OTP=''
    # Length OTP can be changed by Changing the value in range
    for i in range(4):
        OTP+=digit[math.floor(random.random()*10)]
        # math. floor() returns floor of any flooting number to an integer value
        #random.random() return any random numbers between 0 to 1
    return OTP

#Now let's try to generate OTP Using String Constants to do that first we need to --> import string
def generateOTP1(size):
    generate_pwd=''
    for n in range(size):
        generate_pwd+=''.join([random.choice(string.ascii_uppercase
                                             +string.ascii_lowercase
                                             +string.digits)])
    return generate_pwd



if __name__ == "__main__":
    print("OTP is ",generateOTP())
    password = generateOTP1(6)
print(password)

