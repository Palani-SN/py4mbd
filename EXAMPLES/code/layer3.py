
from py4mbd.inner import pod
from code.layer4 import layer4

class layer3(pod):

    l4 = layer4()
    
    # Sample Function that gets two input strings, ( inp1, inp2 )
    # Prints them side by side
    # returns nothing (None)
    def dummy(self, inp1:str=None, inp2:str=None):
        """
        model 

        YML format

        - dummy:
            inp1: "Hello"
            inp2: "World"
        
        JSON format

        {
            "dummy": {
                "inp1": "Hello",
                "inp2": "World"
            }
        }

        """
        print("dummy", inp1, inp2)
        return ("dummy", inp1, inp2)

    # Sample Function that gets two input strings, ( inp1, inp2 )
    # Prints them side by side
    # returns nothing (None)
    def summa(self, inp1:str=None, inp2:str=None):
        """
        model 

        YML format

        - dummy:
            inp1: "Hello"
            inp2: "World"
        
        JSON format

        {
            "dummy": {
                "inp1": "Hello",
                "inp2": "World"
            }
        }

        """
        print("summa", inp1, inp2)
        return ("summa", inp1, inp2)