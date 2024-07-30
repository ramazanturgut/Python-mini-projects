import random
import string

strings= string.ascii_lowercase+string.ascii_uppercase+string.digits+string.punctuation

length=12
password="".join(random.sample(strings,length))
print(password)