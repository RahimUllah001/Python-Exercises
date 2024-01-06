try:
    value = 19/0

    num = int(input("Enter an number"))

    print(num)
   

except ZeroDivisionError as err:        #this thing is as too write  except exception as e:
    print(err)
except:
    print("invalid inpiut")  

finally:
    print("this finally will always run ")       

# specific error except should be above than general except
    
class valueTooHigh(Exception):
    pass


class valueTooSmall(Exception):
    def __init__(self,message,value):
        self.message = message
        self.value = value



def test_value(x):
    if x>100:
        raise valueTooHigh("value is too high")
    if x < 5:
        raise valueTooSmall("value is too small",x)    



try:
    test_value(3)
except valueTooHigh as e:
    print(e)
except valueTooSmall as e:
    print(e.message,e.value)